# ⚖️ Ethics Statement – CogniViz

This document outlines the ethical considerations, compliance measures, and participant protection protocols implemented during the CogniViz study. It covers procedures for informed consent, data anonymization, ethics review approval, and risk mitigation.

## 1. Overview

- CogniViz investigates real-time cognitive load detection based on user interaction patterns (e.g., mouse, keyboard, and cursor telemetry).
- All data collection was non-invasive, fully anonymized, and conducted under informed consent procedures approved by the relevant ethics review board.
- The study adheres to the ethical standards outlined in the ACM Code of Ethics (2018) and the Declaration of Helsinki (2013).

## 2. Informed Consent Procedures

### 2.1 Participant Recruitment

- Participants were recruited via internal university mailing lists and bulletin announcements.
- **Eligibility criteria:** Age ≥ 18, basic computer literacy, and familiarity with everyday web interfaces.
- Participation was voluntary, and no personally identifying information (PII) was collected.

### 2.2 Consent Process

Before participation, each individual:

**Received a written Information Sheet describing:**
- The study purpose and duration
- The nature of interaction logging (non-sensitive event capture only)
- The use of anonymized data for research and publication
- Rights to withdraw without penalty

**Signed a digital consent form via a secure web interface confirming that:**
- Participation is voluntary
- Interaction data will be anonymized and used for academic purposes only
- No physical, psychological, or privacy risk is expected

### 2.3 Right to Withdraw

Participants could withdraw their data at any point during or after participation by contacting the research team via the provided anonymized identifier.

## 3. Data Anonymization and De-Identification

### 3.1 Data Types Collected

Only interaction telemetry was logged:
- Mouse movement coordinates, click timing, drag actions
- Form focus changes and keystroke timings (no keystroke content)
- Idle-time and hover metrics
- Task identifiers (e.g., "form-entry", "travel-planning")

No personal text entries, names, emails, or other identifiable information were captured.

### 3.2 Anonymization Protocol

- Each participant was assigned a random alphanumeric ID (e.g., P01–P25).
- All telemetry data were stored under these pseudonyms.
- No linkable metadata (e.g., IP, device ID, or system username) was stored.
- Data were aggregated and normalized before analysis, ensuring that no re-identification was possible even indirectly.

### 3.3 Data Storage and Access

- All data were stored on encrypted university servers with access limited to authorized researchers.
- Raw telemetry was retained only for feature extraction, after which de-identified feature tables were used for analysis.
- The final dataset released for replication includes no PII and conforms to GDPR-compliant data sharing standards.

## 4. Ethics Board Review and Compliance

### 4.1 Institutional Review

The study protocol was reviewed and approved by the University Human Research Ethics Committee (HREC) under protocol number **HCI–2025–04** (Behavioral Interaction Study: Cognitive Load Estimation via Interaction Telemetry).

### 4.2 Compliance Frameworks

CogniViz adheres to the following ethical standards:
- ACM Ethics and Plagiarism Guidelines (2024 update)
- GDPR (EU General Data Protection Regulation) for data handling and anonymization
- APA Ethical Principles of Psychologists (2017) for human-participant research
- ISO 9241-210 principles for Human-Centered Design research

## 5. Risk Assessment and Mitigation

| Potential Risk | Description | Mitigation Measures |
|----------------|-------------|---------------------|
| Privacy concerns | Users may worry that their actions or typing are tracked. | Only non-sensitive interaction telemetry (e.g., clicks, movement) recorded. No text, identity, or content captured. |
| Psychological discomfort | Participants may feel monitored during interaction. | Clear briefing emphasized that no judgment or evaluation of ability was involved. Participants could stop anytime. |
| Data misuse risk | Re-identification or unauthorized access. | Strict anonymization, encrypted storage, and limited access to research team only. |
| Bias or unfair inference | Models might reflect task-specific behavioral biases. | Cross-task and cross-user validation (LOUO) to ensure generalizability and fairness. |

**Overall risk classification:** Minimal to none.

## 6. Data Retention and Sharing

- **Retention period:** De-identified feature data retained for 5 years post-publication for reproducibility.
- **Open access policy:** Only fully anonymized, aggregated datasets and code are shared publicly in the CogniViz repository and supplementary materials.
- No raw telemetry or identifiable logs are distributed.

## 7. Participant Debriefing

At the end of each session:
- Participants were provided with a debrief summary explaining the study's purpose and potential applications.
- Follow-up contact (optional) was offered to access the published findings or dataset summary.