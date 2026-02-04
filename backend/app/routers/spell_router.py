from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database import get_db
from app.schemas import SpellRead, SpellCreate, SpellUpdate
from app.crud import spell_crud

spell_router = APIRouter(prefix="/spells", tags=["spells"])

@spell_router.get("/", response_model=List[SpellRead])
def read_spells(skip: int = 0, limit: int=100, db: Session = Depends(get_db)):
    spells = spell_crud.get_spells(db, skip=skip, limit=limit)
    return spells

@spell_router.get("/{spell_name}", response_model=SpellRead)
def read_spell(spell_name: str, db: Session = Depends(get_db)):
    spell = spell_crud.get_spell_by_name(db, spell_name)
    if not spell:
        raise HTTPException(status_code=404, detail="Spell not found.")
    return spell

@spell_router.get("/id/{spell_id}", response_model=SpellRead)
def read_spell(spell_id: str, db: Session = Depends(get_db)):
    spell = spell_crud.get_spell(db, spell_id)
    if not spell:
        raise HTTPException(status_code=404, detail="Spell not found.")
    return spell

@spell_router.post("/", response_model=SpellRead)
def create_spell(spell: SpellCreate, db: Session = Depends(get_db)):
    return spell_crud.create_spell(db, spell)

@spell_router.put("/{spell_id}", response_model=SpellRead)
def update_spell(spell_id: UUID, spell: SpellUpdate, db: Session = Depends(get_db)):
    updated = spell_crud.update_spell(db, spell_id, spell)
    if not updated: 
        raise HTTPException(status_code=404, detail="Spell not found.")
    
@spell_router.delete("/{spell_id}", status_code=204)
def delete_spell(spell_id: UUID, db: Session = Depends(get_db)):
    deleted = spell_crud.delete_spell(db, spell_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Spell not found.")
    return