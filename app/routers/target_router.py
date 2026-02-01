from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database import get_db
from app.schemas import TargetBase, TargetRead, TargetUpdate
from app.crud import target_crud

target_router = APIRouter(prefix="/targets", tags=["targets"])

@target_router.get("/", response_model=List[TargetRead])
def read_targets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return target_crud.get_targets(db, skip=skip, limit=limit)

@target_router.get("/{target_id}", response_model=TargetRead)
def read_target(target_id: UUID, db: Session = Depends(get_db)):
    target = target_crud.get_target(db, target_id)
    if not target:
        raise HTTPException(status_code=404, detail="Target not found.")
    return target

@target_router.post("/", response_model=TargetRead)
def create_target(target: TargetBase, db: Session = Depends(get_db)):
    return target_crud.create_target(db, target)

@target_router.put("/{target_id}", response_model=TargetRead)
def update_target(target_id: UUID, target: TargetUpdate, db: Session = Depends(get_db)):
    updated = target_crud.update_target(db, target_id, target)
    if not updated:
        raise HTTPException(status_code=404, detail="Target not found.")
    return updated

@target_router.delete("/{target_id}", response_model=TargetRead)
def delete_target(target_id: UUID, db: Session = Depends(get_db)):
    deleted = target_crud.delete_target(db, target_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Target not found.")
    return deleted
