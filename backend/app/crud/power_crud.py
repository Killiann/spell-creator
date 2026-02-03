from sqlalchemy.orm import Session
from uuid import UUID
from app.models import Power
from app.schemas import PowerBase, PowerUpdate

def get_power(db: Session, power_id: UUID):
    return db.query(Power).filter(Power.id == power_id).first()

def get_powers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Power).offset(skip).limit(limit).all()

def create_power(db: Session, power: PowerBase):
    db_power = Power(
        tier=power.tier,
        binary_code=power.binary_code
    )
    db.add(db_power)
    db.commit()
    db.refresh(db_power)
    return db_power

def update_power(db: Session, power_id: UUID, power: PowerUpdate):
    db_power = db.query(Power).filter(Power.id == power_id).first()
    if not db_power:
        return None

    for key, value in power.model_dump(exclude_unset=True).items():
        setattr(db_power, key, value)

    db.commit()
    db.refresh(db_power)
    return db_power

def delete_power(db: Session, power_id: UUID):
    db_power = db.query(Power).filter(Power.id == power_id).first()
    if not db_power:
        return None

    db.delete(db_power)
    db.commit()
    return db_power