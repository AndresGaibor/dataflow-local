---
source: https://qlik.dev/embed/machine-learning/tutorial/dataset-profiling/
last_updated: 2026-09-23T10:41:26+02:00
---

# Step 2: Profile your dataset

Profiling your dataset helps ensure it is suitable for machine learning.
This process generates insights about features, highlights potential issues, and identifies features that align with
your experiment goals.

## Retrieve dataset information

Use the following call to the [Items API](https://qlik.dev/apis/rest/items/) to find all datasets in your tenant:

```bash
curl -L "https://<TENANT>/api/v1/items?resourceType=dataset" \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

Locate your dataset in the response and save its `resourceId` (for example, `6749ddb893296645bb4bd795`).
You'll need this ID for profiling the dataset.

<details>
  <summary>
    **Response example**
  </summary>

  ```json
  "data": [
          {
              "name": "AutoML Example - Churn data - training.csv",
              "spaceId": "6745f737f536738170dfe82f",
              "resourceAttributes": {
                  "appType": "QIX-DF",
                  "dataStoreName": "DataFilesStore",
                  "dataStoreType": "qix-datafiles",
                  "qri": "qdf:qix-datafiles:GIlHILBfb5R6drAY2L7Zvi2c_YnlFDHR:sid@6745f737f536738170dfe82f:AutoML Example - Churn data - training.csv",
                  "secureQri": "qri:qdf:space://cxT3ijCQNKeVFuqux1p1C7SLfDe7crQa8-BAbZvXXDA#UitfNqc2PShxZs6qPzkllSp7PQ37AQYCZri7OIdcLgo",
                  "sourceSystemId": "QIX-DF_88b30e9b-5738-4c9b-bd4e-dd2c2d3b542d",
                  "technicalDescription": "",
                  "technicalName": "AutoML Example - Churn data - training.csv",
                  "type": "DELIMETED",
                  "version": "1"
              },
              "resourceCustomAttributes": null,
              "resourceUpdatedAt": "2024-11-26T16:29:55Z",
              "resourceType": "dataset",
              "resourceSubType": "qix-df",
              "resourceId": "6745f77ebf86ce46d48ed34f",
              "resourceCreatedAt": "2024-11-26T16:29:50Z",
              "id": "6745f77ef10262fdb0a50c55",
              "createdAt": "2024-11-26T16:29:50Z",
              "updatedAt": "2024-11-26T16:29:55Z",
              "creatorId": "62d58b0a6cdb747267985bb2",
              "updaterId": "62d58b0a6cdb747267985bb2",
              "tenantId": "GIlHILBfb5R6drAY2L7Zvi2c_YnlFDHR",
              "isFavorited": false,
              "links": {
                  "self": {
                      "href": "https://tenant.us.qlik.com/api/v1/items/6745f77ef10262fdb0a50c55"
                  },
                  "collections": {
                      "href": "https://tenant.us.qlik.com/api/v1/items/6745f77ef10262fdb0a50c55/collections"
                  }
              },
              "actions": [
                  "create",
                  "delete",
                  "list",
                  "profile",
                  "read",
                  "update"
              ],
              "collectionIds": [],
              "meta": {
                  "isFavorited": false,
                  "actions": [
                      "create",
                      "delete",
                      "list",
                      "profile",
                      "read",
                      "update"
                  ],
                  "tags": [],
                  "collections": []
              },
              "ownerId": "62d58b0a6cdb747267985bb2",
              "resourceReloadEndTime": "",
              "resourceReloadStatus": "",
              "resourceSize": {
                  "appFile": 0,
                  "appMemory": 0
              },
              "itemViews": {}
          }
          ]
  ```
</details>

## Profile your dataset

Use the following call to generate insights about your dataset, identifying features suitable for training and
highlighting potential issues.

Include the `resourceId` obtained previously as the `dataSetId` in the request body:

```bash
curl -L -X POST "https://<TENANT>/api/v1/ml/profile-insights" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-d '{
    "data": {
        "type": "profile-insights",
        "attributes": {
            "dataSetId": "<DATASET_ID>"
        }
    }
}'
```

The response includes feature-level insights.

In the following example, the response contains the following key insights:

- `high_cardinality`: Features with many unique values.
- `will_be_one_hot_encoded`: Feature will be one-hot encoded during preprocessing.
- `will_be_impact_encoded`: Feature will use impact encoding for categorical data.
- `willBeDropped`: When `true`, the feature will be excluded from the training process.
- `cannotBeTarget`: When `true`, the feature isn't suitable as a target variable.

The `experimentTypes` property lists suitable experiment types for each feature.

The response also includes a `defaultVersionConfig` property, which serves as a template for creating experiment
versions. This property provides a feature list with data types, inclusion settings, and other configuration for
downstream processes. You can copy, edit, and use this in the body of the
`POST /ml/experiments/{experimentId}/versions` request to [create an experiment version](https://qlik.dev/embed/machine-learning/tutorial/dataset-profiling/create-experiment-version).

In this example, the `experimentMode` returned is set to `intelligent`. Intelligent model optimization automatically
refines models through iterations. For more information, see [Intelligent model optimization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/intelligent-model-optimization.htm)
on Qlik Help.

<details>
  <summary>
    **Response example**
  </summary>

  ```json
{
    "data": {
        "type": "profile-insights",
        "id": "6749ddb893296645bb4bd795",
        "attributes": {
            "tenantId": "GIlHILBfb5R6drAY2L7Zvi2c_YnlFDHR",
            "ownerId": "67475097984561d02f0cb3dc",
            "status": "ready",
            "insights": [
                {
                    "name": "AccountID",
                    "experimentTypes": [],
                    "insights": [
                        "high_cardinality",
                        "will_be_impact_encoded",
                        "valid_index"
                    ],
                    "willBeDropped": true,
                    "cannotBeTarget": true
                },
                {
                    "name": "Territory",
                    "experimentTypes": [],
                    "insights": [
                        "will_be_impact_encoded"
                    ],
                    "willBeDropped": false,
                    "cannotBeTarget": true
                },
                {
                    "name": "Country",
                    "experimentTypes": [],
                    "insights": [
                        "constant",
                        "will_be_one_hot_encoded"
                    ],
                    "willBeDropped": true,
                    "cannotBeTarget": true
                },
                {
                    "name": "DeviceType",
                    "experimentTypes": [
                        "multiclass"
                    ],
                    "insights": [
                        "will_be_one_hot_encoded"
                    ],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "Promotion",
                    "experimentTypes": [
                        "binary"
                    ],
                    "insights": [
                        "will_be_one_hot_encoded"
                    ],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "HasRenewed",
                    "experimentTypes": [
                        "binary"
                    ],
                    "insights": [
                        "will_be_one_hot_encoded"
                    ],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "PlanType",
                    "experimentTypes": [
                        "multiclass"
                    ],
                    "insights": [
                        "will_be_one_hot_encoded"
                    ],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "BaseFee",
                    "experimentTypes": [
                        "regression"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "AdditionalFeatureSpend",
                    "experimentTypes": [
                        "regression"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "NumberOfPenalties",
                    "experimentTypes": [
                        "multiclass"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "CurrentPeriodUsage",
                    "experimentTypes": [
                        "regression"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "PriorPeriodUsage",
                    "experimentTypes": [
                        "regression"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "DaysSinceLastService",
                    "experimentTypes": [
                        "regression"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "ServiceRating",
                    "experimentTypes": [
                        "regression"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "ServiceTickets",
                    "experimentTypes": [
                        "regression"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
                {
                    "name": "StartMonth",
                    "experimentTypes": [],
                    "insights": [
                        "will_be_one_hot_encoded"
                    ],
                    "willBeDropped": false,
                    "cannotBeTarget": true
                },
                {
                    "name": "StartWeek",
                    "experimentTypes": [],
                    "insights": [
                        "will_be_impact_encoded"
                    ],
                    "willBeDropped": false,
                    "cannotBeTarget": true
                },
                {
                    "name": "CustomerTenure",
                    "experimentTypes": [
                        "regression"
                    ],
                    "insights": [],
                    "willBeDropped": false,
                    "cannotBeTarget": false
                },
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
            ],
            "defaultVersionConfig": {
                "name": "2024-12-10T15:08:06.570Z",
                "datasetOrigin": "new",
                "dataSetId": "6749ddb893296645bb4bd795",
                "experimentMode": "intelligent",
                "featuresList": [
                    {
                        "name": "AccountID",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "Territory",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "Country",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "DeviceType",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "Promotion",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "HasRenewed",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "PlanType",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "BaseFee",
                        "dataType": "DOUBLE",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "AdditionalFeatureSpend",
                        "dataType": "INTEGER",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "NumberOfPenalties",
                        "dataType": "INTEGER",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "CurrentPeriodUsage",
                        "dataType": "DOUBLE",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "PriorPeriodUsage",
                        "dataType": "DOUBLE",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "DaysSinceLastService",
                        "dataType": "INTEGER",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "ServiceRating",
                        "dataType": "DOUBLE",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "ServiceTickets",
                        "dataType": "INTEGER",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "StartMonth",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "StartWeek",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "CustomerTenure",
                        "dataType": "INTEGER",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    },
                    {
                        "name": "Churned",
                        "dataType": "STRING",
                        "include": true,
                        "featureType": "numeric",
                        "changeType": null
                    }
                ]
            }
        }
    }
}
  ```
</details>

## Select the target feature

Use the `insights` property from the profile insights response to select a target feature. A suitable target feature:

- Has `"cannotBeTarget": false`.
- Shouldn't be flagged as unsuitable (for example, `high_cardinality`).
- Represents a meaningful and actionable objective.

In the example response, the `Churned` column is a valid target because:

- `"cannotBeTarget": false` shows it can be used as the target.
- Predicting churn is actionable for improving customer retention.

## Next step

Profiling your dataset provides everything you need to start creating an experiment version::

- Feature insights help you select which features to include or exclude.
- A basis for selecting a meaningful target feature.
- Experiment types (`experimentTypes`) for the selected target feature.
- A `defaultVersionConfig` template that simplifies the creation of an experiment version.

With this, you can now [create your experiment versions](https://qlik.dev/embed/machine-learning/tutorial/dataset-profiling/create-experiment-version) and train models.
