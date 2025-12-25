import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ============================================================
# PATH SETUP
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

MODELS_DIR = os.path.join(BASE_DIR, "models")
METRICS_DIR = os.path.join(BASE_DIR, "metrics")
FEATURE_COLUMNS_PATH = os.path.join(BASE_DIR, "feature_columns.txt")
DEFAULT_MODEL_PATH = os.path.join(BASE_DIR, "default_model.txt")

DATA_PATH = os.path.join(
    PROJECT_ROOT, "data", "processed", "bank_data_encoded.csv"
)

os.makedirs(METRICS_DIR, exist_ok=True)

# ============================================================
# LOAD DATA
# ============================================================

data = pd.read_csv(DATA_PATH)

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
# MODELS TO EVALUATE
# ============================================================

model_names = [
    "logistic_regression",
    "random_forest",
    "knn",
    "svm",
    "naive_bayes"
]

# ============================================================
# EVALUATION
# ============================================================

results = []

for model_name in model_names:
    model_path = os.path.join(MODELS_DIR, f"{model_name}.pkl")

    if not os.path.exists(model_path):
        print(f"⚠️ Model not found: {model_name}, skipping...")
        continue

    model = joblib.load(model_path)
    y_pred = model.predict(X_test)

    results.append({
        "model": model_name,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred)
    })

# ============================================================
# SAVE METRICS
# ============================================================

results_df = pd.DataFrame(results)

metrics_path = os.path.join(METRICS_DIR, "model_comparison.csv")
results_df.to_csv(metrics_path, index=False)

# ============================================================
# 🏆 AUTOMATIC BEST MODEL SELECTION (BY F1)
# ============================================================

best_model_row = results_df.loc[results_df["f1_score"].idxmax()]
best_model_name = best_model_row["model"]

with open(DEFAULT_MODEL_PATH, "w") as f:
    f.write(best_model_name)

# ============================================================
# OUTPUT
# ============================================================

print("\n📊 MODEL EVALUATION RESULTS")
print(results_df)

print("\n🏆 BEST MODEL SELECTED")
print(f"Model: {best_model_name}")
print(f"F1 Score: {best_model_row['f1_score']:.4f}")

print(f"\n✅ Default model saved to: {DEFAULT_MODEL_PATH}")
