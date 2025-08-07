import csv, os
from util.db import execute, bulk_insert

RAW_TABLE = "raw.raw_gl_balances"
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "sample_gl_balances.csv")

DDL = f'''
CREATE TABLE IF NOT EXISTS {RAW_TABLE} (
    period_end date,
    entity text,
    department text,
    account_number text,
    currency text,
    end_balance numeric(18,2)
);
TRUNCATE TABLE {RAW_TABLE};
'''

INSERT_SQL = f"INSERT INTO {RAW_TABLE} (period_end, entity, department, account_number, currency, end_balance) VALUES %s"

def run():
    print("Creating raw table and truncating…")
    execute(DDL)
    print(f"Loading data from {DATA_FILE} …")
    rows = []
    with open(DATA_FILE) as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append((r["period_end"], r["entity"], r["department"], r["account_number"], r["currency"], r["end_balance"]))
    bulk_insert(INSERT_SQL, rows)
    print("Load complete.")

if __name__ == "__main__":
    run()
