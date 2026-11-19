---
source: https://qlik.dev/changelog/249-semantic-types-api-endpoints/
last_updated: 2026-10-01T15:03:30+02:00
---

# New Semantic types API endpoints for managing semantic types

The Semantic types API now includes endpoints for creating, retrieving, updating, and deleting semantic types, and for
querying dataset fields associated with a semantic type.

These endpoints let you manage semantic type definitions programmatically and identify where a semantic type is used
across dataset fields:

- `GET /api/data-governance/semantic-types`: List semantic types
- `POST /api/data-governance/semantic-types`: Create a semantic type
- `GET /api/data-governance/semantic-types/{semanticTypeId}`: Retrieve a semantic type
- `PATCH /api/data-governance/semantic-types/{semanticTypeId}`: Update a semantic type
- `DELETE /api/data-governance/semantic-types/{semanticTypeId}`: Delete a semantic type
- `GET /api/data-governance/semantic-types/{semanticTypeId}/dataset-fields`: List dataset fields using a semantic type

For more information, see the [Semantic types API reference](https://qlik.dev/apis/rest/data-governance/semantic-types/)
and [Managing semantic types](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Managing-semantic-types.htm)
on Qlik Help.
