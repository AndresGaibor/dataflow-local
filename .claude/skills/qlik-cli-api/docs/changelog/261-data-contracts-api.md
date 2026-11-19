---
source: https://qlik.dev/changelog/261-data-contracts-api/
last_updated: 2026-10-22T18:16:22+02:00
---

# New REST API - Data contracts API for managing dataset expectations

The new [Data contracts API](https://qlik.dev/apis/rest/data-governance/data-contracts/) lets you manage data contracts for datasets in
your Qlik Cloud tenant. Data contracts define quality expectations, such as error thresholds for Qlik Trust Score™
dimensions or a record range for data volume.

Use the API to create data contracts for multiple datasets and manage their expectations programmatically, for example
as part of a data onboarding or governance workflow.

The following endpoints are available:

- `POST /api/data-governance/data-contracts/datasets/actions/create`: Creates data contracts for up to 100 datasets in a
  single request, with expectations specified for each dataset. The response includes a result for each dataset, and
  existing contracts aren't overwritten.
- `GET /api/data-governance/data-contracts/datasets/{datasetId}/expectations`: Returns a dataset's expectations,
  including their activation status, configured thresholds or ranges, and last evaluation results.
  If no data contract exists, the endpoint returns the default, non-activated expectations.
- `PATCH /api/data-governance/data-contracts/datasets/{datasetId}/expectations`: Activates, deactivates, or updates
  expectations. Activating an expectation also creates a data contract if one doesn't exist yet. The response includes a
  result for each expectation.
- `DELETE /api/data-governance/data-contracts/datasets/{datasetId}`: Deletes a dataset's data contract and its
  associated expectations.

For more information, see the [Data contracts API reference](https://qlik.dev/apis/rest/data-governance/data-contracts/).
To learn more about data contracts in Qlik Cloud, see [Managing data contracts](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Managing-data-contracts.htm)
on Qlik Help.
