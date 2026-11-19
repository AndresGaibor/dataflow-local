---
source: https://qlik.dev/changelog/237-trust-scores-api/
last_updated: 2026-07-17T12:50:11+02:00
---

# New REST API - Trust Scores API for retrieving Qlik Trust Score™ in bulk

The new [Trust Scores API](https://qlik.dev/apis/rest/data-governance/trust-scores/) lets you retrieve the current
Qlik Trust Score™ for multiple datasets in a single request.

Use `POST /api/data-governance/trust-scores/results/data-sets/actions/filter` to retrieve the Qlik
Trust Score™ for up to 100 datasets at a time, including the overall score plus a per-axis and
per-metric breakdown. Datasets with no computed Qlik Trust Score™ are omitted from the response.

Combine it with the [Data products API](https://qlik.dev/apis/rest/data-governance/data-products/) to trigger a data
quality refresh, the [Data qualities API](https://qlik.dev/apis/rest/data-governance/data-qualities/) to poll for
completion, and this endpoint to retrieve the updated Qlik Trust Score™. Schedule the whole flow with
[Qlik Automate](https://qlik.dev/toolkits/no-code/) for recurring quality and trust checks without manual
intervention.

For more information, see the [Trust Scores API reference](https://qlik.dev/apis/rest/data-governance/trust-scores/)
and the [Data Products API](https://qlik.dev/apis/rest/data-governance/data-products/).
