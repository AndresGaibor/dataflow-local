---
source: https://qlik.dev/changelog/29-api-updates-automl/
last_updated: 2025-07-08T16:09:30Z
---

# New APIs - AutoML Dataset Predictions, AutoML Real-time Predictions

### AutoML Dataset Predictions

This API allows the creation and manipulation of machine learning models, and generation of predictions.

With AutoML Dataset Predictions you can:

- `GET/api/v1/automl-predictions/{predictionId}/coordinate-shap`: Return a file containing the shapley
  values in coordinate form that are associated with a predictionId.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/automl-predictions/{predictionId}/coordinate-shap" \
 -H "Authorization: Bearer <API-key>"
```

- `POST/api/v1/automl-predictions/{predictionId}/jobs` : Retrieve jobs that are associated
  with a prediction.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/automl-predictions/{predictionId}/jobs" \
 -X POST \
 -H "Authorization: Bearer <API-key>"
```

- `GET/api/v1/automl-predictions/{predictionId}/predictions`: Return a file containing the predicted
  values that are associated with a predictionId.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/automl-predictions/{predictionId}/predictions" \
 -H "Authorization: Bearer <API-key>"
```

And more, see full API reference [here](https://qlik.dev/apis/rest/automl-predictions)

### AutoML Real-time Predictions

With AutoML Real-time Predictions you can:

- `POST/api/v1/automl-deployments/{deploymentId}/realtime-predictions`: Generate predictions in a
  synchronous request and response.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/automl-deployments/{deploymentId}/realtime-predictions" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{"schema":{"rows":[],"schema":[{"name":"string"}]}}'
```

See [API reference here](https://qlik.dev/apis/rest/automl-deployments).
