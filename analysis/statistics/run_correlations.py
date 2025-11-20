#!/usr/bin/env python3
"""
analysis/statistics/run_correlations.py

Compute Pearson correlations between engineered features and NASA-TLX.
Produces:
 - overall correlations CSV
 - heatmap saved as PNG
 - per-task (task_id) correlation CSV


"""

import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

DEFAULT_CSV = "../../data/modeling_dataset.csv"

# Default feature list - adjust if your CSV uses slightly different names
DEFAULT_FEATURES = [
    "scheduling_difficulty",
    "constraint_violation_rate",
    "budget_management_stress",
    "multitasking_load",
    "drag_attempts",
    "recovery_efficiency",
    "form_efficiency",
    "form_hesitation_index",
    "mouse_entropy_avg",
    "filter_optimization_score",
    "planning_time_ratio",
    "rapid_hovers",
    "action_density",
    "idle_time_ratio",
    "exploration_breadth",
    "decision_uncertainty"
]

def ensure_dirs(out_dir):
    os.makedirs(out_dir, exist_ok=True)

def load_data(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV not found at {csv_path}")
    df = pd.read_csv(csv_path)
    return df

def detect_features(df, candidate_features):
    present = [f for f in candidate_features if f in df.columns]
    missing = [f for f in candidate_features if f not in df.columns]
    return present, missing

def compute_overall_correlations(df, features):
    results = []
    for f in features:
        try:
            x = pd.to_numeric(df[f].fillna(0.0), errors="coerce")
            y = pd.to_numeric(df["tlx"], errors="coerce")
            mask = (~x.isna()) & (~y.isna())
            if mask.sum() < 3:
                r, p = np.nan, np.nan
            else:
                r, p = pearsonr(x[mask], y[mask])
            direction = "positive" if (not np.isnan(r) and r > 0) else ("negative" if (not np.isnan(r) and r < 0) else "nan")
            results.append({"feature": f, "pearson_r": r, "p_value": p, "direction": direction, "n": int(mask.sum())})
        except Exception as e:
            results.append({"feature": f, "pearson_r": np.nan, "p_value": np.nan, "direction": "error", "n": 0})
    dfres = pd.DataFrame(results)
    dfres["rank"] = dfres["pearson_r"].abs().rank(ascending=False, method="first")
    dfres = dfres.sort_values("rank")
    return dfres

def compute_taskwise_correlations(df, features):
    rows = []
    for task, g in df.groupby("task_id"):
        for f in features:
            if f not in g.columns:
                rows.append({"task_id": task, "feature": f, "pearson_r": np.nan, "p_value": np.nan, "n": 0})
                continue
            x = pd.to_numeric(g[f].fillna(0.0), errors="coerce")
            y = pd.to_numeric(g["tlx"], errors="coerce")
            mask = (~x.isna()) & (~y.isna())
            if mask.sum() < 3:
                r, p = np.nan, np.nan
            else:
                r, p = pearsonr(x[mask], y[mask])
            rows.append({"task_id": task, "feature": f, "pearson_r": r, "p_value": p, "n": int(mask.sum())})
    return pd.DataFrame(rows)

def save_heatmap(df, features, out_path):
    # Build a matrix: features x [tlx] only - show correlation magnitudes
    corr_vals = {}
    for f in features:
        if f in df.columns:
            try:
                x = pd.to_numeric(df[f].fillna(0.0), errors="coerce")
                y = pd.to_numeric(df["tlx"], errors="coerce")
                mask = (~x.isna()) & (~y.isna())
                if mask.sum() >= 3:
                    r, _ = pearsonr(x[mask], y[mask])
                else:
                    r = np.nan
            except:
                r = np.nan
        else:
            r = np.nan
        corr_vals[f] = r
    series = pd.Series(corr_vals).rename("pearson_r")
    # Heatmap will be a single-column heatmap (features vs TLX)
    heat_df = series.to_frame().sort_values("pearson_r", ascending=False)
    plt.figure(figsize=(6, max(4, len(features)*0.25)))
    sns.heatmap(heat_df, annot=True, cmap="vlag", center=0, cbar_kws={"label": "Pearson r"})
    plt.title("Feature correlations with TLX (overall)")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()

def main(argv=None):
    """
    If argv is None, parse known args and ignore unknown (useful in Jupyter/Colab where the kernel injects args).
    If argv is a list, parse that list as usual (useful when calling from code or tests).
    """
    parser = argparse.ArgumentParser(description="Compute Pearson correlations between features and TLX.")
    parser.add_argument("--csv", type=str, default=DEFAULT_CSV, help="Path to modeling CSV (default: uploaded modeling dataset).")
    parser.add_argument("--outdir", type=str, default="analysis/results", help="Output directory for results/figures.")
    parser.add_argument("--features", type=str, default=None, help="Comma-separated list of features to analyze (overrides default list).")
    if argv is None:
        args, _unknown = parser.parse_known_args()
    else:
        args = parser.parse_args(argv)

    ensure_dirs(args.outdir)
    df = load_data(args.csv)

    # Normalize whitespace in column names for robustness
    df = df.rename(columns=lambda x: x.strip() if isinstance(x, str) else x)

    # Basic checks
    if "tlx" not in df.columns:
        # accept alternative capitalization
        if "TLX" in df.columns:
            df = df.rename(columns={"TLX": "tlx"})
        else:
            raise ValueError("Input CSV must contain 'tlx' column.")

    if args.features:
        features = [s.strip() for s in args.features.split(",")]
    else:
        features = DEFAULT_FEATURES

    present, missing = detect_features(df, features)
    if len(present) == 0:
        raise ValueError(f"None of the requested features found in CSV. Available columns: {list(df.columns)}")

    # Compute overall correlations
    corr_df = compute_overall_correlations(df, present)
    out_csv = os.path.join(args.outdir, "correlations_summary.csv")
    corr_df.to_csv(out_csv, index=False)

    # Compute taskwise correlations
    taskwise_df = compute_taskwise_correlations(df, present)
    taskwise_csv = os.path.join(args.outdir, "taskwise_feature_correlations.csv")
    taskwise_df.to_csv(taskwise_csv, index=False)

    # Save heatmap
    heatmap_path = os.path.join(args.outdir, "correlation_matrix_heatmap.png.png")
    save_heatmap(df, present, heatmap_path)

    # Also write a small textual summary file
    summary_txt = os.path.join(args.outdir, "correlations_summary.txt")
    with open(summary_txt, "w") as fh:
        fh.write("Feature correlations summary\n")
        fh.write("="*60 + "\n\n")
        fh.write("Features analyzed (present):\n")
        fh.write(", ".join(present) + "\n\n")
        fh.write("Missing features (not in CSV):\n")
        fh.write(", ".join(missing) + "\n\n")
        fh.write("Top correlations (absolute value):\n")
        top = corr_df.dropna(subset=["pearson_r"]).sort_values("pearson_r", key=lambda s: s.abs(), ascending=False).head(20)
        fh.write(top.to_string(index=False))
        fh.write("\n\nFull CSVs saved to:\n")
        fh.write(f"- {out_csv}\n- {taskwise_csv}\n- {heatmap_path}\n")

    print(f"Correlation analysis complete. Results saved to {args.outdir}")

if __name__ == "__main__":
    main()