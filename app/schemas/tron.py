from pydantic import BaseModel
from datetime import datetime

class AddressRequest(BaseModel):
    address: str

class AddressResponse(BaseModel):
    id: int
    address: str
    balance: float
    bandwidth: int
    energy: int
    timestamp: datetime

    class Config:
        orm_mode = True