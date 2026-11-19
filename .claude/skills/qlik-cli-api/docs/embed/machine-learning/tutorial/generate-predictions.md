---
source: https://qlik.dev/embed/machine-learning/tutorial/generate-predictions/
last_updated: 2026-09-23T10:41:26+02:00
---

# Step 6: Make predictions

Predictions use deployed models that are activated to infer outcomes based on input data.
They can be generated in real-time or as batch jobs.

## Generate real-time predictions

Use a deployed model to infer outcomes for input feature sets and get immediate insights based on live data.
To generate real-time predictions, send the following API call:

```bash
curl -L -X POST "https://<TENANT>/api/v1/ml/deployments/<DEPLOYMENT_ID>/realtime-predictions/actions/run" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-H "Accept: text/csv" \
-d '{
    "schema": [
        {
            "name": "<string>"
        },
        {
            "name": "<string>"
        }
    ],
    "rows": [
        [
            "<string>",
            "<string>"
        ],
        [
            "<string>",
            "<string>"
        ]
    ]
}'
```

### Query parameters for real-time predictions

The request includes optional query parameters:

- `includeShap=<boolean>`: When set to `true`, the response includes [SHAP (SHapley Additive exPlanations) values](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/prediction-shap.htm)
  to explain predictions.
- `includeSource=<boolean>`: When set to `true`, the response includes original input data in the response.
- `includeNotPredictedReason=<boolean>`: When set to `true`, the response includes reasons for any prediction failures.
- `index=<string>`: Specify a unique identifier column for tracking predictions.

### Structure the request body for real-time predictions

You need to send input data that matches the features the model expects.
Here's how you can structure the request body:

- `schema` defines the features (columns) expected by the model to make a prediction.
- `rows` contains the actual data to predict outcomes for. Each row is an array of feature values in the same order as
  the schema.

