# Feature Correlation Summary with Average NASA-TLX

This table summarizes Pearson correlations (r) between engineered behavioral features and average NASA-TLX across all tasks (N = 75).  
Only features with computed correlations are shown. p-values are two-tailed.

| Rank | Feature                      | Pearson r | p-value        | Direction |
|------|------------------------------|----------:|---------------:|:---------:|
| 1    | scheduling_difficulty        |   0.80662 | 2.4490e-18     | Positive  |
| 2    | constraint_violation_rate    |   0.80335 | 4.2449e-18     | Positive  |
| 3    | budget_management_stress     |   0.79824 | 9.8158e-18     | Positive  |
| 4    | multitasking_load            |   0.73257 | 1.7555e-13     | Positive  |
| 5    | drag_attempts                |   0.66377 | 8.5464e-11     | Positive  |
| 6    | recovery_efficiency         |  -0.61809 | 3.4593e-09     | Negative  |
| 7    | form_efficiency             |  -0.58485 | 3.5924e-08     | Negative  |
| 8    | form_hesitation_index       |  -0.53308 | 8.4885e-07     | Negative  |
| 9    | mouse_entropy_avg           |   0.53215 | 1.0632e-06     | Positive  |
| 10   | filter_optimization_score   |  -0.42474 | 1.6210e-04     | Negative  |
| 11   | planning_time_ratio         |   0.37699 | 8.5607e-04     | Positive  |
| 12   | rapid_hovers                |   0.19624 | 9.1526e-02     | Positive (ns) |

**Notes**
- (ns) indicates p > 0.05 (not statistically significant at α = 0.05).
- Table shows features for which correlation values were provided. Other features were either not computed in the supplied output or had non-significant correlations and are omitted here for brevity.
- Correlations were computed across all N = 75 samples (25 participants × 3 tasks).
