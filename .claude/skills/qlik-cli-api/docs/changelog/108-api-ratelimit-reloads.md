---
source: https://qlik.dev/changelog/108-api-ratelimit-reloads/
last_updated: 2026-04-20T13:34:03+01:00
---

# API rate limit change - Reloads API

The [Reloads API](https://qlik.dev/apis/rest/reloads/) is used to start and monitor the refresh of Qlik
Cloud Analytics apps.

To better support programmatic external task management of
reloads, the rate limit for [`POST /api/v1/reloads`](https://qlik.dev/apis/rest/reloads/#post-v1-reloads)
has been increased from 10 requests per minute to 50 requests per minute.

Requests to this `POST` endpoint are metered over a 5-minute window. This means you
can make up to 250 requests within that window before you are rate limited.

Learn more about reloads and system concurrency in [manage analytics reloads](https://qlik.dev/manage/analytics-applications/),
or delve into [how rate limiting works](https://qlik.dev/apis/rest/rate-limiting/) for REST APIs in Qlik Cloud.
