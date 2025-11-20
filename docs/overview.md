# Study Overview & Documentation Map

## 1. Introduction

This project investigates how observable user behavior during interactive digital tasks can be used to infer cognitive load. The study combines:

- Fine-grained interaction logging (mouse behavior, hesitation, corrections, drag attempts, constraint violations, etc.)
- Human workload reports using NASA-TLX
- Feature engineering grounded in cognitive load theory
- Machine learning modeling
- Model interpretability using SHAP
- Design implications and adaptive UI demonstrations

The dataset includes **25 participants**, each completing three tasks of increasing complexity:

- **Task 1** – Shipping Form Entry (low cognitive load)
- **Task 2** – Product Exploration & Filtering (medium cognitive load)
- **Task 3** – Travel Planning & Scheduling (high cognitive load)

This yields **75 samples**, with a rich set of engineered behavioral features and subjective TLX scores.

---

## 2. Study Objectives

### 2.1 Scientific Goals

- Identify which behavioral patterns are most predictive of cognitive load
- Validate whether cognitive load can be reliably inferred without physiological sensors
- Evaluate whether behavioral metrics reflect intrinsic vs. extraneous load
- Understand task-specific cognitive signatures

### 2.2 Applied Goals

- Provide actionable guidance for adaptive UI systems
- Demonstrate how high-load interactions can be detected in real time
- Provide designers and engineers with design rules informed by behavioral analytics

---

## 3. Experimental Design

### 3.1 Tasks

| Task | Description | Expected Load |
|------|-------------|---------------|
| **Task 1 – Shipping Form** | Users complete a simple form with typical fields. | Low |
| **Task 2 – Product Exploration** | Users filter, browse, compare items, reset filters. | Medium |
| **Task 3 – Travel Planning** | Users assemble a flight–hotel–transport itinerary + schedule meetings. | High |

Each task was chosen to reflect increasing information density, decision complexity, and interaction variety.

---

## 4. Data Pipeline Overview

A high-level flow of the end-to-end system:
```
Raw Interaction Logs + TLX
        ↓
Data Ingestion (JSON → standardized tables)
        ↓
Behavioral Feature Engineering
        ↓
Processed Modeling Dataset (75 rows × 20+ features)
        ↓
Statistical Analysis (ANOVA, correlations)
        ↓
Machine Learning (LOUO cross-validation)
        ↓
SHAP Interpretability
        ↓
Design Guidelines + Adaptive UI Examples
```

---

## 5. Repository Structure (Documentation Map)

This folder (`docs/`) contains the full analytical and interpretive outputs of the study:

| File | Purpose |
|------|---------|
| `00_overview.md` | High-level summary (this file) |
| `reproducibility.md` | How to reproduce preprocessing, modeling, SHAP |
| `feature_correlation_summary.md` | Statistical correlations between behavioral features and TLX |
| `ML_Insights.md` | Machine learning performance, Random Forest vs. baselines |
| `SHAP_Insights.md` | Interpretability results and explanation clustering |
| `insights.md` | Applied UX implications and design storytelling |
| `threats_to_validity.md` | Internal/external validity considerations |

---

## 6. Dataset Summary

- **75 samples** (25 participants × 3 tasks)
- **Target variable**: High vs. Low cognitive load (TLX > 60)
- **~20 engineered behavioral features**, including:
  - `scheduling_difficulty`
  - `constraint_violation_rate`
  - `form_hesitation_index`
  - `exploration_breadth`
  - `mouse_entropy_avg`
  - `budget_management_stress`

### Data Availability

- **Raw JSON logs**: `data/raw/`
- **Example schemas**: `data/examples/`
- **Modeling-ready CSV**: `data/processed/modeling_dataset.csv`

---

## 7. Key Findings Summary

This redirects readers to deeper analysis, but provides a snapshot:

- **ANOVA** confirmed that Task 1 < Task 2 < Task 3 in TLX (p < .001)

- **Cognitive load** correlated most strongly with:
  - `scheduling_difficulty` (r ≈ .81)
  - `constraint_violation_rate` (r ≈ .80)
  - `budget_management_stress` (r ≈ .80)

- **Random Forest (LOUO)** achieved:
  - Accuracy = .96
  - F1 = .67
  - ROC-AUC = .95

- **SHAP analysis** revealed two consistent behavioral profiles:
  - **High-load cluster**: frequent violations, long planning time, high entropy
  - **Low-load cluster**: efficient workflows, fewer corrections, smoother navigation

---

## 8. Intended Use

This repository supports:

- Academic theses (HCI, cognitive science, UX, AI)
- Research in adaptive interfaces
- Behavioral modeling
- Simulation environment building
- UI/UX guidelines based on cognitive metrics

All code, data, and visualizations are designed for full reproducibility, transparency, and downstream extension.

---

## 9. License & Ethics

- Behavioral dataset (non-identifiable)
- NASA-TLX included with original scale attribution
- Adaptive UI examples are conceptual mockups for research only
- Code released under MIT License (if applicable)

---

## 10. Contact

For questions, troubleshooting, or collaboration:

**Your Name (Dyra)**  
*(Add email or GitHub handle if desired)*

---

**Last Updated**: November 2025  
**Version**: 1.0