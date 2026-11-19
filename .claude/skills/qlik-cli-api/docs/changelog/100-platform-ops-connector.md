---
source: https://qlik.dev/changelog/100-platform-ops-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Block updates - Qlik Platform Operations connector

The [Qlik Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) enables the deployment and
management of Qlik Cloud tenants without requiring any coding.

New blocks:

- `Import And Replace App In Shared Space By Name`: Use the Import And Replace App
  In Shared Space By Name block to simplify importing apps to a shared space for
  deployments where the goal of importing the app is to then publish or republish
  that imported copy into a managed space. The block will first identify and delete
  any other apps in the shared space with the same name (using an exact case-sensitive
  match on the provided name), then import the app and return an object containing
  the imported app and the IDs of any deleted apps.

Updated blocks:

- `Create Space If Not Existing`: Added the ability to set and update the space
  description.
- `Deactivate Tenant`: Fixed an issue with the example output.

Review [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview)
for information on how to get started using the connector.
