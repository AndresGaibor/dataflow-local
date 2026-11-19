---
source: https://qlik.dev/changelog/98-platform-ops-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Block updates - Qlik Platform Operations connector

The [Qlik Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) enables the deployment and
management of Qlik Cloud tenants without requiring any coding.

New blocks:

- `Deallocate All Licenses From User`: This block removes any licenses assigned
  to the specified user subject.
- `Delete User And Deallocate All Licenses`: This block removes any licenses assigned
  to the specified user ID and deallocates any licenses assigned to the
  user subject associated with that user ID.

Updated blocks:

- `Run Automation`: Now supports providing the input payload for the automation
  within the block.

Review [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview)
for information on how to get started using the connector.
