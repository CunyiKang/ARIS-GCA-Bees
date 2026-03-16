<p align="right">
  <a href="./README.md"><img src="https://img.shields.io/badge/Language-English-blue" alt="English"></a>
  <a href="./README.zh-CN.md"><img src="https://img.shields.io/badge/语言-中文-red" alt="中文"></a>
</p>

# ARIS-GCA-Bees

A computational neuroethology project on **functional self-awareness in bees**, developed through an [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) automated research pipeline.

## Overview

This repository contains the code, figures, results, process logs, and manuscript materials for a theory-driven computational project proposing a **unified predictive coding account of functional self-awareness in bees**(see final [PDF here](https://cunyikang.github.io/ARIS-GCA-Bees/), including English and Chinese version). 

The core claim is that a single latent parameter — **precision** in a predictive coding architecture instantiated in the **central complex (CX)** — can jointly explain four behavioral domains:

- metacognitive opt-out behavior
- tool-use anticipation
- caste-appropriate learning
- general cognitive ability (GCA)

## Main Idea

This project asks whether multiple apparently self-referential behaviors in bees can be explained by a single computational principle.

The proposed answer is yes:

- **Metacognitive performance follows an inverted-U relationship with precision**
- **Higher GCA can paradoxically predict worse metacognitive calibration**
- **Circadian disruption can reverse the sign of the metacognition–GCA relationship**

This repository is intended as a **theory + simulation** project that generates falsifiable predictions for future empirical work.

## Repository Structure

```text
ARIS-GCA-Bees/
├── code/                  # Simulation scripts
├── figures/               # Figure generation scripts and exported figures
├── paper/                 # Manuscript files
├── process/               # Research pipeline reports and review logs
├── results/               # Numerical outputs from simulations
├── README.md
└── README.zh-CN.md
```

## Key Files

- `process/RESEARCH_PIPELINE_REPORT.md` — summary of the full research pipeline
- `code/experiment_r2_4domain.py` — main Round-2 simulation script
- `figures/generate_figures.py` — figure generation script
- `paper/main.tex` — LaTeX manuscript source
- `paper/main.html` — HTML version of the manuscript

## Research Highlights

- A unified predictive coding model parameterized by **precision**
- An analytically derived optimum for metacognitive accuracy
- A simulated **metacognition–GCA anti-correlation**
- A sign flip under circadian disruption
- A manuscript-ready pipeline connecting idea generation, simulation, review, and paper writing

## How to Use This Repository

### 1. Explore the project logic

Start with:

- [`Research Pipeline Report`](./process/RESEARCH_PIPELINE_REPORT.md)
- [`Paper source`](./paper/main.tex)
- [`HTML manuscript`](./paper/main.html)

### 2. Run the main simulation

```bash
python code/experiment_r2_4domain.py
```

### 3. Generate figures

```bash
python figures/generate_figures.py
```

## Project Workflow

The repository follows a research-generation workflow:

```text
idea discovery
→ pilot testing
→ full simulation
→ review loop
→ paper planning
→ manuscript drafting
```

## Current Status

This project is currently at the **theory and simulation** stage.  
It is not an empirical dataset repository. The main value of the project is:

- formalization
- computational unification
- falsifiable prediction generation
- manuscript-ready research packaging

## Paper

Working title:

**A Unified Predictive Coding Account of Functional Self-Awareness in Bees: Analytically Derived Precision Trade-offs Across Four Behavioral Domains**

Related files:

- [`LaTeX source`](./paper/main.tex)
- [`HTML manuscript`](./paper/main.html)

## Citation

If you wish to reference this repository before formal publication, please cite it as:

```text
Kang, C. (2026). ARIS-GCA-Bees: A unified predictive coding account of functional self-awareness in bees. GitHub repository.
```

## Contact

Maintainer: **Cunyi Kang**

For questions, comments, or collaboration, please open an issue on GitHub.
