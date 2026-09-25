import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df.dropna(inplace=True)

    df.drop(
        columns=["customerID"],
        inplace=True
    )

    return df