---
source: https://qlik.dev/changelog/165-api-updates-di-projects-monitoring/
last_updated: 2025-10-31T14:06:52+01:00
---

# Updated API - Monitoring enhancements in the Data Integration Projects API

The Data Integration Projects API now includes improvements for real-time task monitoring.

The `GET /v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state` endpoint now returns additional fields to help
you monitor tasks in real time, including:

- Run state
- Start and end time
- Duration
- Task dataset count (including datasets in error)
- Gateway ID, name, and gateway task name
- Latency for continuous tasks

The new `GET /v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/state/datasets` endpoint provides dataset-level
details for your tasks, including:

- Dataset name and ID
- Dataset state
- Processing start and end time
- Processed record count (when applicable)

Both endpoints will be available for use in Qlik Automate:

- The enhanced runtime state API is available via the `Get Data Task Runtime State` block
  in the `Qlik Talend Data Integration` connector.
- The new dataset state API will be added to the `Qlik Talend Data Integration` connector soon.
  In the meantime, it can be called using the `Raw API Request` block in the `Qlik Platform Operations`
  connector.

For more information, see the [Data Integration Projects API reference](https://qlik.dev/apis/rest/di-projects/).
