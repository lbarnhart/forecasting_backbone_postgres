with src as (
  select
    period_end::date,
    entity::text,
    nullif(department,'All')::text as department,
    account_number::text,
    currency::text,
    end_balance::numeric(18,2)
  from raw.raw_gl_balances
)
select * from src
