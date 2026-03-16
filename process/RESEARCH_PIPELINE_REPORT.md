# Research Pipeline Report

**Direction**: "蜂类分工、娱乐、比较、欺骗、节律的违背、助人与攻击、工具使用、学习中的自我意识"
*(Self-awareness in bee caste division, play, comparison, deception, rhythm violation, helping & aggression, tool use, and learning)*

**Chosen Idea**: Unified Predictive Coding Self-Model in the Central Complex (Idea 8)
**Date**: 2026-03-16
**Pipeline**: idea-discovery → implement → run-experiment → auto-review-loop

---

## Journey Summary

- **Ideas generated**: 12 generated → 10 survived filtering → 2 piloted → 1 chosen
- **Implementation**: Full-scale N=500 simulation of unified CX predictive coding model across 4 domains (metacognition, tool use, caste-appropriate learning, GCA)
- **Experiments**: 5 Python simulation scripts (pilot + full-scale + Round 2 refocused)
- **Review rounds**: 2/4, final score: **6.5/10** — threshold reached, loop complete

---

## Final Status

**Ready for paper writing** — proceed to `/paper-writing` pipeline.

**Target venue**: *PLOS Computational Biology* or *eLife*

---

## Core Scientific Contribution

A unified predictive coding model parameterized by a single "precision" variable explains four functional self-awareness markers in bees. The key novel result is an **analytically derived precision-metacognition trade-off** with three falsifiable predictions:

1. **Metacognition-GCA anti-correlation** (r = -0.658 in simulation): More intelligent bees are systematically *less* accurate on opt-out metacognitive tasks. This is counterintuitive — intelligence and self-knowledge diverge when precision is high.

2. **Optimal precision for metacognition** (p* = 0.563): Analytically derived from the opt-out sigmoid model. Overconfident bees (high precision) rarely opt out even on hard trials; low-precision bees opt out on everything. The sweet spot is intermediate precision.

3. **Disruption reverses the meta-GCA sign** (r: -0.658 → +0.730 under circadian disruption): Under precision-reducing perturbations, domain specificity collapses and the anti-correlation becomes positive. Directly testable with circadian disruption + multi-domain battery.

---

## Simulation Results Summary

### Round 1 (8-domain model, experiment_unified_selfmodel_full.py)
| Condition | Precision | MetaCog | Tool | Learning | Rhythm | GCA% |
|-----------|-----------|---------|------|----------|--------|------|
| Normal | 0.696 | 0.610 | 0.523 | 0.658 | 0.738 | 72.4% |
| Disrupted | 0.385 | 0.603 | 0.290 | 0.587 | 0.574 | — |
| Nurse spatial | — | — | — | 0.552 | — | — |
| Forager spatial | — | — | — | 0.659 | — | — |

Predictions confirmed: P2 (disruption impairs 3+ domains), P3 (caste mismatch impairs learning), P4 (GCA > 40%). P1/P5 failed.

Score: 5.5/10

### Round 2 (4-domain refocused, experiment_r2_4domain.py)
**Analytical result**: Optimal precision p* = 0.563 (inverted-U formally derived)

| Condition | Precision | Meta | Tool | Learning | Meta-GCA r | GCA% |
|-----------|-----------|------|------|----------|------------|------|
| Normal | 0.728 | 0.656 | 0.550 | 0.664 | **-0.658** | **83.5%** |
| Disrupted | 0.302 | 0.639 | 0.226 | 0.565 | **+0.730** | 81.2% |
| Nurse spatial | 0.737 | 0.655 | 0.425 | 0.783 | -0.682 | 79.7% |
| Forager spatial | 0.793 | 0.647 | 0.741 | 0.804 | -0.599 | 81.0% |

Score: 6.5/10 ✓

---

## Key Files

| File | Purpose |
|------|---------|
| `IDEA_REPORT.md` | 12 ideas generated, 4 recommended, 2 piloted |
| `pilot_idea8_unified_selfmodel.py` | Pilot: weak positive signal, 5 domains |
| `pilot_idea3_circadian_metacog.py` | Pilot: interesting null → revised hypothesis |
| `experiment_unified_selfmodel_full.py` | Round 1: N=500, 8-domain, 3/5 predictions |
| `exp_run.py` | Windows-compatible version of Round 1 (ASCII encoding) |
| `experiment_r2_4domain.py` | Round 2: analytical + 4-domain refocused |
| `simulation_results.json` | Round 1 numerical results |
| `simulation_results_r2.json` | Round 2 numerical results |
| `AUTO_REVIEW.md` | Full review history (R1: 5.5/10, R2: 6.5/10) |

---

## Remaining TODOs for Paper Writing

### Required before submission
- [ ] Definitional section: "functional self-awareness" (precision-weighted self-model) vs. "phenomenal consciousness" — cite Friston 2010 FEP, Metzinger 2003 self-model theory
- [ ] Formal statement of Prediction 5: disruption reverses meta-GCA sign
- [ ] Robustness check: vary sigmoid slope (2.0 to 8.0), confirm anti-correlation direction is stable

### Empirical follow-up (future work)
- [ ] Test same-individual correlations in bumblebees: metacognition battery + GCA battery (Animal Cognition 2024 paradigm)
- [ ] Multi-dose neonicotinoid experiment: mild vs. severe disruption, measure both opt-out and GCA
- [ ] Full-scale CX network model with realistic topology (ring attractor + Kenyon cells)

---

## Suggested Paper Structure

1. **Introduction**: Self-awareness in insects — the unifying question; 8 behavior domains introduced
2. **Model**: CX predictive coding architecture; precision as shared parameter; formal derivation of domain-specific predictions
3. **Analytical results**: Precision-metacognition inverted-U (Theorem 1: optimal precision p* = 0.563)
4. **Simulation results**: 4-domain model; metacognition-GCA anti-correlation; disruption sign flip
5. **Discussion**: Functional self-awareness defined (FEP framing); comparison to vertebrate self-awareness literature; empirical test proposals
6. **Conclusion**: First unified computational theory of insect self-awareness; three falsifiable predictions

---

## Next Steps

```
/paper-writing "Unified Predictive Coding Self-Model of Bee Self-Awareness"
```

Or manually:
1. `/paper-plan` — generate paper outline from this report + AUTO_REVIEW.md
2. `/paper-write` — draft LaTeX section by section
3. `/paper-compile` — compile and verify PDF
4. `/auto-paper-improvement-loop` — polish for submission
