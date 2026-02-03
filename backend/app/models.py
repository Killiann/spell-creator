import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Form(Base):
    __tablename__ = "forms"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    spell_school = Column(String, nullable=False)
    latin_title = Column(String)
    sanskrit_title = Column(String)
    gaelic_title = Column(String)
    polynesian_title = Column(String)
    benoue_title = Column(String)
    algonquian_title = Column(String)
    binary_code = Column(String, nullable=False)
    
    spells = relationship("Spell", back_populates="form")
    
class Power(Base):
    __tablename__ = "powers" 
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    tier = Column(Integer, nullable=False, unique=True)
    binary_code = Column(String, nullable=False)
    
    spells = relationship("Spell", back_populates="power")
    
class Shape(Base):  
    __tablename__ = "shapes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    delivery_name = Column(String, nullable=False)
    delivery_type = Column(String)
    binary_code = Column(String, nullable=False)
    
    spells = relationship("Spell", back_populates="shape")
    
class Target(Base):
    __tablename__ = "targets"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)    
    binary_code = Column(String, nullable=False)
    binary_code_connected = Column(String, nullable=False)
    
    spells = relationship("Spell", back_populates="target")
    
class Technique(Base):
    __tablename__ = "techniques"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)    
    name = Column(String, nullable=False)
    binary_code = Column(String, nullable=False)
    
    spells = relationship("Spell", back_populates="technique")
    sub_techniques = relationship("SubTechnique", back_populates="technique")
class SubTechnique(Base):
    __tablename__ = "sub_techniques"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)    
    technique_id = Column(UUID(as_uuid=True), ForeignKey("techniques.id"), nullable=False)
    name = Column(String, nullable=False)
    binary_code = Column(String, nullable=False)
    
    technique = relationship("Technique", back_populates="sub_techniques")
    
class Spell(Base):
    __tablename__ = "spells"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    form_id = Column(UUID(as_uuid=True), ForeignKey("forms.id"), nullable=False)
    power_id = Column(UUID(as_uuid=True), ForeignKey("powers.id"), nullable=False)
    shape_id = Column(UUID(as_uuid=True), ForeignKey("shapes.id"), nullable=False)
    target_id = Column(UUID(as_uuid=True), ForeignKey("targets.id"), nullable=False)
    technique_id = Column(UUID(as_uuid=True), ForeignKey("techniques.id"), nullable=False)
    
    form = relationship("Form")
    power = relationship("Power")
    shape = relationship("Shape")
    target = relationship("Target")
    technique = relationship("Technique")
    