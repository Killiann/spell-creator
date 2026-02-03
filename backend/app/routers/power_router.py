from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database import get_db
from app.schemas import PowerBase, PowerRead, PowerUpdate
from app.crud import power_crud

power_router = APIRouter(prefix="/powers", tags=["powers"])

@power_router.get("/", response_model=List[PowerRead])
def read_powers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    powers = power_crud.get_powers(db, skip=skip, limit=limit)
    return powers

@power_router.get("/{power_id}", response_model=PowerRead)
def read_power(power_id: UUID, db: Session = Depends(get_db)):
    power = power_crud.get_power(db, power_id)
    if not power:
        raise HTTPException(status_code=404, detail="Power not found.")
    return power

@power_router.post("/", response_model=PowerRead)
def create_power(power: PowerBase, db: Session = Depends(get_db)):
    return power_crud.create_power(db, power)

@power_router.put("/{power_id}", response_model=PowerRead)
def update_power(power_id: UUID, power: PowerUpdate, db: Session = Depends(get_db)):
    updated = power_crud.update_power(db, power_id, power)
    if not updated:
        raise HTTPException(status_code=404, detail="Power not found.")
    return updated

@power_router.delete("/{power_id}", status_code=204)
def delete_power(power_id: UUID, db: Session = Depends(get_db)):
    deleted = power_crud.delete_power(db, power_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Power not found.")
    return