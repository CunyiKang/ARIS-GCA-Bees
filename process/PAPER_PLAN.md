# Paper Plan — Unified CX Predictive Coding Self-Model

**Title**: A Unified Predictive Coding Account of Functional Self-Awareness in Bees: Analytically Derived Precision Trade-offs Across Four Behavioral Domains

**Short title**: Precision and Self-Awareness in Bees

**Target venue**: PLOS Computational Biology
**Format**: Single-column, no page limit (target ~10,000 words main text)
**Date**: 2026-03-16

---

## Claims-Evidence Matrix

| Claim | Evidence | Figure | Section |
|-------|----------|--------|---------|
| C1: Metacognitive accuracy is an inverted-U function of precision | Analytical derivation of p* = 0.563 from opt-out sigmoid model | Fig 1 (inverted-U curve) | §3 Analytical Results |
| C2: A single precision parameter explains 83.5% of variance across non-metacognitive domains | Simulation: GCA factor 83.5%, N=500 | Fig 2 (GCA factor bar chart) | §4 Simulation Results |
| C3: More intelligent bees (high GCA) are less accurate at opt-out metacognition | Simulation: meta-GCA r = -0.658 in normal condition | Fig 3 (scatter + correlation matrix) | §4 Simulation Results |
| C4: Circadian disruption reverses the metacognition-intelligence relationship | Simulation: meta-GCA r shifts -0.658 → +0.730 under disruption | Fig 4 (disruption effect) | §4 Simulation Results |
| C5: Caste-appropriate learning is precision × caste-match weighted | Simulation: nurse spatial 0.783 vs. cross-caste 0.664 | Table 1 | §4 Simulation Results |
| C6: Functional self-awareness = precision-weighted self-model, not phenomenal consciousness | Theoretical framing via Friston FEP and Metzinger self-model theory | None (text) | §2 Model |

---

## Section Structure

### 1. Abstract (~250 words)
- Background: Self-awareness markers in insects, computational framework lacking
- Method: Predictive coding model with shared precision parameter; analytical + simulation study
- Key results: p* = 0.563 analytically derived; metacognition-GCA anti-correlation r = -0.658; disruption reverses sign to +0.730; GCA factor 83.5%
- Significance: First formal computational theory of insect functional self-awareness; three falsifiable predictions

### 2. Introduction (~1200 words)
- Paragraph 1: Evidence for self-awareness markers in insects (metacognition, tool use, caste learning)
- Paragraph 2: The gap — no unified computational framework
- Paragraph 3: Predictive coding and the Free Energy Principle as candidate theory
- Paragraph 4: The central complex as shared substrate
- Paragraph 5: Definitional section — "functional self-awareness" vs. "phenomenal consciousness"
  - Functional self-awareness: precision-weighted generative self-model that enables uncertainty-appropriate behavior
  - We do NOT claim subjective experience — only functional, computational analogs
  - Follows Metzinger (2003) self-model theory; Friston (2010) FEP
- Paragraph 6: Overview of paper and 3 main predictions

### 3. Model: CX Predictive Coding Architecture (~1500 words)
- Subsection 3.1: Self-state representation
  - The CX maintains a generative model of self-state: [precision, caste_identity, circadian_phase, energy]
  - Precision = inverse uncertainty = quality of internal predictions
  - Mathematical notation: p ∈ [0,1], u = 1-p
- Subsection 3.2: Domain-specific observation functions
  - Metacognition: opt-out accuracy as function of precision (sigmoid model)
  - Tool use: monotone increasing with precision × caste_weight
  - Caste learning: precision × caste_match
  - GCA: linear in precision
- Subsection 3.3: Empirical parameter grounding
  - Precision distributions fitted to bee d' from Avarguès-Weber et al. reversal learning
  - Beta distribution parameters derived from published d' range [0.3, 2.1] normalized to [0.2, 0.95]
- Subsection 3.4: Conditions modeled
  - Normal, circadian-disrupted, nurse-spatial, forager-spatial

