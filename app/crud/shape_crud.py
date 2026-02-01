from sqlalchemy.orm import Session
from uuid import UUID
from app.models import Shape
from app.schemas import ShapeBase, ShapeUpdate

def get_shape(db: Session, shape_id: UUID):
    return db.query(Shape).filter(Shape.id == shape_id).first()

def get_shapes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Shape).offset(skip).limit(limit).all()

def create_shape(db: Session, shape: ShapeBase):
    db_shape = Shape(
        delivery_name=shape.delivery_name,
        delivery_type=shape.delivery_type,
        binary_code=shape.binary_code
    )
    db.add(db_shape)
    db.commit()
    db.refresh(db_shape)
    return db_shape

def update_shape(db: Session, shape_id: UUID, shape: ShapeUpdate):
    db_shape = db.query(Shape).filter(Shape.id == shape_id).first()
    if not db_shape:
        return None

    for key, value in shape.model_dump(exclude_unset=True).items():
        setattr(db_shape, key, value)

    db.commit()
    db.refresh(db_shape)
    return db_shape

def delete_shape(db: Session, shape_id: UUID):
    db_shape = db.query(Shape).filter(Shape.id == shape_id).first()
    if not db_shape:
        return None

    db.delete(db_shape)
    db.commit()
    return db_shape