select
  account_number,
  account_name,
  account_type,
  parent_account_number,
  rollup_group,
  gaap_tag
from {{ ref('chart_of_accounts') }}
