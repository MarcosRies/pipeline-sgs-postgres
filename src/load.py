from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME=os.getenv("DB_NAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_PORT=os.getenv("DB_PORT")

database_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(database_url)

def loading_data(df, engine):

    with engine.connect() as conn:
        conn.execute(text(
            'CREATE TABLE IF NOT EXISTS data_sgs ("date" DATE PRIMARY KEY, "value" DECIMAL)'
        ))
        conn.commit()

    df.to_sql(name="stg_data_sgs", con = engine, if_exists = "replace", index = False)

    with engine.connect() as conn:
        conn.execute(text(
            """INSERT INTO data_sgs ("date", "value")
               SELECT "data", "valor" FROM stg_data_sgs
               ON CONFLICT ("date")
               DO UPDATE SET "value" = EXCLUDED."value";"""))
        conn.execute(text("DROP TABLE IF EXISTS stg_data_sgs;"))
        conn.commit()

