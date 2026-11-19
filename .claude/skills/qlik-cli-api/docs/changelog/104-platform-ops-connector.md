---
source: https://qlik.dev/changelog/104-platform-ops-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Block updates - Qlik Platform Operations connector

The [Qlik Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) enables the deployment and
management of Qlik Cloud tenants without any coding.

New blocks:

- `List Tags`: List all tags (collections where type=public) in
  the tenant.
- `List Items By Tag Name`: List all items (apps, automations,
  data sets, etc) which have a tag matching the provided tag name.
- `Create Tag If Not Existing`: If a tag doesn't exist, create it. If it exists,
  return the tag definition.
- `Delete Tag By Name`: Deletes a tag by name if found.
- `Add Tag To Item By Name`: Add a tag to an item by specifying the tag name. If the
  tag doesn't exist, create it.
- `Remove Tag From Item By Name`: Remove a tag from an item by specifying the tag
  name.
- `List Automation Runs`: Retrieve the most recent run information for an automation.
- `List Reload Tasks`: Retrieve all reload tasks configured in the tenant.
- `Get Reload Task`: Retrieve an individual reload task definition.

Updated blocks:

- `List Data Files`: Added all API params as inputs to block to support in-block
  filtering and sorting.
- `List Data Files From Space`: Added all API params as inputs to block to support
  in-block filtering and sorting.

Review [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview)
for information on how to get started using the connector.
