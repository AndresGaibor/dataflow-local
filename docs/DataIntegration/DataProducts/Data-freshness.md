---
title: "Data freshness"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Data-freshness.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog"]
---

# Data freshness

After opening a dataset, you can see the Freshness tile in the Overview tab. The data freshness indicates the last update of the data source.

The data freshness is available for some data sources only:

- Created from a file: The freshness corresponds to the last time the data was updated.
- Published from a pipeline: The freshness corresponds to the last time the dataset was updated by a pipeline.

  The time depends on the update method:

  - The Change Data Capture (CDC) method: The time corresponds to the last event on the data source. For example, the data source has been updated at 9:00 AM. The pipeline runs at 10:00 AM. You open the overview at 11:00 AM. The data freshness is 2 hours ago.
  - The Reload and compare method: The time corresponds to the last run. For example, the data source has been updated at 9:00 AM. The pipeline runs at 10:00 AM. You open the overview at 11:00 AM. The data freshness is 1 hour ago.

Computing the profile or the data quality does not impact the data freshness.

The data freshness is available in the dataset overview only. The Last modified column in the Catalog tab indicates the last modification on the dataset itself, renaming it or editing the description for instance.
