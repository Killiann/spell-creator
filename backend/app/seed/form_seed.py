from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Form
forms = [
    {
        "spell_school": "Fire",
        "latin_title": "Ignum",
        "sanskrit_title": "Agniḥ",
        "gaelic_title": "Teine",
        "polynesian_title": "Ahi",
        "benoue_title": "Tũndi",
        "algonquian_title": "iškotêw",
        "binary_code": "00000000101",
    },
    {
        "spell_school": "Ice",
        "latin_title": "Glacies",
        "sanskrit_title": "Himaḥ",
        "gaelic_title": "Deigh",
        "polynesian_title": "Huka",
        "benoue_title": "Yì",
        "algonquian_title": "miteh",
        "binary_code": "00000001001",
    },
    {
        "spell_school": "Wind",
        "latin_title": "Aurum",
        "sanskrit_title": "Vāyuḥ",
        "gaelic_title": "Adhair",
        "polynesian_title": "Hau",
        "benoue_title": "Ŋw̃ɛ",
        "algonquian_title": "yowa⋅ni",
        "binary_code": "00000100101",
    },
    {
        "spell_school": "Earth",
        "latin_title": "Terram",
        "sanskrit_title": "Bhūmiḥ",
        "gaelic_title": "Talamh",
        "polynesian_title": "Papa",
        "benoue_title": "Àlɛ",
        "algonquian_title": "askiy",
        "binary_code": "00000101011",
    },
    {
        "spell_school": "Lightning",
        "latin_title": "Fulmen",
        "sanskrit_title": "Vidyutḥ",
        "gaelic_title": "Dealanach",
        "polynesian_title": "Uila",
        "benoue_title": "Tsíá",
        "algonquian_title": "wasi·kwe·w",
        "binary_code": "00001000101",
    },
    {
        "spell_school": "Wilderness",
        "latin_title": "Forma Vita",
        "sanskrit_title": "Jīvanarūpāḥ",
        "gaelic_title": "Cruthan Beatha",
        "polynesian_title": "Ngaa Ora",
        "benoue_title": "Bì-Ukwũ",
        "algonquian_title": "Nepesewak Kamacitowiniwa",
        "binary_code": "00000100011",
    },
    {
        "spell_school": "Radiance",
        "latin_title": "Splendens Divinus",
        "sanskrit_title": "Divyaḥ prakāśaḥ",
        "gaelic_title": "Rèididheachd diadhaidh",
        "polynesian_title": "Teatea Atua",
        "benoue_title": "Ìkɛmɛ Chukwu",
        "algonquian_title": "Waskwayawi mitoon",
        "binary_code": "00000110101",
    },
    {
        "spell_school": "Shadow",
        "latin_title": "Umbra Forma",
        "sanskrit_title": "Andhakārarūpāḥ",
        "gaelic_title": "Cruthan Dorchadais",
        "polynesian_title": "Ngaa Poouri",
        "benoue_title": "Bì-Ọchịchị Ĩjẹ",
        "algonquian_title": "Nepawi-tepiko-atisok",
        "binary_code": "00010001011",
    },
    {
        "spell_school": "Void",
        "latin_title": "Aether Tempus",
        "sanskrit_title": "antarikṣaṁ tathā kālaḥ",
        "gaelic_title": "àite agus ùine",
        "polynesian_title": "Vaa-tea ma te taima",
        "benoue_title": "Mbárá na Ìgbà",
        "algonquian_title": "Ki šāwanaw ēlāpwiw",
        "binary_code": "00000001101",
    },
    {
        "spell_school": "Dream",
        "latin_title": "Imaginem Mente",
        "sanskrit_title": "kalpitamanaḥ",
        "gaelic_title": "Inntinn mac-meanmnach",
        "polynesian_title": "Manatu Fafau",
        "benoue_title": "Èchìchì Uche",
        "algonquian_title": "Nepamāw",
        "binary_code": "00000010101",
    },
    {
        "spell_school": "Hexbinder",
        "latin_title": "Vetesta Via",
        "sanskrit_title": "purātanaḥ mārgaḥ cha",
        "gaelic_title": "seann shlighe",
        "polynesian_title": "Ala Taito",
        "benoue_title": "Ụzọ́ ochie",
        "algonquian_title": "Menekatay",
        "binary_code": "00000001111",
    },
]

def seed_forms():
    db: Session = SessionLocal()
    
    try:
        for form in forms:
            existing = (
                db.query(Form)
                .filter(Form.spell_school == form["spell_school"])
                .first()
            )
            
            if not existing: 
                new_form = Form(**form)
                db.add(new_form)
                
        db.commit()
        print("Forms seeded successfully.")
    
    except Exception as e:
        db.rollback()
        print("Form seeding failed: ",e)
        
    finally: 
        db.close()
        
if __name__ == "__main__":
    seed_forms()