with d as (
  select date as period_end, year, month from {{ ref('dim_date') }}
),
g as (
  select * from {{ ref('stg_gl_balances') }}
)
select
  g.period_end,
  g.entity,
  coalesce(g.department, 'All') as department,
  g.account_number,
  g.currency,
  g.end_balance
from g
join d on d.period_end = g.period_end
