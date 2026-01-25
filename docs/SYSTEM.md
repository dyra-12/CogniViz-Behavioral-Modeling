# CogniViz System  
## Deployment, Infrastructure, and Runtime Architecture

## Overview

This document describes the operational system architecture of CogniViz, a browser-native, sensor-free framework for real-time cognitive load inference from natural interaction behavior. While the modeling and adaptation layers define *what* the system infers and *how* it responds, this file formalizes *how the system runs* as a deployable, low-latency, scalable Human–AI Interaction (HAI) service.

CogniViz is designed to operate as a closed-loop, real-time cognitive sensing system that:

- Captures interaction telemetry in the browser  
- Aggregates behavioral metrics locally  
- Performs server-side inference and explanation  
- Returns predictions and explanations to the client  
- Applies explanation-driven UI adaptation  

The system prioritizes **low latency, privacy preservation, interpretability, and deployability** under real-world web constraints.

---

## 1. System Architecture Summary

CogniViz follows a **three-tier distributed architecture**:

1. **Client Layer (Browser)**  
   - Event capture  
   - Local feature aggregation  
   - UI rendering  
   - Adaptation execution  

2. **Inference Layer (Server)**  
   - Feature normalization  
   - Machine learning inference  
   - SHAP explanation generation  

3. **Control Layer (Client)**  
   - Temporal smoothing  
   - Hysteresis logic  
   - Explanation-driven adaptation  

The system executes as a continuous loop with an end-to-end latency of approximately **150–400 ms** per inference cycle.

---

## 2. Client Layer

The client layer is implemented as a **React-based web application** instrumented with native browser event listeners.

---

### 2.1 Event Capture Module

The Event Capture Module listens to standard browser events:

- `pointermove`, `mousedown`, `mouseup`, `click`  
- `keydown`, `keyup`, `input`, `change`  
- `focus`, `blur`  
- `mouseenter`, `mouseleave`  
- `dragstart`, `dragover`, `drop`  

Each event is:

- Time-stamped at millisecond resolution  
- Associated with a UI element identifier  
- Buffered locally  

No raw keystrokes or content values are persisted.

---

### 2.2 Event Processing Module

Raw events are segmented into rolling temporal windows (150–300 ms).

Within each window, low-level statistics are computed:

- Cursor velocity, acceleration, entropy  
- Input latency and dwell time  
- Idle bursts  
- Hover oscillations  
- Error events  
- Correction attempts  

This enables high-frequency sensing while maintaining low computational overhead.

---

### 2.3 Metric Extractor

Low-level statistics are aggregated into higher-level behavioral metrics:

- Temporal features (hesitation, idle time ratio)  
- Decision complexity features (scheduling difficulty)  
- Constraint features (constraint violation rate)  
- Multitasking features  
- Recovery efficiency  
- Motor variability  

Only derived behavioral summaries are transmitted to the server.

---

### 2.4 Client-Side Control Logic

The client implements:

- Temporal smoothing  
- Hysteresis logic  
- Calibration phases  
- Adaptation thresholds  

This logic prevents reactive or jittery UI behavior.

---

## 3. Inference Layer

The inference layer is implemented as a **stateless FastAPI service**.

---

### 3.1 API Interface

The server exposes a lightweight HTTPS endpoint:

**POST /infer**

**Request payload:**

```json
{
  "participant_id": "p001",
  "task_id": "task_3_travel",
  "features": {
    "form_hesitation_index": 0.73,
    "constraint_violation_rate": 0.29,
    "idle_time_ratio": 0.34,
    ...
  }
}
