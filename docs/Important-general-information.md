---
title: "Important information about Qlik database tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Important-general-information.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver"]
---

# Important information about Qlik database tables

The tables /QTQVC/CONTROL and /QTQVC/JOB\_SQL contains information about SQL Connector jobs.

The table /QTQVC/TRACE is used to store trace information for the SQL Connector. Records are written when the connection string property ;Trace=1; is part of the connection string in the Qlik script.

The table /QTQVC/STATUS contains information about jobs started for all connectors. It is also used for Process chain handling and to store the result of deletion of the Qlik database tables (when performed in background mode).

## Overview

The Qlik database records can be deleted at any time.

Warning noteDo not perform any connector jobs when there is an ongoing deletion job.

If there is a need to perform the deletion at the same time as connector jobs are running, use the transaction /N/QTQVC/DELETE\_SAFE (program /QTQVC/DELETE\_TABLES\_SAFE). The program can be executed anytime without affecting ongoing connector jobs since it does not delete records from the latest week. Before deleting records from the table /QTQVC/STATUS also check that there are no active ‘Process chain’ records (with JOBSTATUS ‘R’ or ‘N’) in the table.

## Delete the database table content in dialog mode

Use transaction /N/QTQVC/DELETE. This mode is suitable to use when the number of records to delete are not too many. The reason is that there is a timeout after a while in SAP for jobs executed in a dialog process.

![Delete database table records dialog](_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_Delete-database-table-records.png)

With this transaction it is possible to delete records from the /QTQVC/ tables or a single record from the table /QTQVC/STATUS. For the first four options all records from the specified table and year are deleted at one time. The option Simulate Deletion can be used to see how many records will be deleted (no deletion takes place). To delete the records, select the option Delete Records.

Click the Execute button when the appropriate options have been selected.

Information noteRecords in the table /QTQVC/STATUS with JOBSTATUS = ‘K’ will never be deleted, because they are used by the Extractor Connector.

## Delete database table content in background mode

This mode is suitable to use for tables with a large amount of records. Since the job is performed in the background there is no timeout.

### Schedule the deletion job from an SAP transaction

Use transaction /N/QTQVC/DELETE\_BGD. To perform the deletion at the same time as there are ongoing SAP connector jobs, use the transaction /N/QTQVC/DELETE\_SAFE

![Delete records from Qlik database tables dialog](_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_Delete-records-from-Qlik-database-tables.png)

Select which table(s) to delete records from. It is possible to limit the number of records to be deleted in the job. It is also possible to change the number of records to be deleted between each database Commit.

Start the background job by pressing the button Delete records from selected table(s).

Check the status of the background job in the SAP transaction SM37, Jobname is /QTQVC/DELETE\_TABLES or /QTQVC/DELETE\_TABLES\_SAFE.

The result of the finished deletion job is also stored in a record in the table /QTQVC/STATUS. Key to the record is CONNECTOR = ‘DELETION’, JOBDATE = current date and JOBTIME = current time.

Information noteIf records from the table /QTQVC/STATUS are deleted, records from previous deletion jobs will also be deleted. However, the result of the current deletion job itself will not be deleted. To delete that record as well, use the transaction /N/QTQVC/DELETE.

Records in the table /QTQVC/STATUS with JOBSTATUS = ‘K’ will never be deleted, because they are used by the Extractor Connector.

### Schedule the deletion job by using the BAPI Connector

Use the BAPI /QTQVC/ADMIN. It will execute the program /QTQVC/DELETE\_TABLES.

![BAPI Connecter admin script dialog](_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_BAPI-QTQVC-ADMIN.png)

Enter ‘X’ for the table(s) where records should be deleted. It is possible to change the values for ‘Records to delete between each Commit’ and ‘Maximum records to delete’. Mode should be ‘D’.

Reload the BAPI script. A field (RESULT) is received as Output.

![Deletion batch job started notification](_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_BAPI-script-result-msg.png)

To fetch status table records containing the result of previous deletion jobs, use the same function module with the following parameters:

- CONNECTOR: DELETION
- JOBSTATUS: F
- MAX\_RECORDS: 99999999
- MODE: G

![BAPI Connecter admin script dialog with listed deletion parameters](_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_BAPI-status-table-records.png)

Reload the BAPI script. A table (STATUSTABLE) containing status table records is received as Output.

### Schedule the deletion job directly in SAP

It is possible to schedule a deletion job directly in SAP (transaction SM36) by using the Report /QTQVC/DELETE\_TABLES. To perform the deletion at the same time as there are ongoing SAP connector jobs, schedule the program /QTQVC/DELETE\_TABLES\_SAFE instead. This task requires SAP Basis knowledge.

## Update database table content

Use Transaction /N/QTQVC/UPDATE.

![Update database table records dialog](_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_Update-database-table-records.png)

With this transaction it is possible to update single records from the tables /QTQVC/CONTROL and /QTQVC/STATUS. To update a record, select the wanted table, enter the key for the record, enter a new value in JOBSTATUS and click the Execute button.
