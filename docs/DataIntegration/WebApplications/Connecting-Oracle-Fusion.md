---
title: "Oracle Fusion"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Oracle-Fusion.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Oracle Fusion

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

Oracle Fusion is a suite of open standards-based applications that enable organizations to deploy business applications.

Business Intelligence Cloud Connector (BICC) is used to sync data from Oracle Fusion Cloud applications to your destination. Once we connect to your Oracle instance, the BICC extract jobs are created for each object to extract data. The connectors manage the life cycle of these jobs.

During syncs, the connectors re-use and schedule the BICC jobs which write incremental data files to UCM, then extract the data files from Oracle UCM and sync the data to your destination.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your Oracle Fusion data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Before you start using the Oracle Fusion application, it is recommended to read the [Overview of Business Intelligence Cloud Connector](https://docs.oracle.com/en/cloud/saas/applications-common/24c/biacc/overview-of-business-intelligence-cloud-connector.html)
in the Oracle documentation.

To connect to Oracle Fusion, you need:

- An Oracle Cloud account.
- An active Oracle Cloud Fusion subscription.
- Access to the application console. For more information, see [Use the Application Console](https://docs.oracle.com/en/cloud/paas/app-container-cloud/csjse/use-application-console.html#GUID-DFF3E1F8-B19B-45FE-99D9-2E41F6C15972) in the Oracle documentation.
- The Security Manager role to access the security console.
- To follow the procedures:
  - [*Finding the Server URL*](#Finding).
  - [*Creating a user*](#Creating).
  - [*Creating BICC and UCM roles*](#Creating2).
  - [*Configuring the UCM storage for BICC*](#Configur).

### Supported services

The following Oracle Fusion Cloud applications are supported:

- [Customer Experience](https://www.oracle.com/cx/)
- [Enterprise Resource Planning](https://www.oracle.com/erp/)
- [Supply Chain Management](https://www.oracle.com/scm/)
- [Human Capital Management](https://www.oracle.com/human-capital-management/)

### Finding the Server URL

The server URL is required to configure the UCM storage for BICC.

1. Log in to [Oracle Cloud](https://www.oracle.com/cloud/sign-in.html).
2. Navigate to Application Console. For more information, see [Use the Application Console](https://docs.oracle.com/en/cloud/paas/app-container-cloud/csjse/use-application-console.html#GUID-DFF3E1F8-B19B-45FE-99D9-2E41F6C15972) in the Oracle documentation.
3. Click your Oracle application instance in the Active Applications section. If you do not have an instance, see [Create an instance](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/csgsg/create-instance.html) in the Oracle documentation.
4. From the application instance details, copy and paste the Service Environment URL.

   For example, `https://servername.fa.us2.oraclecloud.com`.

### Creating a user

Information noteTo create a user, you need the Security Manager role.

Creating a user is required to get your username and password necessary for the connection.

1. Log in to the Oracle Fusion Cloud Application instance for which you want to sync the data.
2. From the left panel, click Tools > Security Console, then Users > Add User Account.
3. Navigate to the Application Console. For more information, see [Use the Application Console](https://docs.oracle.com/en/cloud/paas/app-container-cloud/csjse/use-application-console.html#GUID-DFF3E1F8-B19B-45FE-99D9-2E41F6C15972) in the Oracle documentation.
4. On the Add User Account page, enter the user details in the User information section.
5. Copy and paste your User Name and Password into a secured file.
6. Click Save and Close.

### Creating BICC and UCM roles

Information noteTo create roles, you need the Security Manager role.

For more information about Business Intelligence Cloud Connector (BICC), see [Overview of Business Intelligence Cloud Connector](https://docs.oracle.com/en/cloud/saas/applications-common/24c/biacc/overview-of-business-intelligence-cloud-connector.html) in the Oracle documentation.

1. Log in to the Oracle Fusion Cloud Application instance for which you want to sync the data.
2. From the left panel, click Tools > Security Console, then Roles.
3. In the top-right corner, click Create Role > Basic information and enter the role details.

   Connection settings

   | Field name | Description |
   | --- | --- |
   | Role Name | Enter the role name. Example: BICC\_QLIK\_ROLE, UCM\_QLIK\_ROLE |
   | Role Code | Enter the role code. Example: BICC\_ADMIN\_QLIK, UCM\_ADMIN\_QLIK |
   | Role Category | Enter BI - Abstract Role. |
   | Predefined | Clear the checkbox. |
   | Description | Enter a description for the role. This field is optional. |
4. Click Next.
5. Click Next to skip the Function Security Policies and Data Security Policies pages.
6. One the Role Hierarchy page, click Add Role.
7. In the Add Role Membership dialog box, search for the following roles:

   Connection settings

   | Roles | Description |
   | --- | --- |
   | ESS Administration Role | Creates and manages schedules for global data extracts or jobs. |
   | ORA\_ASM\_APPLICATION\_IMPLEMENTATION\_ADMIN\_ABSTRACT | Gets job information, describes data store, and performs other BICC related operations. |
   | OBIA\_EXTRACTTRANSFORMLOAD\_RWD | Views and downloads extracted files from UCM. |
8. Click Add Role Membership.
9. Close the dialog box and click Next.
10. Click Next to skip the Segregation of Duties page.
11. On the Users page, click Add User and enter the user created in [*Creating a user*](#Creating).
12. Click Next. You are on the Summary page.
13. Verify the details and click Save and Close.

### Configuring the UCM storage for BICC

To configure the UCM storage, you need the server URL and your username and password created in the previous procedures.

1. Using the server URL, launch the BI Applications Configuration Manager.

   For example, when the server URL is `https://my-oracle-fusion-cloud.oraclecloud.com`, use `https://my-oracle-fusion-cloud.oraclecloud.com/biacm`.
2. Log in using your username and password.
3. Click Configure External Storage on the right.
4. Select the UCM Connections tab and click Test UCM Connection. The External Storage Connection Succeeded window pops up.
5. Click OK to close the window.

You are all set. You can create the connection.

### Preventing file collisions

In order to prevent file collisions, the files are named in the UCM storage as follows: `file_datastore-name_schedule-id_timestamp`

For example: `file_fscmtopmodelam_analyticsserviceam_currenciestlpvo-batch1209716923-20150615_105514.zip`

### Optional settings

The following procedures are optional. They let you configure more settings that are not required to connect to Oracle Fusion.

#### Adding custom object to an offering

Tables that are not part of an offering are excluded from the sync.

Follow [Add a Datastore for an Offering](https://docs.oracle.com/en/cloud/saas/applications-common/24b/biacc/add-a-data-store-for-an-offering.html) in the Oracle documentation.

#### Selecting primary keys for custom objects

Tables with no defined primary keys are excluded from the sync.

You need the server URL and your username and password created in the previous procedures.

1. Using the server URL, launch the BI Applications Configuration Manager.

   For example, when the server URL is `https://my-oracle-fusion-cloud.oraclecloud.com`, use `https://my-oracle-fusion-cloud.oraclecloud.com/biacm`.
2. Log in using your username and password.
3. Click Manage Offerings and Data Stores on the right.
4. Navigate to the offering associated with the custom objects.
5. Select your custom data store, then the Edit Columns tab.
6. Select the checkbox of the corresponding objects in the Primary Key column.
7. Click Save.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Base URL | Base URL. |
| Username | Oracle Fusion user name. |
| Password | Oracle Fusion password. |
