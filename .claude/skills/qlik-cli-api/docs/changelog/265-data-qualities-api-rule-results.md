---
source: https://qlik.dev/changelog/265-data-qualities-api-rule-results/
last_updated: 2026-11-06T18:02:45+01:00
---

# New Data qualities API endpoint for retrieving rule results across datasets

The Data qualities API adds a new endpoint to retrieve data quality results for a specific rule across multiple
datasets.

Use `POST /api/data-governance/data-qualities/global-results/data-quality-rules/actions/filter` to retrieve the latest
computed results for a rule, including field-level results, aggregated metrics per dataset, and an overall aggregation
across datasets.

The request requires a `ruleId` and optionally accepts up to 100 dataset IDs. If you omit the dataset IDs, the API
retrieves results from all datasets you can access that use the rule.

The endpoint supports pagination and sorting by dataset ID. The overall aggregation includes all matching datasets,
regardless of pagination.

For more information, see the [Data qualities API reference documentation](https://qlik.dev/apis/rest/data-governance/data-qualities/).
