---
title: "Configuring and troubleshooting Qlik Data Gateway - Direct Access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Qlik Data Gateway - Direct Access"]
---

# Configuring and troubleshooting Qlik Data Gateway - Direct Access

This topic describes various actions you can perform to configure and troubleshoot Direct Access gateway.

Information noteAll of the configuration options described in this topic can also be performed via the Direct Access gateway public API. For more information, see <https://qlik.dev/apis/rest/direct-access-agents/>.

## Configuring Direct Access gateway from your Qlik Cloud tenant

While the Direct Access gateway default settings are appropriate for most environments, you might need to override the defaults to improve performance, troubleshoot an issue (via the logging settings), or overcome various connectivity issues.

Information note

- Configuring Direct Access gateway from Qlik Cloud is supported from 1.7.2 or later although it is recommended to upgrade to the latest version to benefit from the full set of configuration options.
- While most Direct Access gateway settings can be configured in the Qlik Cloud Administration activity center, some settings can only be changed by editing the configuration files [directly on the Direct Access gateway machine](#Configur2).

To be able to edit the settings in Qlik Cloud, either of the following permissions is required:

- Tenant admin and gateway space owner
- Tenant member with Can consume data in the gateway space

To open the gateway settings:

1. In your Qlik Cloud tenant, navigate to Administration > Data gateways and locate your Direct Access gateway.
2. Click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) at the end of the row, and select Gateway settings.

   The Gateway settings for <name> dialog opens.

   The settings are divided into general settings (below) and [connector settings](#Connecto). Note that changing settings might also require you to [restart the Direct Access gateway service](#Restarti).

### General settings

These settings are relevant to the general functionality of Direct Access gateway, regardless of which connector you are using.

#### Agent ID

The Agent ID to use with the Direct Access gateway public API.

#### Connector agent port

The port to use when connecting to the connector agent. This setting cannot be changed.

#### Connector agent health failure threshold

Periodic health checks are performed on Direct Access gateway components. The health checks sometimes fail initially and then
succeed. If the health checks continue to fail after the specified
threshold, the Direct Access gateway service will be restarted. You should only change this setting if requested by [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

#### Load request timeout

When network interruptions occur, reloads might fail with the following errors:

Connector error: The session does not exist (DirectAccess-1509)

Connector error: The stream session expired for the load data request (DirectAccess-1012)

If you frequently encounter the above errors, try extending the timeout to 5-10 minutes.

#### Connector agent logging level

For troubleshooting purposes, you might need to change the logging level of the connector agent components. You should only change this setting if requested by [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

#### Connector agent logging options

For troubleshooting issues with a specific connector agent component, you might need to select its corresponding log file. You should only change this setting if requested by [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

#### Limit connector agent log file size to

Set a maximum size in MB for the connector agent log file before rolling into a new file.

#### Limit retention of connector agent files to

Set a number of days for which connector agent log files are kept before being automatically deleted.

#### Memory for cached data chunks

For each reload operation, Direct Access gateway can cache data chunks in memory and offload them to disk (when the size allocated for caching is exceeded). This is especially useful if you do not use automatic recovery, and frequently encounter 4025, 4020, and 4021 errors. When the specified threshold is reached, the gateway will offload the next encrypted chunks to the disk of the Direct Access gateway machine. The default value is 100 MB. A value of 0 disables chunks recovery.

#### Chunk recovery duration threshold

This is the threshold (in minutes) for the chunks recovery duration. If the reload has not resumed by the time the recovery duration threshold has been reached, it will fail with an appropriate message.

This option is useful for reloads that might otherwise exceed the three hour limit, following a long recovery. For example, let's say it takes 90 minutes to retrieve the data from the database, but as soon as the reload starts, one of the chunks becomes corrupted. In this case, all of the chunks will be stored in the cache, and sent from the cache. In such a scenario, the entire reload process (storing in cache + actual reload) could take three hours to complete.

#### Override the default cache directory

Set a new cache directory.

#### DCaaS port

The port to use when connecting to DCaaS. This setting cannot be changed.

#### DCaaS logging level

For troubleshooting purposes, you might need to change the logging level of the DCaaS logs. You should only change this setting if requested by [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

#### Limit retention of DCaaS log files to (days)

You can limit the number of days that Qlik Data Gateway - Direct Access retains component log files (connectors, DCaaS, agent, and so on). Log files older than the specified number of days are automatically deleted.

#### Data port range start

Set the start of the data port range for process isolation.

#### Load performance metrics

These configuration properties are related to load performance results. The properties control how much data is kept on the gateway machine, and how it gets cleaned up over time.

Information noteSupported from Direct Access gateway 1.7.17.

- Load performance metrics recording enabled: Choose whether load performance metrics are persisted or not.
- Benchmark retention cleanup enabled: Choose whether or not to automatically clean up benchmark records.
- Benchmark retention: Set the number of days for which to keep benchmark records before cleanup.
- Benchmark retention check interval: Set the interval at which to check for benchmark records that can be cleaned up.
- Benchmark retention database size: Set a target database size in MB for benchmark records.
- Benchmark retention cleanup batch size: Set the number of benchmark records to delete per cleanup batch.

### Connector settings

To change connector settings, select the connector type on the left and then change the settings below as needed.

#### Port

The port to use when connecting to the data source. This setting cannot be changed.

#### Logging level

For troubleshooting purposes, you might need to change the logging level of the connector logs. You should only change this setting if requested by [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

#### Process isolation

Information note

Requires Direct Access gateway 1.6.1 or later.

Process isolation allows administrators with access to the Direct Access gateway server operating system to control how many processes are available for reloads and/or metadata commands per connector type. Spreading reloads and/or metadata commands across multiple connector processes increases the level of isolation by reducing the number of reloads/or metadata commands running concurrently on each connector process. This in turn can improve overall Direct Access gateway stability in cases where connector crashes have occurred.

With a clean installation, process isolation is enabled by default. The default number of concurrent reloads/or metadata commands for each connector type is 9. You can override the default as described in Number of concurrent reload/command processes below.

The following options are available:

- Disabled: Qlik Support might ask you to disable process isolation for troubleshooting purposes.
- Metadata: Enable process isolation for metadata commands only. This can be useful, for example, for customers with ODBC drivers that do not support multi-threading, but who want to run metadata commands concurrently (mainly for preview purposes).

  Information noteSupported from Direct Access gateway 1.7.9.
- Reload (Default): Enable process isolation for reload commands only.
- All: Enable process isolation for both reload and metadata commands.

  Information noteSupported from Direct Access gateway 1.7.9.

#### Number of concurrent reload/command processes

The number of concurrent reload/command processes allocated for the connector, including the command process. So, for example, a value of 30 would mean a maximum of 29 concurrent reloads/commands. Note that this setting is only relevant when process isolation is enabled.

Information noteStarting from Direct Access gateway version 1.6.7, this value can exceed 10 without needing to change other settings. To fully isolate reloads with a particular connector type (that is, no more than one reload per connector process), this value should be set to a minimum of 30, but you might need to be set it as high as 60 depending on the workload.

#### Reload session life

Information noteRelevant for the ODBC (via Direct Access gateway) connector only.

If the connection between Direct Access gateway and Qlik Cloud is idle for 20 seconds or more, the reload operation might sometimes fail with the following error:

Invalid object name '#<TempTableName>' (indicating that the Direct Access gateway temp tables are unavailable).

The default session life is 20 seconds, but if you frequently experience this error, you can extend the session life as needed.

#### Maximum number of tables to unload

Information note

- Relevant for the ODBC (via Direct Access gateway) connector only.
- Requires Direct Access gateway 1.7.1 or later.

By default, a maximum of 10,000 tables are retrieved from the database. You can override the default when your database has more than 10,000 tables.

#### Show detailed error message

Information note

- Relevant for the ODBC-based connectors only.
- Visibility in the UI requires Direct Access gateway 1.7.11 or later.

Due to security concerns, the default error message returned by the ODBC driver contains minimal information. However, in certain scenarios, you might need more information to troubleshoot a specific issue. To generate a more detailed error message, enable this option. Once you have resolved your issue, for optimal security, it is strongly recommended to disable this option.

#### Limiting the URLs that Direct Access gateway can access using the REST connector

You can limit access to specific URLs or URL paths that can be accessed with the REST connector.

Information noteAny changes you make (adding, editing, or deleting URLS) will only take effect after you restart the Direct Access gateway service.

To limit access to a specific URL, enter the URL in the Allowed URLs field and click Add. Do the same to limit access to a URL path, but append the URL with an asterisk (\*). Repeat as necessary.

Example

In the following example, the Allowed URLs list contains two entries:

- The first entry only allows access to https://mypublicrestservice.com/restricted/source.
- The second entry allows access to https://mypublicrestservice.com/open and any path under it such as https://mypublicrestservice.com/open/shared

| Allowed URLs |
| --- |
| https://mypublicrestservice.com/restricted/source |
| https://mypublicrestservice.com/open\* |

Editing or deleting URLs

To edit a URL, click the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) button at the end of the row, and edit the URL as desired. Then click ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg) to save your changes or ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg) to cancel.

To delete a URL, click the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) button at the end of the row.

See also: [Create a REST connection](/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/Create-REST-connection/Create-REST-connection.htm).

#### Limiting the list of paths that Direct Access gateway can access using the File connector

You can limit access to paths that can be accessed with the File connector. You can also pair a path with one or more spaces to further restrict access to the specified path.

Information note

- Paired spaces are supported from Direct Access gateway 1.7.6.
- When using Direct Access gateway 1.7.4 or 1.7.5, any changes you make (adding, editing, or deleting paths or spaces) will only take effect after you restart the Direct Access gateway service.
- Only users with the Can consume data role or higher (Can edit, Can edit data in applications, Can manage) will be able to access the paths.
- All Windows file systems and network drives are supported, including standard DOS paths and UNC paths.

To limit access to a specific path, enter the path in the File paths field and click Add. Repeat as necessary.

To pair a space with a path, after adding the path, click the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) button at the end of the row and select one or more spaces from the drop-down list in the Paired spaces column. If a path is paired with spaces, only users that belong to at least one of the spaces will be able to access the specified path. Note that members of the specified spaces will be able to access the path from any space they belong to (even if not explicitly defined), including their personal space.

Example

In the following example, the File paths list contains two entries:

- The first entry allows any user with the required role to access C:\mypath\source.
- The second entry only allows members of the mosheSharedSpace space to access C:\restricted.

| Source file path | Paired spaces |
| --- | --- |
| C:\mypath\source | No spaces selected |
| C:\restricted | mosheSharedSpace |

Editing or deleting entries

To edit an entry, click the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) button at the end of the row, and edit the entry as desired. Then click ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg) to save your changes or ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg) to revert your changes.

