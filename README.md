# Forecasting Backbone (Postgres + dbt + Python)

Minimal, auditable data backbone for finance: Postgres warehouse, dbt models, Python ingestion, and CI via GitHub Actions.

## What this does
- Ingests sample GL balances to Postgres (`raw_gl_balances`).
- Builds star schema with `dim_date`, `dim_account`, and `f_gl_balances` (dbt).
- Publishes a finance-friendly mart: `mart_pnl_by_dept`.
- Runs tests in CI (PRs fail if reconciliation tests fail).

## Local Setup (dev)
1) **Install deps**
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

2) **Set env vars** (copy `.env.example` → `.env` and edit values)
```bash
export $(grep -v '^#' .env | xargs)  # mac/linux
# on Windows: use your shell's equivalent
```

3) **Create DB & schemas**
```bash
psql -h $PGHOST -U $PGUSER -p $PGPORT -d $PGDATABASE -f scripts/init_db.sql
```

4) **Load sample data**
```bash
python ingestion/load_gl_balances.py
```

5) **Build dbt models**
```bash
# dbt looks for profiles in ./profiles
export DBT_PROFILES_DIR=$(pwd)/profiles
dbt deps
dbt build    # runs models + tests
```

6) **Explore**
- Staging: `stg_gl_balances`
- Core: `dim_date`, `dim_account`, `f_gl_balances`
- Mart: `mart_pnl_by_dept`

## CI
On every PR, GitHub Actions will:
- Install python + dbt-postgres
- Run `dbt build` (models + tests)
- Fail the build if data quality tests fail

## Next Steps
- Replace sample ingestion with connectors (Airbyte/Fivetran) or your own loaders.
- Add facts: revenue events, expense details, forecast outputs.
- Extend marts: SaaS KPIs (ARR/NRR), cash, cohorts.
- Lock CoA mapping via PRs and dbt tests.
# forecasting_backbone_postgres
