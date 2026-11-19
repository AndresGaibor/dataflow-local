---
source: https://qlik.dev/changelog/132-api-updates-ml-model-aliases/
last_updated: 2025-04-03T16:21:21+02:00
---

# Updated API - The Machine Learning API now supports multiple models per deployment

The [Machine Learning API](https://qlik.dev/apis/rest/ml/) has been updated with new endpoints that allow you to deploy multiple models,
referenced as aliases, within a single deployment.

The new system of aliases allows you to seamlessly swap models without modifying deployment configurations or disrupting
downstream integrations.

The new endpoints are:

- `POST /v1/ml/deployments/{deploymentId}/models/actions/add` - Add deployed models to the specified deployment
- `POST /v1/ml/deployments/{deploymentId}/models/actions/remove` - Remove models from the specified deployment
- `POST /v1/ml/deployments/{deploymentId}/aliases` - Create an alias
- `GET /v1/ml/deployments/{deploymentId}/aliases` - Retrieve a list of aliases
- `GET /v1/ml/deployments/{deploymentId}/aliases/{aliasId}` - Retrieve an alias
- `PATCH /v1/ml/deployments/{deploymentId}/aliases/{aliasId}` - Update an alias
- `DELETE /v1/ml/deployments/{deploymentId}/aliases/{aliasId}` - Delete an alias
- `POST /v1/ml/deployments/{deploymentId}/aliases/{aliasName}/realtime-predictions/actions/run` - Generate real-time
  predictions using an alias

For more information, see the [reference documentation for the Machine Learning API](https://qlik.dev/apis/rest/ml/).