The [example model](https://qlik.dev/embed/machine-learning/tutorial/generate-predictions/evaluate-models) `v03_RAFC_01_00` that has been deployed in the previous steps expects the
following features:

- `PlanType`
- `NumberOfPenalties`
- `HasRenewed`
- `BaseFee`
- `ServiceTickets`
- `AdditionalFeatureSpend`
- `ServiceRating`
- `Promotion`

Now, imagine you're predicting churn for two customers:

| Feature                  | Customer 1 | Customer 2 |
| ------------------------ | ---------- | ---------- |
| `PlanType`               | Standard   | Premium    |
| `NumberOfPenalties`      | 1          | 3          |
| `HasRenewed`             | true       | false      |
| `BaseFee`                | $50.00     | $80.00     |
| `ServiceTickets`         | 5          | 2          |
| `AdditionalFeatureSpend` | $15.50     | $25.00     |
| `ServiceRating`          | 4.2        | 3.8        |
| `Promotion`              | true       | false      |

These details are placed into the `rows` section of the request body.

Put all this together:

```json
{
  "schema": [
    { "name": "PlanType" },
    { "name": "NumberOfPenalties" },
    { "name": "HasRenewed" },
    { "name": "BaseFee" },
    { "name": "ServiceTickets" },
    { "name": "AdditionalFeatureSpend" },
    { "name": "ServiceRating" },
    { "name": "Promotion" }
  ],
  "rows": [
    ["Standard", 1, true, 50.0, 5, 15.5, 4.2, true],
    ["Premium", 3, false, 80.0, 2, 25.0, 3.8, false]
  ]
}
```

<details>
  <summary>
    **Request example with SHAP values and reasons for prediction failures**
  </summary>

  ```bash
  curl -L -X POST "https://<TENANT>/api/v1/ml/deployments/<DEPLOYMENT_ID>/realtime-predictions/actions/run?includeShap=true&includeNotPredictedReason=true" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
  "schema": [
      { "name": "PlanType" },
      { "name": "NumberOfPenalties" },
      { "name": "HasRenewed" },
      { "name": "BaseFee" },
      { "name": "ServiceTickets" },
      { "name": "AdditionalFeatureSpend" },
      { "name": "ServiceRating" },
      { "name": "Promotion" }
  ],
  "rows": [
      ["Standard", 1, true, 50.0, 5, 15.5, 4.2, true],
      ["Premium", 3, false, 80.0, 2, 25.0, 3.8, false]
  ]
  }'
  ```
</details>

## Understand real-time predictions

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  {
      "data": {
          "type": "realtime-prediction",
          "attributes": {
              "schema": [
                  {
                      "name": "automl_row_index",
                      "type": "numeric"
                  },
                  {
                      "name": "Churned_predicted",
                      "type": "categorical"
                  },
                  {
                      "name": "Churned_no",
                      "type": "numeric"
                  },
                  {
                      "name": "Churned_yes",
                      "type": "numeric"
                  },
                  {
                      "name": "PlanType_SHAP",
                      "type": "numeric"
                  },
                  {
                      "name": "NumberOfPenalties_SHAP",
                      "type": "numeric"
                  },
                  {
                      "name": "BaseFee_SHAP",
                      "type": "numeric"
                  },
                  {
                      "name": "HasRenewed_SHAP",
                      "type": "numeric"
                  },
                  {
                      "name": "ServiceTickets_SHAP",
                      "type": "numeric"
                  },
                  {
                      "name": "AdditionalFeatureSpend_SHAP",
                      "type": "numeric"
                  },
                  {
                      "name": "Promotion_SHAP",
                      "type": "numeric"
                  },
                  {
                      "name": "ServiceRating_SHAP",
                      "type": "numeric"
                  },
                  {
                      "name": "not_predicted_reason",
                      "type": "categorical"
                  }
              ],
              "rows": [
                  [
                      0,
                      "no",
                      0.5748563288337797,
                      0.4251436711662205,
                      -0.08696714660398806,
                      -0.016504858877164276,
                      0.31270329674944836,
                      0.0751632395258829,
                      -0.026030621640180034,
                      -0.008297165265234656,
                      -0.07740939502064204,
                      -0.08043817693148562,
                      null
                  ],
                  [
                      1,
                      "yes",
                      0.4220295388409809,
                      0.5779704611590192,
                      -0.08042057594415754,
                      -0.023509910893523875,
                      0.29031823511489696,
                      0.07309979343955059,
                      0.08679203458265218,
                      0.09052554583195933,
                      -0.07936633175213981,
                      -0.11239282844980283,
                      null
                  ]
              ]
          }
      }
  }
  ```
</details>

The response contains the results of the real-time prediction request:

- Prediction: The predicted class for each input row (in this example, whether the customer is likely to churn).
- Confidence scores: How sure the model is about its predictions, expressed as probabilities (in this example,
  the likelihood of "yes" or "no").
- SHAP values: The importance of each feature to the prediction. SHAP values help you understand why the model made its
  predictions. For more information, see [Understanding SHAP importance in experiment training](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/shap-importance.htm)
  on Qlik Help.
- Errors: Reasons why the model couldn't make a prediction, if any.

`schema` lists all the columns in the prediction response:

| **Column Name**               | **Type**      | **Description**                                                              |
| ----------------------------- | ------------- | ---------------------------------------------------------------------------- |
| `automl_row_index`            | `numeric`     | The index of the input row from the request.                                 |
| `Churned_predicted`           | `categorical` | The predicted outcome ("yes" for churn or "no" for not churn).               |
| `Churned_no`                  | `numeric`     | The model's confidence score (probability) that the customer will not churn. |
| `Churned_yes`                 | `numeric`     | The model's confidence score (probability) that the customer will churn.     |
| `PlanType_SHAP`               | `numeric`     | SHAP value indicating how the `PlanType` feature influenced the prediction.  |
| `NumberOfPenalties_SHAP`      | `numeric`     | SHAP value for `NumberOfPenalties`.                                          |
| `BaseFee_SHAP`                | `numeric`     | SHAP value for `BaseFee`.                                                    |
| `HasRenewed_SHAP`             | `numeric`     | SHAP value for `HasRenewed`.                                                 |
| `ServiceTickets_SHAP`         | `numeric`     | SHAP value for `ServiceTickets`.                                             |
| `AdditionalFeatureSpend_SHAP` | `numeric`     | SHAP value for `AdditionalFeatureSpend`.                                     |
| `Promotion_SHAP`              | `numeric`     | SHAP value for `Promotion`.                                                  |
| `ServiceRating_SHAP`          | `numeric`     | SHAP value for `ServiceRating`.                                              |
| `not_predicted_reason`        | `categorical` | If the row wasn't predicted, this provides the reason.                       |

`rows` contains the prediction results for each input (in this example, Customer 1 and Customer 2):

| **Row index** | **Prediction** | **Confidence (No)** | **Confidence (Yes)** | **SHAP Values**                                                                   |
| ------------- | -------------- | ------------------- | -------------------- | --------------------------------------------------------------------------------- |
| `0`           | `no`           | `0.5749`            | `0.4251`             | Importance of `PlanType`, `BaseFee`, `ServiceTickets`, etc., for predicting "no"  |
| `1`           | `yes`          | `0.4220`            | `0.5780`             | Importance of `PlanType`, `BaseFee`, `ServiceTickets`, etc., for predicting "yes" |

The predictions can be interpreted as follows:

- Predictions (`Churned_predicted`):
  - `"yes"` means the model predicts the customer is likely to churn.
  - `"no"` means the model predicts the customer is unlikely to churn.

- Confidence scores (`Churned_no` and `Churned_yes`) show how sure the model is about each outcome. They are
  probabilities. For example:
  - For Customer 1 (row 0), the model is `57.49%` confident they will not churn (`Churned_no` = `0.5749`) .
  - For Customer 2 (row 1), the model is `57.80%` confident they will churn (`Churned_yes` = `0.5780`).

- SHAP Values explain how strongly each feature impacted the prediction. They are "pushes" towards a decision. Positive
  values mean the feature makes the model more likely to predict "yes" (churn). Negative values mean the feature makes
  the model more likely to predict "no" (not churn). For example:
  - For Customer 1 (row 0), `BaseFee_SHAP` has a positive contribution towards predicting "no" (churn).
  - For Customer 2 (row 1), `AdditionalFeatureSpend_SHAP` has a positive contribution towards predicting "yes"
    (not churn).

- Errors (`not_predicted_reason`): If a prediction is not made for a row, the `not_predicted_reason` column explains
  why. In this example, all predictions succeeded, so the column is `null`.

## Generate batch predictions

You can also use a deployed model to generate batch predictions to process larger datasets asynchronously. This is
useful when you have a significant volume of data to analyze or when real-time predictions aren't feasible.

### Create a batch prediction job

To create a batch prediction job, use the following API call:

```bash
curl -L -X POST "https://<TENANT>/api/v1/ml/deployments/<DEPLOYMENT_ID>/batch-predictions" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d "{
    \"data\": {
        \"type\": \"batch-prediction\",
        \"attributes\": {
            \"name\": \"<NAME>\",
            \"deploymentId\": \"<DEPLOYMENT_ID>\",
            \"description\": \"<DESCRIPTION>\",
            \"dataSetId\": \"<DATASET_ID>\",
            \"indexColumn\": \"<INDEX_COLUMN>\",
            \"schedule\": {
                \"timezone\": \"<TIMEZONE>\",
                \"recurrence\": [\"RECURRENCE_RULE\"],
                \"endDateTime\": \"<END_TIME>\",
                \"startDateTime\": \"<START_TIME>\",
                \"applyDatasetChangeOnly\": boolean
            },
            \"writeback\": {
                \"format\": \"<FORMAT>\",
                \"dstName\": \"<OUTPUT_FILE_NAME>\",
                \"spaceId\": \"<SPACE_ID>\",
                \"dstShapName\": \"<SHAP_FILE_NAME>\",
                \"dstSourceName\": \"<SOURCE_FILE_NAME>\",
                \"dstCoordShapName\": \"<COORDINATE_SHAP_FILE_NAME>\",
                \"dstNotPredictedName\": \"<NOT_PREDICTED_FILE_NAME>\"
            }
        }
    }
}"
```

### Structure the request body for batch predictions

The `attributes` field specifies general job details:

- `name`: A name for the batch prediction job.
- `description`: A short description of the job's purpose.
- `dataSetId`: The unique identifier for the apply dataset (the new dataset for which you will generate batch
  predictions).
- `indexColumn`: (Optional) A column in the apply dataset used to uniquely identify rows in the prediction results.
  If not specified, a column will be automatically generated.

The `schedule` field defines when and how frequently the batch prediction runs:

- `timezone`: The time zone for the schedule (for example, `"America/Toronto"`).
- `recurrence`: A recurrence rule in RFC 5545 format. For example, `RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=16;BYMINUTE=30;BYSECOND=0`.
- `startDateTime` and `endDateTime`: Define the prediction job's start and end times.
- `applyDatasetChangeOnly`: When `true`, triggers predictions only when the dataset changes.
  If you don't want to schedule the batch prediction job and run it manually, set this to `null`.

The `writeback` field specifies how and where the prediction results are saved. At a minimum, it requires the `spaceId`,
`format`, and `dstName` properties.

| **Property**          | **Type** | **Description**                                                                                                                             |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `spaceId`             | `string` | The ID of the storage space where prediction results will be saved. Leave as an empty string (`""`) to save results to your personal space. |
| `format`              | `string` | File format for the output. The supported formats are `"qvd"`, `"parquet"`, `"csv"`.                                                        |
| `dstName`             | `string` | The name of the main output file containing the prediction results.                                                                         |
| `dstShapName`         | `string` | The name of the file containing SHAP (SHapley Additive exPlanations) values for feature importance explanations.                            |
| `dstSourceName`       | `string` | The name of the apply dataset, which contains the input data rows used for predictions (useful for traceability and debugging).             |
| `dstCoordShapName`    | `string` | The name of the file containing SHAP values for geospatial coordinates, if applicable.                                                      |
| `dstNotPredictedName` | `string` | The name of the file containing rows that could not be predicted, along with associated error messages.                                     |

Here is an example:

```json
"writeback": {
    "spaceId": "6745f737f536738170dfe82f",
    "format": "parquet",
    "dstName": "customer_predictions",
    "dstShapName": "customer_predictions_shap.parquet",
    "dstSourceName": "customer_predictions_source.parquet",
    "dstCoordShapName": "customer_predictions_coord_shap.parquet",
    "dstNotPredictedName": "customer_predictions_not_predicted.parquet"
}
```

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  {
    "data": {
        "type": "batch-prediction",
        "id": "9bf8c57e-5f65-4ed5-b504-21daa33248db",
        "attributes": {
            "id": "9bf8c57e-5f65-4ed5-b504-21daa33248db",
            "deploymentId": "f822f467-6a81-4cb7-bb90-ebe3b4224c30",
            "createdAt": "2024-12-13T14:24:48.704645172Z",
            "updatedAt": "2024-12-13T14:24:48.704645172Z",
            "name": "Churn_predictions",
            "dataSetId": "6749ddb8bf86ce46d48fe0a3",
            "createdBy": "67475097984561d02f0cb3dc",
            "ownerId": "67475097984561d02f0cb3dc",
            "errorMessage": null,
            "indexColumn": null,
            "status": "modified",
            "schedule": null,
            "writeback": {
                "spaceId": "6745f737f536738170dfe82f",
                "format": "parquet",
                "dstName": "customer_predictions.parquet",
                "dstShapName": "customer_predictions_shap.parquet",
                "dstSourceName": "customer_predictions_source.parquet",
                "dstCoordShapName": "customer_predictions_coord_shap.parquet",
                "dstNotPredictedName": "customer_predictions_not_predicted.parquet"
            }
        }
    }
  }
  ```
