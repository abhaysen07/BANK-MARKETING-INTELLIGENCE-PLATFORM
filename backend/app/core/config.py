import os

# backend/app/core/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# backend/app/
APP_DIR = os.path.dirname(BASE_DIR)

# backend/
BACKEND_DIR = os.path.dirname(APP_DIR)

# project root
PROJECT_ROOT = os.path.dirname(BACKEND_DIR)

# ml paths
ML_DIR = os.path.join(PROJECT_ROOT, "ml")
MODELS_DIR = os.path.join(ML_DIR, "models")

FEATURE_COLUMNS_PATH = os.path.join(ML_DIR, "feature_columns.txt")
DEFAULT_MODEL_PATH = os.path.join(ML_DIR, "default_model.txt")
