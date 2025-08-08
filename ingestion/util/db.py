import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return psycopg2.connect(
        host=os.getenv("PGHOST"),
        port=int(os.getenv("PGPORT", "5432")),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        dbname=os.getenv("PGDATABASE"),
        sslmode=os.getenv("PGSSLMODE", "prefer"),
    )

def execute(sql, params=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)

def bulk_insert(sql, rows):
    with get_conn() as conn:
        with conn.cursor() as cur:
            execute_values(cur, sql, rows)
