# Paper Improvement Log

**Paper**: A Unified Predictive Coding Account of Functional Self-Awareness in Bees
**Date**: 2026-03-16
**Improvement rounds**: 2

---

## Round 0 (Baseline)

**Score**: 6.0/10 (estimated)

**Files**: `main_round0_original.html`, `main_round0_original.docx`

**State**: Initial draft from PAPER_PLAN.md. Used `\input{}` to separate sections but pandoc
rendered only partial heading structure. The `align` environment was used for multi-line equations,
causing pandoc conversion warnings.

**Issues identified**:
1. [Major] `aligned` math environment caused pandoc conversion warning (DOCX generation)
2. [Major] Prediction 2 (inverted-U dose-response) lacked a concrete experimental design
3. [Moderate] Limitations section did not acknowledge the 4 dropped domains (play, rhythm, deception, helping)
4. [Moderate] Some `\subsection*{}` headings not rendering in pandoc HTML due to `\paragraph` interleaving
5. [Minor] `\ref{sec:model:state}` and similar sub-labels used in text but `\label` only defined in section files

---

## Round 1

**Score**: 6.5/10

**Files**: `main_round1.html`, `main_round1.docx`

**Changes made**:
- Merged all section content into `main.tex` for better pandoc compatibility and single-file LaTeX compilation
- Added `\label{eq:meta}` to the metacognitive accuracy equation (referenced from Introduction)
- Added formal statement of the overconfidence paradox as a mathematical result: $d\,\text{Perf}/d\precision > 0$ vs $d\metaacc/d\precision < 0$ for $\precision > \pstar$
- Added clear normal-condition regime justification: mean precision $\approx 0.64 > \pstar = 0.563$
- Added quantitative caste learning prediction ($\Delta = 0.14$)
- Improved figure captions with more interpretive text

**Remaining issues after Round 1**:
- `aligned` LaTeX environment still causing pandoc warning
- Prediction 2 still lacked concrete experimental protocol
- Limitations still missing the 4 dropped domains

---

## Round 2

**Score**: 7.0/10

**Files**: `main_round2.html`, `main_round2.docx`

**Changes made**:
1. Replaced `\begin{align}...\end{align}` with `\begin{equation}...\end{equation}` for the single equation to eliminate pandoc conversion warning
2. Expanded Prediction 2 with a concrete experimental design: three groups trained to easy/medium/hard discrimination, transferred to opt-out paradigm; medium group predicted to show highest opt-out accuracy
3. Added Limitation 5: explicitly flags the four dropped domains (play, rhythm, deception, helping) as consistent with the model but deferred to future work

**Remaining issues (not addressed)**:
- Pandoc still warns about custom macro expansion in DOCX (cosmetic only; LaTeX source is correct)
- No LaTeX-compiled PDF available (requires pdflatex/MiKTeX installation)
- `\paragraph{}` headings in the Model section are not rendered as h3 in HTML

---

## Final Assessment

**Final score**: 7.0/10

**Submission readiness**: Ready for LaTeX compilation and submission pending:
1. Install MiKTeX or TeX Live to compile `paper/main.tex` to PDF
2. Verify figure paths resolve (`../figures/*.pdf`) during compilation
3. Add author affiliations and ORCID numbers to `main.tex`
4. Check journal-specific formatting requirements

**Output files**:
- `paper/main.tex` — Complete single-file LaTeX source (recommended for compilation)
- `paper/main_round2.html` — Final HTML (viewable in browser, printable to PDF)
- `paper/main_round2.docx` — Final DOCX (Word-compatible)
- `paper/main_round0_original.*` — Baseline for comparison
- `paper/main_round1.*` — After Round 1 improvements
- `paper/references.bib` — 16 bibliography entries
- `paper/math_commands.tex` — Math macros (for separate section compilation)
- `paper/sections/*.tex` — Individual section files (for modular editing)
- `figures/*.pdf` — 4 publication-quality figures

---

## Improvement Score Trajectory

| Round | Score | Key Changes |
|-------|-------|-------------|
| Round 0 | 6.0/10 | Baseline: all sections written, figures generated |
| Round 1 | 6.5/10 | Merged to single file, formal math statement of paradox, better figure captions |
| Round 2 | 7.0/10 | Fixed equation environment, concrete Prediction 2 protocol, added dropped-domain limitation |
