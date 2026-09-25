from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)


def evaluate_model(
    model,
    X_test,
    y_test
):

    y_pred = model.predict(X_test)

    y_prob = model.predict_proba(
        X_test
    )[:, 1]

    print("\nClassification Report")
    print("=" * 50)
    print(
        classification_report(
            y_test,
            y_pred
        )
    )

    print("\nConfusion Matrix")
    print("=" * 50)
    print(
        confusion_matrix(
            y_test,
            y_pred
        )
    )

    print("\nROC AUC Score")
    print("=" * 50)
    print(
        roc_auc_score(
            y_test,
            y_prob
        )
    )