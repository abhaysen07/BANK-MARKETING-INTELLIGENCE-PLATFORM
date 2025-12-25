from fastapi import APIRouter, HTTPException

from app.schemas.customer import CustomerInput
from app.services.model_service import predict_customer

router = APIRouter()

@router.post("/predict")
def predict(data: CustomerInput):
    try:
        return predict_customer(data.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Please try again later."
        )
