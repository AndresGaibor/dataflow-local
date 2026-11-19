---
source: https://qlik.dev/embed/machine-learning/tutorial/deploy-model/
last_updated: 2026-09-23T10:41:26+02:00
---

# Step 5: Deploy a model

Model deployments make trained models available in your environment.
Follow these steps to create, activate, and verify model deployments.

## Create a deployment

To deploy a model, specify its `modelId`, deployment name, `spaceId`, and other configuration details in the
request.
You also need to set `enablePredictions` to `true` to enable predictions for this model in the following API call:

```bash
curl -L -X POST "https://<TENANT>/api/v1/ml/deployments" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
    "data": {
        "type": "deployment",
        "attributes": {
            "name": "<NAME>",
            "spaceId": "<SPACE_ID>",
            "description": "<DESCRIPTION>",
            "modelId": "<MODEL_ID>",
            "enablePredictions": true,
            "deprecated": false
        }
    }
}'
```

If the deployment is successful, the `201` response includes:

- the `id`, which is the deployment ID that you'll need for activating the model and generating predictions.
- the `modelId`, which is the model ID associated with the deployment.

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  {
      "data": {
          "type": "deployment",
          "id": "4215f16e-4cc7-432c-bb5d-fc02f16b9c06",
          "attributes": {
              "id": "4215f16e-4cc7-432c-bb5d-fc02f16b9c06",
              "createdAt": "2024-12-01T16:34:31.552381459Z",
              "updatedAt": "2024-12-01T16:34:31.552381459Z",
              "name": "Model deployment for churn predictions",
              "spaceId": "6745f737f536738170dfe82f",
              "description": "Model deployment for churn predictions",
              "modelId": "bed12707-7deb-4a83-99f1-c936aa4a0ebd",
              "enablePredictions": true,
              "deprecated": false,
              "createdBy": "67475097984561d02f0cb3dc",
              "ownerId": "67475097984561d02f0cb3dc",
              "errorMessage": null
          }
      }
  }
  ```
</details>

With your model deployed in your environment, you can now activate it to make it ready to generate predictions.

### Activate a model

Once a deployment is created, it needs to be activated to generate predictions.
Use the deployment ID from the previous step to activate the model.

You can activate a model with the following API call:

```bash
curl -L -X POST "https://<TENANT>/api/v1/ml/deployments/<DEPLOYMENT_ID>/actions/activate-models" \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

When the model is successfully activated, you'll get a `204` response.

### Verify model activation

After activation, verify that the model's status is updated to `enabled`.
Use the model's `modelId` to review its details with the following API call:

```bash
curl -L "https://<TENANT>/api/v1/ml/experiments/<EXPERIMENT_ID>/models/<MODEL_ID>" \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

In the response, `"modelState": "enabled"` means that the model is activated and ready to generate predictions.

## Next step

With the model deployment activated, you can now [generate predictions](https://qlik.dev/embed/machine-learning/tutorial/deploy-model/generate-predictions) in real-time or batch.
Predictions allow you to use the deployed model for inference on new data.
