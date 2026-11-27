---
title: "Automation connectors"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/connector-blocks/connectors-list.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Connector blocks"]
---

# Automation connectors

Qlik Automate includes a set of connectors that let you integrate third-party services and applications into your data analytics workflows. This section lists the available connectors and what they are used for.

This table lists the available Qlik Automate connectors and their compatibility with Qlik Cloud Government and Qlik Cloud Government - DoD.

| Connector | Description | Supported by Qlik Cloud Government | Supported by Qlik Cloud Government - DoD |
| --- | --- | --- | --- |
| Qlik logo | **Qlik Cloud** is a native connector that lets you integrate events, data, data assets, sets, stores and objects from your tenant into your automation. This connector does not require authentication.  This connector can also be used to help you better understand your Qlik Cloud system. For example, this connector can run a health check on automation usage in your organization, report on connector usage in a tenant, and automate management across your tenant. | Yes | Yes |
|  | **Airtable** is a database and collaboration tool. | No | No |
|  | **Alation Cloud Catalog** serves enterprises in organizing and consolidating their data. | No | No |
| Amazon Bedrock logo | **Amazon Bedrock** allows you to automate your interactions with any of the native text and large language models (LLMs). The generated output can then be sent to another Bedrock model or other automation block for further processing. | Yes | No |
| Amazon DynamoDB | **Amazon DynamoDB** allows you to easily integrate and synchronize DynamoDB data with Qlik Automate, enhancing real-time analytics and operational efficiency. | Yes | No |
| Amazon Redshift logo | **Amazon Redshift** is a managed data warehouse service. | Yes | No |
| Amazon S3 logo | **Amazon S3** is a cloud-based object storage service that stores objects in buckets. | Yes | No |
|  | **Amazon SageMaker** is a cloud-based machine learning platform. | Yes | No |
| Amazon SNS logo | **Amazon SNS** (Simple Notification Service) is a web service that coordinates and manages the delivery or sending of messages to subscribing endpoints or clients. With this connector, users can register a webhook to listen to events occuring in AWS. Use cases include listening to upload events and reloading a Qlik Sense app, triggering data pipeline, and other tasks. | Yes | No |
| Apache Kafka logo | **Apache Kafka** is a distributed event store and stream-processing platform. | Yes | No |
| API Key logo | **API key** is a generic connector that authenticates using an API key. It has a similar function as the [Call URL block](../basic/call-url-block.htm) and generic blocks that perform CRUD and List operations depending on the pagination type. | Yes | Yes |
| AWS KMS logo | **AWS Key Management Service** (AWS KMS) helps you manage the lifecycle of cryptographic keys that are used to protect the data in your tenant. For more information, see [Getting started with the AWS KMS Connector in Qlik Automate](https://community.qlik.com/t5/Official-Support-Articles/How-to-get-started-with-the-Amazon-KMS-connector-and-Qlik-s/ta-p/2104061). | Yes | No |
| AWS Lambda logo | **AWS Lambda** is a computing service that runs your code in response to events and automatically manages the computing resources, making it the fastest way to turn ideas into modern, production, serverless applications. | Yes | No |
|  | **Azure Blob Storage** is a an encrypted storage solution for storing unstructured data. | Yes | No |
| Azure Key Vault logo | **Azure Key Vault** is a secure secrets storage, providing management for secrets, keys, and certificates. | No | No |
| Azure OpenAI logo | **Azure OpenAI** provides REST API access to OpenAI's powerful language models including the GPT-4, GPT-4 Turbo with Vision, GPT-3.5-Turbo, and Embeddings model series. | Yes | No |
| Basic Authentication connector logo | **Basic Authentication** is a connector that allows advanced users to connect to platforms that do not have a specialized connector. This connector uses a basic authentication flow that requires only a username and password. It has RAW API blocks that support all methods as well as pagination. | Yes | Yes |
| Databricks logo | **Databricks** is a cloud-based collaborative data science, data engineering, and data analytics platform that combines the best of data warehouses and data lakes into a lakehouse architecture. | Yes | No |
|  | **DataRobot** is a predictive analytics platform using artificial intelligence and machine learning. | No | No |
|  | **Dbt Cloud** is a data build tool that lets you transform data in a data warehouse. | No | No |
|  | **Dropbox** is a cloud-based storage provider. | No | No |
|  | **Eventbrite** is an event hosting platform. | No | No |
|  | **FTP** is a file transfer protocol to send and receive files. | Yes | No |
|  | **GitHub** is a code hosting platform for version control and collaboration. | Yes | No |
|  | **GitLab** is a DevOps platform for development, operations, and security teams. | Yes | No |
|  | **Google BigQuery** is a managed enterprise data warehouse. | No | No |
|  | **Google Cloud Storage** is a cloud-based storage provider. | No | No |
|  | **Google Cloud Storage with service account** is a cloud-based storage provider. | No | No |
|  | **Google Sheets** is a spreadsheet program. | No | No |
|  | **HubSpot** is a cloud-based CRM for sales and marketing teams. | No | No |
|  | **Hugging Face** is a platform for building NLP systems. | No | No |
| Inphinity logo | **Inphinity** enables active intelligence through workflows, actions, data capture and process and data intelligence. | No | No |
|  | **Jira** is a platform for issue tracking and project management. | No | No |
|  | **Mail** is a connector for sending automation output to an email server. | Yes | No |
|  | **Mailchimp** is a marketing automation platform. | No | No |
|  | **Marketo** is a marketing automation platform. | No | No |
|  | **Microsoft Dynamics 365** is a cloud-based business applications platform. | No | No |
|  | **Microsoft Excel** is a spreadsheet program.  Note-lightQlik Cloud Government supports this connector with Office 365 Commercial and Office 365 Government Community Cloud (GCC). Qlik Cloud Government - DoD supports this connector in GCC High is only. | Yes | Yes |
|  | **Microsoft OneDrive** is a cloud-based storage service.  Note-lightQlik Cloud Government supports this connector with Office 365 Commercial and Office 365 Government Community Cloud (GCC). Qlik Cloud Government - DoD supports this connector in GCC High is only. | Yes | Yes |
| Outlook | **Microsoft Outlook** is a personal information manager software system, available as a part of the Microsoft Office suite.  Note-lightQlik Cloud Government supports this connector with Office 365 Commercial and Office 365 Government Community Cloud (GCC). Qlik Cloud Government - DoD supports this connector in GCC High is only. | Yes | Yes |
|  | **Microsoft Power BI** is an interactive data visualization software. | No | No |
|  | **Microsoft SharePoint** is a collaborative server environment.  Note-lightQlik Cloud Government supports this connector with Office 365 Commercial and Office 365 Government Community Cloud (GCC). Qlik Cloud Government - DoD supports this connector in GCC High is only. | Yes | Yes |
|  | **Microsoft SQL Server** is a relational database management system. | No | No |
|  | **Microsoft Teams** is a chat-based collaboration platform.  Note-lightQlik Cloud Government supports this connector with Office 365 Commercial and Office 365 Government Community Cloud (GCC). Qlik Cloud Government - DoD supports this connector in GCC High is only. | Yes | Yes |
| Monday.com logo | **Monday.com** is a cloud-based platform that allows users to create their own applications and project management software. | Yes | No |
|  | **MySQL** is an open-source relational database management system. | Yes | No |
|  | **OAuth2** is a protocol for authorization. It provides authorization flows for web applications, desktop applications, and mobile phones. | Yes | Yes |
|  | **Okta** is a customizable and secure Identity as a Service platform. The Okta connector in Qlik Automate allows you to manage your users and groups in an automation. | No | No |
| OpenAI logo | **OpenAI** is a non-profit research laboratory that promotes and develops friendly artificial general intelligence (AGI) through open-source research and tools, and the alignment of AGI with human values.  For more information, see [Getting started with the OpenAI Connector in Qlik Automate](https://community.qlik.com/t5/Official-Support-Articles/How-to-Getting-started-with-the-OpenAI-Connector-in-Qlik/ta-p/2077315).  Note-lightThe OpenAI connector is not compatible with Azure OpenAI Government Community Cloud (GCC) or GCC High. | Yes | No |
| Oracle Eloqua logo | **Oracle Eloqua** is a software as a service (SaaS) platform for marketing automation that aims to help B2B marketers and organizations manage marketing campaigns and sales lead generation. | No | No |
| PagerDuty | **PagerDuty** is an operations performance platform that integrates data from IT alert monitoring tools, on-call scheduling, and escalation policies used to fix issues in different environments throughout the incident's life-cycle. | Yes | No |
|  | **Postgres** is an open-source relational database management system. | Yes | No |
| Qlik Answers icon | **Qlik Answers** is a Qlik-native connector that enables the creation of data sources in knowledge bases using existing data connections. It allows users to interact with assistants by asking questions related to the data source and receive answers based on the existing data.  Qlik Cloud Government noteWhile the Qlik Answers connector is visible in Qlik Cloud Government and Qlik Cloud Government - DoD tenants, it does not work due to the lack of Qlik Answers support for Qlik Cloud Government and Qlik Cloud Government - DoD. | No | No |
| Qlik Predict logo | **Qlik Predict** is a Qlik-native connector that lets you integrate predictive analytics and machine learning for Qlik Cloud.  Qlik Cloud Government noteWhile the Qlik Predict connector is visible in Qlik Cloud Government and Qlik Cloud Government - DoD tenants, it does not work due to the lack of Qlik Predict support for Qlik Cloud Government and Qlik Cloud Government - DoD. | No | No |
| Qlik Catalog | **Qlik Catalog** is a Qlik-native connector that uses the metadata stored in Qlik Catalog (on-premises) and enables the creation of automated workflows. | No | No |
| Qlik Cloud Catalog | **Qlik Cloud Catalog** is a native connector that lets you automate tasks related to the Data Products Catalog and Data Quality workflows. With this connector you can enable the scheduling of quality computations for datasets, streamlining data validation processes across your organization. Aligning Data Quality execution with ELT or ETL processes helps you assess the trustworthiness of your data, especially as it may be consumed downstream by analytics, AI models, or other consumers. | Yes | Yes |
| Qlik Platform Operations | **Qlik Platform Operations** is a Qlik-native connector that can orchestrate one or many Qlik Cloud tenants using either tenant or subscription OAuth clients. Use this connector to deploy and manage tenants in Qlik Cloud without code. For more information, see [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview) on the Qlik Cloud Developer site. | Yes | Yes |
|  | **Qlik Reporting** is a Qlik-native connector that lets you build customized, multi-page reports based on app sheets. | Yes | Yes |
| Qlik Cloud Data Integration | **Qlik Talend Data Integration** is a Qlik-native connector that helps you deliver, transform, and unify enterprise data in real-time for every analytics, ML or digital transformation initiative. | Yes | Yes |
|  | **Salesforce** is a customer relationship management platform. | No | No |
|  | **SendGrid** is a cloud-based SMTP provider. | No | No |
|  | **ServiceNow** is a cloud-based workflow automation platform.  The ServiceNow connector is compatible with ServiceNow Commercial and ServiceNow Government Community Cloud (GCC). | Yes | No |
|  | **SFTP** is a secure file transfer protocol to send and receive files. | Yes | No |
|  | **Slack** is a chat-based collaboration platform With this connector, you can create channels, send messages to Slack channels and invite users to channels. You can also send alerts to Slack based on actions occurring in Qlik Cloud, such as Slack integration with task chains. For more information, see [*Slack*](Slack-connector.htm). | No | No |
|  | **Snowflake** is a cloud-based data warehousing solution. | Yes | No |
|  | **Splunk** is a platform used for monitoring, searching, and analyzing machine-generated data. | No | No |
| Stitch logo | **Stitch** is an ETL platform that connects to all your databases and SaaS applications, and replicates that data to a destination of your choosing. The Stitch connector allows users to subscribe their automation to a completed data load event in Stitch. The automation will run each time new data lands in the user's data warehouse. If the run was successful, the automation can then evaluate the pipeline's status and start Tasks in Talend or jobs in dbt. | Yes | No |
| SugarCRM logo | **SugarCRM** is a cloud-based customer relationship management (CRM) software that helps businesses manage their sales, marketing, and customer support activities. | Yes | No |
| Swapcard logo | Swapcard is an event and community platform for running large and complex in-person, hybrid and virtual events. | No | No |
| Talend | **Talend Cloud** is a data management platform providing solutions for data integration, data quality, data preparation, big data, and application integration. With the Talend Cloud connector, users can orchestrate their Talend tasks and integrate them with Qlik Cloud and use Data Prep to easily identify errors and apply rules across large datasets. It's also possible to interact with the Data Inventory for data quality and data governance needs. | Yes | No |
|  | **UiPath** is a robotic process automation tool for desktop automation. | Yes | No |
|  | **Zendesk** is a cloud-based help desk management solution. | No | No |
| Zenput logo | **Zenput** provides operations execution software for multi-unit restaurants, c-stores, and grocers. | No | No |

Contact your account representative to request Qlik Cloud Government - DoD-specific cloud applications not on the supported list.
