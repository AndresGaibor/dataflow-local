---
source: https://qlik.dev/embed/machine-learning/tutorial/create-experiment/
last_updated: 2026-09-23T10:41:26+02:00
---

# Step 1: Create an experiment

The first step in the automated machine learning workflow is to create an experiment.

An experiment defines the problem you want to solve.
It serves as the container for all training versions and acts as a foundation for training models.
For example, in a churn prediction use case, the experiment organizes all configurations and models to predict which
customers are likely to churn.

> **Note:** Access to the Machine Learning API may be restricted by custom roles and access controls set by your organization.
> If you encounter an error related to access, contact your system administrator to verify your permissions.

## Create an experiment

Create an experiment in the relevant space with the following API call:

```bash
curl -L -X POST "https://<TENANT>/api/v1/ml/experiments" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
    "data": {
        "type": "experiment",
        "attributes": {
            "name": "<EXPERIMENT_NAME>",
            "spaceId": "<SPACE_ID>",
            "description": "<DESCRIPTION>"
        }
    }
}'
```

This request defines the experiment name, an optional description, and the space where the experiment will be stored.

> **Note:** If you don't specify a space, the experiment will be created in your personal space.

The response includes an experiment ID (`id`). Save this `id` to manage the experiment in the next steps.

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  {
      "data": {
          "type": "experiment",
          "id": "4aaf4e82-d2d4-4fb3-9ff3-4dda6731a35b",
          "attributes": {
              "id": "4aaf4e82-d2d4-4fb3-9ff3-4dda6731a35b",
              "createdAt": "2024-11-29T17:31:30.257174561Z",
              "updatedAt": "2024-11-29T17:31:30.257174561Z",
              "tenantId": "GIlHILBfb5R6drAY2L7Zvi2c_YnlFDHR",
              "ownerId": "67475097984561d02f0cb3dc",
              "spaceId": "6745f737f536738170dfe82f",
              "name": "Churn Prediction Experiment",
              "description": "Experiment to predict churn"
          }
      }
  }
  ```
</details>

> **Note:** You can also:
>
> - List all experiments using **GET** `https://<TENANT>/api/v1/ml/experiments`.
> - Update the name or description of an experiment using **PATCH** `https://<TENANT>/api/v1/ml/experiments/{experimentId}`.

## Next step

Once your experiment is created, [profile your dataset](https://qlik.dev/embed/machine-learning/tutorial/create-experiment/dataset-profiling).
