from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Shape

shapes = [
    {
        "delivery_name": "Touch Spells",
        "delivery_type": "Targets",
        "binary_code": "00000000101"
    },
    {
        "delivery_name": "Remote Spells",
        "delivery_type": "Targets",
        "binary_code": "00000001001"
    },
    {
        "delivery_name": "point of origin",
        "delivery_type": "Areas of Effect",
        "binary_code": "00000010001"
    },
    {
        "delivery_name": "Sphere",
        "delivery_type": "Areas of Effect",
        "binary_code": "00000000111"
    },
    {
        "delivery_name": "Cylinder",
        "delivery_type": "Areas of Effect",
        "binary_code": "00000010011"
    },
    {
        "delivery_name": "Aura",
        "delivery_type": "Areas of Effect",
        "binary_code": "00000001101"
    },
    {
        "delivery_name": "Cube",
        "delivery_type": "Areas of Effect",
        "binary_code": "00000011001"
    },
    {
        "delivery_name": "Cone",
        "delivery_type": "Areas of Effect",
        "binary_code": "00000010101"
    },
    {
        "delivery_name": "Line",
        "delivery_type": "Areas of Effect",
        "binary_code": "00000001111"
    }
]

def seed_shapes():
    db: Session = SessionLocal()
    
    try:
        for shape in shapes:
            existing = (
                db.query(Shape)
                .filter(Shape.delivery_name == shape["delivery_name"])
                .first()
            )
            
            if not existing:
                new_shape = Shape(**shape)
                db.add(new_shape)
                
        db.commit()
        print("Shapes seeded successfully.")
    
    except Exception as e:
        db.rollback()
        print("Shape seeding failed: ", e)
        
    finally:
        db.close()
        
if __name__ == "__main__":
    seed_shapes()