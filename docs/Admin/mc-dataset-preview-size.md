---
title: "Configuring dataset preview size"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-dataset-preview-size.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Configuring dataset preview size

Dataset preview size lets tenant admins configure how many rows are shown when previewing datasets.

1. In the Administration activity center, go to the Settings page.
2. Select the Feature control tab.
3. In the Dataset preview size section, select the maximum preview size from the list (100 or 1,000 rows).

The preview is always a subset of the computed sample.

Note that changing the preview size does not affect already existing previews across the tenant. The new configuration applies when previews are recomputed upon dataset quality computes.

### Partial dataset preview due to system limitations

When a dataset is previewed, the system attempts to store and display as much data as possible. If the dataset exceeds internal system limits, such as the maximum storage size for previews, only a portion of the data you expect to see will be stored and shown.

If this occurs, users will see an informational warning:

**Preview truncated due to system limitations. The number of records shown may be less than expected.**

This behavior ensures application performance and stability, even with very large datasets.

For best results, consider filtering or reducing dataset size if a complete preview is required.
