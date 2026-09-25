from sklearn.pipeline import Pipeline as SklearnPipeline
from sklearn.linear_model import LogisticRegression

from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler


def train_balanced_model(
    preprocessor,
    X_train,
    y_train
):
    """
    Logistic Regression with class_weight='balanced'
    """

    model = SklearnPipeline([
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced"
            )
        )
    ])

    model.fit(
        X_train,
        y_train
    )

    return model


def train_smote_model(
    preprocessor,
    X_train,
    y_train
):
    """
    Logistic Regression with SMOTE
    """

    model = ImbPipeline([
        (
            "preprocessor",
            preprocessor
        ),
        (
            "smote",
            SMOTE(
                random_state=42
            )
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ])

    model.fit(
        X_train,
        y_train
    )

    return model


def train_undersample_model(
    preprocessor,
    X_train,
    y_train
):
    """
    Logistic Regression with Random UnderSampling
    """

    model = ImbPipeline([
        (
            "preprocessor",
            preprocessor
        ),
        (
            "undersample",
            RandomUnderSampler(
                random_state=42
            )
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ])

    model.fit(
        X_train,
        y_train
    )

    return model