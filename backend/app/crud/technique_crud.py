from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from app.models import Technique, SubTechnique
from app.schemas import TechniqueBase, TechniqueUpdate, SubTechniqueBase, SubTechniqueUpdate

# ---------- Technique ----------

def get_technique(db: Session, technique_id: UUID):
    return db.query(Technique).filter(Technique.id == technique_id).first()

def get_techniques(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Technique).offset(skip).limit(limit).all()

def create_technique(db: Session, technique: TechniqueBase):
    db_tech = Technique(
        name=technique.name,
        binary_code=technique.binary_code
    )
    db.add(db_tech)
    db.commit()
    db.refresh(db_tech)
    return db_tech

def update_technique(db: Session, technique_id: UUID, technique: TechniqueUpdate):
    db_tech = db.query(Technique).filter(Technique.id == technique_id).first()
    if not db_tech:
        return None

    for key, value in technique.model_dump(exclude_unset=True).items():
        setattr(db_tech, key, value)

    db.commit()
    db.refresh(db_tech)
    return db_tech

def delete_technique(db: Session, technique_id: UUID):
    db_tech = db.query(Technique).filter(Technique.id == technique_id).first()
    if not db_tech:
        return None
    db.delete(db_tech)
    db.commit()
    return db_tech

# ---------- SubTechnique ----------

def get_subtechnique(db: Session, subtech_id: UUID):
    return db.query(SubTechnique).filter(SubTechnique.id == subtech_id).first()

def get_subtechniques(db: Session, technique_id: UUID = None, skip: int = 0, limit: int = 100) -> List[SubTechnique]:
    query = db.query(SubTechnique)
    if technique_id:
        query = query.filter(SubTechnique.technique_id == technique_id)
    return query.offset(skip).limit(limit).all()

def create_subtechnique(db: Session, subtech: SubTechniqueBase, technique_id: UUID):
    db_sub = SubTechnique(
        name=subtech.name,
        binary_code=subtech.binary_code,
        technique_id=technique_id
    )
    db.add(db_sub)
    db.commit()
    db.refresh(db_sub)
    return db_sub

def update_subtechnique(db: Session, subtech_id: UUID, subtech: SubTechniqueUpdate):
    db_sub = db.query(SubTechnique).filter(SubTechnique.id == subtech_id).first()
    if not db_sub:
        return None
    for key, value in subtech.model_dump(exclude_unset=True).items():
        setattr(db_sub, key, value)
    db.commit()
    db.refresh(db_sub)
    return db_sub

def delete_subtechnique(db: Session, subtech_id: UUID):
    db_sub = db.query(SubTechnique).filter(SubTechnique.id == subtech_id).first()
    if not db_sub:
        return None
    db.delete(db_sub)
    db.commit()
    return db_sub
