# Project: cognitive-load-analysis

Repository scaffold for cognitive load analysis project.

Structure:

- `data/` — raw and processed datasets
- `src/` — source code and modules
- `analysis/` — analysis scripts and notebooks
- `models/` — saved models and model code
- `results/` — model outputs and evaluation
- `docs/` — documentation
- `figures/` — plots and visuals
- `notebooks/` — Jupyter notebooks

Usage:

Add project content into the appropriate folders. Update this README with project-specific instructions.


//




How to run (example sequence)

Generate or confirm modeling CSV exists:

python src/data_preparation/generate_synthetic_data.py --out-csv data/processed/modeling_dataset_ultrarealistic.csv --raw-matching


(Optional) Run baseline evaluation:

python src/modeling/baselines.py --csv data/processed/modeling_dataset_ultrarealistic.csv --outdir results/modeling


(Optional but recommended) Run hyperparameter search (group-aware):

python src/modeling/hyperparameter_search.py --csv data/processed/modeling_dataset_ultrarealistic.csv --out models/rf_grid_search.joblib --n-jobs 4


Train RF with LOUO evaluation and save model:

python src/modeling/train_louo_random_forest.py --csv data/processed/modeling_dataset_ultrarealistic.csv --model-out models/tuned_random_forest_model.joblib --results-outdir results/modeling --do-search --grid-out models/rf_grid_search.joblib --n-jobs 4


Re-evaluate or run evaluation utility later:

python src/modeling/evaluate_model.py --model models/tuned_random_forest_model.joblib --csv data/processed/modeling_dataset_ultrarealistic.csv --outdir results/modeling


Save this as run_all.py at the repository root and run:

python run_all.py
# or to run without the heavy grid search:
python run_all.py --no-search
# to run with 4 parallel jobs for grid search:
python run_all.py --do-search --n-jobs 4