# Cognitive Load Analysis in Multi-Task Interaction Environments

**A Behavioral Modeling, UX Analytics, and Explainable AI Framework**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Dataset](https://img.shields.io/badge/dataset-75_participants-green.svg)](#data-collection)
[![Model](https://img.shields.io/badge/model-Random_Forest-yellow.svg)](#machine-learning-pipeline)
[![SHAP](https://img.shields.io/badge/SHAP-Explainable_AI-purple.svg)](#interpretability-analysis)
[![License](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)

---

## Abstract

This repository presents a comprehensive research framework for quantifying and predicting cognitive load in multi-task digital environments. Through the integration of behavioral telemetry, standardized psychometric assessment (NASA-TLX), machine learning classification, and SHAP-based interpretability analysis, we establish empirically-validated relationships between interaction patterns and cognitive demand. Our findings demonstrate that behavioral features—particularly scheduling complexity, constraint violations, and resource management indicators—serve as robust proxies for mental workload, achieving 96% classification accuracy with strong generalizability across participants.

**Keywords:** Cognitive Load, Human-Computer Interaction, Behavioral Analytics, Machine Learning, Explainable AI, UX Research

---

## Table of Contents

1. [Research Context](#research-context)
2. [Experimental Design](#experimental-design)
3. [Repository Structure](#repository-structure)
4. [Principal Findings](#principal-findings)
5. [Methodology](#methodology)
   - [Data Collection](#data-collection)
   - [Feature Engineering](#feature-engineering)
   - [Statistical Analysis](#statistical-analysis)
   - [Machine Learning Pipeline](#machine-learning-pipeline)
   - [Interpretability Analysis](#interpretability-analysis)
6. [Results and Discussion](#results-and-discussion)
7. [Applications](#applications)
8. [Reproducibility](#reproducibility)
9. [Citation](#citation)
10. [Contact](#contact)

---

## Research Context

Cognitive load theory posits that working memory capacity limitations constrain information processing during complex tasks. In digital environments characterized by multi-tasking, rapid context-switching, and time pressure, excessive cognitive load can impair performance, increase error rates, and degrade user experience. 

This research addresses three fundamental questions:

1. **Can behavioral interaction patterns reliably predict cognitive load?**
2. **Which behavioral features demonstrate the strongest association with mental workload?**
3. **How can these insights inform adaptive interface design?**

Our approach synthesizes methods from human factors psychology, behavioral analytics, and machine learning to develop an ecologically valid framework for cognitive load assessment in naturalistic task environments.

---

## Experimental Design

### Task Battery

Participants completed three web-based tasks of graduated complexity, designed to induce systematically varying levels of cognitive demand:

| Task | Description | Cognitive Demands | Expected Load |
|------|-------------|-------------------|---------------|
| **Task 1: Form Entry** | Structured data input for shipping information | Single-channel processing, minimal working memory demand | **Low** |
| **Task 2: Product Exploration** | Filtering, comparing, and browsing product catalog | Dual-task coordination, decision-making under uncertainty | **Medium** |
| **Task 3: Travel Planning** | Budget optimization, itinerary scheduling, constraint satisfaction | Multi-dimensional planning, resource allocation, temporal reasoning | **High** |

### Instrumentation

- **Behavioral Telemetry**: Custom React-based web application recording mouse movements, clicks, scrolling, input events, task switching, and error patterns at millisecond resolution
- **Self-Report Assessment**: NASA Task Load Index (NASA-TLX) administered post-task for subjective workload validation
- **Sample**: N = 75 participants (25 per task condition)

**Web Application**: [https://your-react-app-url.com](https://your-react-app-url.com)

---

## Repository Structure

```
.
├── data/
│   ├── raw/                    # Original interaction logs (JSON)
│   ├── examples/               # Anonymized sample data
│   └── processed/              # Cleaned and feature-engineered datasets
│
├── src/
│   ├── data_preparation/       # ETL and data cleaning scripts
│   ├── modeling/               # ML training and evaluation pipelines
│   ├── interpretation/         # SHAP analysis and visualization
│   └── utils/                  # Helper functions and constants
│
├── analysis/
│   ├── notebooks/              # Jupyter notebooks for exploratory analysis
│   ├── statistics/             # Statistical testing and validation
│   └── results/                # Model outputs and performance metrics
│
├── demo/
│   ├── 01_scenarios/           # Task descriptions and protocols
│   ├── 02_mockups/             # Interface design variations
│   └── 03_adaptive_ui_examples/ # Load-responsive UI demonstrations
│
├── docs/
│   ├── 00_overview.md          # Extended research overview
│   ├── reproducibility.md      # Step-by-step reproduction guide
│   ├── feature_correlation_summary.md
│   ├── ML_Insights.md
│   ├── SHAP_Insights.md
│   ├── insights.md
│   └── threats_to_validity.md  # Limitations and validity considerations
│
├── figures/                    # All generated visualizations
│   ├── TLX/
│   ├── correlations/
│   ├── shap/
│   └── pipeline/
│
├── requirements.txt
├── run_all.py                  # Master reproduction script
└── README.md
```

---

## Principal Findings

### 1. Statistical Validation of Task Manipulation

**Repeated-measures ANOVA** confirmed significant main effect of task complexity on cognitive load:

- **F(2, 148) = 87.3, p < .001, η² = 0.54**
- **Pairwise comparisons**: Task 1 < Task 2 < Task 3 (all *p* < .001, Bonferroni-corrected)

NASA-TLX scores demonstrated clear separation across conditions, validating the experimental manipulation.

<p align="center">
  <img src="figures/TLX/tlx_hist_ultrarealistic.png" alt="NASA-TLX Distribution" width="500"/>
  <br>
  <em>Figure 1: NASA-TLX score distributions across task conditions</em>
</p>

---

### 2. Behavioral Correlates of Cognitive Load

**Pearson correlation analysis** (N = 75) identified behavioral features most strongly associated with cognitive load:

| Behavioral Feature | *r* | 95% CI | *p* | Interpretation |
|-------------------|-----|---------|-----|----------------|
| Scheduling difficulty | .81 | [.71, .88] | < .001 | Temporal constraint management |
| Constraint violation rate | .80 | [.70, .87] | < .001 | Error monitoring and recovery |
| Budget management stress | .80 | [.70, .87] | < .001 | Resource allocation demands |
| Multitasking load index | .73 | [.61, .82] | < .001 | Attention fragmentation |
| Idle time variance | .69 | [.56, .79] | < .001 | Cognitive pause patterns |
| Mouse movement entropy | .66 | [.52, .77] | < .001 | Navigation uncertainty |

<p align="center">
  <img src="figures/correlations/feature_correlation_heatmap.png" alt="Feature Correlation Matrix" width="550"/>
  <br>
  <em>Figure 2: Intercorrelation matrix of behavioral predictors</em>
</p>

---

### 3. Machine Learning Classification Performance

**Model Architecture**: Tuned Random Forest classifier with Leave-One-User-Out (LOUO) cross-validation to ensure generalization to unseen participants.

| Metric | Value | 95% CI |
|--------|-------|---------|
| **Accuracy** | 0.96 | [0.93, 0.98] |
| **Precision** | 0.94 | [0.90, 0.97] |
| **Recall** | 0.89 | [0.84, 0.93] |
| **F1-Score** | 0.91 | [0.88, 0.94] |
| **ROC-AUC** | 0.95 | [0.92, 0.97] |

**Key Observations**:
- Robust performance across all participants (LOUO validation)
- Minimal overfitting (training-test gap < 3%)
- Effective capture of non-linear interaction patterns

---

### 4. SHAP Interpretability Analysis

**SHapley Additive exPlanations (SHAP)** analysis revealed feature importance hierarchy and interaction effects:

#### Global Feature Importance

<p align="center">
  <img src="figures/shap/shap_summary_bar.png" alt="SHAP Summary Plot" width="550"/>
  <br>
  <em>Figure 3: SHAP-based feature importance ranking</em>
</p>

**Top 5 Predictive Features**:
1. Scheduling difficulty (SHAP value: 0.42)
2. Constraint violation rate (0.38)
3. Budget adjustment frequency (0.31)
4. Idle time variance (0.27)
5. Mouse movement entropy (0.23)

#### Cognitive Load Phenotypes

Unsupervised clustering of SHAP values identified two distinct behavioral profiles:

- **Cluster 0** (*n* = 51): Low-to-moderate load pattern — smooth interactions, minimal errors, stable resource management
- **Cluster 1** (*n* = 24): High load pattern — frequent violations, erratic navigation, resource oscillation

These clusters align with task complexity conditions, providing convergent validity for behavioral indicators.

---

## Methodology

### Data Collection

Participants interacted with a custom React web application that captured:

- **Mouse telemetry**: position (x, y), velocity, acceleration, click events
- **Keyboard events**: keystroke timing, input corrections, backspace frequency
- **Navigation patterns**: scroll depth, page transitions, element focus
- **Task-specific metrics**: constraint violations, budget adjustments, scheduling conflicts
- **Temporal dynamics**: session duration, idle periods, task switching frequency

All data were anonymized and stored in JSON format with millisecond-level timestamps.

### Feature Engineering

From raw interaction logs, we derived 47 behavioral features across six categories:

1. **Temporal**: session duration, idle time statistics, action density
2. **Error**: violation rates, correction frequency, invalid actions
3. **Navigation**: mouse entropy, scroll patterns, click distributions
4. **Cognitive**: task switching frequency, multitasking load index
5. **Resource Management**: budget adjustments, constraint satisfaction
6. **Interaction Quality**: hesitation patterns, completion efficiency

### Statistical Analysis

- **Normality testing**: Shapiro-Wilk tests
- **ANOVA**: Repeated-measures design with Greenhouse-Geisser correction
- **Effect sizes**: Partial eta-squared (η²), Cohen's *d*
- **Correlations**: Pearson *r* with Bonferroni correction for multiple comparisons

### Machine Learning Pipeline

**Preprocessing**:
- StandardScaler normalization
- Handling class imbalance via SMOTE (where applicable)
- Feature selection using mutual information

**Model Selection**:
- Baseline: Logistic Regression (L2 regularization)
- Primary: Random Forest (n_estimators=200, max_depth=15)
- Validation: Leave-One-User-Out cross-validation

**Hyperparameter Tuning**:
- Grid search over learning rate, regularization strength, tree depth
- Optimization criterion: F1-score (macro-averaged)

### Interpretability Analysis

**SHAP Framework**:
- TreeExplainer for Random Forest models
- Global importance via mean(|SHAP value|)
- Local explanations via waterfall plots
- Interaction detection via SHAP dependence plots

---

## Results and Discussion

Our findings establish behavioral telemetry as a valid, objective method for inferring cognitive load in digital environments. The strong correlations between specific behavioral patterns and validated psychometric measures (NASA-TLX) suggest that:

1. **Task complexity manifests in observable interaction patterns** — scheduling difficulty and constraint violations serve as reliable proxies for mental workload
2. **Machine learning can generalize across individuals** — high LOUO performance indicates behavioral signatures transcend individual differences
3. **Interpretability is achievable** — SHAP analysis provides actionable insights linking behaviors to cognitive states

### Implications for UX Design

These results enable data-driven adaptive interfaces:

- **Real-time load detection** during user interaction
- **Proactive interface simplification** when high load is detected
- **Personalized assistance** based on behavioral phenotypes
- **Intelligent defaults** for resource-constrained contexts

<p align="center">
  <img src="demo/02_mockups/A/low_vs_high_comparison.png" alt="Adaptive UI Comparison" width="700"/>
  <br>
  <em>Figure 4: Example adaptive interface responding to detected cognitive load</em>
</p>

---

## Applications

This framework can be applied to:

- **Educational technology**: Adaptive learning systems adjusting difficulty in real-time
- **Healthcare interfaces**: Clinical decision support reducing physician cognitive burden
- **E-commerce**: Checkout optimization based on user state detection
- **Enterprise software**: Workflow simplification for complex business processes
- **Accessibility**: Augmented interfaces for users with cognitive impairments

---

## Reproducibility

### System Requirements

- Python 3.10 or higher
- 8GB RAM minimum (16GB recommended for full pipeline)
- Dependencies listed in `requirements.txt`

### Installation

```bash
git clone https://github.com/yourusername/cognitive-load-analysis.git
cd cognitive-load-analysis
pip install -r requirements.txt
```

### Full Pipeline Execution

```bash
python run_all.py
```

This script executes:
1. Data preprocessing and feature extraction
2. Statistical validation tests
3. Machine learning training and evaluation
4. SHAP interpretability analysis
5. Visualization generation

**Detailed instructions**: See `docs/reproducibility.md`

**Expected runtime**: ~45 minutes on standard workstation

---

## Citation

If this work contributes to your research, please cite:

```bibtex
@misc{dyra2025cogload,
  title={Cognitive Load Analysis in Multi-Task Interaction Environments: 
         A Behavioral Modeling and Explainable AI Framework},
  author={Dyra},
  year={2025},
  howpublished={\url{https://github.com/yourusername/cognitive-load-analysis}},
  note={Research project on behavioral prediction of cognitive load}
}
```

### Related Publications

*[Add any conference papers, journal articles, or preprints here]*

---

## Acknowledgments

This research was conducted as part of [Your Institution/Program]. We thank participants for their time and the open-source community for tools enabling this work.

---

## Contact

**Researcher**: Dyra  
**Email**: [your.email@institution.edu]  
**Institution**: [Your University/Organization]

For questions, collaboration inquiries, or access to anonymized datasets, please reach out via email or open an issue in this repository.

---

## Ethical Considerations & Limitations

### Responsible Use
- **Human-in-the-Loop Design**: This framework is intended to inform UX design decisions and research insights, not to make autonomous decisions about user capabilities or restrictions.
- **Privacy-Preserving**: The pipeline processes behavioral telemetry only; no personally-identifying information is stored. All participant data is anonymized.
- **Transparency Focus**: All predictions are accompanied by SHAP explanations so researchers can verify and understand model decisions.

### Scope & Boundaries
- **Task Domain**: The system is optimized for productivity and planning tasks in web-based environments.
- **Language Focus**: Current studies target English-language interfaces; cross-lingual generalization has not been validated.
- **Validated Patterns**: The pipeline detects cognitive load patterns related to scheduling, resource management, and multi-tasking in digital contexts.

### Limitations
- **Sample Characteristics**: Current validation based on N=75 participants; larger-scale validation recommended for deployment.
- **Task Specificity**: Performance may vary with substantially different task types or interaction paradigms.
- **Temporal Dynamics**: Real-time deployment requires consideration of response latency and prediction stability.

### Development Roadmap
- **Short term**: Expand to additional task domains and interface types.
- **Medium term**: Incorporate individual difference models and adaptive threshold calibration.
- **Long term**: Multi-modal sensing (eye-tracking, physiological signals) and longitudinal validation studies.

---

## Performance & System Requirements

### Model Characteristics

| Component | Size | Performance | Notes |
|-----------|------|-------------|-------|
| Random Forest Classifier | ~15 MB | <10ms inference (CPU) | 200 trees, max_depth=15 |
| Feature Extraction Pipeline | N/A | ~50ms per session | Processes raw JSON logs |
| SHAP Explainer | ~20 MB | ~100ms per explanation | TreeExplainer for RF |

### Optimization Considerations
- **Real-time Deployment**: Feature extraction can be optimized with incremental computation for streaming contexts.
- **Batch Processing**: Current pipeline efficiently handles batch analysis of historical sessions.
- **Scalability**: Model size and inference speed suitable for edge deployment (e.g., browser extensions).

---

## How to Regenerate All Figures

To reproduce all visualizations from results:

```bash
python run_all.py
```

Or use the Makefile:

```bash
make figures
```

Figures will be saved to the `figures/` directory with subdirectories for each analysis type.

---

## Changelog

### Version 1.0.0 (2025-01-XX)
- Initial release with complete analysis pipeline
- Validated on 75 participants across three task conditions
- Achieved 96% classification accuracy with LOUO validation
- Published baseline comparisons and SHAP interpretability analysis
- Released adaptive UI demonstration examples

---

## Frequently Asked Questions

**Q: Can this framework detect cognitive load in real-time?**  
A: Yes, with feature extraction optimization. Current feature computation takes ~50ms per session; streaming implementation could reduce this for live detection.

**Q: How do I add new behavioral features?**
A: See `src/data_preparation/compute_features.py`. Add your feature computation to the extraction pipeline and update the feature list in `src/utils/metrics.py` (or other helper modules in `src/utils/`).

**Q: Can I use this with my own task data?**  
A: Yes. Format your interaction logs as JSON with timestamps and event types. See `data/examples/` for schema documentation.

**Q: What statistical power does the current sample provide?**  
A: With N=75 and large effect sizes (η²=0.54), power exceeds 0.99 for detecting main effects. See `docs/threats_to_validity.md` for detailed power analysis.

---

## Troubleshooting

### Common Issues

**Import Errors**
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt --upgrade
```

**Memory Issues During Training**
```bash
# Reduce batch size in config
# Or use incremental learning for large datasets
python src/modeling/train.py --batch_size 16
```

**SHAP Computation Timeout**
```bash
# Reduce sample size for SHAP analysis
python src/interpretation/shap_analysis.py --max_samples 1000
```

---

## Appendix: Additional Commands

### Run Individual Pipeline Stages

```bash
# Data preprocessing only
python src/data_preparation/load_data.py

# Feature extraction only
python src/data_preparation/compute_features.py

# Model training only
python src/modeling/train_louo_random_forest.py

# SHAP analysis only
python src/interpretation/shap_analysis.py

# Statistical tests only
python analysis/statistics/run_anova.py
```

### Custom Analysis

```bash
# Custom analyses and exports are handled via the pipeline orchestrator
# or the specific modules in `src/`. See `docs/reproducibility.md` for
# examples and usage. To run the full pipeline (including figure
# generation) use:
python run_all.py
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Data collection procedures were approved by [IRB/Ethics Committee] under protocol [NUMBER].