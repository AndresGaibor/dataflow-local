---
title: "Amazon Comprehend analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-amazon-comprehend-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Amazon Comprehend analytics source

Amazon Comprehend is a managed service for text analysis available to customers of the AWS platform.

The following Amazon Comprehend services are supported:

- Sentiment Analysis
- Key phrase Extraction
- Language Detection
- Entity Recognition
- Syntax Analysis
- Personally Identifiable Information (PII) Detection

Each of these services requires a separate [connection](#glossary-0 "Glossary term") to be created with the specific parameters applicable to the service in question.

[Amazon Comprehend](https://aws.amazon.com/comprehend/).

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Limitations

- Amazon Comprehend has several quotas and limitations that can be increased using the AWS Service Quotas and AWS Support Center.

  For example, the document size (UTF-8 characters) is 5000 bytes which means that the limit per application row size in Qlik Sense is 5000 bytes.

  Using the Amazon Comprehend endpoint with data rows larger than 5K bytes will cause an TextSizeLimitExceededException error. Such an error message can for example state: "Input text size exceeds limit. Max length of request text allowed is 5000 bytes while in this request the text size is 5276 bytes"

  [Guidelines and quotas](https://docs.aws.amazon.com/comprehend/latest/dg/guidelines-and-limits.html)
- The Amazon Comprehend connector is limited to 1000 rows per request. These are sent to the endpoint service in batches of 25 rows. In scenarios where more rows are required to be processed, use a Loop within the data [load script](#glossary-2 "Glossary term") to process more rows in batches.
- The Amazon Comprehend Personally Identifiable Information (PII) Detection service is limited to 100 rows per request. These are sent to the endpoint service 1 at a time.
- In a scenario where an application is regularly reloaded, it is best practice to cache the prediction using a [QVD](#glossary-3 "Glossary term") file and only send the new rows to the prediction endpoint. This will improve the performance of the Qlik Sense application reload and reduce the load on the Amazon Comprehend endpoint.
- There is a known limitation at the Amazon Comprehend side, where sending null values, or blanks, to Amazon Comprehend will result in an error returned by Amazon Comprehend.
- If you are using a relative connection name, and if you decide to move your application from a [shared space](#glossary-4 "Glossary term") to another shared space, or if you move your application from a shared space to your private space, then it will take some time for the analytic connection to be updated to reflect the new space location.
- You cannot create and manage connections to this connector in Data manager within an analytics application.
