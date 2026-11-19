---
source: https://qlik.dev/changelog/117-platform-ops-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Block updates - Qlik Platform Operations connector

The [Qlik Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) enables the deployment and
management of Qlik Cloud tenants without any code.

This release adds native file handling support, which allows for files up to
100 MB in size and works with a larger selection of connectors.

New blocks:

- `Import App`: A version of the `Import App From Base 64 Encoded File` block which uses
  native file handling.
- `Export App`: A version of the `Export App To Base 64 Encoded File` block which uses
  native file handling.
- `Import File From Temporary Contents`: A version of the `Import Base 64 Encoded File To Temporary Contents`
  block which uses native file handling.
- `Export File From Temporary Contents`: A version of the `Export Base 64 Encoded File From Temporary Contents`
  block which uses native file handling.
- `Import And Replace App In Shared Space By Name`: A version of the `Import And Replace Base 64 Encoded App In Shared Space`
  block which uses native file handling.

Renamed blocks:

- `Import And Replace Base 64 App In Shared Space By Name`: This block was formerly
  `Import And Replace App In Shared Space`, and has been renamed for consistency
  with other file handling blocks.

Review [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview)
for information on how to get started using the connector.
