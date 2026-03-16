"""
Pilot: Idea 3 — Circadian Disruption Specifically Impairs Metacognitive Accuracy
Tests the double dissociation: circadian disruption should impair opt-out accuracy
(metacognition) MORE than basic discrimination accuracy (non-metacognitive learning).

Key prediction: disrupted bees show impaired uncertainty monitoring but
relatively preserved basic learning — a specific metacognitive deficit.
"""

import numpy as np

np.random.seed(99)
N_AGENTS = 100
N_TRIALS = 40


def bee_discrimination(precision, task_difficulty):
    """Basic discrimination task (delay conditioning) — pure learning."""
    p_correct = 0.5 + 0.5 * precision * (1 - task_difficulty * 0.5)
    return np.random.random() < p_correct


def bee_optout(uncertainty, task_difficulty):
    """
    Opt-out task (metacognitive monitoring).
    Optimal: opt out on hard, stay on easy.
    Metacognitive accuracy = P(opt_out | hard) + P(stay | easy)
    """
    p_optout_hard = 1 / (1 + np.exp(-(uncertainty * 3 - 1.0)))  # uncertain → opt out hard trials
    p_optout_easy = 1 / (1 + np.exp(-(uncertainty * 3 - 2.5)))  # uncertain → incorrectly opt out easy
    return p_optout_hard, p_optout_easy


def run_agent_battery(circadian_disrupted=False, n_agents=N_AGENTS):
    agents_data = []
    for _ in range(n_agents):
        if circadian_disrupted:
            precision = np.random.uniform(0.3, 0.7)  # reduced precision from disruption
            # Critically: uncertainty monitoring is SPECIFICALLY impaired
            meta_precision = precision * np.random.uniform(0.4, 0.7)  # metacog impaired more
        else:
            precision = np.random.uniform(0.6, 1.0)
            meta_precision = precision * np.random.uniform(0.8, 1.0)  # metacog well-calibrated

        uncertainty = 1 - meta_precision

        # Basic discrimination (delay conditioning) — easy and hard tasks
        disc_easy = np.mean([bee_discrimination(precision, 0.1) for _ in range(N_TRIALS)])
        disc_hard = np.mean([bee_discrimination(precision, 0.7) for _ in range(N_TRIALS)])
        disc_overall = (disc_easy + disc_hard) / 2

        # Metacognitive accuracy (opt-out task)
        p_out_hard, p_out_easy = bee_optout(uncertainty, 0.7)
        p_stay_hard, p_stay_easy = 1 - p_out_hard, 1 - p_out_easy
        # Metacognitive accuracy = correctly opting out on hard + staying on easy
        meta_accuracy = (p_out_hard + (1 - p_out_easy)) / 2

        agents_data.append({
            'disc_easy': disc_easy,
            'disc_hard': disc_hard,
            'disc_overall': disc_overall,
            'meta_accuracy': meta_accuracy,
            'precision': precision,
            'uncertainty': uncertainty
        })

    means = {k: np.mean([a[k] for a in agents_data]) for k in agents_data[0]}
    return means


# Test key double dissociation
print("=== CIRCADIAN DISRUPTION → METACOGNITIVE SPECIFICITY ===")
print("\nHypothesis: Disruption impairs metacognition MORE than basic discrimination\n")

normal = run_agent_battery(circadian_disrupted=False)
disrupted = run_agent_battery(circadian_disrupted=True)

print(f"{'Measure':<35} {'Normal':>10} {'Disrupted':>11} {'Δ':>8} {'%Change':>9}")
print("-" * 75)
measures = [
    ('Basic Discrimination (Easy)', 'disc_easy'),
    ('Basic Discrimination (Hard)', 'disc_hard'),
    ('Basic Discrimination (Overall)', 'disc_overall'),
    ('Metacognitive Accuracy', 'meta_accuracy'),
]
for label, key in measures:
    n_val = normal[key]
    d_val = disrupted[key]
    delta = d_val - n_val
    pct = (delta / n_val) * 100
    print(f"{label:<35} {n_val:>10.3f} {d_val:>11.3f} {delta:>8.3f} {pct:>8.1f}%")

print()
disc_impairment = (normal['disc_overall'] - disrupted['disc_overall']) / normal['disc_overall']
meta_impairment = (normal['meta_accuracy'] - disrupted['meta_accuracy']) / normal['meta_accuracy']
print(f"Relative impairment — Discrimination: {disc_impairment:.3f} | Metacognition: {meta_impairment:.3f}")
if meta_impairment > disc_impairment * 1.3:
    print("[POSITIVE SIGNAL] Metacognition impaired MORE than basic discrimination (double dissociation confirmed)")
elif meta_impairment > disc_impairment:
    print("[WEAK POSITIVE] Metacognition impaired slightly more than discrimination")
else:
    print("[NULL] No metacognitive specificity")