To delete an entry, click the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) button at the end of the row.

See also: [File (via Direct Access gateway)](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/File-DG-storage-provider-connector.htm).

### Disabling chunks recovery per connection

Information noteRequires Direct Access gateway 1.7.16 or later.

Direct Access gateway automatically recovers corrupted chunks (encrypted data segments) during reload operations. This helps reloads succeed even when network interruptions or data source issues cause chunk loss.

By default, chunks recovery is enabled for all connections. However, you can disable this feature on a per-connection basis if you want to prioritize reload speed over resilience, or if your workload does not require recovery.

To disable chunks recovery for a specific connections:

1. In your Qlik Cloud tenant, open the relevant connector.
2. Locate the Advanced section.
3. Set disableDataChunksRecovery (Name) to true (Value)
4. Save your changes.

You can also disable chunks recovery via the Direct Access gateway public API. For API details, see [Direct Access Gateway REST API](https://qlik.dev/apis/rest/direct-access-agents/#put-api-v1-direct-access-agents-agentId-connectors-connectorType-files-fileType).

Information notePer-connection settings take precedence over the global Chunk recovery duration threshold setting (configured in general gateway settings). This allows fine-grained control on a per-connection basis.

### Monitoring reload performance in 1.7.16

Information noteRequires Direct Access gateway 1.7.16 or later.

Direct Access gateway 1.7.16 includes automatic performance enhancements to reload stream throughput. These optimizations are enabled by default and require no configuration.

The following improvements are included:

- Thread pool optimization: Enhanced thread pool management reduces overhead and improves resource utilization during high-concurrency reloads.
- WebSocket protocol enhancements: Improved WebSocket handling between Direct Access gateway and Qlik Cloud reduces latency and increases throughput.
- Adaptive pacing: Dynamic pacing algorithms adjust data transfer rates based on network conditions and queue depth, preventing congestion and timeouts.

To verify the performance improvements, monitor reload times and logs in your environment. You should observe faster reload completion times compared to previous versions. If you experience unexpected behavior or performance degradation, contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

### Additional ODBC (via Direct Access gateway) connector settings

When using the ODBC (via Direct Access gateway) connector, you can restrict the use of specific DSNs and drivers, and override the default data type mappings.

Information note

- Relevant for the ODBC (via Direct Access gateway) connector only.
- Visibility in the UI requires Direct Access gateway 1.7.11 or later.

#### Allowing only specific DSNs

For security or administrative reasons, you might want to limit the use of certain DSNs.

To do this

1. Select ODBC from the list of connectors and scroll down to the DSNs section.
2. Toggle on only the DSNs you want to allow.

   In the ODBC (via Direct Access gateway) connector dialog, when System DSN is selected, only the allowed DSNs will appear in the ODBC source dropdown list.
3. Restart the Qlik Data Gateway - Direct Access service.

#### Allowing only specific drivers

For security or administrative reasons, you might want to limit the use of certain drivers.

To do this

1. Select ODBC from the list of connectors and scroll down to the Drivers section.
2. Toggle on only the drivers you want to allow.
3. Restart the Qlik Data Gateway - Direct Access service.

   In the ODBC (via Direct Access gateway) connector dialog, when ODBC driver is selected, only the allowed drivers will appear in the ODBC source dropdown list.

#### Overriding the default Qlik Cloud data type mappings

Sometimes, due to an issue with the vendor ODBC driver's handling of source data types, either an error will occur during reload or incorrect data will be loaded to Qlik Cloud. In such cases, you can override the default mapping between the source data type and the Qlik Cloud data type.

To do this

1. Select ODBC from the list of connectors and scroll down to the Drivers section.
2. Locate your driver and click the![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/arrow_down.svg) at the end of the row to expand the section.
3. Click Add data type mapping.

   The following columns (properties) will be displayed:

   - Source data type: The source data type.
   - Qlik Cloud data type: The data type on Qlik Cloud to which the source data type will be mapped.
   - Size: The size (precision ) of the mapped data type on Qlik Cloud.
   - IsBit: Whether the mapped data type is a bit (stores 1 or 0 values).
4. Set each of the properties and save your settings.

   The mapping will be saved, as in the following example:

   | Source data type | Qlik Cloud data type | Size | IsBit |
   | --- | --- | --- | --- |
   | timestamp with time zone | Datetime | 27 | false |
5. Restart the Qlik Data Gateway - Direct Access service.
6. Reload the data.

Warning noteWhile many issues can be resolved by simply changing QlikDataType to String, if it is not possible to do this, we recommend contacting [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) for guidance about the Qlik Cloud data types the source data type can be mapped to.

Editing and deleting mappings

To edit a mapping

- Click the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/edit.svg) at the end of the row and edit the columns as required.

