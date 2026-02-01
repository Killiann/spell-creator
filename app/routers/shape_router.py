from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database import get_db
from app.schemas import ShapeBase, ShapeRead, ShapeUpdate
from app.crud import shape_crud

shape_router = APIRouter(prefix="/shapes", tags=["shapes"])

@shape_router.get("/", response_model=List[ShapeRead])
def read_shapes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return shape_crud.get_shapes(db, skip=skip, limit=limit)

@shape_router.get("/{shape_id}", response_model=ShapeRead)
def read_shape(shape_id: UUID, db: Session = Depends(get_db)):
    shape = shape_crud.get_shape(db, shape_id)
    if not shape:
        raise HTTPException(status_code=404, detail="Shape not found.")
    return shape

@shape_router.post("/", response_model=ShapeRead)
def create_shape(shape: ShapeBase, db: Session = Depends(get_db)):
    return shape_crud.create_shape(db, shape)

@shape_router.put("/{shape_id}", response_model=ShapeRead)
def update_shape(shape_id: UUID, shape: ShapeUpdate, db: Session = Depends(get_db)):
    updated = shape_crud.update_shape(db, shape_id, shape)
    if not updated:
        raise HTTPException(status_code=404, detail="Shape not found.")
    return updated

@shape_router.delete("/{shape_id}", response_model=ShapeRead)
def delete_shape(shape_id: UUID, db: Session = Depends(get_db)):
    deleted = shape_crud.delete_shape(db, shape_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Shape not found.")
    return deleted
