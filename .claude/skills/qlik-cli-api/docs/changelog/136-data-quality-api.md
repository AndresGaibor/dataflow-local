---
source: https://qlik.dev/changelog/136-data-quality-api/
last_updated: 2025-04-25T12:36:25+02:00
---

# New REST API - Data Quality API for assessing data quality in Qlik Cloud

The new [Data Quality](https://qlik.dev/apis/rest/data-qualities/) API allows you to programmatically compute and retrieve data quality
results for datasets in Qlik Cloud.

The API allows evaluating the quality of a dataset based on a sample of its rows. It returns counts of valid, invalid,
and empty cells within the sample. This helps you assess the trustworthiness of your data, especially as it may be
consumed downstream by analytics, AI models, or other consumers.

The new endpoints are:

- `POST /v1/data-qualities/computations`: Trigger a data quality computation.
- `GET /v1/data-qualities/computations/{computationId}`: Retrieve the status of a data quality computation.
- `GET /v1/data-qualities/global-results`: Retrieve global data quality results for a dataset.

For more information, see the [reference documentation for the Data Quality API](https://qlik.dev/apis/rest/data-qualities/).
