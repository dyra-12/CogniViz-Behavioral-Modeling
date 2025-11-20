#!/usr/bin/env python3
"""
analysis/statistics/run_anova.py

Repeated-measures ANOVA on NASA-TLX across tasks (Task 1, Task 2, Task 3).
Performs:
 - data loading (default CSV path)
 - basic checks
 - Repeated measures ANOVA (statsmodels AnovaRM)
 - Pairwise post-hoc paired t-tests (Bonferroni corrected)
 - Saves results and a TLX boxplot to analysis/results/

"""

import os
import argparse
import textwrap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.anova import AnovaRM
from scipy.stats import ttest_rel

# Default path to the modeling CSV (the file you uploaded)
DEFAULT_CSV = "../../data/modeling_dataset.csv"

def ensure_dirs(out_dir):
    os.makedirs(out_dir, exist_ok=True)

def load_data(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV not found at {csv_path}")
    df = pd.read_csv(csv_path)
    return df

def prepare_tlx_dataframe(df):
    # Expect participantId, task_id, tlx columns
    # Normalize column names
    df = df.rename(columns=lambda x: x.strip())
    required = {"participantId", "task_id", "tlx"}
    if not required.issubset(set(df.columns)):
        # try alternative column names
        alt_map = {}
        if "participantId" not in df.columns and "participant_id" in df.columns:
            alt_map["participant_id"] = "participantId"
        if "task_id" not in df.columns and "task" in df.columns:
            alt_map["task"] = "task_id"
        if "tlx" not in df.columns and "TLX" in df.columns:
            alt_map["TLX"] = "tlx"
        if alt_map:
            df = df.rename(columns=alt_map)
    if not required.issubset(set(df.columns)):
        raise ValueError(f"Input CSV must contain columns: {required}. Found: {list(df.columns)}")
    # keep only needed cols
    df = df[["participantId", "task_id", "tlx"]].dropna()
    # Ensure participantId is categorical
    df["participantId"] = df["participantId"].astype(str)
    df["task_id"] = df["task_id"].astype(str)
    df["tlx"] = pd.to_numeric(df["tlx"], errors="coerce")
    df = df.dropna(subset=["tlx"])
    return df

def run_anova(df):
    # AnovaRM expects a wide-ish long-format: subject, within, dv
    # Ensure enough data per subject
    counts = df.groupby("participantId")["task_id"].nunique()
    if (counts < 2).any():
        raise ValueError("Each participant must have TLX for at least 2 tasks for repeated-measures ANOVA.")
    # Fit AnovaRM
    aov = AnovaRM(df, depvar="tlx", subject="participantId", within=["task_id"])
    res = aov.fit()
    return res

def pairwise_posthoc(df, out_fh):
    # Create wide table with participantId as index, columns per task_id
    pivot = df.pivot_table(index="participantId", columns="task_id", values="tlx", aggfunc="mean")
    pivot = pivot.dropna(axis=0, how="any")  # only participants with all tasks
    tasks = pivot.columns.tolist()
    n = len(tasks)
    out_fh.write("\nPairwise paired t-tests (Bonferroni corrected):\n")
    comparisons = []
    for i in range(n):
        for j in range(i+1, n):
            t, p = ttest_rel(pivot.iloc[:, i], pivot.iloc[:, j])
            comparisons.append((tasks[i], tasks[j], t, p))
    # Bonferroni correction
    m = len(comparisons)
    out_fh.write(f"Number of comparisons = {m}. Bonferroni alpha = 0.05/{m} = {0.05/m:.5f}\n\n")
    for a, b, t, p in comparisons:
        p_bonf = min(p * m, 1.0)
        out_fh.write(f"{a} vs {b}: t = {t:.4f}, p = {p:.4e}, p_bonf = {p_bonf:.4e}\n")
    out_fh.write("\nNote: Paired t-tests require participants to have TLX in both tasks.\n")

def save_boxplot(df, out_path):
    sns.set(style="whitegrid")
    plt.figure(figsize=(6,5))
    order = sorted(df["task_id"].unique())
    ax = sns.boxplot(x="task_id", y="tlx", data=df, order=order)
    ax = sns.stripplot(x="task_id", y="tlx", data=df, order=order, color="black", size=4, jitter=True, alpha=0.7)
    ax.set_xlabel("Task")
    ax.set_ylabel("NASA-TLX (raw score)")
    ax.set_title("Task-wise NASA-TLX distribution")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()

def main(argv=None):
    """
    If argv is None, parse known args and ignore unknown (useful in Jupyter/Colab where the kernel injects args).
    If argv is a list, parse that list as usual (useful when calling from code or tests).
    """
    parser = argparse.ArgumentParser(description="Run repeated-measures ANOVA on TLX across tasks.")
    parser.add_argument("--csv", type=str, default=DEFAULT_CSV, help="Path to modeling CSV (default: uploaded modeling dataset).")
    parser.add_argument("--outdir", type=str, default="analysis/results", help="Output directory for results/figures.")
    if argv is None:
        # In environments like Jupyter/Colab the process argv contains kernel arguments (-f ...).
        # parse_known_args will return (known_args, unknown_args) and won't raise on the kernel's extra flags.
        args, _unknown = parser.parse_known_args()
    else:
        args = parser.parse_args(argv)

    ensure_dirs(args.outdir)
    df_raw = load_data(args.csv)
    df = prepare_tlx_dataframe(df_raw)

    # Basic descriptive stats
    desc = df.groupby("task_id")["tlx"].describe()

    anova_res = run_anova(df)

    out_file = os.path.join(args.outdir, "anova_results.txt")
    with open(out_file, "w") as fh:
        fh.write("Repeated-Measures ANOVA on NASA-TLX\n")
        fh.write("="*60 + "\n\n")
        fh.write("Descriptive statistics by task:\n")
        fh.write(desc.to_string())
        fh.write("\n\nANOVA results:\n")
        fh.write(anova_res.summary().as_text())
        fh.write("\n\n")
        # Post-hoc paired t-tests
        pairwise_posthoc(df, fh)

    # Save boxplot
    boxplot_path = os.path.join(args.outdir, "tlx_boxplot.png")
    save_boxplot(df, boxplot_path)

    print(f"ANOVA complete. Results written to: {out_file}")
    print(f"Boxplot saved to: {boxplot_path}")

if __name__ == "__main__":
    main()