import os
import joblib
import pandas as pd
from datetime import datetime

from app.core.config import (
    MODELS_DIR,
    FEATURE_COLUMNS_PATH,
    DEFAULT_MODEL_PATH
)

# ============================================================
# LOAD FEATURE SCHEMA (ORDER IS CRITICAL)
# ============================================================

with open(FEATURE_COLUMNS_PATH, "r") as f:
    FEATURE_COLUMNS = [line.strip() for line in f.readlines()]

# ============================================================
# LOAD DEFAULT MODEL (GOVERNANCE)
# ============================================================

with open(DEFAULT_MODEL_PATH, "r") as f:
    MODEL_NAME = f.read().strip()

MODEL_PATH = os.path.join(MODELS_DIR, f"{MODEL_NAME}.pkl")
model = joblib.load(MODEL_PATH)

# ============================================================
# CATEGORICAL PREFIX MAP (RAW → ONE-HOT)
# ============================================================

CATEGORICAL_PREFIX = {
    "job": "job_",
    "marital": "marital_",
    "education": "education_",
    "contact": "contact_",
    "month": "month_",
    "poutcome": "poutcome_"
}

# ============================================================
# ALLOWED CATEGORIES FOR VALIDATION
# ============================================================

ALLOWED_CATEGORIES = {
    "job": [
        "admin.", "blue-collar", "entrepreneur", "housemaid",
        "management", "retired", "self-employed", "services",
        "student", "technician", "unemployed", "unknown"
    ],
    "marital": ["divorced", "married", "single"],
    "education": ["primary", "secondary", "tertiary", "unknown"],
    "contact": ["cellular", "telephone", "unknown"],
    "month": [
        "jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec"
    ],
    "poutcome": ["failure", "other", "success", "unknown"]
}



# ============================================================
# PREDICTION LOGGING (STEP 3)
# ============================================================

LOG_FILE = "prediction_logs.csv"

def log_prediction(input_data: dict, output: dict): # type: ignore
    with open(LOG_FILE, "a") as f:
        f.write(
            f"{datetime.now()},"
            f"{output['prediction']},"
            f"{output['probability']},"
            f"{output['confidence']}\n"
        )

# ============================================================
# MAIN PREDICTION FUNCTION
# ============================================================

def predict_customer(input_data: dict) -> dict: # type: ignore
    """
    Raw input → encoded vector → model → business decision
    """

    # --------------------------------------------------------
    # STEP 1: Zero-initialize feature vector
    # --------------------------------------------------------
    features = {col: 0 for col in FEATURE_COLUMNS}

    # --------------------------------------------------------
    # STEP 2: Numeric + binary features (AS TRAINED)
    # --------------------------------------------------------
    numeric_binary = [
        "age", "balance", "day", "duration",
        "campaign", "pdays", "previous",
        "default", "housing", "loan"
    ]

    for col in numeric_binary:
        features[col] = int(input_data[col]) # type: ignore

    # --------------------------------------------------------
    # STEP 3: Controlled one-hot encoding
    # --------------------------------------------------------
    for raw_col, prefix in CATEGORICAL_PREFIX.items():
        value = input_data[raw_col] # type: ignore

        if value not in ALLOWED_CATEGORIES[raw_col]:
            raise ValueError(
                f"Invalid value '{value}' for '{raw_col}'. "
                f"Allowed: {ALLOWED_CATEGORIES[raw_col]}"
            )

        encoded_col = f"{prefix}{value}"
        features[encoded_col] = 1

    # --------------------------------------------------------
    # STEP 4: DataFrame with exact feature order
    # --------------------------------------------------------
    df = pd.DataFrame(
        [[features[col] for col in FEATURE_COLUMNS]],
        columns=FEATURE_COLUMNS
    )

    # --------------------------------------------------------
    # STEP 5: Prediction
    # --------------------------------------------------------
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    # --------------------------------------------------------
    # STEP 6: BUSINESS INTERPRETATION (STEP 1)
    # --------------------------------------------------------
    confidence = (
        "High" if prob >= 0.7 else
        "Medium" if prob >= 0.4 else
        "Low"
    )

    recommendation = (
        "Contact customer" if prob >= 0.5
        else "Do not contact"
    )

    result = { # type: ignore
        "prediction": "yes" if pred == 1 else "no",
        "probability": round(float(prob), 4),
        "confidence": confidence,
        "recommendation": recommendation
    }

    # --------------------------------------------------------
    # STEP 7: Log prediction
    # --------------------------------------------------------
    log_prediction(input_data, result)

    return result # type: ignore
