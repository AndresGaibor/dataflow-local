---
source: https://qlik.dev/changelog/229-adaptive-cards-api/
last_updated: 2026-06-26T11:39:12+01:00
---

# New REST API - Retrieve Discovery Agent insight cards

The new Discovery Agent adaptive cards API enables you to retrieve insights that have been
automatically generated from triggers configured in your Qlik Cloud Analytics applications.

Use the following endpoint to retrieve insights structured as "cards" in JSON format for
use in your custom applications and integrations:

- `GET /api/analytics/discovery-agent/adaptive-cards`

You can retrieve cards across the metrics available to the authenticated user, or filter the results by criteria
including:

- Application and metric IDs
- Measures and dimensions
- Breakdown selections
- Analysis types
- Comparison periods
- Insight time ranges

The endpoint also supports pagination and sorting by creation time.

When you make a request without filters, the API returns the top-ranked result for each metric.
When you provide a supported filter, all results matching the filter are returned without applying the ranking
restriction.

Use this API when you need to render Discovery Agent insights in a custom interface, process them programmatically, or
integrate them into your own workflows.
For a ready-to-use embedded feed interface, use the `insights/feed-cards` UI in qlik-embed.

For more information, see the [Discovery Agent adaptive cards API reference](https://qlik.dev/apis/rest/analytics/discovery-agent/adaptive-cards)
and [Analyzing Discovery Agent feeds](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/feeds.htm)
on Qlik Help.
