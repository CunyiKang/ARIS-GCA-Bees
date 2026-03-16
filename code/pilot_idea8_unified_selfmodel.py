"""
Pilot: Idea 8 — Unified Predictive Coding Self-Model for Bee Self-Awareness
Tests whether a single predictive coding (PC) architecture with shared self-state
representation can reproduce key self-awareness behaviors across domains:
  - Play (intrinsic prediction error drive)
  - Metacognition/opt-out (uncertainty monitoring)
  - Caste role (self-state as prior on task performance)
  - Tool use anticipation (forward model)
  - Rhythm calibration (time as self-state dimension)

Key prediction: All 5 behaviors emerge from the same PC network with
shared parameters — self-awareness is a unified substrate, not modular.
"""

import numpy as np

np.random.seed(42)
N_AGENTS = 50
N_TRIALS = 200


def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -10, 10)))


class BeeSelfModel:
    """
    Minimal predictive coding self-model.

    State: [caste_role (0=nurse,1=forager), circadian_phase (0-1), energy, uncertainty]
    World belief: prediction of sensory input
    Action: based on prediction error + self-state
    """
    def __init__(self, true_caste=1.0, circadian_disrupted=False):
        # Self-state representation
        self.caste_belief = true_caste + np.random.normal(0, 0.1)
        self.true_caste = true_caste
        self.circadian_disrupted = circadian_disrupted
        self.circadian_phase = np.random.uniform(0, 1)
        self.energy = 0.8

        # Prediction precision (inverse variance) — disruption reduces precision
        if circadian_disrupted:
            self.precision = np.random.uniform(0.3, 0.6)
        else:
            self.precision = np.random.uniform(0.7, 1.0)

        # Uncertainty estimate (metacognitive variable)
        self.uncertainty = 1 - self.precision

        # Play drive: intrinsic prediction error seeking (novelty drive)
        self.play_drive = np.random.uniform(0.2, 0.8)

    def update_self_model(self, sensory_input, expected):
        """Update self-state via prediction error."""
        pred_error = sensory_input - expected
        # Precision-weighted update
        self.caste_belief += 0.1 * self.precision * pred_error
        self.uncertainty = abs(pred_error) * (1 - self.precision)

    def opt_out_decision(self, task_difficulty):
        """Metacognitive opt-out: opt out if uncertainty > difficulty threshold."""
        threshold = 0.5 * (1 + self.precision)
        p_opt_out = sigmoid(self.uncertainty * task_difficulty - threshold)
        return np.random.random() < p_opt_out

    def play_behavior(self):
        """Play: driven by intrinsic prediction error seeking."""
        # Play occurs when energy > threshold AND environment is novel/uncertain
        p_play = self.play_drive * self.energy * self.uncertainty
        return np.random.random() < p_play

    def tool_use_anticipation(self, task_step):
        """Goal-directed tool use: anticipatory forward model."""
        if task_step == 1:  # first step of two-step puzzle
            # Anticipation = forward model accuracy = precision
            anticipation_prob = self.precision * (1 + self.caste_belief) / 2
            return np.random.random() < anticipation_prob
        return False

    def caste_appropriate_learning(self, task_type):
        """Learning performance based on caste-task match."""
        # Foragers excel at spatial (task_type=1), nurses at social (task_type=0)
        caste_match = 1 - abs(self.caste_belief - task_type)
        base_accuracy = 0.5 + 0.4 * caste_match * self.precision
        return np.random.random() < base_accuracy


def run_domain_tests(n_agents=N_AGENTS, circadian_disrupted=False, caste=1.0):
    agents = [BeeSelfModel(true_caste=caste, circadian_disrupted=circadian_disrupted)
              for _ in range(n_agents)]

    results = {
        'play_rate': [],
        'metacognitive_accuracy': [],  # correct opt-out on hard, correct stay on easy
        'tool_anticipation': [],
        'caste_learning': [],
        'cross_domain_corr': []
    }

    for agent in agents:
        # Play behavior
        play_count = sum(agent.play_behavior() for _ in range(10))
        results['play_rate'].append(play_count / 10)

        # Metacognitive accuracy (should opt out on hard=0.9, not on easy=0.1)
        correct_hard = agent.opt_out_decision(0.9)  # should opt out
        correct_easy = not agent.opt_out_decision(0.1)  # should stay
        results['metacognitive_accuracy'].append((correct_hard + correct_easy) / 2)

        # Tool use anticipation (step 1 of 2-step puzzle)
        anticipation = agent.tool_use_anticipation(task_step=1)
        results['tool_anticipation'].append(float(anticipation))

        # Caste-appropriate learning
        learning = agent.caste_appropriate_learning(task_type=1.0)  # spatial
        results['caste_learning'].append(float(learning))

    # Cross-domain correlation (key test: shared substrate prediction)
    play = np.array(results['play_rate'])
    meta = np.array(results['metacognitive_accuracy'])
    tool = np.array(results['tool_anticipation'])
    caste_l = np.array(results['caste_learning'])

    # Correlation matrix
    domain_matrix = np.vstack([play, meta, tool, caste_l])
    corr_matrix = np.corrcoef(domain_matrix)
    mean_cross_corr = (np.sum(corr_matrix) - 4) / (4 * 3)  # off-diagonal mean

    return {k: np.mean(v) for k, v in results.items()}, mean_cross_corr


print("=== UNIFIED SELF-MODEL PILOT ===")
print("\nPrediction: Shared substrate → significant cross-domain correlation of metrics\n")

conditions = [
    ("Normal (intact self-model)", False, 1.0),
    ("Circadian disrupted", True, 1.0),
    ("Nurse caste (forager tasks)", False, 0.0),
    ("Forager caste (forager tasks)", False, 1.0),
]

print(f"{'Condition':<35} {'Play':>7} {'MetaCog':>8} {'ToolAntic':>10} {'Learning':>9} {'CrossCorr':>10}")
print("-" * 85)
for label, disrupted, caste in conditions:
    metrics, cross_corr = run_domain_tests(circadian_disrupted=disrupted, caste=caste)
    print(f"{label:<35} {metrics['play_rate']:>7.3f} {metrics['metacognitive_accuracy']:>8.3f} "
          f"{metrics['tool_anticipation']:>10.3f} {metrics['caste_learning']:>9.3f} {cross_corr:>10.3f}")

# Test key prediction: disrupted condition should reduce cross-domain correlations
print("\n[Key Test] Cross-domain correlation: Normal vs Disrupted")
_, corr_normal = run_domain_tests(circadian_disrupted=False, n_agents=200)
_, corr_disrupted = run_domain_tests(circadian_disrupted=True, n_agents=200)
print(f"  Normal:    {corr_normal:.4f}")
print(f"  Disrupted: {corr_disrupted:.4f}")
print(f"  Reduction: {(corr_normal - corr_disrupted):.4f} {'← POSITIVE SIGNAL' if corr_normal > corr_disrupted else '← NULL'}")
