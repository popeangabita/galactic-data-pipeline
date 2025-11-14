import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

def build_url(db=None):
    """Building the conn"""
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = db or os.getenv("DB_NAME", "cosmic_catalog")
    db_user = os.getenv("DB_USER", "postgres")
    db_pass = os.getenv("DB_PASS", "")
    return f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

def ensure_database():
    """Creates the target db if it does not exist."""
    target_db = os.getenv("DB_NAME", "cosmic_catalog")
    engine = create_engine(build_url("postgres"))
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :d"),
            {"d": target_db}
        ).scalar()
        if not result:
            conn.execute(text(f"COMMIT")) 
            conn.execute(text(f"CREATE DATABASE {target_db}"))
            print(f"Created database {target_db}")
        else:
            print(f"Database {target_db} already exists")

def run_sql_file(engine, path):
    with open(path, "r") as f:
        sql = f.read()
    with engine.begin() as conn:
        for statement in sql.split(";"):
            stmt = statement.strip()
            if stmt:
                conn.execute(text(stmt))

def main():
    load_dotenv()
    ensure_database()

    engine = create_engine(build_url())

    sql_dir = os.path.join(os.path.dirname(__file__), "..", "sql")
    sql_files = [
        "create_raw.sql",
        "create_curate.sql",
        "create_marts.sql"
    ]
    for f in sql_files:
        path = os.path.join(sql_dir, f)
        print(f"Running {path} ...")
        run_sql_file(engine, path)

    print("Database setup complete.")

if __name__ == "__main__":
    main()
