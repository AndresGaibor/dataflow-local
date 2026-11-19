---
source: https://qlik.dev/embed/machine-learning/tutorial/create-experiment-version/
last_updated: 2026-09-23T10:41:26+02:00
---

# Step 3: Create an experiment version to train models

After creating an experiment and profiling your dataset, you can create an experiment version which represents a
specific configuration for your experiment.
This allows you to refine your approach and optimize model performance by testing different configurations.
Training generates models based on your configurations.

## Create an experiment version

Create an experiment using the following API call:

```bash
curl -L -X POST "https://<TENANT>/api/v1/ml/experiments/<EXPERIMENT_ID>/versions" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-d '{
  "data": {
      "type": "experiment-version",
      "attributes": {
      "name": "<EXPERIMENT_NAME>",
      "datasetOrigin": "new",
      "dataSetId": "<DATASET_ID>",
      "experimentMode": "<EXPERIMENT_MODE>",
      "featuresList": [
          { "name": "<FEATURE_NAME>", "dataType": "<DATA_TYPE>", "include": true, "changeType": "<TYPE>" }
      ],
      "target": "<TARGET_VARIABLE>",
      "experimentType": "<EXPERIMENT_TYPE>",
      "algorithms": ["<ALGORITHM>", "<ALGORITHM>"]
      }
  }
}'
```

