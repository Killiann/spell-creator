from pathlib import Path
from dotenv import load_dotenv
import os

# Root of the repo
BASE_DIR = Path(__file__).resolve().parent.parent.parent 
print(BASE_DIR)

# Choose which env file to load
env_file = os.getenv("ENV_FILE", BASE_DIR / ".env.dev")
load_dotenv(BASE_DIR / env_file)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError(f"DATABASE_URL not set. Loaded env file: {env_file}")

# SQLAlchemy setup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
