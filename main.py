from src.data.load_data import load_data

from src.data.preprocess import (
    split_data,
    create_preprocessor
)

from src.models.train import train_model
from src.models.evaluate import evaluate_model

from src.experiments.imbalance import (
    train_balanced_model,
    train_smote_model,
    train_undersample_model
)

import joblib
from src.models.random_forest import (
    train_random_forest
)
from src.models.random_forest_tune import (
    train_tuned_random_forest
)
from src.explainability.shap_analysis import (
    run_shap_analysis
)

# ==========================================
# Load Dataset
# ==========================================

df = load_data(
    "data/raw/Telco-Customer-Churn.csv"
)


# ==========================================
# Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = split_data(df)


# ==========================================
# Create Preprocessor
# ==========================================

preprocessor = create_preprocessor(X_train)


# ==========================================
# BASELINE MODEL
# ==========================================

print("\n" + "=" * 60)
print("BASELINE LOGISTIC REGRESSION")
print("=" * 60)

baseline_model = train_model(
    preprocessor,
    X_train,
    y_train
)

evaluate_model(
    baseline_model,
    X_test,
    y_test
)

joblib.dump(
    baseline_model,
    "artifacts/logistic_baseline.pkl"
)


# ==========================================
# BALANCED MODEL
# ==========================================

print("\n" + "=" * 60)
print("BALANCED LOGISTIC REGRESSION")
print("=" * 60)

balanced_model = train_balanced_model(
    preprocessor,
    X_train,
    y_train
)

evaluate_model(
    balanced_model,
    X_test,
    y_test
)

joblib.dump(
    balanced_model,
    "artifacts/logistic_balanced.pkl"
)


# ==========================================
# SMOTE MODEL
# ==========================================

print("\n" + "=" * 60)
print("SMOTE LOGISTIC REGRESSION")
print("=" * 60)

smote_model = train_smote_model(
    preprocessor,
    X_train,
    y_train
)

evaluate_model(
    smote_model,
    X_test,
    y_test
)

joblib.dump(
    smote_model,
    "artifacts/logistic_smote.pkl"
)


# ==========================================
# UNDERSAMPLING MODEL
# ==========================================

print("\n" + "=" * 60)
print("UNDERSAMPLING LOGISTIC REGRESSION")
print("=" * 60)

undersample_model = train_undersample_model(
    preprocessor,
    X_train,
    y_train
)

evaluate_model(
    undersample_model,
    X_test,
    y_test
)

joblib.dump(
    undersample_model,
    "artifacts/logistic_undersample.pkl"
)

# ==========================================
# RANDOM FOREST
# ==========================================

print("\n" + "=" * 60)
print("RANDOM FOREST")
print("=" * 60)

rf_model = train_random_forest(
    preprocessor,
    X_train,
    y_train
)

evaluate_model(
    rf_model,
    X_test,
    y_test
)

joblib.dump(
    rf_model,
    "artifacts/random_forest.pkl"
)


# ==========================================
# RANDOM FOREST TUNED
# ==========================================

print("\n" + "=" * 60)
print("TUNED RANDOM FOREST")
print("=" * 60)

rf_tuned = train_tuned_random_forest(
    preprocessor,
    X_train,
    y_train
)

evaluate_model(
    rf_tuned,
    X_test,
    y_test
)

joblib.dump(
    rf_tuned,
    "artifacts/random_forest_tuned.pkl"
)

# ==========================================
# SHAP ANALAYSIS
# ==========================================

print("\nGenerating SHAP Analysis...")

run_shap_analysis(
    "artifacts/logistic_balanced.pkl",
    X_test.head(100)
)

# ==========================================
# COMPLETE
# ==========================================

print("\n" + "=" * 60)
print("ALL MODELS TRAINED SUCCESSFULLY")
print("=" * 60)

print("\nSaved Models:")
print("1. logistic_baseline.pkl")
print("2. logistic_balanced.pkl")
print("3. logistic_smote.pkl")
print("4. logistic_undersample.pkl")
print("5. random_forest.pkl")
print("6. random_forest_tuned.pkl")