You can use the `defaultVersionConfig` template returned when [profiling the dataset](https://qlik.dev/embed/machine-learning/tutorial/create-experiment-version/dataset-profiling) as the basis
for the `attributes` property in the request body. However, you must edit or add the following properties:

- You can edit the `name` property to describe the purpose of the experiment. By default, the name of the experiment
  version is a timestamp (for example, `2024-12-01T23:59:59.123Z`).

- Add a `target` property to specify the target variable. For example, `"target": "Churned"`. For guidance, see
  [Select the target](https://qlik.dev/embed/machine-learning/tutorial/create-experiment-version/dataset-profiling#select-the-target).

- Add an `experimentType` property to specify the experiment type. The experiment type for the selected target must be
  one of the `experimentTypes` from the `insights` property returned when [profiling the dataset](https://qlik.dev/embed/machine-learning/tutorial/create-experiment-version/dataset-profiling).
  In the following example, if the target feature is `Churned`, `binary` can be used as the experiment type.

  <details>
      <summary>
        Profile insights response example
      </summary>

      ```json
      {
        "insights": [
                    {
                        "name": "Churned",
                        "experimentTypes": [
                            "binary"
                        ],
                        "insights": [
                            "will_be_one_hot_encoded"
                        ],
                        "willBeDropped": false,
                        "cannotBeTarget": false
                    }
        ]
      }
      ```
    </details>

- If you don't add an `algorithms` property to specify the algorithms to test, all compatible for the specified
  experiment type will automatically be used to train models. Specifying a subset of compatible algorithms can help
  reduce model training duration. The following table shows the compatible algorithms for each experiment type:

  | **Experiment type** | **Description**                                     | **Compatible algorithms**                                                                                                                                                 |
  | ------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `binary`            | Binary classification (for example, churn/no churn) | `catboost_classifier`, `elasticnet_regression`, `gaussian_nb`, `lasso_regression`, `lgbm_classifier`, `logistic_regression`, `random_forest_classifier`, `xgb_classifier` |
  | `multiclass`        | Multiclass classification (for example, categories) | `catboost_classifier`, `elasticnet_regression`, `gaussian_nb`, `lasso_regression`, `lgbm_classifier`, `logistic_regression`, `random_forest_classifier`, `xgb_classifier` |
  | `regression`        | Predicting continuous numerical values              | `catboost_regression`, `lgbm_regression`, `linear_regression`, `random_forest_regression`, `sgd_regression`, `xgb_regression`                                             |

  For example, if the `experimentType` is `binary` and the target is `Churned`, you can add
  `"algorithms": ["gaussian_nb", "random_forest_classifier"]` to only train models with these algorithms.
  For more information about algorithms, see [Understanding model algorithms](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/algorithms.htm)
  on Qlik Help.

<details>
  <summary>
    **Request example**
  </summary>

  ```bash
  curl -L "https://<TENANT>/api/v1/ml/experiments/<EXPERIMENT_ID>/versions" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "data": {
        "type": "experiment-version",
        "attributes": {
            "name": "Experiment version for churn predictions",
            "datasetOrigin": "new",
            "dataSetId": "6749ddb893296645bb4bd795",
            "experimentMode": "intelligent",
            "featuresList": [
                {"name": "AccountID", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "Territory", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "Country", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "DeviceType", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "Promotion", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "HasRenewed", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "PlanType", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "BaseFee", "dataType": "DOUBLE", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "AdditionalFeatureSpend", "dataType": "INTEGER", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "NumberOfPenalties", "dataType": "INTEGER", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "CurrentPeriodUsage", "dataType": "DOUBLE", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "PriorPeriodUsage", "dataType": "DOUBLE", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "DaysSinceLastService", "dataType": "INTEGER", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "ServiceRating", "dataType": "DOUBLE", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "ServiceTickets", "dataType": "INTEGER", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "StartMonth", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "StartWeek", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "CustomerTenure", "dataType": "INTEGER", "include": true, "featureType": "numeric", "changeType": null},
                {"name": "Churned", "dataType": "STRING", "include": true, "featureType": "numeric", "changeType": null}
            ],
            "target": "Churned",
            "experimentType": "binary",
            "algorithms": ["gaussian_nb", "random_forest_classifier"]
        }
    }
  }'
  ```
</details>

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  {
    "data": {
        "type": "experiment-version",
        "id": "d06918b6-0bf8-404d-9b0d-dad9b4b0b17d",
        "attributes": {
            "id": "b336d5b6-f62b-4ef3-863e-99e737c53582",
            "experimentId": "4aaf4e82-d2d4-4fb3-9ff3-4dda6731a35b",
            "experimentType": "binary",
            "algorithms": [
                "gaussian_nb",
                "random_forest_classifier"
            ],
            "target": "Churned",
            "name": "Experiment version for churn predictions",
            "datasetOrigin": "new",
            "createdAt": "2024-12-01T14:17:43.641375111Z",
            "updatedAt": "2024-12-01T14:17:43.641375111Z",
            "createdByUserId": "67475097984561d02f0cb3dc",
            "topModelId": null,
            "status": "pending",
            "experimentMode": "intelligent",
            "featuresList": [
                {
                    "name": "AccountID",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "Territory",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "Country",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "DeviceType",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "Promotion",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "HasRenewed",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "PlanType",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "BaseFee",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "AdditionalFeatureSpend",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "NumberOfPenalties",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "CurrentPeriodUsage",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "PriorPeriodUsage",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "DaysSinceLastService",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "ServiceRating",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "ServiceTickets",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "StartMonth",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "StartWeek",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "CustomerTenure",
                    "changeType": null,
                    "include": true
                },
                {
                    "name": "Churned",
                    "changeType": null,
                    "include": true
                }
            ],
            "dataSetId": "6749ddb893296645bb4bd795"
        }
    }
  }
  ```
</details>

After creating an experiment version, the training process starts.

## Monitor training progress

Monitoring the training progress ensures your experiment version is running as expected and helps you track when results
are ready.

After the training has started, you can monitor its status with the following API call:

```bash
curl -L "https://<TENANT>/api/v1/ml/experiments/<EXPERIMENT_ID>/versions/<VERSION_ID>" \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

The API returns details about the experiment version, including:

- The training status. For example, `pending` means the training is in progress, while `ready` means that training has
  completed, and you can evaluate the results.
- The list of features used.
- The algorithms tested.
- The top-performing model, once models finish training. `topModelId` is the identifier for the best-performing model.
- Other configuration attributes.

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  {
      "data": {
          "type": "experiment-version",
          "id": "eb60cbd9-838f-4d4e-bb1c-18aaa6ad3ccf",
          "attributes": {
              "id": "eb60cbd9-838f-4d4e-bb1c-18aaa6ad3ccf",
              "experimentId": "22b753dc-8ffb-473c-987f-7ebf67c34d27",
              "experimentType": "binary",
              "algorithms": [
                  "gaussian_nb",
                  "random_forest_classifier"
              ],
              "target": "Churned",
              "name": "Experiment version for churn predictions",
              "datasetOrigin": "new",
              "createdAt": "2024-11-27T13:18:57.335013Z",
              "updatedAt": "2024-11-27T13:19:49.223574Z",
              "createdByUserId": "673dff8f87fc59e2a6a76f7c",
              "topModelId": "e87ee00a-e1cc-48ed-b1a5-0e56b7c5f5a1",
              "status": "ready",
              "experimentMode": "intelligent",
              "featuresList": [
                  {
                      "name": "AccountID",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "Territory",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "Country",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "DeviceType",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "Promotion",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "HasRenewed",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "PlanType",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "BaseFee",
                      "changeType": null,
                      "include": true,
                      "dataType": "DOUBLE"
                  },
                  {
                      "name": "AdditionalFeatureSpend",
                      "changeType": null,
                      "include": true,
                      "dataType": "INTEGER"
                  },
                  {
                      "name": "NumberOfPenalties",
                      "changeType": null,
                      "include": true,
                      "dataType": "INTEGER"
                  },
                  {
                      "name": "CurrentPeriodUsage",
                      "changeType": null,
                      "include": true,
                      "dataType": "DOUBLE"
                  },
                  {
                      "name": "PriorPeriodUsage",
                      "changeType": null,
                      "include": true,
                      "dataType": "DOUBLE"
                  },
                  {
                      "name": "ServiceRating",
                      "changeType": null,
                      "include": true,
                      "dataType": "DOUBLE"
                  },
                  {
                      "name": "ServiceTickets",
                      "changeType": null,
                      "include": true,
                      "dataType": "INTEGER"
                  },
                  {
                      "name": "StartMonth",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "StartWeek",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  },
                  {
                      "name": "CustomerTenure",
                      "changeType": null,
                      "include": true,
                      "dataType": "INTEGER"
                  },
                  {
                      "name": "Churned",
                      "changeType": null,
                      "include": true,
                      "dataType": "STRING"
                  }
              ],
              "dataSetId": "6749ddb893296645bb4bd795"
          }
      }
  }
  ```
</details>

> **Note:** Every version of an experiment must use the same `target` feature and `experimentType` as the first
> version.
> These settings can't change between versions.
> If they don't match, the API will return an error.

## Next step

Once training is complete, [retrieve and evaluate models](https://qlik.dev/embed/machine-learning/tutorial/create-experiment-version/evaluate-models) to identify the best-performing model for
deployment based on metrics like accuracy and precision.
