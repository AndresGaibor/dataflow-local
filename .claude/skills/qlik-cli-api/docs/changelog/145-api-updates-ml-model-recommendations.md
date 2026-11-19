---
source: https://qlik.dev/changelog/145-api-updates-ml-model-recommendations/
last_updated: 2025-06-11T13:02:26+02:00
---

# Updated API - The Machine Learning API adds an endpoint for model recommendations

The [Machine Learning API](https://qlik.dev/apis/rest/ml/) has been updated with a new endpoint to help you quickly identify the most
suitable model for a given experiment:

`POST /api/v1/experiments/{experimentId}/recommendations` - Request recommended models for an experiment.

This endpoint analyzes available models and selects those that perform best across three categories:

- **Best model** - The model with the best balance of performance and speed.
- **Fastest model** - The model with the highest prediction speed among those with accuracy within 10% of the top model.
- **Most accurate model** - The model with the highest predictive accuracy.

For more information, refer to the [Machine Learning API reference documentation](https://qlik.dev/apis/rest/ml/).
