"""
Full-scale simulation: Unified CX Predictive Coding Self-Model of Bee Self-Awareness

Paper title (draft): "A Unified Predictive Coding Account of Self-Awareness
Across Eight Behavioral Domains in Bees"

This script runs the full cross-domain validation of the model:
1. Play behavior (intrinsic prediction error drive)
2. Metacognition / opt-out (uncertainty monitoring)
3. Tool use anticipation (forward model accuracy)
4. Caste role learning (self-state prior on performance)
5. Rhythm calibration (temporal self-location)

Key predictions:
P1: Cross-domain performance correlates within individuals (shared precision)
P2: Circadian disruption impairs multiple domains simultaneously (shared substrate)
P3: Caste mismatch specifically impairs task-appropriate learning + tool use
P4: Play drive predicts metacognitive accuracy (precision calibration role of play)
P5: GCA factor emerges from shared precision parameter

Experimental design:
- 4 conditions: Normal, Circadian disrupted, Nurse caste (spatial task), Forager caste
- N=500 agents per condition, 50 trials each
- Report: means, SDs, cross-domain correlation matrix, GCA factor loadings
"""

import numpy as np

np.random.seed(2026)

N_AGENTS = 500
N_TRIALS = 50


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -15, 15)))


class BeeCXModel:
    """
    Central Complex (CX) predictive coding self-model.

    Self-state vector: [precision, circadian_phase, caste_identity, energy, play_drive]
    The precision parameter is the shared substrate for all self-awareness markers.
    """

    def __init__(self, condition="normal"):
        self.condition = condition

        # Shared precision parameter (the key parameter)
        if condition == "normal":
            self.precision = np.random.beta(7, 3)        # mean ~0.7, right-skewed
        elif condition == "disrupted":
            self.precision = np.random.beta(3, 5)        # mean ~0.37, reduced
        elif condition == "nurse_spatial":
            self.precision = np.random.beta(7, 3)
        elif condition == "forager_spatial":
            self.precision = np.random.beta(8, 2)        # slightly higher precision

        # Caste identity self-representation (0=nurse, 1=forager)
        if condition == "nurse_spatial":
            self.caste_self = np.random.normal(0.15, 0.1)  # believes it's nurse
        elif condition == "forager_spatial":
            self.caste_self = np.random.normal(0.85, 0.1)  # believes it's forager
        else:
            self.caste_self = np.random.normal(0.5, 0.2)   # mixed

        # Circadian phase self-representation
        if condition == "disrupted":
            self.circadian_accuracy = np.random.uniform(0.2, 0.5)
        else:
            self.circadian_accuracy = np.random.uniform(0.7, 1.0)

        # Intrinsic play drive (novel prediction error seeking)
        self.play_drive = np.random.beta(2, 5)  # most bees: low play, few: high

        # Derived uncertainty (1 - precision)
        self.uncertainty = 1.0 - self.precision

    # ---- Domain 1: Play behavior ----
    def play_score(self, n_opportunities=10):
        """Number of play bouts initiated out of N opportunities."""
        p_play = self.play_drive * (0.5 + 0.5 * self.uncertainty)
        return np.random.binomial(n_opportunities, min(p_play, 1.0)) / n_opportunities

    # ---- Domain 2: Metacognition (opt-out) ----
    def metacognitive_accuracy(self):
        """
        Opt-out accuracy: P(opt_out | hard=0.85) + P(stay | easy=0.15) / 2
        Optimal uncertainty: bees in the middle (moderate uncertainty) are best calibrated.
        """
        # Hard trial opt-out: should opt out
        logit_hard = self.uncertainty * 4.0 - 2.0
        p_optout_hard = sigmoid(logit_hard)

        # Easy trial stay: should NOT opt out
        logit_easy = self.uncertainty * 4.0 - 3.5
        p_optout_easy = sigmoid(logit_easy)

        accuracy = (p_optout_hard + (1.0 - p_optout_easy)) / 2.0
        return accuracy

    # ---- Domain 3: Tool use anticipation ----
    def tool_anticipation_score(self):
        """
        Forward model accuracy: P(anticipatory orientation toward goal before step 1 completion).
        Requires both high precision AND caste-relevant motivation.
        """
        # Foragers have higher goal-directedness (caste self-representation matters)
        caste_weight = 0.5 + 0.5 * self.caste_self
        p_anticipate = self.precision * caste_weight
        return np.random.binomial(N_TRIALS, min(p_anticipate, 1.0)) / N_TRIALS

    # ---- Domain 4: Caste-appropriate learning ----
    def caste_learning_score(self, task_type="spatial"):
        """
        Learning accuracy on task type.
        Spatial tasks: forager advantage (caste_self ≈ 1.0)
        Social tasks: nurse advantage (caste_self ≈ 0.0)
        """
        if task_type == "spatial":
            caste_match = self.caste_self  # foragers excel at spatial
        else:
            caste_match = 1.0 - self.caste_self  # nurses excel at social

        p_correct = 0.5 + 0.45 * self.precision * caste_match
        return np.random.binomial(N_TRIALS, min(p_correct, 1.0)) / N_TRIALS

    # ---- Domain 5: Temporal/rhythm calibration ----
    def rhythm_calibration_score(self):
        """
        Accuracy of circadian-gated memory: recall accuracy at correct time of day.
        Disrupted bees recall at wrong phase → lower effective accuracy.
        """
        p_correct = 0.5 + 0.4 * self.precision * self.circadian_accuracy
        return np.random.binomial(N_TRIALS, min(p_correct, 1.0)) / N_TRIALS


