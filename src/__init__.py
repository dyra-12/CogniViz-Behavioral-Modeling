"""
src package

Provides the full experimental pipeline:

 - data_preparation  : feature engineering from raw data
 - modeling          : LOUO evaluation, baselines, hyperparameter search
 - interpretation    : SHAP, clustering, feature importance
 - utils             : shared helpers for I/O, plotting, metrics

Import examples:
    from src.utils import read_json
    from src.modeling import train_louo_random_forest
    from src.interpretation import shap_analysis
"""
