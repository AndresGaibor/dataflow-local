---
source: https://qlik.dev/changelog/242-qlik-automate-connector-updates/
last_updated: 2026-07-30T17:17:05Z
---

# Block updates - Qlik Cloud Services & Qlik Platform Operations connectors

Updates have been made to
[Qlik Automate](https://qlik.dev/toolkits/no-code/) connectors and blocks.

### Qlik Cloud Services connector \{#242-qlik-cloud-services-connector}

**New blocks**:

- `Restore Analytics App`: Restores a soft-deleted Analytics application to its original
  space, retaining the properties it had at the time of deletion.

**Updated blocks**:

- `Do reload`: Reload requests triggered by this block are now carry metadata indicating
  that they were triggered by an automation, and include the ID of the calling
  automation. This allows administrators to trace which automations are starting
  reloads.

### Qlik Platform Operations connector \{#242-qlik-platform-operations-connector}

**Updated blocks**:

- All blocks: Improved error messages returned when a block fails due to an
  authentication or tenant configuration issue, surfacing the underlying API
  error instead of a generic message.
- `Reload Analytics App`: Reload requests triggered by this block are now carry
  metadata indicating that they were triggered by an automation. Note this does
  not currently include the automation ID.
