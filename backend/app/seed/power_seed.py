from sqlalchemy.orm import Session
from app.database import SessionLocal  
from app.models import Power

powers = [
    {"tier": 1, "binary_code": "00000000000"},
    {"tier": 2, "binary_code": "00000000001"},
    {"tier": 3, "binary_code": "00000000011"},
    {"tier": 4, "binary_code": "00000000101"},
    {"tier": 5, "binary_code": "00000000111"},
    {"tier": 6, "binary_code": "00000001001"},
    {"tier": 7, "binary_code": "00000001011"},
    {"tier": 8, "binary_code": "00000001101"},
    {"tier": 9, "binary_code": "00000001111"},
    {"tier": 10, "binary_code": "00000010001"},
    {"tier": 11, "binary_code": "00000010011"},
    {"tier": 12, "binary_code": "00000010101"},
    {"tier": 13, "binary_code": "00000010111"},
    {"tier": 14, "binary_code": "00000011001"},
    {"tier": 15, "binary_code": "00000011011"},
    {"tier": 16, "binary_code": "00000011101"},
    {"tier": 17, "binary_code": "00000011111"},
    {"tier": 18, "binary_code": "00000100001"},
    {"tier": 19, "binary_code": "00000100011"},
    {"tier": 20, "binary_code": "00000100101"},
    {"tier": 21, "binary_code": "00000100111"},
    {"tier": 22, "binary_code": "00000101001"},
    {"tier": 23, "binary_code": "00000101011"},
    {"tier": 24, "binary_code": "00000101101"},
    {"tier": 25, "binary_code": "00000101111"},
    {"tier": 26, "binary_code": "00000110001"},
    {"tier": 27, "binary_code": "00000110011"},
    {"tier": 28, "binary_code": "00000110101"},
    {"tier": 29, "binary_code": "00000110111"},
    {"tier": 30, "binary_code": "00000111001"},
    {"tier": 31, "binary_code": "00000111011"},
    {"tier": 32, "binary_code": "00000111101"},
    {"tier": 33, "binary_code": "00000111111"},
    {"tier": 34, "binary_code": "00001000011"},
    {"tier": 35, "binary_code": "00001000101"},
    {"tier": 36, "binary_code": "00001000111"},
    {"tier": 37, "binary_code": "00001001001"},
    {"tier": 38, "binary_code": "00001001011"},
    {"tier": 39, "binary_code": "00001001101"},
    {"tier": 40, "binary_code": "00001001111"},
    {"tier": 41, "binary_code": "00001010001"},
    {"tier": 42, "binary_code": "00001010011"},
    {"tier": 43, "binary_code": "00001010101"},
    {"tier": 44, "binary_code": "00001010111"},
    {"tier": 45, "binary_code": "00001011001"},
    {"tier": 46, "binary_code": "00001011011"},
    {"tier": 47, "binary_code": "00001011101"},
    {"tier": 48, "binary_code": "00001011111"},
    {"tier": 49, "binary_code": "00001100011"},
    {"tier": 50, "binary_code": "00001100101"}
]

def seed_powers():
    db:Session = SessionLocal()
    
    try:
        for power in powers:
            existing = (
                db.query(Power)
                .filter(Power.tier == power["tier"])
                .first()
            )
            
            if not existing:
                new_power = Power(**power)
                db.add(new_power)
            
            db.commit()
            print("Powers seeded successfully.")
            
    except Exception as e:
        db.rollback()
        print("Power seeding failed: ", e)
    
    finally:
        db.close()
        
if __name__ == "__main__":
    seed_powers()