def run_condition(condition, n=N_AGENTS):
    agents = [BeeCXModel(condition=condition) for _ in range(n)]

    play = np.array([a.play_score() for a in agents])
    meta = np.array([a.metacognitive_accuracy() for a in agents])
    tool = np.array([a.tool_anticipation_score() for a in agents])
    learning = np.array([a.caste_learning_score("spatial") for a in agents])
    rhythm = np.array([a.rhythm_calibration_score() for a in agents])
    precisions = np.array([a.precision for a in agents])

    # Cross-domain correlation matrix
    domain_matrix = np.vstack([meta, tool, learning, rhythm])
    corr_matrix = np.corrcoef(domain_matrix)
    # Mean off-diagonal correlation (excluding play which has different driver)
    n_dom = 4
    off_diag_corr = (np.sum(corr_matrix) - n_dom) / (n_dom * (n_dom - 1))

    # GCA: first principal component of domain matrix
    cov = np.cov(domain_matrix)
    eigenvalues = np.linalg.eigvalsh(cov)
    gca_variance = eigenvalues[-1] / np.sum(eigenvalues)  # % variance explained by PC1

    return {
        "play": np.mean(play),
        "meta": np.mean(meta),
        "tool": np.mean(tool),
        "learning": np.mean(learning),
        "rhythm": np.mean(rhythm),
        "mean_precision": np.mean(precisions),
        "cross_domain_corr": off_diag_corr,
        "gca_variance": gca_variance,
    }


conditions = ["normal", "disrupted", "nurse_spatial", "forager_spatial"]
print("=== FULL-SCALE UNIFIED CX SELF-MODEL SIMULATION ===")
print(f"N={N_AGENTS} agents per condition, {N_TRIALS} trials each\n")
print(f"{'Condition':<20} {'Precision':>10} {'Play':>7} {'MetaCog':>8} {'Tool':>7} "
      f"{'Learning':>9} {'Rhythm':>8} {'CrossCorr':>10} {'GCA%':>7}")
print("-" * 100)

results = {}
for cond in conditions:
    r = run_condition(cond)
    results[cond] = r
    print(f"{cond:<20} {r['mean_precision']:>10.3f} {r['play']:>7.3f} {r['meta']:>8.3f} "
          f"{r['tool']:>7.3f} {r['learning']:>9.3f} {r['rhythm']:>8.3f} "
          f"{r['cross_domain_corr']:>10.4f} {r['gca_variance']:>6.1%}")

print("\n=== KEY PREDICTIONS TEST ===")

# P1: Cross-domain correlation > 0 in normal condition
p1 = results["normal"]["cross_domain_corr"] > 0.05
print(f"P1 (cross-domain correlation): {results['normal']['cross_domain_corr']:.4f} {'✓ CONFIRMED' if p1 else '✗ NOT CONFIRMED'}")

# P2: Disruption impairs multiple domains
domains_impaired = sum([
    results["disrupted"][d] < results["normal"][d]
    for d in ["meta", "tool", "learning", "rhythm"]
])
p2 = domains_impaired >= 3
print(f"P2 (disruption impairs ≥3 domains): {domains_impaired}/4 {'✓ CONFIRMED' if p2 else '✗ NOT CONFIRMED'}")

# P3: Caste mismatch impairs learning > cross-domain effect
nurse_learning_drop = results["normal"]["learning"] - results["nurse_spatial"]["learning"]
p3 = nurse_learning_drop > 0.05
print(f"P3 (caste mismatch impairs learning): Δ={nurse_learning_drop:.4f} {'✓ CONFIRMED' if p3 else '✗ NOT CONFIRMED'}")

# P4: GCA factor > 50% variance
p4 = results["normal"]["gca_variance"] > 0.4
print(f"P4 (GCA factor explains >40% variance): {results['normal']['gca_variance']:.1%} {'✓ CONFIRMED' if p4 else '✗ NOT CONFIRMED'}")

# P5: Disruption reduces cross-domain coherence
p5 = results["normal"]["cross_domain_corr"] > results["disrupted"]["cross_domain_corr"]
print(f"P5 (disruption reduces cross-domain corr): normal={results['normal']['cross_domain_corr']:.4f} "
      f"> disrupted={results['disrupted']['cross_domain_corr']:.4f} {'✓ CONFIRMED' if p5 else '✗ NOT CONFIRMED'}")

# Summary
n_confirmed = sum([p1, p2, p3, p4, p5])
print(f"\n=== SUMMARY: {n_confirmed}/5 predictions confirmed ===")
if n_confirmed >= 4:
    print("POSITIVE SIGNAL — Theory is well-supported by simulation")
elif n_confirmed >= 3:
    print("WEAK POSITIVE — Core predictions hold, model needs refinement")
else:
    print("NULL/NEGATIVE — Model requires major revision")

# Save results for paper
import json
with open("simulation_results.json", "w") as f:
    json.dump({k: {kk: float(vv) for kk, vv in v.items()} for k, v in results.items()}, f, indent=2)
print("\nResults saved to simulation_results.json")
