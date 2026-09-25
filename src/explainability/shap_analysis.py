import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt


def run_shap_analysis(
    model_path,
    X_sample
):

    model = joblib.load(model_path)

    preprocessor = model.named_steps["preprocessor"]
    classifier = model.named_steps["classifier"]

    X_transformed = preprocessor.transform(X_sample)

    feature_names = (
        preprocessor.get_feature_names_out()
    )

    X_transformed_df = pd.DataFrame(
        X_transformed,
        columns=feature_names
    )

    explainer = shap.Explainer(
        classifier,
        X_transformed_df
    )

    shap_values = explainer(
        X_transformed_df
    )

    plt.figure(figsize=(12, 8))

    shap.plots.bar(
        shap_values,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        "artifacts/shap_feature_importance.png"
    )

    print(
        "SHAP plot saved successfully."
    )