### 4. Analytical Results: The Precision-Metacognition Trade-off (~1000 words)
- Subsection 4.1: Derivation
  - Opt-out accuracy = (P(opt_out|hard) + P(stay|easy)) / 2
  - P(opt_out|d) = σ(u·slope − threshold(d))
  - As p → 1: u → 0, P(opt_out|hard) → 0 → accuracy → 0.5
  - As p → 0: u → 1, P(opt_out|easy) → 1 → accuracy → 0.5
  - Maximum exists at intermediate p: numerically p* = 0.563 for slope=4.0, thresholds 1.0/2.5
- Subsection 4.2: Interpretation
  - Overconfident agents (high p) fail metacognition not because they're bad at the task but because they never feel uncertain enough to opt out
  - The "overconfidence paradox": higher precision drives better task performance but worse self-knowledge
- Subsection 4.3: Robustness
  - Qualitative result holds for slope ∈ [2.0, 8.0] and reasonable threshold separations
  - Fig 1: inverted-U curve with shaded robustness band

### 5. Simulation Results (~2000 words)
- Subsection 5.1: 4-domain model results (Table 1 + Fig 2)
  - Normal condition: precision=0.728, meta=0.656, tool=0.550, learning=0.664
  - GCA factor: 83.5% variance explained across non-metacognitive domains
- Subsection 5.2: The metacognition-intelligence anti-correlation (Fig 3)
  - Meta-GCA r = -0.658 in normal condition
  - Meta-tool r = -0.725 (even stronger)
  - Contrast: tool-GCA r = +0.696 (positive, expected)
  - Interpretation: precision splits domain performance — simultaneously drives GCA up and metacognition down
- Subsection 5.3: Caste-appropriate learning (Table 1)
  - Forager spatial: 0.804, nurse spatial: 0.783, normal mixed: 0.664
  - Caste-match amplifies precision-driven learning
- Subsection 5.4: Disruption effects and sign flip (Fig 4)
  - All domains impaired under circadian disruption (precision drops 0.728 → 0.302)
  - Key prediction: meta-GCA anti-correlation reverses to +0.730
  - Interpretation: under disruption, precision is uniformly low — all domains co-vary positively with any residual precision

### 6. Discussion (~1800 words)
- Subsection 6.1: The overconfidence paradox in context
  - Relates to Dunning-Kruger (inverted at individual level by mechanism, not just correlation)
  - Vertebrate analogs: high-IQ individuals show worse metacalibration in some studies
- Subsection 6.2: Empirical test proposals
  - Prediction 1 (direct): Correlate GCA battery score (Animal Cognition 2024 paradigm) with opt-out accuracy in same individuals → expect r < −0.3
  - Prediction 2 (direct): Test opt-out accuracy at three precision levels (mild, moderate, high training) → expect inverted-U, peak at ~60% precision
  - Prediction 3 (indirect): Apply circadian disruption; verify meta-GCA sign flips from negative to positive
- Subsection 6.3: Limitations
  - Precision is a scalar simplification — real CX has multiple precision channels
  - No neural implementation details — ring attractor topology not modeled
  - Empirical validation requires same-individual measurements across 4 paradigms
  - "Self-awareness" framing: critics may prefer "metacognition" or "uncertainty monitoring"
- Subsection 6.4: Relation to FEP framework
  - Friston (2010) FEP: agents minimize expected free energy; precision = inverse variance of generative model
  - Our model is a behavioral-level abstraction; future work: connect to full FEP with variational inference

### 7. Conclusion (~300 words)
- Three falsifiable predictions from a single parameter
- Invites experimental test across domains in same individuals
- First formal computational theory of insect functional self-awareness