To delete a mapping

- Click the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/delete.svg) at the end of the row.

### Restarting Direct Access gateway after changing the settings

Some settings will only be applied after the Direct Access gateway service is restarted. In such a case, you will be prompted to restart the service when you save your settings. If there are active reloads, you will not be able to restart the service until they complete. When there are no active reloads, you can restart the service at any time as follows:

1. In your Qlik Cloud tenant, navigate to Administration > Data gateways and locate your Direct Access gateway.
2. Click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) at the end of the row, and select Restart service.

You can also restart the service directly on the Direct Access gateway machine, as described in [*Starting, stopping, or restarting the service*](direct-access-gateway-managing.htm#Starting)

## Configuring Direct Access gateway directly on the Direct Access gateway machine

While most Direct Access gateway settings can be [configured in Qlik Cloud](#Configur), some settings can only be changed by editing the configuration files directly on the Direct Access gateway machine.

### Overriding the default chunks cache directory

Information noteRequires Direct Access gateway 1.7.1 or later.

For each reload operation, Direct Access gateway can cache data chunks in memory and offload them to disk (when the size allocated for caching is exceeded). You can override the default chunks cache directory (C:\ProgramData\Qlik\Gateway\tmp) directory if you do not have enough disk space on the system drive.

Information noteTo ensure stability and optimize performance, best practice is to use local paths only.

To do this:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Locate the OVERRIDE\_CHUNKS\_CACHE\_DIR property and set it to the directory of your choice.

   Example:

   OVERRIDE\_CHUNKS\_CACHE\_DIR=C:\tmp

   Information noteDo not enclose the path in quotation marks.
3. Save the configuration.properties file.
4. Do one of the following, depending on installation workflow:

   - Windows server installation:

     Restart the Qlik Data Gateway - Direct Access service as described in [*Configuring and troubleshooting Qlik Data Gateway - Direct Access*](#Managing).
   - Containerized installation:

     Restart the direct-access-agent container.

See also: [*Memory for cached data chunks*](#Memory)

### Forcing Direct Access gateway to reconnect to Qlik Cloud

By default, if Direct Access gateway becomes disconnected from Qlik Cloud, it should reconnect after 45 seconds. If you notice it taking significantly longer, you can force the gateway to reconnect sooner.

To do this:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected. This file contains an example source to Qlik Cloud data types.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Add AGENT\_PONG\_TIMEOUT\_SECONDS=<time-in-seconds> to the # Connector Agent section at the beginning of the file.

   Example:

   AGENT\_PONG\_TIMEOUT\_SECONDS=30

   Information noteThe minimum time is 30 seconds.
3. Save the configuration.properties file.
4. Do one of the following, depending on installation workflow:

   - Windows server installation:

     Restart the Qlik Data Gateway - Direct Access service as described in [*Configuring and troubleshooting Qlik Data Gateway - Direct Access*](#Managing).
   - Containerized installation:

     Restart the direct-access-agent container.

### Performing Load Data requests asynchronously

Information note

Requires Direct Access gateway 1.7.5 or later.

Performing load data request asynchronously on the agent significantly shortens the time the cloud service needs to wait for responses from the agent.

To enable asynchronous load data requests:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Add the following line to the file if it does not already exist:

   OPTIONAL\_CAPABILITIES=AsyncLoadDataRequest

   If OPTIONAL\_CAPABILITIES= already exists with another parameter (AsyncLoadSlotRequest, for example), simply append it to the existing parameter, separated by a comma without a space.

   Example:

   OPTIONAL\_CAPABILITIES=AsyncLoadSlotRequest,AsyncLoadDataRequest
3. Save the configuration.properties file.
4. For containerized installations only: Restart the direct-access-agent container.

Tip noteChanges are picked up by the next reload so restarting the Direct Access gateway service is not required. All changes will be logged to the connector-agent\_logs\_[date].txt file.

To disable asynchronous load data requests:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Set OPTIONAL\_CAPABILITIES=None, or simply delete AsyncLoadDataRequest if there are other OPTIONAL\_CAPABILITIES parameters.
3. Save the configuration.properties file.
4. For containerized installations only: Restart the direct-access-agent container.

### Downloading files asynchronously

Information noteSupported from Direct Access gateway 1.8.1.

AsyncFileDownloadRequest is an optional capability for File connector downloads. If the capability is not negotiated, file downloads remain synchronous.

To enable asynchronous file download requests:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Add the following line to the file if it does not already exist:

   OPTIONAL\_CAPABILITIES=AsyncFileDownloadRequest

   If OPTIONAL\_CAPABILITIES= already exists with another parameter (AsyncFileDownloadRequest, for example), simply append it to the existing parameter, separated by a comma without a space:

   Example:

   OPTIONAL\_CAPABILITIES=AsyncLoadDataRequest,AsyncFileDownloadRequest
3. Save the configuration.properties file.

Tip noteChanges are picked up by the next reload so restarting the Direct Access gateway service is not required. All changes will be logged to the connector-agent\_logs\_[date].txt file.

To disable asynchronous file download requests:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Set OPTIONAL\_CAPABILITIES=None, or simply delete AsyncFileDownloadRequest if there are other OPTIONAL\_CAPABILITIES parameters.
3. Save the configuration.properties file.

### Requesting load slots asynchronously

Information note

Requires Direct Access gateway 1.7.7 or later.

Requesting load slots asynchronously alleviates temporary command pipe congestion to Direct Access gateway during creation of the reload data WebSocket to Qlik Cloud. This might be useful when performing a considerable number of concurrent reloads.

Information noteYou should only enable this capability if instructed by [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

To enable asynchronous load slot requests:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Add the following line to the file if it does not already exist:

   OPTIONAL\_CAPABILITIES=AsyncLoadSlotRequest

   If OPTIONAL\_CAPABILITIES= already exists with another parameter (AsyncLoadDataRequest, for example), simply append it to the existing parameter, separated by a comma without a space:

   Example:

   OPTIONAL\_CAPABILITIES=AsyncLoadDataRequest,AsyncLoadSlotRequest
3. Save the configuration.properties file.

Tip noteChanges are picked up by the next reload so restarting the Direct Access gateway service is not required. All changes will be logged to the connector-agent\_logs\_[date].txt file.

To disable asynchronous load slot requests:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Set OPTIONAL\_CAPABILITIES=None, or simply delete AsyncLoadSlotRequest if there are other OPTIONAL\_CAPABILITIES parameters.
3. Save the configuration.properties file.

### Configuring connector startup

You can increase the timeout value and number of attempts for connector startup. This might be useful when performing a considerable number of concurrent reloads. Increasing these parameters will give Direct Access gateway more time and attempts to run the connector before exiting with failure and requiring a restart.

Information noteYou should only enable this capability if instructed by [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

Information note

Requires Direct Access gateway 1.7.7 or later.

To adjust connector startup parameters:

1. Using a text editor, open the following file as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.

   - Windows server installation:

     C:\ProgramData\Qlik\Gateway\configuration.properties
   - Containerized installation:

     /usr/share/Qlik/Gateway/configuration.properties
2. Add the following lines to the file:

   # CONNECTOR STARTUP TIMEOUT between 30 and 120 seconds

   CONNECTOR\_STARTUP\_TIMEOUT\_SECONDS=your-value

   # CONNECTOR STARTUP MAX ATTEMPTS between 1 and 5

   CONNECTOR\_STARTUP\_MAX\_ATTEMPTS=your-value

   Information note To prevent command pipe congestion, adjusting these values requires AsyncLoadDataRequest to be enabled, as described in Requesting load slots asynchronously above. These settings will revert to fixed legacy values of 30 and 3 respectively when AsyncLoadSlotRequest is disabled.
3. Save the configuration.properties file.
4. For containerized installations only: Restart the direct-access-agent container.

### Overriding the default starting port set by process isolation

When process isolation is enabled, you can now override the default starting port (49152) that Direct Access gateway uses for inter-process communication with all isolated connector processes. This can be useful when the default port is in use by another process.

Information note

- You should only enable this capability if instructed by [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).
- Requires Direct Access gateway 1.7.8 or later.
- This capability is also supported via the [Public API](https://qlik.dev/apis/rest/direct-access-agents/).

To do this:

1. Using a text editor, open C:\ProgramData\Qlik\Gateway\configuration.properties as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected.
2. Under the # Connector Agent section, add the following line to the file:

   DATA\_PORT\_RANGE\_START=port-value

   where port-value is the default starting port.
3. Save the configuration.properties file.
4. Do one of the following, depending on installation workflow:

   - Windows server installation:

     Restart the Qlik Data Gateway - Direct Access service as described in [*Configuring and troubleshooting Qlik Data Gateway - Direct Access*](#Managing).
   - Containerized installation:

     Restart the direct-access-agent container.

## Metrics collector

In a typical customer's environment, numerous data reloads pass through Direct Access gateway into Qlik Cloud Analytics on a daily basis. The ability to log and monitor resource consumption and utilization impacted by these reloads will help customers plan their reloads accordingly.

The new metrics collector (which runs in the background on the Direct Access gateway machine) offers basic logging and monitoring of resource utilization by Direct Access gateway, connectors, and the Operating System.
The metrics collector can either be configured locally in a JSON file or via the [Public API](https://qlik.dev/apis/rest/direct-access-agents/).

### Configuring the metrics collector

On the Direct Access gateway machine, open the following file and configure it as required:

- Windows server installation:

  <INSTALL\_DIR>\ConnectorAgent\MetricsCollector\metricscollectorsettings.json
- Containerized installation:

  /usr/runMetricsCollector/metricscollectorsettings.json

#### Configuring collector settings (MetricsCollectorSettings)

- Enabled: Set to true (default) to enable metrics collection or false to disable it.
- BaseScrapeIntervalSeconds: How often to poll for connector metrics in seconds. Each connector has its own polling interval.
- Port: The port used by the API or metrics connector (REST via Direct Access gateway).
- LocalDataRetentionDays: Data older than the specified value will be deleted from the local database.
- localDataRetentionDatabaseSizeInMb: The total size of metrics data to store on the gateway machine (in MB). The default is 500 MB. Old data will be deleted to ensure that the quota is not exceeded.

  Information note
  - Requires Direct Access gateway 1.7.10 or later.
  - A large number of concurrent reloads might require increasing the default value. For example, a tenant with 60 concurrent reloads could require as much as 1 GB.
- DataRetentionCheckIntervalMinutes: The frequency of the retention check.
- LocalDatabaseFileLocation: The location of the local database. This can also be an UNC path. The default location is as follows:

  - Windows server installation:

    C:\ProgramData\Qlik\Gateway\tmp
  - Containerized installation:

    /usr/share/Qlik/Gateway/tmp

#### Configuring connector settings (ConnectorConfigurations)

For all Direct Access gateway connectors, you can set the metrics polling interval (ScrapeIntervalSeconds) and enable (true) or disable (false) metrics collection.

#### Example metricscollectorsettings.json file

```
{
  "MetricsCollectorSettings": {
    "Enabled": true,
    "BaseScrapeIntervalSeconds": 1,
    "Port": 5052,
    "LocalDataRetentionDays": 30,
    "localDataRetentionDatabaseSizeInMb": 500,
    "DataRetentionCheckIntervalMinutes": 60,
    "LocalDatabaseFileLocation": ""
  },
  "ConnectorConfigurations": {
    "OdbcConnector": {
      "MetricsCollectionEnabled": true,
      "ScrapeIntervalSeconds": 30
    },
    "SystemMetrics": {
      "MetricsCollectionEnabled": true,
      "ScrapeIntervalSeconds": 30
    },
    "ConnectorAgent": {
      "MetricsCollectionEnabled": false,
      "ScrapeIntervalSeconds": 30
    },
    "RestConnector": {
      "MetricsCollectionEnabled": false,
      "ScrapeIntervalSeconds": 30
    },
    "SapSqlConnector": {
      "MetricsCollectionEnabled": false,
      "ScrapeIntervalSeconds": 30
    },
    "SapBwConnector": {
      "MetricsCollectionEnabled": false,
      "ScrapeIntervalSeconds": 30
    },
    "SapPackageConnector": {
      "MetricsCollectionEnabled": false,
      "ScrapeIntervalSeconds": 30
    },
    "FileConnector": {
      "MetricsCollectionEnabled": false,
      "ScrapeIntervalSeconds": 30
    }
  }
}
```

### Loading metrics

Use the REST (via Direct Access gateway) connector to collect the metrics from Direct Access gateway machine.

To do this:

1. In the REST (via Direct Access gateway) connection settings, enable Allow working with localhost connection.

   For details, see [Create a REST connection](/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/Create-REST-connection/Create-REST-connection.htm).
2. Add http://localhost:5052/api/metrics to the list of allowed URLs.

   See [*Limiting the URLs that Direct Access gateway can access using the REST connector*](#Limiting) above.
3. Restart the Direct Access gateway service.
4. Create an application and load the metrics from http://localhost:5052/api/metrics via the REST (via Direct Access gateway) connection.

### Supported metrics

- System metrics:

  - network\_bytes\_sent\_total: The total number of bytes transmitted through Direct Access gateway since the system started
  - network\_bytes\_received\_total: The total number of bytes received through Direct Access gateway since the system started
- Connector metrics:

  - process\_start\_time\_seconds: Time elapsed since the process started in seconds.
  - process\_cpu\_seconds\_total: The cumulative number of seconds a CPU has been in a specific state
  - process\_virtual\_memory\_bytes: The current size, in bytes, of the virtual memory consumed by the process.
  - process\_working\_set\_bytes: The current size, in bytes, of the Working Set of the process.
  - process\_private\_memory\_bytes: The current size, in bytes, of the private memory consumed by the process.
  - process\_num\_threads: The number of threads used by the process.

## Viewing and downloading log files

The log files provide information about Direct Access gateway operations. Qlik Support might ask you to provide log files for troubleshooting purposes. You can view or download the log files in the Log viewer. Under normal circumstances, there is no reason to examine the log files, but if you experience repeated failures or other issues, the log files will often help pinpoint the cause.

Information noteViewing and downloading the logs requires the Can consume data role.

To open the Log viewer:

1. In the Administration activity center, go to Data gateways and locate your Direct Access gateway.
2. Click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) at the end of the row, and select View logs.

   The Log viewer window opens.
3. From the drop-down list in the top left, choose the type of log that Qlik Support has asked you to view or download.

   The following logs are available:

   - Direct Access gateway logs (DirectAccessAgent)
   - DCaaS logs (dcaas\_logs)
   - ODBC-based connector logs (odbc-connector\_logs)
   - SAP BW connector logs (QvSAPBwConnector-<date + timestamp>)
   - SAP SQL connector logs (QvSqlBwConnector-<date + timestamp>)
   - Connector agent logs (connector-agent\_logs\_<date>)
   - SAP ODP and SAP Report connectors logs (QvSapConnectorPackage-<process\_id>)
   - REST connector logs (rest-connector\_logs\_<timestamp>)
   - File connector logs (file-connector\_logs\_<timestamp>)

   Information noteFrom Direct Access gateway 1.7.1, connector start, exit, and restart events will be written to the Direct Access gateway (DirectAccessAgent) log file. In previous versions, they were written to the Connector agent logs (connector-agent\_logs\_<date>) log file.
4. From the adjacent drop-down list, select the log you want to view or download. The log files are ordered from the newest (the currently active log file) to the oldest. After you select a log file, you can use the ![Arrow to scroll to the top](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_up_stop.svg) and ![Arrow to scroll to the bottom](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down_stop.svg) buttons to jump to the start or end of the log file respectively.

   Tip noteThe view of the log file is not updated automatically with the latest messages. To update the view, click ![Arrow to scroll to the bottom](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down_stop.svg) to jump to the end of the log file, which will be updated with the latest messages.
5. To download the log file, click Download.

   The file will either be downloaded to your computer or you will be prompted to save it, depending on your browser settings.

### Opening Direct Access gateway logs on the Direct Access gateway machine

In addition to being able to download the Direct Access gateway (DirectAccessAgent) logs from the Administration activity center, you can also open them directly from the Direct Access gateway machine.

With a default installation, these logs are located in:

C:\Program Files\Qlik\ConnectorAgent\data\logs

- Windows server installation:

  C:\Program Files\Qlik\ConnectorAgent\data\logs
- Containerized installation:

  /usr/data/logs

#### Changing the DirectAccessAgent logging level

For troubleshooting purposes, you might need to change the logging level of the DirectAccessAgent logs. DirectAccessAgent is responsible for the connection to Qlik Cloud services. To view and change the logging detail level of the DirectAccessAgent logs, run the following commands from the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation):

- To view the current logging level, run:

  - Windows server installation:

    connectoragent configuration getloggers
  - Containerized installation:

    dotnet ConnectorAgent.dll configuration getloggers
- To set the logging level to Trace, run:

  - Windows server installation:

    connectoragent configuration setloggers -l Root -v DEBUG
  - Containerized installation:

    dotnet ConnectorAgent.dll configuration setloggers -l Root -v DEBUG
- To set the logging level to Verbose, run:

  - Windows server installation:

    connectoragent configuration setloggers -l Root –v DETAILED\_DEBUG
  - Containerized installation:

    dotnet ConnectorAgent.dll configuration setloggers -l Root –v DETAILED\_DEBUG

For additional logging options, see Configuring Direct Access gateway in Qlik Cloud below.

## Updating the registration key

Changing the registration key might be necessary in the unlikely event that the key becomes corrupted or if you suspect the data gateway server was accessed by an unauthorized user.

To update the registration key:

1. Do one of the following depending on your installation workflow:

   - Windows server installation:

     On the Direct Access gateway server, open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation).
   - Containerized installation:

     Open a console inside the direct-access-agent container.
2. Run the following commands:

   - Generate the new key:

     - Windows server installation:

       connectoragent qcs generate\_keys
     - Containerized installation:

       dotnet ConnectorAgent.dll qcs generate\_keys
   - Show the key:

     - Windows server installation:

       connectoragent qcs get\_registration
     - Containerized installation:

       dotnet ConnectorAgent.dll qcs get\_registration

     The key is shown:

     ![Image of the Direct Access registration key](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/da_reg_key.png)
3. Copy the entire key as shown in the example above.
4. In the Administration activity center, open the data gateway settings by clicking the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button at the end of the relevant row and selecting Edit.
5. Paste the key into the Key field (replacing the current key) and save the settings.
6. Return to the Direct Access gateway server and do one of the following, depending on installation workflow:

   - Windows server installation:

     Restart the Qlik Data Gateway - Direct Access service as described in [*Configuring and troubleshooting Qlik Data Gateway - Direct Access*](#Managing).
   - Containerized installation:

     Restart the direct-access-agent container.
