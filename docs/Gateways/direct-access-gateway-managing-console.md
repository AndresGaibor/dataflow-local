---
title: "Managing Qlik Data Gateway - Direct Access in Administration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Qlik Data Gateway - Direct Access"]
---

# Managing Qlik Data Gateway - Direct Access in Administration

This section describes how to manage the Direct Access gateway in Administration.

## Editing the data gateway data properties

Information noteIf you need to update the registration key, follow the procedure described in [*Managing the Qlik Data Gateway - Direct Access server*](direct-access-gateway-managing.htm#Updating).

1. In Administration, go to Data gateways.
2. Click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button at the end of the row, and select Edit.

   The Edit data gateway dialog opens.
3. Update the properties as needed, and then click Save.

## Enabling and disabling data gateways

1. In Administration, go to Data gateways.
2. Do one of the following:

   - Select the check box at the beginning of the row and click the Enable or Disable toolbar button.
   - Click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button at the end of the row, and select Enable or Disable.
3. Confirm the action.

Warning noteAfter enabling the data gateway, you must restart the data gateway service. For details, see [*Starting, stopping, or restarting the service*](direct-access-gateway-managing.htm#Starting).

## Deleting data gateways

1. In Administration, go to Data gateways.
2. Do one of the following:

   - Select the check box at the beginning of the row, and click the Delete toolbar button.
   - Click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button at the end of the row, and select Delete.
3. Confirm the deletion.

## Configuring load balancing with gateway pools

A gateway pool is a group of Direct Access gateways that you can assign to a data connection. When a reload or metadata operation runs through that connection, Qlik Cloud automatically selects one gateway from the pool, based on its availability and current load.

Use a gateway pool to:

- **Distribute load**: Spread reloads across several gateways so that no single gateway becomes a bottleneck.
- **Improve availability**: If a gateway is unavailable, operations are routed to another gateway in the pool.
- **Scale out**: Add capacity by adding gateways to the pool, with no changes to the data connections that use it.

Gateway pools are configured in the Administration activity center. When you create a [data connection](#glossary-0 "Glossary term") to the gateway, you configure the connection for a single gateway or use the pool of gateways.

### How a gateway is selected

When a data connection uses a pool, Qlik Cloud picks a gateway for each operation in two steps:

1. **Availability**: Gateways that are offline or unreachable are excluded.
2. **Load**: From the remaining gateways, the one with the lowest load is chosen. Load is determined by:

   - CPU usage
   - Memory usage
   - Number of concurrent reloads

Selection happens per operation. Two reloads that use the same data connection can run on different gateways.

### Limitations and requirements

- All gateways in a pool must have the same configuration. This includes:

  - Supported connectors.
  - Allowed URLs for the REST connector.
  - Allowed path for the File connector.
  - Allowed DSN, drivers, and datatype mapping for the Generic ODBC connector.
- All gateways in a pool should be defined with the same gateway space in order to avoid permissions issues.
- All gateways in the pool must be able to reach the same data sources. Examples are network and firewall access, drivers, and credentials or certificates.
- A mismatch can cause reloads to fail depending on which gateway is picked.

### Creating pools and applying them to gateways

You create and apply pools when creating or editing a Direct Access gateway.

1. Create a new Direct Access gateway, or edit an existing one.
2. In the Pool field, select an existing gateway pool name or type a new one to create a pool that includes this gateway.
3. After creating and applying the pool, configure your data connection to select the pool or gateway.

## Setting notifications for Direct Access gateway

### Notifications for a specific Direct Access gateway

You can set notifications to be alerted at changes in the operation of your data gateway. You can get a notification in your browser, by email, or a push message to the Qlik Analytics mobile app.

1. Select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then select Data gateways.
2. Click ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a data gateway, and select Notifications.
3. Select which events to receive a notification for.

   Notifications are available for the following events:

   - Data gateway state has changed
   - Data gateway version requires an update

     Information noteThis notification will only be sent in the rare case of Qlik forcibly deactivating the gateway (usually due to a critical issue).
4. Click Done.

You can view and edit gateway-specific notifications in your settings. You can find them under Settings > Notifications > Custom notifications > Data gateways.

### Notification for a new Direct Access gateway version

Under Settings > Notifications > Data gateways, you can set the following additional notification:

- New data gateway version is available

When enabled, the notification will be sent to the data gateway creator only, whenever a new Direct Access gateway version becomes available for download.

## Viewing and running benchmark tests

### Overview

Benchmark tests are diagnostic operations that measure network connectivity and performance between the Direct Access gateway and Qlik Cloud. Use them to troubleshoot reload performance, establish performance baselines, or compare gateways.

Information note

In the Administration activity center, benchmark tests require Direct Access gateway 1.7.17 or later. The benchmark API is available from Direct Access gateway 1.7.8 or later. For API details, see the [Direct Access Gateway benchmarks API](https://qlik.dev/apis/rest/direct-access-agents/#post-api-v1-direct-access-agents-agentId-benchmarks).

Benchmark results can help you identify network conditions that affect reload performance and provide information for troubleshooting.

### Prerequisites

Before you run a benchmark test, verify the following requirements:

- The gateway runs version 1.7.17 or later.
- The gateway is connected and running in Qlik Cloud.
- You are assigned the Tenant Admin role and are either the gateway space owner or a member of the gateway space with the Can consume data role.

### Creating a new benchmark test

To create a benchmark test:

1. In the Administration [activity center](#glossary-1 "Glossary term"), click Data gateways.
2. Next to a gateway that you want to benchmark, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Benchmarks.

   The Direct access gateway benchmarks tab opens. All existing benchmarks associated with the gateway are listed.
3. Click Create benchmark.
4. Type a Name and optionally a Description.
5. As needed, adjust the Data size and Overlap policy.
6. To set up a schedule for when to run the benchmark tests, check the option for Schedule this benchmark. For more information, see [*Scheduling benchmark tests*](#Scheduling).
7. Click Create benchmark.

#### Scheduling benchmark tests

Information noteSupported from Direct Access gateway 1.8.2.

To schedule a benchmark test, configure the schedule in the Create benchmark dialog. Options include hourly, daily, weekly, and monthly frequencies. Then click Create benchmark.

Viewing and managing schedules

Open the Direct access gateway benchmarks tab, then click Schedules. The list shows each schedule's state, start and end dates, next run, and last run.

The date-range filter applies to Benchmarks, Reloads, and Schedules. A schedule appears when its date range overlaps the selected range.

Select a schedule to view its configuration and triggered benchmark runs. From its details, you can click Run now, enable or disable the schedule, edit it in the Edit schedule dialog, or delete it.

### Running a benchmark test

To run an existing benchmark test:

1. In the Administration activity center, click Data gateways.
2. Open the Direct access gateway benchmarks tab.
3. Next to a benchmark test that you want to run, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Run.

The benchmark runs as a background task. You can also create and monitor a benchmark through the [Direct Access Gateway benchmarks API](https://qlik.dev/apis/rest/direct-access-agents/#post-api-v1-direct-access-agents-agentId-benchmarks).

### Viewing benchmark results

The Direct access gateway benchmarks tab allows you to view and compare benchmark results. You can view results for a single benchmark or reload run, or compare multiple benchmark and reload runs. You can also compare metrics across different gateways.

To analyze benchmark results:

1. In the Administration activity center, click Data gateways.
2. Open the Direct access gateway benchmarks tab.
3. Navigate between the Benchmarks and Reloads sections as needed, selecting any items you wish to analyze.
4. You can compare benchmark and reload runs across different gateways. After selecting one or more items for a gateway, use the gateway selector in the top bar to switch gateways, and then select more items.
5. Click View results or Compare selected.

Analysis results

The results of benchmark and reload analysis consist of the following, depending on the option you use:

- View results: Trend analysis to track latency over time between benchmark and reload runs.
- Compare selected: Metrics such as latency and throughput, analyzed as poor, basic, or good on a per-run basis.

### Troubleshooting benchmarks

| Issue | Possible cause | Solution |
| --- | --- | --- |
| Benchmark request is rejected | The requester does not have the required tenant or gateway space permissions. | Verify that the requester has the Tenant Admin role and is either the gateway space owner or a member of the gateway space with the Can consume data role. |
| Benchmark is unavailable | The gateway version does not support the requested interface. | For the Administration activity center, use Direct Access gateway 1.7.17 or later. For the API, use Direct Access gateway 1.7.8 or later. |

### Limitations

Only the 100 most recent reloads and the 100 most recent benchmarks are presented per gateway.

## Data gateway properties

To access the Data gateways table, select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then select Data gateways. The Data gateways table shows basic information about each data gateway.

Data gateway properties

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gateways-table.png "Click to view full size")

The table columns are as follows:

- Name – The name specified when the data gateway was created.
- Type – Should be Direct Access gateway.
- Version - The current version. For more information, see [*Upgrading and uninstalling Qlik Data Gateway - Direct Access*](direct-access-gateway-upgrading.htm).
- Description – The description provided when the data gateway was created.
- Data gateway ID – A unique identifier, which might be useful for troubleshooting purposes.
- State – Can be one of the following:

  - Connected
    - Indicates that the data gateway service has established a connection with Qlik Cloud.
  - Disconnected
     - If the status is Disconnected, start the data gateway service as described above.
  - Disabled
    - The data gateway is disabled in the Administration activity center.
  - Establishing session - Shown when the data gateway establishes a connection to the data source.
- Space - The space with which the data gateway is associated.
- Date created – When the data gateway was created.
