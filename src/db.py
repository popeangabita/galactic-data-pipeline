import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def build_url(db=None):
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = db or os.getenv("DB_NAME", "cosmic_catalog")
    db_user = os.getenv("DB_USER", "postgres")
    db_pass = os.getenv("DB_PASS", "")
    return f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

def get_engine():
    return create_engine(build_url())
