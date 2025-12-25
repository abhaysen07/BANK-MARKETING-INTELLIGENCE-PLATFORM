import pandas as pd
import os

# -----------------------------
# Paths
# -----------------------------
RAW_DATA_PATH = "data/raw/bank-full.csv"
PROCESSED_DATA_PATH = "data/processed/bank_data_encoded.csv"
FEATURE_COLUMNS_PATH = "ml/feature_columns.txt"

# -----------------------------
# Load raw data
# -----------------------------
df = pd.read_csv(RAW_DATA_PATH, sep=";")

# -----------------------------
# Target encoding (y)
# -----------------------------
df["y"] = df["y"].map({"no": 0, "yes": 1})

# -----------------------------
# Separate column groups
# -----------------------------
numeric_cols = [
    "age",
    "balance",
    "day",
    "duration",
    "campaign",
    "pdays",
    "previous"
]

binary_cols = [
    "default",
    "housing",
    "loan"
]

categorical_cols = [
    "job",
    "marital",
    "education",
    "contact",
    "month",
    "poutcome"
]

# -----------------------------
# Process numeric columns (NO CHANGE)
# -----------------------------
df_numeric = df[numeric_cols]

# -----------------------------
# Process binary columns (yes/no → 1/0)
# -----------------------------
binary_map = {"yes": 1, "no": 0}
df_binary = df[binary_cols].replace(binary_map)

# -----------------------------
# Process categorical columns (One-Hot)
# -----------------------------
df_categorical = pd.get_dummies(
    df[categorical_cols],
    drop_first=False
)

# FORCE one-hot to int (THIS IS CRITICAL)
df_categorical = df_categorical.astype(int)

# -----------------------------
# Combine ALL features
# -----------------------------
df_features = pd.concat(
    [df_numeric, df_binary, df_categorical],
    axis=1
)

# -----------------------------
# Append target column at END
# -----------------------------
df_final = df_features.copy()
df_final["y"] = df["y"]

# -----------------------------
# Save feature column order
# -----------------------------
feature_columns = df_features.columns.tolist()

os.makedirs(os.path.dirname(FEATURE_COLUMNS_PATH), exist_ok=True)
with open(FEATURE_COLUMNS_PATH, "w") as f:
    for col in feature_columns:
        f.write(col + "\n")

# -----------------------------
# Save processed dataset
# -----------------------------
os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
df_final.to_csv(PROCESSED_DATA_PATH, index=False)

print("✅ Preprocessing completed successfully")
print(f"📄 Saved encoded data to: {PROCESSED_DATA_PATH}")
print(f"📄 Saved feature columns to: {FEATURE_COLUMNS_PATH}")
print(f"🔢 Total features: {len(feature_columns)}")
