---
title: "Data sources in Qlik Cloud Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data"]
---

# Data sources in Qlik Cloud Analytics

Whether your data is stored on-premise or in the cloud, you can quickly load it into Qlik Cloud. You can even stream your social media data into your Qlik apps.

There are different ways you can add and load data from data sources.

- [Adding and managing data sources from spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-data-resources-spaces.htm)
- [Loading and managing data with Data Manager](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/managing-data.htm)
- [Loading and transforming data with scripting](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-data-modeling.htm)

The following data sources are supported in Qlik Cloud Analytics. For information about data sources supported in Qlik Talend Data Integration, see [*Setting up connections to data sources*](../Sense_Hub/DataIntegration/Landing/connecting-data-2.htm).

## Qlik Data Gateway - Direct Access

Connectors that support Direct Access gateway (ODBC-based and others) appear twice in the Create data connection dialog. Once with just the data source name and once with the data source name followed by (via Direct Access gateway). You can quickly filter the connectors list to show only connectors that support Direct Access gateway, by typing "Access" into the Data connectors search box.

Qlik Data Gateway - Direct Access eliminates the need to open inbound firewall ports, allowing Qlik Cloud applications to securely access firewalled data. If your enterprise data source is located behind a firewall and can be accessed via Qlik Data Gateway - Direct Access, it is strongly recommended to connect to it via the Direct Access gateway.

Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides.

For more information on Qlik Data Gateway - Direct Access, see [Data gateways](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm).

## List of supported data sources

Information noteA tenant admin can enable or disable access to individual data sources via an API call. This controls which data sources can be accessed in Qlik Cloud Analytics.

For more information, see [Data sources](https://qlik.dev/apis/rest/data-sources/) on the Qlik Developer site.

Information noteData source connectors that support Qlik Data Gateway - Direct Access are marked with an asterisk.

## A

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/athena-square.png)

### [\*Amazon Athena](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Athena/Athena-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/dynamo-square.png)

### [Amazon DynamoDB](/en-US/cloud-services/Subsystems/JDBC_connector_help/Content/Connectors_ODBC/DynamoDB/DynamoDB-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/redshift-square.png)

### [\*Amazon Redshift](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Redshift/Redshift-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/AmazonS3Connector-square.png)

### [Amazon S3](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/Amazon-S3-storage-provider-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/AmazonS3Connector-square.png)

### [Amazon S3 V2](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/Amazon-S3-V2-storage-provider-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/File_AmazonS3Connector-square.png)

### [Amazon S3 Metadata](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Amazon-S3-Metadata-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/File_AmazonS3Connector-square.png)

### [Amazon S3 Metadata V2](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Amazon-S3-Metadata-Connector-V2-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/drill-square.png)

### [\*Apache Drill](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/ApacheDrill/ApacheDrill-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/apache-hive-square.png)

### [\*Apache Hive](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/ApacheHive/Apache-hive-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/apache-phoenix-square.png)

### [\*Apache Phoenix](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/ApachePhoenix/Apache-Phoenix-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/apache-spark-square.png)

### [\*Apache Spark](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/ApacheSPARK/ApacheSPARK-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/azure_sql-square.png)

### [\*Azure SQL Database](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/MS-Azure/MS-Azure-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/AzureStorageConnector-square.png)

### [Azure Storage](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProviders/Storage%20provider%20connectors/Azure-Storage-storage-provider-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/AzureStorageConnector-square.png)

### [Azure Storage Metadata](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Azure-Storage-Metadata-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/azure-synapse-square.png)

### [\*Azure Synapse Analytics](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/MS-Azure/MS-AzureSynapse-connector.htm)

## C

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/cassandra-square.png)

### [Cassandra](/en-US/cloud-services/Subsystems/JDBC_connector_help/Content/Connectors_JDBC/Introduction/JDBC-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/impala-square.png)

### [\*Cloudera Impala](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/ClouderaImpala/Cloudera-impala-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/couchbase-square.png)

### [Couchbase](/en-US/cloud-services/Subsystems/JDBC_connector_help/Content/Connectors_JDBC/Introduction/JDBC-connector.htm)

## D

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/databricks-square.png)

### [\*Databricks](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Databricks/Databricks-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/DropboxConnector-square.png)

### [Dropbox](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProviders/Storage%20provider%20connectors/Dropbox-storage-provider-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/File_DropboxConnector-square.png)

### [Dropbox Metadata](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Dropbox-Metadata-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/dynamo-square.png)

### [DynamoDB](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/DynamoDB/DynamoDB-connector.htm)

## F

![Icon for File via Direct Gateway access](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/File-DG-square.png)

### [File (via Direct Access gateway)](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/File-DG-storage-provider-connector.htm)

## G

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GitHubConnector-square.png)

### [GitHub](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/GitHub-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GoogleAdsConnector-square.png)

### [Google Ads](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Google-Ads-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GoogleAnalyticsConnector-square.png)

### [Google Analytics](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Google-Analytics-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/google-square.png)