</details>

In this example:

- Results are saved in the parquet format and saved in the space with the identifier `6745f737f536738170dfe82f`.
- SHAP values are saved to `customer_predictions_shap.parquet`.
- Source rows are saved to `customer_predictions_source.parquet`.
- SHAP values for geospatial coordinates are saved to `customer_predictions_coord_shap.parquet`.
- Non-predicted rows are saved to `customer_predictions_not_predicted.parquet`.

### Start a batch prediction job

Once the batch prediction is configured, start the job with the following API call:

```bash
curl -L -X POST "https://<TENANT>/api/v1/ml/deployments/<DEPLOYMENT_ID>/batch-predictions/<BATCH_PREDICTION_ID>/actions/predict" \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

Batch predictions run as background jobs. The `201 Created` confirms job creation.

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  {
      "data": {
          "id": "e217457-8087-47d6-84b1-3f9dfce4955c",
          "type": "job",
          "attributes": {
              "id": "e217457-8087-47d6-84b1-3f9dfce4955c",
              "createdAt": "2024-12-13T14:24:48.704645172Z",
              "updatedAt": "2024-12-13T14:24:48.704645172Z",
              "deletedAt": null,
              "tenantId": "GIlHILBfb5R6drAY2L7Zvi2c_YnlFDHR",
              "createdBy": "67475097984561d02f0cb3dc",
              "status": "pending",
              "corrId": "fe4f2cbd-7961-4596-bfd8-3b4520acf712",
              "jobType": "prediction",
              "corrType": "prediction",
              "deploymentId": "f822f467-6a81-4cb7-bb90-ebe3b4224c30",
              "spaceId": "6745f737f536738170dfe82f",
              "name": "Churn_predictions",
              "parentName": "Model deployment for churn predictions",
              "details": {
                  "outputFiles": [],
                  "isScheduled": false
              },
              "trigger": "manual",
              "success": null,
              "modelId": "f7336f07-978e-45f7-b449-fc1da6f17c37"
          }
      }
  }
  ```
