from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.spell_router import spell_router
from app.routers.form_router import form_router
from app.routers.power_router import power_router
from app.routers.shape_router import shape_router
from app.routers.target_router import target_router
from app.routers.technique_router import tech_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Spell Creator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(spell_router)
app.include_router(form_router)
app.include_router(power_router)
app.include_router(shape_router)
app.include_router(target_router)
app.include_router(tech_router)