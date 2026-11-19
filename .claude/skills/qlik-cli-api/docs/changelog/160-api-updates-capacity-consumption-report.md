---
source: https://qlik.dev/changelog/160-api-updates-capacity-consumption-report/
last_updated: 2025-10-31T14:06:52+01:00
---

# Updated API - Audits API capacity consumption reports

A new Audits API endpoint is now available:

- `POST /api/v1/audits/actions/fetch-consumption-app` returns a Qlik Sense application (QVF file) containing usage data
  for the tenant's subscription. The report is updated once per day.

It requires the **TenantAdmin** role and is available only for **Capacity-based subscriptions**.

For more information, see the [Audits API reference](https://qlik.dev/apis/rest/audits/#post-api-v1-audits-actions-fetch-consumption-app).
