from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database import get_db
from app.schemas import TechniqueBase, TechniqueRead, TechniqueUpdate
from app.schemas import SubTechniqueBase, SubTechniqueRead, SubTechniqueUpdate
from app.crud import technique_crud

tech_router = APIRouter(prefix="/techniques", tags=["techniques"])

# ---------- Technique ----------

@tech_router.get("/", response_model=List[TechniqueRead])
def read_techniques(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return technique_crud.get_techniques(db, skip=skip, limit=limit)

@tech_router.get("/{tech_id}", response_model=TechniqueRead)
def read_technique(tech_id: UUID, db: Session = Depends(get_db)):
    tech = technique_crud.get_technique(db, tech_id)
    if not tech:
        raise HTTPException(status_code=404, detail="Technique not found.")
    return tech

@tech_router.post("/", response_model=TechniqueRead)
def create_technique(tech: TechniqueBase, db: Session = Depends(get_db)):
    return technique_crud.create_technique(db, tech)

@tech_router.put("/{tech_id}", response_model=TechniqueRead)
def update_technique(tech_id: UUID, tech: TechniqueUpdate, db: Session = Depends(get_db)):
    updated = technique_crud.update_technique(db, tech_id, tech)
    if not updated:
        raise HTTPException(status_code=404, detail="Technique not found.")
    return updated

@tech_router.delete("/{tech_id}", response_model=TechniqueRead)
def delete_technique(tech_id: UUID, db: Session = Depends(get_db)):
    deleted = technique_crud.delete_technique(db, tech_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Technique not found.")
    return deleted

# ---------- SubTechnique ----------

@tech_router.get("/{tech_id}/subtechniques", response_model=List[SubTechniqueRead])
def read_subtechniques(tech_id: UUID, db: Session = Depends(get_db)):
    return technique_crud.get_subtechniques(db, technique_id=tech_id)

@tech_router.post("/{tech_id}/subtechniques", response_model=SubTechniqueRead)
def create_subtechnique(tech_id: UUID, subtech: SubTechniqueBase, db: Session = Depends(get_db)):
    return technique_crud.create_subtechnique(db, subtech, tech_id)

@tech_router.put("/subtechniques/{subtech_id}", response_model=SubTechniqueRead)
def update_subtechnique(subtech_id: UUID, subtech: SubTechniqueUpdate, db: Session = Depends(get_db)):
    updated = technique_crud.update_subtechnique(db, subtech_id, subtech)
    if not updated:
        raise HTTPException(status_code=404, detail="SubTechnique not found.")
    return updated

@tech_router.delete("/subtechniques/{subtech_id}", response_model=SubTechniqueRead)
def delete_subtechnique(subtech_id: UUID, db: Session = Depends(get_db)):
    deleted = technique_crud.delete_subtechnique(db, subtech_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="SubTechnique not found.")
    return deleted
