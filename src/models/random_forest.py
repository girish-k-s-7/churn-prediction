from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier


def train_random_forest(
    preprocessor,
    X_train,
    y_train
):
    """
    Random Forest Baseline
    """

    model = Pipeline([
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
        )
    ])

    model.fit(
        X_train,
        y_train
    )

    return model