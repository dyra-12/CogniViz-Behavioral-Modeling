#!/usr/bin/env python3
"""
plot_utils.py
Centralized plotting utilities for consistent visual style.

Used by:
 - modeling (evaluation plots)
 - interpretation (SHAP plots)
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import numpy as np

sns.set(style="whitegrid", font_scale=1.2)


# ------------------------------------------------------------------
# Figure saving helper
# ------------------------------------------------------------------

def save_fig(path: str, dpi=300):
    """Safely save current Matplotlib figure."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=dpi)
    plt.close()


# ------------------------------------------------------------------
# Bar plot utility
# ------------------------------------------------------------------

def plot_bar(series, title, xlabel, ylabel, outpath):
    plt.figure(figsize=(8, 5))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    save_fig(outpath)


# ------------------------------------------------------------------
# Scatter / PCA plots
# ------------------------------------------------------------------

def plot_scatter(x, y, labels, title, outpath):
    plt.figure(figsize=(7, 6))
    plt.scatter(x, y, c=labels, cmap="coolwarm", s=80)
    plt.title(title)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    save_fig(outpath)


# ------------------------------------------------------------------
# Confusion matrix (used in modeling/evaluation)
# ------------------------------------------------------------------

def plot_confusion_matrix(y_true, y_pred, outpath, title="Confusion Matrix"):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("True")
    save_fig(outpath)
