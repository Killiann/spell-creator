from sqlalchemy.orm import Session
from uuid import UUID
from app.models import Spell
from app.schemas import SpellUpdate, SpellCreate

def get_spell(db: Session, spell_id: UUID):
    return db.query(Spell).filter(Spell.id == spell_id).first()

def get_spells(db: Session, skip: int=0, limit: int=100):
    return db.query(Spell).offset(skip).limit(limit).all()

def create_spell(db: Session, spell: SpellCreate):
    db_spell = Spell(
        name=spell.name,
        form_id=spell.form_id,
        power_id=spell.power_id,
        shape_id=spell.shape_id,
        target_id=spell.target_id,
        technique_id=spell.technique_id
    )
    db.add(db_spell)
    db.commit()
    db.refresh(db_spell)
    return db_spell

def update_spell(db: Session, spell_id: UUID, spell: SpellUpdate):
    db_spell=db.query(Spell).filter(Spell.id == spell_id).first()
    
    if not db_spell:
        return None
    
    for key, value in spell.model_dump(exclude_unset = True).items():
        setattr(db_spell, key, value)
    
    db.commit()
    db.refresh(db_spell)
    return db_spell

def delete_spell(db:Session, spell_id: UUID):
    db_spell = db.query(Spell).filter(Spell.id == spell_id).first()
    if not db_spell:
        return None
    db.delete(db_spell)
    db.commit()
    return db_spell