from sqlalchemy.orm import Session
from uuid import UUID
from app.models import Target
from app.schemas import TargetBase, TargetUpdate

def get_target(db: Session, target_id: UUID):
    return db.query(Target).filter(Target.id == target_id).first()

def get_targets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Target).offset(skip).limit(limit).all()

def create_target(db: Session, target: TargetBase):
    db_target = Target(
        name=target.name,
        binary_code=target.binary_code,
        binary_code_connected=target.binary_code_connected
    )
    db.add(db_target)
    db.commit()
    db.refresh(db_target)
    return db_target

def update_target(db: Session, target_id: UUID, target: TargetUpdate):
    db_target = db.query(Target).filter(Target.id == target_id).first()
    if not db_target:
        return None

    for key, value in target.model_dump(exclude_unset=True).items():
        setattr(db_target, key, value)

    db.commit()
    db.refresh(db_target)
    return db_target

def delete_target(db: Session, target_id: UUID):
    db_target = db.query(Target).filter(Target.id == target_id).first()
    if not db_target:
        return None

    db.delete(db_target)
    db.commit()
    return db_target
