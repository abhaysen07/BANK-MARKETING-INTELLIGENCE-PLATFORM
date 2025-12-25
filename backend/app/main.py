from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.predict import router as predict_router
from app.routes.health import router as health_router

app = FastAPI(
    title="Bank Marketing Intelligence API",
    version="1.0.0"
)

# =========================================================
# CORS CONFIG (REQUIRED FOR REACT)
# =========================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Later restrict to Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# ROUTES
# =========================================================
app.include_router(predict_router)
app.include_router(health_router)
