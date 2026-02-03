from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Target

targets = [
    {
        "name": "Mind",
        "binary_code": "00000000011",
        "binary_code_connected": "00000010111"
    },
    {
        "name": "Body",
        "binary_code": "00000011001",
        "binary_code_connected": "00000010011"
    },
    {
        "name": "Substance",
        "binary_code": "00000001101",
        "binary_code_connected": "00000000101"
    },
    {
        "name": "Magic",
        "binary_code": "00000011011",
        "binary_code_connected": "00000001001"
    },
    {
        "name": "Threat",
        "binary_code": "00000001011",
        "binary_code_connected": "00000001111"
    }
]

def seed_targets():
    db: Session = SessionLocal()
    
    try:
        for target in targets:
            existing = (
                db.query(Target)
                .filter(Target.name == target["name"])
                .first()
            )
            
            if not existing:
                new_target = Target(**target)
                db.add(new_target)
                
        db.commit()
        print("Targets seeded successfully.")
        
    except Exception as e:
        db.rollback()
        print("Target seeding failed:", e)
        
    finally: 
        db.close()
        
if __name__ == "__main__":
    seed_targets()