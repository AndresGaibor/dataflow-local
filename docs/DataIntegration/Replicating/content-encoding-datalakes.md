---
title: "Content-type and content-encoding properties"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/content-encoding-datalakes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project", "Landing data in a data lake with a Standard, Premium, or Enterprise subscription"]
---

# Content-type and content-encoding properties

Content-type and content-encoding properties of files uploaded to Amazon S3

| Replication Artifact | File Format | Compression | Content-Type | Content-Encoding |
| --- | --- | --- | --- | --- |
| Data file | CSV | None | text/csv; charset=utf-8 | N/A |
| Data file | CSV | gzip | text/csv; charset=utf-8 | gzip |
| Data file | JSON (lines) | None | application/x-ndjson | N/A |
| Data file | JSON (lines) | gzip | application/x-ndjson | gzip |
| Metadata file (DFM) | JSON | None | application/json | N/A |
