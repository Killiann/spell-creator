from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database import get_db
from app.schemas import FormRead, FormCreate, FormUpdate
from app.crud import form_crud

form_router = APIRouter(prefix="/forms", tags=["forms"])

@form_router.get("/", response_model=List[FormRead])
def read_forms(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    forms = form_crud.get_forms(db, skip=skip, limit=limit)
    return forms

@form_router.get("/{form_id}", response_model=FormRead)
def read_form(form_id: UUID, db: Session=Depends(get_db)):
    form =form_crud.get_form(db, form_id)
    if not form:
        raise HTTPException(status_code=404, detail="Form not found.")
    return form

@form_router.post("/", response_model=FormRead)
def create_form(form: FormCreate, db: Session = Depends(get_db)):
    return form_crud.create_form(db, form)

@form_router.put("/{form_id}", response_model=FormRead)
def update_form(form_id: UUID, form: FormUpdate, db: Session=Depends(get_db)):
    updated = form_crud.update_form(db, form_id, form)
    if not updated:
        raise HTTPException(status_code=404, detail="Form not found.")
    return updated
    
@form_router.delete("/{form_id}", status_code=204)
def delete_Form(form_id: UUID, db: Session=Depends(get_db)):
    deleted=form_crud.delete_form(db, form_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Form not found.")
    return 
    