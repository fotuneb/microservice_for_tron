from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.tron_service import TronService
from app.schemas.tron import AddressRequest, AddressResponse
from app.db.session import get_db
from app.db.models import TronQuery
from typing import List

router = APIRouter()

@router.post("/tron", response_model=AddressResponse)
def get_tron_data(request: AddressRequest, db: Session = Depends(get_db)):
    service = TronService()
    try:
        data = service.get_account_info(request.address)
        record = service.save_query(**data)
        return record
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/tron/history", response_model=List[AddressResponse])
def get_tron_history(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    records = db.query(TronQuery).offset(skip).limit(limit).all()
    return records