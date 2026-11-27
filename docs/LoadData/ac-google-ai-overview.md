---
title: "Google AI - Gemini analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-google-ai-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Google AI - Gemini analytics source

Use the Google AI - Gemini analytics connector to communicate with large language models (LLMs) that are available from Google's Gemini API, enriching your Qlik Sense applications with contextual and analytical depth.

With the Google AI - Gemini analytics connector, you can send data from application consumer input, or from data loaded in your script, to Gemini. You can connect to this analytics source from the Create page in the Analytics activity center, the Script, or within an application.

## Prerequisites

To work with this connector, you must be a [Google AI Studio](https://aistudio.google.com/) user with access to the Gemini API.

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Limitations

- This connector has a request limit of 25 rows per request, with a maximum batch size of one row being sent at a time.
- The resources available on the services where the model has been deployed will impact and limit performance in the Qlik Sense reload and [chart](#glossary-0 "Glossary term") responsiveness.
- In a scenario where an application is regularly reloaded, it is best practice to cache the machine learning predictions using a [QVD](#glossary-1 "Glossary term") file and only send the new rows to the endpoint. This will improve the performance of the Qlik Sense application reload and reduce the load on the model endpoint.
- If you are using a relative connection name, and if you decide to move your application from a [shared space](#glossary-3 "Glossary term") to another shared space, or if you move your application from a shared space to your private space, then it will take some time for the analytic connection to be updated to reflect the new space location.
- You cannot create and manage connections to this connector in Data manager within an analytics application.