</details>

## Monitor batch prediction progress

Monitoring the batch prediction progress ensures predictions are running as expected and helps you track when results
are ready.

After the prediction job has started, you can monitor its status with the following API call:

```bash
curl -L "https://<TENANT>/api/v1/ml/deployments/<DEPLOYMENT_ID>/batch-predictions" \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

The API returns details about batch predictions job, including the prediction status. For example, `ready` means that
process has completed, and you can evaluate the prediction results.

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  {
    "type": "batch-prediction",
    "id": "9bf8c57e-5f65-4ed5-b504-21daa33248db",
    "attributes": {
        "id": "9bf8c57e-5f65-4ed5-b504-21daa33248db",
        "deploymentId": "f822f467-6a81-4cb7-bb90-ebe3b4224c30",
        "createdAt": "2024-12-13T14:24:48.704645172Z",
        "updatedAt": "2024-12-13T14:24:48.704645172Z",
        "name": "Churn_predictions",
        "dataSetId": "6749ddb8bf86ce46d48fe0a3",
        "createdBy": "67475097984561d02f0cb3dc",
        "ownerId": "67475097984561d02f0cb3dc",
        "errorMessage": null,
        "indexColumn": null,
        "status": "ready",
        "schedule": null,
        "writeback": {
            "spaceId": "6745f737f536738170dfe82f",
            "format": "parquet",
            "dstName": "customer_predictions.parquet",
            "dstShapName": "customer_predictions_shap.parquet",
            "dstSourceName": "customer_predictions_source.parquet",
            "dstCoordShapName": "customer_predictions_coord_shap.parquet",
            "dstNotPredictedName": "customer_predictions_not_predicted.parquet"
        }
    }
  }
  ```
</details>

Once in `ready` status, predictions are available in the specified space.

## Next steps

- Verify that the predictions align with your expectations.
- Analyze SHAP values to understand which features had the biggest impact on the model's decisions.
- If any prediction fails, review prediction errors and solve the issue.
