---
title: "Advanced Analytics analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-advanced-analytic-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Advanced Analytics analytics source

There are many machine-learning platforms where developers can build, train, and deploy machine-learning models in the cloud.

To connect to a generic model, you must have created your own model and deployed it to an endpoint on the chosen AI/machine learning platform. This endpoint must be publicly accessible by Qlik Cloud.

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Limitations

- The Advanced Analytics connector is limited to 200k rows per request. By default, these are sent to the endpoint service in batches of 2k rows but this can be configured when creating the [connection](#glossary-0 "Glossary term"). In scenarios where more rows are required to be processed, use a Loop within the data [load script](#glossary-1 "Glossary term") to process more rows in batches.
- In a scenario where an application is regularly reloaded, it is best practice to cache the machine learning predictions using a [QVD](#glossary-2 "Glossary term") file and only send the new rows to the endpoint. This will improve the performance of the Qlik Sense application reload and reduce the load on the model endpoint.
- The resources available on the services where the model has been deployed will impact and limit performance in the Qlik Sense reload and [chart](#glossary-3 "Glossary term") responsiveness.
- When using Advanced Analytics connections in a chart expression it is recommended to provide the datatypes of the fields as the model needs to process these in the correct string/numeric format. A limitation of server side extensions in chart expressions is that the data types are not automatically detected as they are in the load script.
- If you are using a relative connection name, and if you decide to move your application from a [shared space](#glossary-5 "Glossary term") to another shared space, or if you move your application from a shared space to your private space, then it will take some time for the analytic connection to be updated to reflect the new space location.
- You cannot create and manage connections to this connector in Data manager within an analytics application.
