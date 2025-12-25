from fastapi import APIRouter, HTTPException
from backend.app.schemas.customer import CustomerInput
from backend.app.services.model_service import predict_customer # type: ignore

router = APIRouter()

@router.post("/predict")
def predict(data: CustomerInput): # pyright: ignore[reportUnknownParameterType]
    try:
        return predict_customer(data.dict()) # pyright: ignore[reportDeprecated, reportUnknownVariableType]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Please try again later."
        )