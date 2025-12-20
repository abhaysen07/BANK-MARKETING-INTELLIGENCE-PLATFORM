import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# --------------------------------
# Setup
# --------------------------------
os.makedirs("models", exist_ok=True)

# --------------------------------
# Load encoded dataset
# --------------------------------
data = pd.read_csv("bank_data_encoded.csv")

X = data.drop("y", axis=1)
y = data["y"]

# --------------------------------
# Train-test split
# --------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# --------------------------------
# Models to train
# --------------------------------
models = {
    "logistic_regression": LogisticRegression(max_iter=1000),
    "random_forest": RandomForestClassifier(n_estimators=150, random_state=42),
    "knn": KNeighborsClassifier(n_neighbors=9),
    "svm": SVC(probability=True),
    "naive_bayes": GaussianNB()
}

# --------------------------------
# Train & save
# --------------------------------
for name, model in models.items():
    model.fit(X_train, y_train)
    joblib.dump(model, f"models/{name}.pkl")
    print(f"[SAVED] {name}")

print("✅ All models trained successfully.")
