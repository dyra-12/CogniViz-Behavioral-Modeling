"""
utils package

Provides shared utilities for:
 - File I/O (io_utils)
 - Plotting helpers (plot_utils)
 - ML metrics (metrics)

Import examples:
    from utils.io_utils import read_json
    from utils.plot_utils import save_fig
    from utils.metrics import compute_fold_metrics
"""

from .io_utils import (
    ensure_dir,
    read_json,
    write_json,
    save_df,
    load_modeling_csv,
    list_json_files,
    load_all_json
)

from .plot_utils import (
    save_fig,
    plot_bar,
    plot_scatter,
    plot_confusion_matrix
)

from .metrics import (
    compute_fold_metrics,
    aggregate_metrics,
    collect_misclassifications
)

__all__ = [
    # io_utils
    "ensure_dir", "read_json", "write_json", "save_df",
    "load_modeling_csv", "list_json_files", "load_all_json",

    # plot_utils
    "save_fig", "plot_bar", "plot_scatter", "plot_confusion_matrix",

    # metrics
    "compute_fold_metrics", "aggregate_metrics", "collect_misclassifications",
]
