from sqlalchemy.orm import Session
from uuid import UUID
from app.models import Form
from app.schemas import FormRead, FormUpdate, FormCreate

def get_form(db: Session, form_id: UUID): 
    return db.query(Form).filter(Form.id == form_id).first()

def get_forms(db: Session, skip: int=0, limit: int=100):
    return db.query(Form).offset(skip).limit(limit).all()

def create_form(db: Session, form: FormCreate):
    db_form = Form(
        spell_school=form.spell_school,
        latin_title=form.latin_title,
        sanskrit_title=form.sanskrit_title,
        gaelic_title=form.gaelic_title,
        polynesian_title=form.polynesian_title,
        benoue_title=form.benoue_title,
        algonquian_title=form.algonquian_title,
        binary_code=form.binary_code
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form

def update_form(db: Session, form_id: UUID, form: FormUpdate):
    db_form=db.query(Form).filter(Form.id == form_id).first()
    
    if not db_form:
        return None
    
    for key, value in form.model_dump(exclude_unset=True).items():
        setattr(db_form, key, value)
    
    db.commit()
    db.refresh(db_form)
    return db_form

def delete_form(db: Session, form_id: UUID):
    db_form = db.query(Form).filter(Form.id == form_id).first()
    if not db_form:
        return None
    db.delete(db_form)
    db.commit()
    return db_form