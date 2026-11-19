---
source: https://qlik.dev/changelog/253-data-qualities-api-assign-field-types/
last_updated: 2026-10-02T14:05:15Z
---

# New Data qualities API endpoint for assigning types to dataset fields

The [Data qualities API](https://qlik.dev/apis/rest/data-governance/data-qualities/) adds the
`PUT /api/data-governance/data-qualities/fields-structures` endpoint, which lets you assign a standard or semantic type
to one or more fields in a dataset. Assigning types programmatically lets you correct or standardize how Qlik Cloud
interprets fields without manually updating each field in the dataset, for example as part of a data onboarding
pipeline.

The request body contains the `datasetId` of the target dataset and a `fields` array. Each item in the array has the
field `name` and a `type` object. Set `type.kind` to `STANDARD` or `SEMANTIC`. For a semantic type, set
`type.semanticTypeId` to the ID of the semantic type. For a standard type, set `type.name`. For date and time fields,
also set `type.precision`.

The endpoint performs a partial update. It changes only the fields in the request, and any field that isn't included
keeps its current assigned type.

To manage semantic types, see the [Semantic types API](https://qlik.dev/apis/rest/data-governance/semantic-types/).

For more information, see the [Data qualities API reference](https://qlik.dev/apis/rest/data-governance/data-qualities/).
