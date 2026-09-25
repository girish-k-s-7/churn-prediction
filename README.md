# Customer Churn Prediction System

> End-to-end Machine Learning application that predicts customer churn using customer subscription and service information. Includes model training, explainability, REST API deployment, Docker support, and a live web interface.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-009688)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# Table of Contents

- [Overview](#overview)
- [Live Demo](#live-demo)
- [Features](#features)
- [Machine Learning Pipeline](#machine-learning-pipeline)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Explainability](#explainability)
- [Getting Started](#getting-started)
- [API Usage](#api-usage)
- [Docker Deployment](#docker-deployment)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

# Overview

Customer churn is one of the most important business problems in subscription-based industries.

This project predicts whether a customer is likely to leave a telecom service provider based on:

- Customer demographics
- Contract details
- Service subscriptions
- Billing information
- Internet usage services

The project includes:

- Data preprocessing
- Class imbalance handling
- Machine learning model training
- Model evaluation
- SHAP explainability
- FastAPI backend
- Interactive frontend
- Docker containerization
- Cloud deployment using Render

---

# Live Demo

### Frontend

🌐 Live Website

```text
https://YOUR-FRONTEND-URL.onrender.com
```

### Backend API

```text
https://YOUR-BACKEND-URL.onrender.com
```

### API Documentation

```text
https://YOUR-BACKEND-URL.onrender.com/docs
```

---

# Features

## Machine Learning

- Customer churn prediction
- Logistic Regression baseline
- Class imbalance handling
- Model comparison
- Probability prediction

## Explainability

- SHAP Feature Importance
- Model interpretation
- Feature contribution analysis

## Backend

- FastAPI REST API
- Pydantic validation
- Health check endpoint
- Prediction endpoint

## Frontend

- User-friendly interface
- Customer data form
- Live prediction results
- Churn probability display

## Deployment

- Dockerized application
- Render deployment
- Public API access

---

# Machine Learning Pipeline

## 1. Data Preprocessing

- Missing value handling
- Feature cleaning
- Categorical encoding
- Numerical feature scaling

## 2. Imbalance Handling

Since churn datasets are highly imbalanced:

- Logistic Regression Baseline
- Logistic Regression with Class Weight
- Random Undersampling
- SMOTE Oversampling

## 3. Model Training

Models evaluated:

- Logistic Regression
- Balanced Logistic Regression
- SMOTE Logistic Regression
- Random Forest

## 4. Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

# Tech Stack

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- Imbalanced-Learn
- SHAP

## Backend

- FastAPI
- Pydantic
- Uvicorn

## Frontend

- HTML
- CSS
- JavaScript

## Deployment

- Docker
- Render
- GitHub

---

# Dataset

### Telco Customer Churn Dataset

Dataset contains:

- Gender
- Senior Citizen Status
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming Services
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges

Target Variable:

```text
Churn
```

Values:

```text
0 = Customer Stays
1 = Customer Leaves
```

---

# Project Structure

```text
churn-prediction
│
├── artifacts
│   ├── logistic_baseline.pkl
│   ├── logistic_balanced.pkl
│   ├── logistic_smote.pkl
│   ├── logistic_undersample.pkl
│   ├── random_forest.pkl
│   └── shap_feature_importance.png
│
├── data
│   └── Telco-Customer-Churn.csv
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── notebooks
│   └── 01_eda.ipynb
│
├── src
│   ├── api
│   │   └── app.py
│   │
│   ├── data
│   │   ├── load_data.py
│   │   └── preprocess.py
│   │
│   ├── experiments
│   │   └── imbalance.py
│   │
│   ├── explainability
│   │   └── shap_analysis.py
│   │
│   ├── models
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   ├── random_forest.py
│   │   └── random_forest_tune.py
│   │
│   └── schemas
│       └── prediction_schema.py
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

---

# Explainability

SHAP (SHapley Additive exPlanations) is used to understand model behavior.

Generated output:

```text
artifacts/shap_feature_importance.png
```

Provides:

- Most influential features
- Positive churn contributors
- Negative churn contributors
- Model transparency

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/girish-k-s-7/churn-prediction.git

cd churn-prediction
```

## Create Virtual Environment

Linux:

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn src.api.app:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

## Run Frontend

Open:

```text
frontend/index.html
```

Or:

```bash
python -m http.server 5500
```

---

# API Usage

## Health Check

```http
GET /
```

Response:

```json
{
  "status": "success",
  "message": "Customer Churn Prediction API is running"
}
```

---

## Predict Churn

```http
POST /predict
```

Example Request:

```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 24,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "Yes",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "Yes",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "One year",
  "PaperlessBilling": "No",
  "PaymentMethod": "Credit card (automatic)",
  "MonthlyCharges": 55.5,
  "TotalCharges": 1200.0
}
```

Response:

```json
{
  "prediction": 0,
  "probability": 0.13
}
```

---

# Docker Deployment

## Build Docker Image

```bash
docker build -t churn-prediction .
```

## Run Docker Container

```bash
docker run -p 8000:8000 churn-prediction
```

---

# Future Improvements

- XGBoost Model
- LightGBM Model
- Hyperparameter Optimization
- Optuna Tuning
- User Authentication
- Prediction History
- Streamlit Dashboard
- CI/CD Pipeline
- Monitoring and Logging

---

# Author

**Girish**

Aspiring:

- Machine Learning Engineer
- AI Engineer
- Data Scientist

GitHub:

```text
https://github.com/girish-k-s-7
```

---

## License

This project is licensed under the MIT License.