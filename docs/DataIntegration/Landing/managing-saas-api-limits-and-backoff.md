---
title: "Managing SaaS API limits and backoff"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/managing-saas-api-limits-and-backoff.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications"]
---

# Managing SaaS API limits and backoff

When a SaaS application limits requests, connectors wait before retrying. The application's limits and the connector's retry strategy affect how long a task takes.

For information about connecting to SaaS applications, see [*Connecting to SaaS applications*](connecting-web-applications.htm).

## SaaS API limits

Each SaaS application sets its own API limits and throttling rules. Limits can apply to an application instance or an individual application client ID. During a full load, Qlik Talend Data Integration can show Full load incomplete for a table or dataset. This can occur on the first run or when the table or dataset uses reload-only loading.

## Managing rate limits and backoff

When an API returns a retryable error, such as an HTTP 429 response, a server error, or certain other client errors, the connector waits before retrying. The retry strategy depends on the API and can vary by connector. It takes into account:

- The maximum number of retries.
- The wait before each retry, which can stay fixed or increase with each attempt. For example, a connector might wait 30 seconds between retries or wait 1, 2, 4, 8, and 16 seconds across successive attempts.
- The multiplier used to increase the wait, such as a factor of 2 or 3.

If a task repeatedly reaches API limits or spends too long waiting to retry, try the following:

- Include only the datasets you need in the task to reduce the data extracted and the number of API requests.
- For tasks that load changes between runs, run the task more frequently to spread API requests across smaller runs.
- Use each connection for one task. Create separate connections for other tasks, but check whether the source shares limits across connections.
- Check the source application's rate limit tier. Contact the SaaS vendor if you need a higher limit.
- Allow the connector to retry after occasional rate limits. If the issue continues, contact Qlik Support.
