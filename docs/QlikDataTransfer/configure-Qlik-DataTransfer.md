---
title: "Configuring Qlik DataTransfer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikDataTransfer/configure-Qlik-DataTransfer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing data governance and transfers", "Installing Qlik DataTransfer"]
---

# Configuring Qlik DataTransfer

Administrators with access to the Qlik DataTransfer installation can configure and customize settings. Settings include ports, logs, data storage, and several other settings that can help manage low bandwidth, large files, and network latency. To modify settings, edit the services.conf file in the %Program Files%\Qlik\DataTransfer folder.

## Configuring ports

Qlik DataTransfer uses the following ports:

| Service | Port | Direction |
| --- | --- | --- |
| Secure web browser communication (HTTPS)  Information noteYou must open this port in your firewall. | 443 | Outbound |
| Data Upload service | 5505 | Internal |
| Engine service | 5506 | Internal |
| Connector Registry proxy | 5507 | Internal |

If you have a port conflict with one of the default service ports, you can change it in the services.conf file, located in %Program Files%\Qlik\DataTransfer.

[globals]
LogPath="${ALLUSERSPROFILE}\Qlik\DataTransfer\Log"
StoragePath="${ALLUSERSPROFILE}\Qlik\DataTransfer"
DataUploadServicePort=5505
EnginePort=5506
ConnectorRegistryPort=5507

## Configuring logs and data file storage

Qlik DataTransfer log files are located here: %ProgramData%\Qlik\DataTransfer\Log

Qlik DataTransfer[data connections](#glossary-0 "Glossary term") are located here: %ProgramData%\Qlik\DataTransfer\DataUpload

You can change the default storage path in the services.conf file, located in %Program Files%\Qlik\DataTransfer.

[globals]
LogPath="${ALLUSERSPROFILE}\Qlik\DataTransfer\Log"
StoragePath="${ALLUSERSPROFILE}\Qlik\DataTransfer"
DataUploadServicePort=5505
EnginePort=5506
ConnectorRegistryPort=5507

Information noteIt's recommended that you back up the files in storage folder to a secure location.

## Configuring other Qlik DataTransfer settings

There are multiple scenarios, such as low bandwidth, large files, network latency, or small application reload delay, where you might encounter issues and receives errors. Qlik DataTransfer offers configurable settings which can help you avoid such errors and improve throughput. You can configure these parameters in the services.config file, located in %Program Files%\Qlik\DataTransfer.

| Parameter name | Parameter Format | Parameter example | Description and usage |
| --- | --- | --- | --- |
| Server hostname | -o [host]  --host [host] | -o localhost  --host localhost | Default value: localhost Server hostname (define the enterprise host).  You can change the hostname other than localhost. |
| Server port | -p [port]  --port [port] | -p 5505  --port 5505 | Default value: 5505 Server port.  If 5505 is already in use by the system, you can modify it. |
| Qlik Engine port | -e [port]  --engine-port [port] | -e 5506  --engine-port 5506 | Default value: 5506 Qlik Engine port.  If 5506 is already in use, you can modify it. |
| Log path | -l [folder]  --log-path [folder] | -l [folder]  --log-path [folder] | Default value: C:\ProgramData\Qlik\DataTransfer\Log Path to where log files are stored. |
| Current working directory | -f [folder]  --working-folder [folder] | -f [folder-path]  --working-folder [folder-path] | Default value: C:\ProgramData\Qlik\DataTransfer\DataUpload Current working folder.  Change the working directory by specifying with this parameter. The working directory contains configuration files. |
| Debug mode | -m [true/false]  --debug-mode [true/false] | -m true  --debug-mode true | Default value: false Add this parameter to make the logging more verbose. |
| Enable polling | --usePolling | --usePolling | Default value: no predetermined default value Enable the polling on the shared folder configured under Data Folder. This will be used to poll the shared folder at a specified interval. |
| Polling interval | --pollingInterval [mSec] | --pollingInterval 10000 | Default value: 100 Interval (in milliseconds) to poll the shared folder to capture the updates. It is used if –usePolling is enabled. |
| Shared folder connection check interval | --folderCheckInterval [mSec] | --folderCheckInterval 30000 | Default value: 30000 Qlik DataTransfer checks for the connection to shared folder at specified intervals. If a connection is lost, it will be marked as disconnected and checked at the next interval. Once connected again, DataTransfer uploads any files which were updated since disconnection. |
| Debounce Delay Time | --debounceDelay [mSec] | --debounceDelay 3000 | Default value: 1000 If a file is generating or updating frequently, you can add some delay before it starts uploading a file. This is called debounce delay and is only applicable to Data Folder connections. |
| Upload file chunk size | --chunkSize [size in MB] | --chunkSize 200 | Default value: 300 File uploads in chunks of data.  Maximum value is 300 MB. Reducing the chunk size might help in a low bandwidth environment for better upload throughput. |
| Remote application reload delay time | --appReloadDelay [mSec] | --appReloadDelay 30000 | Default value: 30000 Qlik DataTransfer triggers reload to dependent applications configured with the connection once the upload is finished. This delay helps the user to avoid frequent reloads of an application in case multiple files are in upload related to dependent applications. |
| Minimum upload bandwidth | --minBandwidth [kbps] | --minBandwidth 10240 | Default value: 25600 Minimum upload stream bandwidth in Kbps.  This bandwidth is used to calculate the correct time-to-live (TTL). |
| Maximum concurrent upload limit | --maxConcurrentUploads [number] | --maxConcurrentUploads 10 | Default value: 10 Maximum number of concurrent uploads.  This is also used to calculate the TTL. Qlik DataTransfer calculates the time to upload based on the assumption of bandwidth being equally divided among concurrent uploads. By lowering the numbers, it helps to utilize more bandwidth. |
| Retry Delays | --tusRetryDelays [list-mSec] | --tusRetryDelays 2000,5000,10000 | Default value: 2000, 5000, 10000, 20000, 3000 If a file chunk fails to upload, the maxConcurrentUploads setting controls the number of times to retry and the time to wait between each retry. Also, the sum of all retry delays is added to the TTL for estimating the worst case TTL. |
| Queuing Delay Time | --queueingDelay [mSec] | --queueingDelay 30000 | Default value: 30000 A concurrent upload queue manages the maximum number of uploads allowed at the same time. This might result in a delay of several seconds to build up the queue before the file uploading begins. The user can configure this wait time and is referred to as the queuing delay. |
| Maximum file size | --maxFileSize [size in GB] | --maxFileSize 6.0 | Default value: 0 Maximum file size in GB that can be uploaded.  Zero means the Qlik Cloud [tenant](#glossary-1 "Glossary term")'s maximum large file size quota. This can be set smaller to prevent users from accidentally uploading very large files. |
| Resource busy delay time | --resourceBusyDelay [mSec] | --resourceBusyDelay 60000 | Default value: 60000 If Qlik Cloud returns a resource busy (423) error during upload, it will wait for a specific amount of time before it retries. You can specify this delay. |
