from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routes.predict import router as predict_router
from backend.app.routes.health import router as health_router

app = FastAPI(
    title="Bank Marketing Intelligence API",
    version="1.0.0"
)

# =========================================================
# CORS CONFIG (ABSOLUTELY REQUIRED FOR REACT)
# =========================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# ROUTES
# =========================================================
app.include_router(predict_router)
app.include_router(health_router)
