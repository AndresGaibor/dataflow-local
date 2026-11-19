---
source: https://qlik.dev/embed/gen-ai/share-insight-advisor-feedback/
last_updated: 2026-04-20T13:34:03+01:00
---

# Collect and share Insight Advisor feedback

The Qlik Natural Language Usage Metrics API allows you to access usage metrics
for Insight Advisor and Insight Advisor chat. These metrics can help you
design better apps.

This tutorial will teach you how to use Postman to view natural language metrics
for the Demo App - Beginner's tutorial app. Specifically, you'll use the API to
filter, sort, and use pagination on the results.

## Prerequisites

- Download and install [Postman](https://getpostman.com).

- An access token or API key. For more information, see [Authentication](https://qlik.dev/authenticate).

- "Demo App - Beginner's tutorial" Qlik Sense application in a shared space.
  To open the app, click `Explore the Demo` in the hub. For more information about moving the app to
  a shared space, see [Using apps in shared spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-apps-in-spaces.htm)
  and [Working in shared spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-shared-spaces.htm)
  on Qlik Help.

- You must have the audit administrator role. For more information, see [User permissions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-user-permissions.htm#anchor-1)
  on Qlik Help.

## Insight Advisor feedback API endpoint

Connection to the Insight Advisor Natural Language feedback API endpoint is made
using HTTPS by default. When communicating with the API, the URL has
the following form:
`{URL}/api/v1/questions/actions/filter`
where \{URL} is your tenant URL.

## API usage examples

### Set up Postman

1. Start Postman.

2. Set the HTTP method to POST.

3. Enter the following path in the URL area:
   `{url}/api/v1/questions/actions/filter`
   The full URL should look something like:
   `https://{your-tenant-URL}.us.qlikcloud.com/api/v1/questions/actions/filter`

4. Select `Headers` and add `Content-Type` as the key with `application/json`
   as the value. Before making API requests, add your access token as a Bearer Token to
   Postman. See [Authentication](https://qlik.dev/authenticate).

### Show the two most recent Insight Advisor questions for an app

This example details how to show the two most recent Insight Advisor questions
posed in the Demo App - Beginner's tutorial app. Default API settings are used.

1. In the body of the request, set the app ID filter:

   ```json
   {
    "filter": "(appId eq \"7c1af1b6-6cee-44d5-b400-17d83aa70bef\")"
   }
   ```

   > **Tips:**
   >
   > - If you don't know the app ID, you can view it in the URL for the app. The app ID appears after `/app/` in the URL.
   > - If the app ID is not present or required, you can also use the `appId eq "unassigned"` filter.
   >   You must include a valid app ID to which you have access to use the unassigned filter.

   ```json
   {
    "filter": "(appId eq \"7c1af1b6-6cee-44d5-b400-17d83aa70bef\" or appID eq \"unassigned\")"
   }
   ```

2. Click `Params`, then, in the `Key` column, enter `sort`, and then enter
   `-createdAt`in the `Value` column.

3. In the `Key` column, enter `limit`, and then enter `2` in the `Value` column.

   > **Note:** You can also edit the URL manually if you don't want to use the Postman interface.
   > The URL should look like this: `{your-tenant-URL}/api/v1/questions/actions/filter?sort=-createdAt&limit=2`

4. Click `Send`. The JSON response from the API should look something like this:

   ```json
   {
    "data": [
        {
            "id": "jvLMm7-_E-YQWAm6u2JBC1VWlK8vamMb",
            "createdBy": "6356de9542b09683bca842e0",
            "tenantId": "rchpF-n7id8V3k2YVrMtCZmqkO6_z1ja",
            "createdAt": "2022-11-08T22:28:08.302Z",
            "updatedAt": "2022-11-08T22:28:09.350Z",
            "appName": "Demo App - Beginner's tutorial",
            "appId": "7c1af1b6-6cee-44d5-b400-17d83aa70bef",
            "apps": [
                {
                    "id": "7c1af1b6-6cee-44d5-b400-17d83aa70bef",
                    "name": null,
                    "space_id": null,
                    "space_type": null,
                    "space_name": null,
                    "last_reload_date": null,
                    "limited_access": null
                }
            ],
            "channelId": "Insight Advisor",
            "chartType": "native",
            "feedback": [],
            "lang": "en",
            "isContextualQuery": false,
            "queryOrigin": "askQuestion",
            "nluInfo": [
                {
                    "text": "Brenda Gibson",
                    "type": "filter",
                    "role": "dimension",
                    "fieldName": "Sales Rep Name",
                    "filterValue": "Brenda Gibson"
                },
                {
                    "text": "Deli",
                    "type": "filter",
                    "role": "dimension",
                    "fieldName": "Product Group",
                    "filterValue": "Deli"
                },
                {
                    "text": "sales",
                    "type": "master_measure",
                    "role": "measure",
                    "fieldName": "Sales"
                },
                {
                    "text": "2020",
                    "type": "filter",
                    "role": "date",
                    "fieldName": "Invoice Date",
                    "filterValue": "from 1/1/2020 to 12/31/2020"
                }
            ],
            "queryError": false,
            "questionId": "27357f62-9d23-4932-9edb-eea8b6374ff6",
            "queryText": "Brenda Gibson Deli sales 2020",
            "queryType": "query",
            "recommendations": [
                {
                    "analysis": "trend",
                    "analysisGroup": "trend",
                    "chartType": "linechart",
                    "dims": [
                        "Invoice Date"
                    ],
                    "msrs": [
                        "Sales"
                    ],
                    "relevance": 1
                },
                {
                    "analysis": "process-control-rolling-mean",
                    "analysisGroup": "trend",
                    "chartType": "linechart",
                    "dims": [
                        "Invoice Date"
                    ],
                    "msrs": [
                        "Sales",
                        "Average",
                        "Upper control limit",
                        "Lower control limit"
                    ],
                    "relevance": 0.9
                },
                {
                    "analysis": "process-control-mean",
                    "analysisGroup": "trend",
                    "chartType": "linechart",
                    "dims": [
                        "Invoice Date"
                    ],
                    "msrs": [
                        "Sales",
                        "Average",
                        "Upper control limit",
                        "Lower control limit"
                    ],
                    "relevance": 0.9
                },
                {
                    "analysis": "fact",
                    "analysisGroup": "fact",
                    "chartType": "kpi",
                    "dims": null,
                    "msrs": [
                        "Sales"
                    ],
                    "relevance": 1
                }
            ],
            "responses": {
                "hasInsights": true,
                "hasChart": true
            },
            "stopWords": [],
            "version": "1.0"
        },
        {
            "id": "GNH4O_0kPitWnLV6pTNANkAaGkYvJlN6",
            "createdBy": "6356de9542b09683bca842e0",
            "tenantId": "rchpF-n7id8V3k2YVrMtCZmqkO6_z1ja",
            "createdAt": "2022-11-08T22:27:27.665Z",
            "updatedAt": "2022-11-08T22:27:27.665Z",
            "appName": "Demo App - Beginner's tutorial",
            "appId": "7c1af1b6-6cee-44d5-b400-17d83aa70bef",
            "apps": [
                {
                    "id": "7c1af1b6-6cee-44d5-b400-17d83aa70bef",
                    "name": null,
                    "space_id": null,
                    "space_type": null,
                    "space_name": null,
                    "last_reload_date": null,
                    "limited_access": null
                }
            ],
            "channelId": "Insight Advisor",
            "chartType": "native",
            "feedback": [],
            "lang": "en",
            "isContextualQuery": false,
            "queryOrigin": "askQuestion",
            "nluInfo": [
                {
                    "text": "Brenda Gibson",
                    "type": "filter",
                    "role": "dimension",
                    "fieldName": "Sales Rep Name",
                    "filterValue": "Brenda Gibson"
                },
                {
                    "text": "total sales",
                    "type": "field",
                    "role": "dimension",
                    "fieldName": "Sales Rep Name"
                },
                {
                    "text": "2020",
                    "type": "filter",
                    "role": "date",
                    "fieldName": "Invoice Date",
                    "filterValue": ">= 1/1/2020"
                }
            ],
            "queryError": false,
            "questionId": "f43dfb38-ad1c-43e5-880a-3ba2ee1e4daf",
            "queryText": "Brenda Gibson total sales 2020",
            "queryType": "query",
            "stopWords": [],
            "version": "1.0"
        }
    ],
    "links": {
        "next": {
            "href": "https://{your-tenant-URL}/api/v1/questions/actions/filter?sort=-createdAt&limit=2&page=636ad79fcca9185d46f59a1e"
        }
    },
    "meta": {
        "total": 17
    }
   }
   ```

The response shows the two most recent questions, "Brenda Gibson Deli sales 2020"
and "Brenda Gibson total sales 2020," which you can see in the
`queryText` property.

### Sort the results returned

The following table describes the sorting parameters.

| Parameter  | Description                                                            |
| ---------- | ---------------------------------------------------------------------- |
| -createdAt | The date the question was first created, sorted from newest to oldest. |
| +createdAt | The date the question was first created, sorted from oldest to newest. |
| -updatedAt | The date the question was updated, sorted from newest to oldest.       |
| +updatedAt | The date the question was updated, sorted from oldest to newest.       |

> **Note:** By default, results are displayed from oldest to newest if you do not specify a sort order.

Now, suppose you want to see only the oldest updated question.

1. In the `Params` area, in the `sort` row, enter `+updatedAt`.

2. In the `limit` row, enter `1`.

3. Click `Send`. The JSON response from the API should look something like this:

   ```json
   {
    "data": [
        {
            "id": "YumPdBNw075wOg4rfJchpjT3HDcbBHt-",
            "createdBy": "6356de9542b09683bca842e0",
            "tenantId": "rchpF-n7id8V3k2YVrMtCZmqkO6_z1ja",
            "createdAt": "2022-11-08T00:42:31.802Z",
            "updatedAt": "2022-11-08T00:42:31.802Z",
            "appName": "Demo App - Beginner's tutorial",
            "appId": "7c1af1b6-6cee-44d5-b400-17d83aa70bef",
            "apps": [
                {
                    "id": "7c1af1b6-6cee-44d5-b400-17d83aa70bef",
                    "name": null,
                    "space_id": null,
                    "space_type": null,
                    "space_name": null,
                    "last_reload_date": null,
                    "limited_access": null
                }
            ],
            "channelId": "Insight Advisor",
            "chartType": "native",
            "feedback": [],
            "lang": "en",
            "isContextualQuery": false,
            "queryOrigin": "askQuestion",
            "nluInfo": [
                {
                    "text": "GrossSales",
                    "type": "field",
                    "role": "measure",
                    "fieldName": "GrossSales"
                }
            ],
            "queryError": false,
            "questionId": "8237b9e2-9e9e-4e9e-9182-b640b5e14321",
            "queryText": "GrossSales",
            "queryType": "query",
            "stopWords": [],
            "version": "1.0"
        }
    ],
    "links": {
        "next": {
            "href": "{your-tenant-URL}/api/v1/questions/actions/filter?sort=+updatedAt&limit=1&page=6369a6371088210efa80f802"
        }
    },
    "meta": {
        "total": 17
    }
   }
   ```

   As you can see, there are 17 total questions but only the oldest updated
   question is returned.

### Limit the number of results returned

The default value for limiting results is 100. Therefore if you have several
hundred results but you do not specify the `limit` value, only 100 results will
be returned.

On the other hand, suppose you want to see only the 10 latest questions users
entered into Insight Advisor.

1. Clear the `sort` checkbox.

2. In the `limit` row, enter `10`.

3. Click `Send`.

   Since you didn't specify a sort order, only the 10 oldest created questions
   are returned.

### Use Pagination

If you've specified a limit for the results, you can use pagination to view the
next record. If you want to view the next record that you have access to, in
the response body, click the link near the bottom to view the next record.

![Postman pagination link](https://qlik.dev/_astro/filter-pagination.D336fTRL.png)

Then, execute the method to get the next record.
