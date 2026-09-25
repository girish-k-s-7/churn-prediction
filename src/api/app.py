from fastapi import FastAPI
from src.schemas.prediction_schema import CustomerData

import pandas as pd
import joblib

from fastapi.middleware.cors import CORSMiddleware





# ==========================================
# Create FastAPI App
# ==========================================

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Load Model Once
# ==========================================

model = joblib.load(
    "artifacts/logistic_balanced.pkl"
)


# ==========================================
# Health Check
# ==========================================

@app.get("/")
def health_check():

    return {
        "status": "success",
        "message": "Customer Churn Prediction API is running"
    }


# ==========================================
# Prediction Endpoint
# ==========================================


@app.post("/predict")
def predict(data: CustomerData):

    input_df = pd.DataFrame([data.dict()])

    prediction = int(
        model.predict(input_df)[0]
    )

    probability = float(
        model.predict_proba(input_df)[0][1]
    )

    return {
        "prediction": prediction,
        "probability": probability
    }