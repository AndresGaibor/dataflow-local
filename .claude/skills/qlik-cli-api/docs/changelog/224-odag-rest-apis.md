---
source: https://qlik.dev/changelog/224-odag-rest-apis/
last_updated: 2026-06-16T07:41:34+01:00
---

# New REST APIs - ODAG (on-demand analytics generation) management APIs

The new ODAG REST APIs provide programmatic access to manage on-demand analytics generation (ODAG) workflows
in Qlik Cloud. These four APIs enable organizations to automate on-demand analytics workflows:

- **Programmatically create ODAG links** between selection and template applications
- **Track and manage generated applications** created through ODAG requests without manual intervention
- **Automate lifecycle operations** like renaming, reloading, or cleaning up generated applications
- **Control ODAG behavior** at the tenant level through settings management

This is particularly valuable for organizations running high-volume analytics generation or integrating ODAG into
automated workflows via orchestration platforms or custom applications.

### New APIs \{#223-new-apis}

- **[ODAG Apps API](https://qlik.dev/apis/rest/analytics/odag-apps/)**: List on-demand generated analytics applications and their
  source templates, plus selection entry points, filtered by type: `selection` (entry-point applications), `template`
  (source applications for generation), or `generated` (on-demand analytics applications created via ODAG requests).
- **[ODAG Links API](https://qlik.dev/apis/rest/analytics/odag-links/)**: Create, list, and manage ODAG links. Find which selection
  applications use specific links.
- **[ODAG Requests API](https://qlik.dev/apis/rest/analytics/odag-requests/)**: Track the status of ODAG requests, delete or reload
  generated applications, rename generated applications, and retrieve request selections.
- **[ODAG Settings API](https://qlik.dev/apis/rest/analytics/odag-settings/)**: Read and update tenant-level ODAG settings.

### API workflow \{#223-api-workflow}

That lifecycle operations on generated applications (delete, reload, rename) are performed through the ODAG
Requests API using the request ID, not directly through the ODAG Apps API.

The ODAG Apps API provides discovery and visibility of all applications by type but does not support mutations.

When you create an ODAG request, store the request ID returned in the response.
Use that ID to manage the generated application throughout its lifecycle.

### Getting started \{#223-getting-started}

For more information, see the ODAG API reference documentation:

- [ODAG Apps API](https://qlik.dev/apis/rest/analytics/odag-apps/)
- [ODAG Links API](https://qlik.dev/apis/rest/analytics/odag-links/)
- [ODAG Requests API](https://qlik.dev/apis/rest/analytics/odag-requests/)
- [ODAG Settings API](https://qlik.dev/apis/rest/analytics/odag-settings/)
