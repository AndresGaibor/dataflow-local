---
source: https://qlik.dev/changelog/70-extension-theme-update/
last_updated: 2025-07-08T16:09:30Z
---

# Guardrails will be added to archive properties for Extensions and Themes APIs

Qlik is implementing guardrails on uploads to the Extensions and Themes APIs. These
APIs enable the addition of third-party visualizations and third-party formatting
and color schemes for use in Qlik Sense applications.

These changes will take effect no later than 30 days from the date of this notice.

Planned changes:

- Maximum archive size: 30 MB - this is larger than any theme currently deployed
  to Qlik Cloud, and it is recommended to make themes as small as possible to ensure
  that they do not impact the load time in Qlik Sense.
- Maximum individual file size: 30 MB - this is linked to the maximum archive
  size.
- Maximum total size of files in ZIP: 100 MB - this value is based on the uncompressed
  size of items in the archive, hence in most cases users will be limited based on
  the maximum archive size of 30 MB.
- Maximum number of files: 500 - if your theme or extension has more files than this,
  consider leveraging a bundler to build similar file types together.

Review the [Extensions API](https://qlik.dev/apis/rest/extensions)
and [Themes API](https://qlik.dev/apis/rest/themes) specifications for
further information on these APIs.
