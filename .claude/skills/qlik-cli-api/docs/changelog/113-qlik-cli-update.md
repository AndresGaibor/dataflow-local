---
source: https://qlik.dev/changelog/113-qlik-cli-update/
last_updated: 2024-10-29T15:30:46Z
---

# qlik-cli Update - October 2024

## qlik-cli 2.26.0

A new release of [qlik-cli](https://qlik.dev/toolkits/qlik-cli/) has been published.

Change summary:

- Republished `qlik-cli` documentation to remove deprecated commands and update with
  improved API specifications.
- Updated command help to match the updated API specifications.
- Deprecated the `collection change-visibility` command as the supporting API is
  no longer published.
- Renamed the flag `webhook ls --eventType` to `--eventTypes` to align with the operation
  of the API. This flag now takes multiple event types, separated by commas, to support
  more precise queries. The old flag still works and is ported to the new one for
  backwards compatibility.

### Notes on deprecation of `collection change-visibility` command

The supported method for changing the visibility of a collection is to use
`collection patch`, for example:

```bash
qlik collection patch COLLECTION_ID --body='[{"op":"replace","path":"/type", "value": "publicgoverned"}]'
```
