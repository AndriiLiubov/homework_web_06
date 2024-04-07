from contextlib import contextmanager
import os

from dotenv import load_dotenv
import psycopg2


load_dotenv()

pg_pass = os.getenv("POSTGRES_PASS")
pg_host = os.getenv("POSTGRES_HOST")


dsn_str = f"host={pg_host} dbname=postgres user=postgres password={pg_pass}"

@contextmanager
def create_connection():

    conn = psycopg2.connect(dsn_str)
    yield conn
    conn.rollback()
    conn.close()





    

