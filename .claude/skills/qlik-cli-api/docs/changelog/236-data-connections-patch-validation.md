---
source: https://qlik.dev/changelog/236-data-connections-patch-validation/
last_updated: 2026-07-24T08:27:55-02:30
---

# Stricter validation for PATCH data connections

The `PATCH /data-connections/{id}` endpoint now enforces stricter validation rules.
The following requests now return `400 Bad Request`:

- Requests containing operations that target both `qConnectStatement` and
  `connectionProperties`.
- Requests that change the connection string (`qConnectStatement`) without including
  credentials in the same request.
- Requests that change `connectionProperties/host`, `connectionProperties/server`, or
  `connectionProperties/url` without including credentials in the same request.
- Requests that supply credentials using both `/qPassword` and the
  `connectionProperties` password field.

Additionally, when a successful PATCH request changes the host of a connection that uses
separate credentials, the API automatically disassociates the previously associated
credentials.

Review your existing PATCH scripts and automation using the
[update data connections](https://qlik.dev/manage/data-connections/update-data-connections/) guide
and the [data connections API reference](https://qlik.dev/apis/rest/data-connections/).
