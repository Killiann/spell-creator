from pydantic import BaseModel, UUID4
from typing import Optional, List

#Form
class FormBase(BaseModel):
    spell_school: str
    latin_title: Optional[str]
    sanskrit_title: Optional[str]
    gaelic_title: Optional[str]
    polynesian_title: Optional[str]
    benoue_title: Optional[str]
    algonquian_title: Optional[str]
    binary_code: str
    
class FormCreate(FormBase):
    pass

class FormUpdate(BaseModel):
    spell_school: Optional[str]
    latin_title: Optional[str]
    sanskrit_title: Optional[str]
    gaelic_title: Optional[str]
    polynesian_title: Optional[str]
    benoue_title: Optional[str]
    algonquian_title: Optional[str]
    binary_code: Optional[str]

class FormRead(FormBase):
    id: UUID4
    
    class Config:
        orm_mode = True

#Power    
class PowerBase(BaseModel):    
    level: int
    binary_code: str
    
class PowerUpdate(BaseModel):
    level: Optional[int] = None
    binary_code: Optional[str] = None
    
class PowerRead(PowerBase):
    id: UUID4
    
    class Config: 
        orm_mode = True

#Shape
class ShapeBase(BaseModel):
    delivery_name: str
    delivery_type: str
    binary_code: str
    
class ShapeUpdate(BaseModel):
    delivery_name: Optional[str]
    delivery_type: Optional[str]
    binary_code: Optional[str]

class ShapeRead(ShapeBase):
    id: UUID4
    
    class Config:
        orm_mode = True

#Target
class TargetBase(BaseModel):
    name: str
    binary_code: str
    binary_code_connected: str
    
class TargetUpdate(BaseModel):
    name: Optional[str]
    binary_code: Optional[str]
    binary_code_connected: Optional[str]

class TargetRead(TargetBase):
    id: UUID4
    
    class Config:
        orm_mode = True
        
#Sub Technique
class SubTechniqueBase(BaseModel):
    name: str
    binary_code: str
    
class SubTechniqueUpdate(BaseModel):
    name: Optional[str]
    binary_code: Optional[str]    

class SubTechniqueRead(SubTechniqueBase):
    id: UUID4
    
    class Config:
        orm_mode = True

#Technique
class TechniqueBase(BaseModel):
    name: str
    binary_code: str

class TechniqueUpdate(BaseModel):
    name: Optional[str]
    binary_code: Optional[str]

class TechniqueRead(TechniqueBase   ):
    id: UUID4
    sub_techniques: List[SubTechniqueRead] = []    
    class Config: 
        orm_mode = True

#Spell
class SpellBase(BaseModel):
    name: str

class SpellCreate(SpellBase):
    form_id: UUID4
    power_id: UUID4
    shape_id: UUID4
    target_id: UUID4
    technique_id: UUID4

class SpellUpdate(BaseModel):
    name: Optional[str]
    form_id: Optional[UUID4]
    power_id: Optional[UUID4]
    shape_id: Optional[UUID4]
    target_id: Optional[UUID4]
    technique_id: Optional[UUID4]

class SpellRead(SpellBase):
    id: UUID4
    
    form: FormRead
    power: PowerRead
    shape: ShapeRead
    target: TargetRead
    technique: TechniqueRead
    
    class Config:
        orm_mode = True