### [\*Google BigQuery](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/GoogleBigQuery/Google-BigQuery-Connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GoogleCalendarConnector-square.png)

### [Google Calendar](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Google-Calendar-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GoogleCloudStorageConnector-square.png)

### [Google Cloud Storage](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/Google-Cloud-storage-provider-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GoogleCloudStorageConnector-square.png)

### [Google Cloud Storage Metadata](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Google-Cloud-Storage-Metadata-connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GoogleDriveConnector-square.png)

### [Google Drive](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/Google-Drive-storage-provider-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GoogleDriveConnector-square.png)

### [Google Drive and Spreadsheets](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Google-Drive-and-Spreadsheets-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GoogleSearchConsoleConnector-square.png)

### [Google Search Console](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Google-Search-Console-connector-integrated.htm)

## J

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/JIRAConnector-square.png)

### [JIRA](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Jira-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/JIRAConnector-square.png)

### [JIRA Cloud](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Jira-Cloud-Connector-integrated.htm)

## M

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/MailboxIMAPConnector-square.png)

### [Mailbox IMAP](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/MailBoxIMAP-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/MailboxIMAPConnector-square.png)

### [Mailbox IMAP OAuth](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/MailBoxIMAP-OAuth-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/MailChimpConnectorV2-square.png)

### [MailChimp V2](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/MailChimp-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/marketo-square.png)

### [Marketo](/en-US/cloud-services/Subsystems/JDBC_connector_help/Content/Connectors_ODBC/Marketo/Marketo-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/TextAnalyser_MeaningCloudConnector-square.png)

### [MeaningCloud](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/MeaningCloud-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/MSCRMConnectorV2-square.png)

### [Microsoft Dynamics CRM V2](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Microsoft-Dynamics-CRM-V2-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/mssql-square.png)

### [\*Microsoft SQL Server](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/SQLServer/SQL-Server-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/mongo-square.png)

### [\*MongoDB](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Mongo/Mongo-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/mysql-square.png)

### [\*MySQL Enterprise Edition](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/MySQL/MySQL-connector.htm)

## O

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/ODataConnector-square.png)

### [OData](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/OData-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/Office365Connector-square.png)

### [Office 365 Sharepoint](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Office-365-Sharepoint-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/OneDriveConnectorV2-square.png)

### [OneDrive](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProviders/Storage%20provider%20connectors/OneDrive-storage-provider-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/OneDriveConnectorV2-square.png)

### [OneDrive Metadata](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/OneDrive-Metadata-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/oracle-square.png)

### [\*Oracle](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Oracle/Oracle-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/Outlook365Connector-square.png)

### [Outlook 365](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Outlook-365-Connector-integrated.htm)

## P

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/postgres-square.png)

### [\*PostgreSQL](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/PostgresSQL/PostgresSQL-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/presto-square.png)

### [\*Presto](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Presto/Presto-connector.htm)

## Q

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/QualtricsConnector-square.png)

### [Qualtrics](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Qualtrics-Connector-integrated.htm)

## R

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/rest-square.png)

### [\*REST](/en-US/cloud-services/Subsystems/REST_connector_help/Content/Connectors_Rest/REST-connector.htm)

## S

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/salesforce-square.png)

### [Salesforce](/en-US/cloud-services/Subsystems/Salesforce_connector_help/Content/Connectors_Salesforce/Introduction/Salesforce-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [\*SAP NetWeaver](/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/SAP-SQL-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [SAP HANA](/en-US/cloud-services/Subsystems/JDBC_connector_help/Content/Connectors_JDBC/Introduction/JDBC-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [\*SAP ODP](/en-US/cloud-services/Subsystems/SAP_ODP_Connectors_Help/Content/Connectors_SAP_ODP/SAP-ODP-intro.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/TextAnalyser_Sentiment140Connector-square.png)

### [Sentiment140](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Sentiment140-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/ServiceNow-square.png)

### [\*ServiceNow](/en-US/connectors/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/ServiceNow/ServiceNow-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/SFTPConnector-square.png)

### [SFTP](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProviders/Storage%20provider%20connectors/SFTP-storage-provider-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/SMTPConnector-square.png)

### [SMTP](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/SMTP-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/SMTPOauth_64x64.png)

### [SMTP OAuth](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/SMTP-OAuth-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/snowflake-square.png)

### [\*Snowflake](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Snowflake/Snowflake-connector.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/StravaConnector-square.png)

### [Strava](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Strava-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/SugarCRMConnector-square.png)

### [SugarCRM](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Sugar-CRM-Connector-integrated.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/SurveyMonkeyConnector-square.png)

### [SurveyMonkey](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Survey-Monkey-Connector-integrated.htm)

## T

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/teradata-square.png)

### [\*Teradata](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Teradata/Teradata-connector.htm)

## W

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/TextAnalyser_WatsonConnector-square.png)

### [Watson Natural Language Understanding](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/Watson-Connector-integrated.htm)

## Y

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/YouTubeAnalyticsConnector-square.png)

### [YouTube Analytics](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Integrated%20connectors/YouTube-Analytics-Connector-integrated.htm)
