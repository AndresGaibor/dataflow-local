---
source: https://qlik.dev/changelog/238-new-data-qualities-endpoints/
last_updated: 2026-07-17T10:59:08Z
---

# New API endpoints for computing and retrieving data quality for datasets in a data product

The [Data products](https://qlik.dev/apis/rest/data-governance/data-products/) and
[Data qualities](https://qlik.dev/apis/rest/data-governance/data-qualities/) APIs add four endpoints that let you trigger a data
quality refresh for the datasets in a data product and retrieve the results programmatically, replacing manual
refreshes in the Qlik Cloud hub. Use them from a pipeline orchestration tool or a scheduled Qlik Automate automation
to keep a data product's quality metrics and
[Qlik Trust Score™](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Qlik-Trust-score.htm)
up to date on a schedule, or automatically whenever new data lands.

Use the following endpoints together, in order:

1. `POST /api/data-governance/data-products/{dataProductId}/actions/compute-datasets-data-quality`: Trigger a data
   quality computation for every dataset in a data product. Returns a `batchComputationId` for tracking progress.
2. `GET /api/data-governance/data-qualities/batch-computations/{batchComputationId}`: Poll with the `batchComputationId`
   from step 1 until `status` is `FINISHED`. The response lists the `datasetId` and `computationId` for every dataset
   in the batch.
3. `POST /api/data-governance/data-qualities/global-results/actions/filter`: Pass the `datasetId` values from step 2
   to retrieve global quality results (valid, invalid, empty, and total sample cell counts) for up to 100 datasets at
   once.
4. `POST /api/data-governance/data-qualities/field-qualities/actions/filter`: Pass the same `datasetId` values to
   retrieve field-level quality results for up to 100 datasets at once. Field-level quality results are now available
   through the public API for the first time.

Once the batch computation finishes, you can also pass the same `datasetId` values to the
[Trust Scores API](https://qlik.dev/apis/rest/data-governance/trust-scores/) to retrieve the updated Qlik Trust Score™ for each
dataset.

For more information, see the reference documentation for the
[Data products](https://qlik.dev/apis/rest/data-governance/data-products/) and
[Data qualities](https://qlik.dev/apis/rest/data-governance/data-qualities/) APIs.
