# CogniViz Experiments

## Overview

This document describes the experimental methodology used to evaluate CogniViz, a browser-native, sensor-free framework for real-time cognitive load inference from natural interaction behavior. The experiments were designed to assess:

1. Whether cognitive load can be reliably inferred from interaction behavior alone  
2. Whether behavioral features generalize across users  
3. Whether inferred load aligns with subjective workload (NASA-TLX)  
4. Whether the model’s predictions are interpretable and psychologically meaningful  
5. Whether the system operates within real-time constraints  

The evaluation integrates controlled task design, interpretable feature engineering, participant-independent machine learning, and explanation-based analysis.

---

## 1. Study Design

### 1.1 Participants

The study included **25 participants**, recruited from a university population with mixed technical backgrounds. All participants completed all experimental tasks.

- Total participants: 25  
- Total task instances: 75 (25 participants × 3 tasks)  
- Design: within-subjects, counterbalanced  
- Input modality: mouse + keyboard  
- Environment: standard desktop browser  

Participants provided informed consent prior to participation. The study protocol was designed to align with established HCI workload research practices.

---

### 1.2 Tasks

Each participant completed three interactive web-based tasks designed to elicit increasing levels of cognitive load while preserving ecological validity.

#### Task 1: Form Completion (Low Cognitive Load)

Participants completed a linear shipping form requesting basic personal information.

- Minimal branching or decision complexity  
- Sequential interaction structure  
- Expected behavioral profile: fluent input, low hesitation, low correction frequency  

This task established a low-load baseline.

---

#### Task 2: Product Exploration (Medium Cognitive Load)

Participants browsed a product catalog, applied filters, compared items, and reset selections.

- Moderate decision complexity  
- Iterative refinement of criteria  
- Selective attention and trade-off reasoning  
- Expected behavioral profile: intermittent hesitation, exploratory navigation, moderate uncertainty  

This task elicited medium cognitive load.

---

#### Task 3: Travel Planning (High Cognitive Load)

Participants constructed a travel itinerary including flights, accommodations, and meetings.

- Multi-panel navigation  
- Drag-and-drop scheduling  
- Conflict detection and resolution  
- Budget constraints  
- Interdependent decision structure  
- Expected behavioral profile: prolonged planning, constraint violations, multitasking, recovery cycles  

This task elicited high cognitive load.

---

## 2. Behavioral Data Collection

### 2.1 Instrumentation

Interaction data were captured using native browser event listeners:

- Pointer events (move, click, drag)  
- Input events (keystrokes, field changes)  
- Focus and blur events  
- Hover and dwell events  

All events were time-stamped at millisecond resolution.

---

### 2.2 Feature Engineering

Raw interaction events were aggregated into **16 primary behavioral metrics** capturing:

- Temporal patterns (e.g., hesitation duration, idle time ratio)  
- Motor behavior (e.g., mouse entropy)  
- Decision complexity (e.g., scheduling difficulty, decision uncertainty)  
- Constraint conflict (e.g., constraint violation rate)  
- Multitasking behavior  
- Error recovery efficiency  

Features were grounded in cognitive load theory and prior micro-interaction research.

Only derived behavioral metrics were transmitted to the inference server. Raw interaction traces remained client-side.

---

## 3. Ground Truth Labeling

### 3.1 NASA-TLX Collection

Following each task, participants completed the NASA Task Load Index (NASA-TLX), comprising six subscales:

- Mental demand  
- Physical demand  
- Temporal demand  
- Performance  
- Effort  
- Frustration  

An overall workload score was computed as the unweighted mean of the six dimensions.

---

### 3.2 Cognitive Load Threshold

Cognitive load was operationalized as a binary classification target:

- **High Load:** NASA-TLX > 60  
- **Low Load:** NASA-TLX ≤ 60  

This threshold is widely used in workload research and reflects a practical separation between moderate and elevated subjective demand.

---

## 4. Validation Strategy

### 4.1 Participant-Independent Evaluation

To evaluate generalization across users, a **Leave-One-User-Out (LOUO)** cross-validation protocol was employed.

- In each fold, data from 24 participants were used for training  
- Data from the remaining participant were used for testing  
- No participant’s data appeared in both training and test sets  

This mirrors real-world deployment conditions where the system must infer cognitive load for previously unseen users.

---

### 4.2 Baselines

Three models of increasing complexity were evaluated:

1. **Majority-class baseline**  
   - Predicts the dominant class per fold  
   - Establishes a lower performance bound  

2. **Logistic Regression**  
   - Linear classifier  
   - Standardized features  
   - Balanced class weights  
   - Evaluates linear separability  

