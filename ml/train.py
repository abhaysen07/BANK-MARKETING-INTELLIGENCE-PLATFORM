import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# ============================================================
# PATH SETUP (DO NOT CHANGE THIS)
# ============================================================

# Directory of this file → ml/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project root → BANK-MARKETING-INTELLIGENCE-PLATFORM/
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Models directory → ml/models/
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Feature columns file
FEATURE_COLUMNS_PATH = os.path.join(BASE_DIR, "feature_columns.txt")

# Processed dataset path
DATA_PATH = os.path.join(
    PROJECT_ROOT, "data", "processed", "bank_data_encoded.csv"
)

# Create models directory if not exists
os.makedirs(MODELS_DIR, exist_ok=True)

# ============================================================
# LOAD DATA
# ============================================================

data = pd.read_csv(DATA_PATH)

# ============================================================
# LOAD FEATURE COLUMNS (CRITICAL)
# ============================================================

with open(FEATURE_COLUMNS_PATH, "r") as f:
    feature_columns = [line.strip() for line in f.readlines()]

X = data[feature_columns]
y = data["y"]

# ============================================================
# TRAIN–TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ============================================================
# MODELS TO TRAIN
# ============================================================

models = {
    "logistic_regression": LogisticRegression(max_iter=1000),
    "random_forest": RandomForestClassifier(
        n_estimators=150,
        random_state=42
    ),
    "knn": KNeighborsClassifier(n_neighbors=9),
    "svm": SVC(probability=True),
    "naive_bayes": GaussianNB()
}

# ============================================================
# TRAIN & SAVE MODELS
# ============================================================

for name, model in models.items():
    print(f"\n🚀 Training {name}...")
    
    model.fit(X_train, y_train)
    
    model_path = os.path.join(MODELS_DIR, f"{name}.pkl")
    joblib.dump(model, model_path)
    
    print(f"[SAVED] {name} → {model_path}")

print("\n✅ All models trained and saved successfully.")
