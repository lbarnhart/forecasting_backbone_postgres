with f as (
  select * from {{ ref('f_gl_balances') }}
),
a as (
  select * from {{ ref('dim_account') }}
)
select
  period_end,
  entity,
  department,
  sum(case when a.account_type = 'Revenue' then end_balance else 0 end) as revenue,
  sum(case when a.account_type = 'COGS' then end_balance else 0 end) as cogs,
  sum(case when a.account_type = 'OpEx' then end_balance else 0 end) as opex,
  sum(case when a.account_type = 'Revenue' then end_balance else 0 end)
    - sum(case when a.account_type = 'COGS' then end_balance else 0 end) as gross_margin,
  sum(end_balance) filter (where a.account_type in ('Revenue','COGS','OpEx')) as pnl_total
from f
join a using (account_number)
group by 1,2,3
