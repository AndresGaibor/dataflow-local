---
title: "Iceberg optimization processes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/iceberg-optimization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Qlik Open Lakehouse architecture"]
---

# Iceberg optimization processes

Adaptive Optimizer for Apache Iceberg is an intelligent agent that continuously audits your data files and optimizes how they are organized and stored for faster queries and lower storage costs.

Qlik uses optimization processes to enhance the performance and manageability of the Iceberg tables in your Qlik Open Lakehouse. These processes are designed to maintain efficient storage and ensure premium query performance. By automatically optimizing your lakehouse in the background, this reduces the operational overhead of manually monitoring, troubleshooting, and maintaining tasks.

## Adaptive Optimizer

Adaptive Optimizer runs algorithmic analysis to determine how to optimize your Iceberg tables that delivers the most impact. The agent decides when and how to optimize your Iceberg data, and calculates when to delete files based on factors such as data profile, table properties, frequency of row-level changes, cost and performance characteristics.

Using advanced algorithms, Adaptive Optimizer continuously evaluates and combines these factors to produce the best possible optimizations for each table, ensuring query speeds remain high and storage costs are low. During ingestion and compaction, Adaptive Optimizer collects and refreshes table statistics without the need to analyze each table. These statistics assist query engines in the planning and execution of queries on Iceberg tables.

Intelligent optimizations uniquely adapt to your data to improve lake hygiene and query performance. Not all tables are created equal in your data lakehouse, so the Adaptive Optimizer adjusts to the individual characteristics of the raw data. It uniquely structures, organizes, and optimizes each table.

The following key optimization processes are performed automatically by Qlik, and do not require intervention:

### Continuous compaction

The compaction process is on-going and specifically optimized for streaming data but supports all workloads. Compaction involves:

- Monitoring and selection: Regularly checking for potential compaction opportunities.
- Optimization criteria: Selecting compactions that offer the highest predicted query performance gains and cost reduction. This decision is relative to the cost of performing the compaction, an approach that ensures the Iceberg tables remain optimized for query performance without incurring unnecessary computational costs.

### Snapshot expiration

Iceberg operations generate new snapshots that are available for user queries. Snapshots enable features such as time travel. However, storing these snapshots can lead to increased storage requirements. To manage this, Qlik automatically removes old snapshots. The clean-up process runs every few hours, ensuring that only necessary snapshots are retained to optimize storage usage.

### Dangling file clean-up

Files may sometimes become unreferenced or "dangling" during Iceberg operations. Dangling files can accumulate, leading to increased storage costs. Qlik performs a daily clean-up of detected dangling files to reduce additional storage costs. The clean-up operation automatically finds and removes dangling files from the table storage location, maintaining a tidy and cost-effective storage environment.
