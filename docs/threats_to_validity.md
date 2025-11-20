# Threats to Validity

This study and its results are subject to several important validity threats. We describe them here and indicate mitigations where applicable.

## Internal Validity
- **Synthetic dataset design.** The modeling dataset used for several experiments is synthetically generated to reflect realistic interaction patterns. While this enables rigorous testing and controlled manipulations, it may not capture all idiosyncratic behaviors present in real users. *Mitigation:* future work will validate the pipeline on collected human subject data and open datasets.
- **Confounding features.** Some engineered features may co-vary (e.g., idle_time_ratio and planning_time_ratio), potentially inflating apparent effect sizes. *Mitigation:* we used correlation analysis and SHAP-based explanations to detect multicollinearity; future models can incorporate feature selection or regularization.
- **Sample size per user for LOUO.** LOUO folds leave only 3 samples per participant for testing (one per task). This small per-fold test size can produce high variance in fold-wise metrics. *Mitigation:* we report aggregated metrics across folds and inspect per-participant failure modes.

## Construct Validity
- **Subjective measures vs. behavioral proxies.** NASA-TLX measures perceived workload; behavioral signals reflect operational indicators. Divergences between the two can arise (e.g., users reporting high TLX despite efficient behaviors). This limits direct interpretability. *Mitigation:* pairwise analyses and qualitative follow-ups (e.g., think-aloud protocols) are recommended.
- **Feature operationalization.** The choice of thresholds, binning, and aggregation windows (for entropy, idle periods, drag attempts) can influence results. *Mitigation:* sensitivity analyses should be performed to ensure robustness to reasonable parameter choices.

## External Validity
- **Generalizability to other populations.** The dataset reflects the demographics and contexts assumed in the synthetic design; generalization to different user groups, device types (mobile vs. desktop), or cultural contexts is not guaranteed. *Mitigation:* replicate studies with diverse participants and platforms.
- **Domain transfer.** Task-specific features (e.g., scheduling_difficulty) may not directly transfer across UI domains beyond forms, product pages, and travel planners. *Mitigation:* identify and rely more heavily on universal features (mouse entropy, action density, idle ratio) for cross-domain models.

## Conclusion Validity
- **Multiple comparisons and statistical significance.** Numerous correlations and model evaluations were computed; without appropriate corrections (e.g., Bonferroni), some reported p-values may be optimistic. *Mitigation:* report effect sizes, confidence intervals, and where appropriate adjust for multiple testing.
- **Synthetic effect inflation.** Because the synthetic dataset was constructed to reflect hypothesized relationships, effect sizes may be larger than in real-world data. *Mitigation:* empirical validation with naturalistic data is required.

---

**Summary:** The current work provides a rigorous proof-of-concept demonstrating that behavioral features can predict reported cognitive load and that adaptive UI strategies can be driven by such models. Nevertheless, the above threats highlight the importance of empirical validation, sensitivity analyses, and careful feature operationalization before deployment in real-world systems.