3. **Tuned Random Forest**  
   - Nonlinear classifier  
   - Balanced class weights  
   - Hyperparameters tuned via grid search  
   - Supports SHAP-based interpretability  

---

## 5. Model Training

### 5.1 Preprocessing

- Feature normalization using training-set statistics  
- No leakage across folds  
- StandardScaler applied for Logistic Regression  
- No scaling required for Random Forest  

---

### 5.2 Hyperparameter Optimization

Hyperparameters for the Random Forest model were optimized using grid search on the training split within each LOUO fold.

Key tuned parameters:

- Number of trees  
- Maximum tree depth  
- Minimum samples per leaf  
- Feature subsampling strategy  

---

## 6. Performance Metrics

Models were evaluated using the following metrics:

- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  

F1-score was treated as the primary metric due to moderate class imbalance.

---

## 7. Results Summary

### 7.1 Classification Performance

| Model              | Accuracy | Precision | Recall | F1   | ROC-AUC |
|--------------------|----------|-----------|--------|------|---------|
| Majority Baseline  | 0.73     | 0.05      | 0.02   | 0.03 | 0.50    |
| Logistic Regression| 0.92     | 0.68      | 0.72   | 0.69 | 0.84    |
| Random Forest      | 0.96     | 0.88      | 0.86   | 0.87 | 0.95    |

The tuned Random Forest achieved the strongest performance, demonstrating robust participant-independent inference.

---

### 7.2 Error Analysis

Misclassifications were concentrated near borderline NASA-TLX values (≈55–62).

Two systematic error modes emerged:

- **Under-reporters:**  
  Participants exhibited behavioral strain but reported low TLX  

- **Over-reporters:**  
  Participants reported high TLX despite efficient interaction behavior  

These discrepancies reflect known limitations of subjective workload measures.

False negatives (high load misclassified as low) were rare.

---

## 8. Behavioral Correlates of Cognitive Load

Univariate Pearson correlations revealed:

Strong positive correlates:

- Scheduling difficulty  
- Constraint violation rate  
- Budget management stress  
- Multitasking load  

Strong negative correlates:

- Recovery efficiency  
- Form efficiency  
- Form hesitation index  

These align with cognitive load theory and breakdown–repair models of interaction.

---

## 9. Explainability Analysis

### 9.1 Global SHAP

Global SHAP rankings showed:

- Budget management stress  
- Constraint violation rate  
- Idle time ratio  
- Scheduling difficulty  
- Planning time ratio  

as the most influential contributors to high-load predictions.

---

### 9.2 Local SHAP

Local explanations demonstrated:

- Coherent combinations of behavioral features drive predictions  
- Planning and constraint-related behaviors dominate high-load cases  
- Recovery efficiency dominates low-load cases  

Local explanations aligned with intuitive interpretations of observed behavior.

---

### 9.3 Explanation-Based Clustering

SHAP attribution vectors were clustered to identify recurring explanation profiles.

Two dominant clusters emerged:

1. Conflict-dominated planning breakdowns  
2. Efficient execution under complexity  

These clusters capture *how* cognitive load is expressed rather than only *whether* it is present.

---

## 10. Real-Time System Evaluation

### 10.1 Latency

- Model inference time: ~5–10 ms  
- End-to-end latency: 150–400 ms  
- Median latency: ~210 ms  
- 95th percentile latency: ~338 ms  

These values satisfy real-time responsiveness requirements for interactive systems.

---

### 10.2 Stability

Temporal smoothing and hysteresis prevented reactive or jittery adaptation.

Load transitions required sustained evidence across multiple windows.

---

## 11. Design Implications

Findings support the following design principles:

- Cognitive load emerges from sustained breakdown–repair cycles  
- Constraint conflict and planning complexity dominate workload  
- Interpretability is essential for adaptive interfaces  
- Adaptation should be proportional and context-specific  

---

## 12. Limitations

- Modest dataset size  
- Binary operationalization of cognitive load  
- Browser-only interaction context  
- Controlled task environments  

---

## 13. Reproducibility

To reproduce experiments:

1. Clone the repository  
2. Install dependencies  
3. Run feature extraction scripts  
4. Train models using the provided LOUO pipeline  
5. Evaluate performance metrics  
6. Generate SHAP explanations  

All experimental scripts are version-controlled.

---

## 14. Summary

The CogniViz experiments demonstrate that cognitive load can be inferred accurately, interpreted transparently, and operationalized in real time using interaction behavior alone. The participant-independent evaluation, interpretable modeling, and explanation-based analysis provide a rigorous foundation for cognitively adaptive interfaces.

