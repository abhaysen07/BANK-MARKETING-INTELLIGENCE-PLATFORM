from pydantic import BaseModel

class CustomerInput(BaseModel):
    age: int
    balance: int
    day: int
    duration: int
    campaign: int
    pdays: int
    previous: int

    default: int
    housing: int
    loan: int

    job: str
    marital: str
    education: str
    contact: str
    month: str
    poutcome: str
