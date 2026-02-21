# CogniViz — Demo Screenshots

This directory contains representative interface screenshots from the **CogniViz** research system, illustrating real-time cognitive load inference and explanation-driven adaptive interface behavior across three experimental tasks.

These screenshots document how cognitive load is detected, explained, and operationalized within the interactive system.

---

## Overview

CogniViz models cognitive load as a **dynamic interaction state** inferred from behavioral telemetry (cursor activity, hesitation, error recovery, planning pauses, and constraint violations).

The interface presents:

- Real-time cognitive load estimation
- Behavioral explanations for inferred states
- Task-specific adaptive UI responses

The figures below capture typical system states observed during controlled experimental sessions.

---

## Task 1 — Form Completion (Low Load / Calibration)

**File:** `cogniviz_task1_form_low_load_calibration.png`

This screenshot shows the initial calibration phase and a stable low-load interaction state during linear form completion.

Key characteristics:

- Smooth field-to-field navigation
- Minimal hesitation or corrections
- Stable focus transitions
- No adaptive intervention required

This condition establishes a baseline behavioral profile for low cognitive load.

---

## Task 1 — Form Completion (Medium Load / Hesitation)

**File:** `cogniviz_task1_form_medium_load_hesitation.png`

This screenshot illustrates a moderate cognitive load state triggered by temporary hesitation during form entry.

Key indicators:

- Increased idle time
- Interrupted input flow
- Localized adaptive pacing message
- Explanation highlighting behavioral causes

The system applies proportional, non-intrusive assistance to maintain task continuity.

---

## Task 2 — Product Exploration (Medium Load)

**File:** `cogniviz_task2_exploration_medium_load.png`

This screenshot shows cognitive load arising during exploratory decision-making in a product comparison task.

Behavioral signals include:

- Frequent option switching
- Filter adjustments
- Hover-based comparison
- Decision uncertainty patterns

Moderate load is treated as a **productive cognitive state** rather than a failure condition.

---

## Task 2 — Adaptive Comparison Assist

**File:** `cogniviz_task2_adaptive_comparison_assist.png`

This figure demonstrates explanation-driven UI adaptation during sustained comparison activity.

Adaptive behavior includes:

- Contextual comparison overlays
- Highlighting frequently referenced attributes
- Reduction of cognitive search effort

Adaptations are reversible and triggered only under sustained behavioral evidence.

---

## Task 3 — Travel Planning (Medium Load)

**File:** `cogniviz_task3_planning_medium_load.png`

This screenshot captures early-stage planning activity in a multi-constraint scheduling environment.

Behavioral characteristics:

- Active exploration of options
- Planning pauses
- Initial constraint awareness

The system interprets this as expected cognitive engagement rather than overload.

---

## Task 3 — Travel Planning (High Load / Constraint Conflict)

**File:** `cogniviz_task3_planning_high_load_constraints.png`

This screenshot illustrates a high cognitive load state caused by repeated constraint violations and breakdown-repair cycles.

Key indicators:

- Recurring scheduling conflicts
- Failed adjustments
- Extended idle periods following errors
- Slow conflict resolution

The interface provides explanatory feedback to support recovery while preserving user autonomy.

---

## Research Significance

These screenshots demonstrate that cognitive load can be:

- Inferred from natural interaction behavior
- Explained using interpretable behavioral features
- Operationalized through real-time adaptive interface responses

without reliance on physiological sensors or intrusive monitoring.

---

## Note

These images are representative research artifacts from controlled experimental sessions and are intended for documentation, demonstration, and academic review purposes.