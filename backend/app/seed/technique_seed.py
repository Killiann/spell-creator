from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Technique, SubTechnique

techniques = [
    {
        "name": "I create",
        "binary_code": "00000100001",
        "sub_techniques": [
            {"name": "I transform", "binary_code": "00000101011"},
            {"name": "I control", "binary_code": "00000100011"},
            {"name": "I destroy", "binary_code": "00000100101"},
            {"name": "I empower", "binary_code": "00000100111"}
        ]
    },
    {
        "name": "I destroy",
        "binary_code": "00000001001",
        "sub_techniques": [
            {"name": "I create", "binary_code": "00000001011"},
            {"name": "I transform", "binary_code": "00000001101"},
            {"name": "I control", "binary_code": "00000011101"},
            {"name": "I empower", "binary_code": "00000101001"}
        ]
    },
    {
        "name": "I transform",
        "binary_code": "00001011001",
        "sub_techniques": [
            {"name": "I create", "binary_code": "00000111011"},
            {"name": "I control", "binary_code": "00010011011"},
            {"name": "I destroy", "binary_code": "00001001001"},
            {"name": "I empower", "binary_code": "00001101011"}
        ]
    },
    {
        "name": "I control",
        "binary_code": "00000111001",
        "sub_techniques": [
            {"name": "I create", "binary_code": "00000010001"},
            {"name": "I transform", "binary_code": "00000110101"},
            {"name": "I destroy", "binary_code": "00010100111"},
            {"name": "I empower", "binary_code": "00001000101"}
        ]
    },
    {
        "name": "I empower",
        "binary_code": "00001100011",
        "sub_techniques": [
            {"name": "I create", "binary_code": "00010001001"},
            {"name": "I transform", "binary_code": "00000010101"},
            {"name": "I control", "binary_code": "0001001001"},
            {"name": "I destroy", "binary_code": "00000101101"}
        ]
    }
]

def seed_techniques():
    db: Session = SessionLocal()
    
    try:
        for t in techniques:
            existing = (
                db.query(Technique)
                .filter(Technique.name == t["name"])
                .first()
            )
            
            if not existing:
                new_technique = Technique()
                new_technique.name = t["name"]
                new_technique.binary_code = t["binary_code"]
                
                db.add(new_technique)
                db.flush()
                
                print(new_technique)
                
                for st in t["sub_techniques"]:
                    new_st = SubTechnique(**st)
                    new_st.technique = new_technique
                    db.add(new_st)
                    
        db.commit()
        print("Techniques seeded successfully.")
    
    except Exception as e:
        db.rollback()
        print("Technique seeding failed: ", e)
        
    finally: 
        db.close()
        
if __name__ == "__main__":
    seed_techniques()