### 8. Methods (~1000 words)
- Simulation implementation (Python, NumPy, seed 2026)
- Analytical derivation details (sigmoid parameters)
- Empirical grounding (beta distribution fitting to d' data)
- Statistical analysis (GCA via eigendecomposition, correlations via Pearson's r)

---

## Figure Plan

### Fig 1 — Precision-Metacognition Inverted-U Curve
- **Type**: Line plot with shaded robustness band
- **X-axis**: Precision (0 to 1)
- **Y-axis**: Metacognitive accuracy (0.5 to 0.7)
- **Data**: `meta_accuracy_analytical(p)` for p in [0.01, 0.99]
- **Key annotation**: vertical dashed line at p* = 0.563, horizontal annotation at max accuracy
- **Robustness band**: vary slope from 2.0 to 6.0, show envelope
- **Source**: `experiment_r2_4domain.py` (analytical function)

### Fig 2 — GCA Factor Across Conditions
- **Type**: Grouped bar chart
- **X-axis**: Four conditions (normal, disrupted, nurse_spatial, forager_spatial)
- **Y-axis**: GCA factor % (0 to 100%)
- **Secondary Y**: Mean precision (line overlay)
- **Data**: `simulation_results_r2.json`
- **Key annotation**: GCA 83.5% for normal condition

### Fig 3 — Cross-Domain Correlation Matrix (Normal Condition)
- **Type**: 4×4 heatmap with correlation values
- **Domains**: Meta, Tool, Learning, GCA_score
- **Color**: Diverging (red = negative, blue = positive)
- **Key annotation**: Meta-GCA r = -0.658 highlighted
- **Data**: Regenerated from simulation with individual-level data saved

### Fig 4 — Disruption Effect: Domain Scores and Meta-GCA Sign Flip
- **Type**: Two-panel figure
  - Left panel: Bar chart of domain scores (meta, tool, learning) for normal vs. disrupted
  - Right panel: Meta-GCA correlation coefficient for 4 conditions (bar chart, with error on normal via bootstrap)
- **Data**: `simulation_results_r2.json`
- **Key annotation**: r = -0.658 (normal) vs. r = +0.730 (disrupted), color-coded positive/negative

### Table 1 — 4-Domain Model Results Across Conditions
- Rows: 4 conditions
- Columns: Precision, Meta, Tool, Learning, Meta-GCA r, GCA%
- Bold: key comparisons
- Source: `simulation_results_r2.json`

---

## Citation Scaffolding

| Key | Reference | Claim supported |
|-----|-----------|----------------|
| Giurfa2013 | Giurfa et al. 2013 PNAS — opt-out metacognition bees | C3, C1 empirical basis |
| AnimalCog2024 | Animal Cognition 2024 — GCA in honeybees | C2 empirical basis |
| ChittkaPhilTrans2025 | Chittka et al. 2025 Phil Trans B — consciousness in insects | C6 framing |
| AvarWeber2012 | Avarguès-Weber et al. 2012 — reversal learning d' | Model parameterization |
| NaturePuzzle2024 | Loukola et al. / Alem et al. 2024 Nature — tool use social learning | C3 background |
| SciAdv2024Caste | Science Advances 2024 — dsx caste gene | C5 background |
| SciReports2020 | Sci Reports 2020 — neonicotinoids + circadian | C4 background |
| Friston2010 | Friston 2010 J Physiology — FEP | C6 theory |
| Metzinger2003 | Metzinger 2003 — Self-model theory | C6 framing |
| AnimalBehav2022 | Animal Behaviour 2022 — bumblebee play | Background |
| FrontEvoEco2025 | Frontiers EvoEco 2025 — brain caste development | C5 background |
| Rao1999 | Rao & Ballard 1999 — predictive coding | Model framework |
| Clark2013 | Clark 2013 — predictive coding & action | Model framework |

---

## Notes for Writing

- Tone: Theoretical/computational, but connect to concrete behavioral experiments throughout
- Key framing word: "functional self-awareness" — use consistently, never "consciousness"
- Inverted-U result is the headline — lead with it in abstract and intro
- Anti-correlation prediction (C3) is counterintuitive — make sure to flag it clearly
- Methods should include enough detail to reproduce the simulation (seed, distributions, parameters)
- Discussion should preemptively address the "self-awareness is just attention" objection
