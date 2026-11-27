---
title: "SAP SQL  Connector user configuration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Configuration/SAP-SQL-user-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector configuration"]
---

# SAP SQL Connector user configuration

Create one or more SAP users that will be used for back-end jobs from Qlik and administrative tasks in SAP. These users are not intended for Qlik end-users so only a few SAP users should be created. Creating several users provides traceability, and you can give the users different authorizations.

Authorizations are required to use the SQL Connector. Qlik provides two roles that contain the necessary authorizations. You can assign different roles to different users, depending on need, or both roles can be assigned to one user.

The QTQVCADMIN role is required for users who perform Qlik transactions in the SAP GUI.

The QTQVCACCESS role is used by a connector back-end user who performs extraction jobs from Qlik.

## Configuring users

After the transports have been installed in the system, create one or more users as needed. You can also assign the roles to existing users.

Do the following:

1. In the SAP system, go to transaction SU01.
2. Click Create (F8).
3. Give the new user a user a name and a password.
4. For an existing user, enter the User ID and click Change (Shift + F6).
5. On the Logon data tab, assign new users to User Type: Service.
6. On the Roles tab, add the desired roles.
7. Click Save.

If the installation is an upgrade from a previous version and the role QTQVCACCESS has been updated, update all users assigned to the role:

1. Go to transaction PFCG.
2. Enter the role name QTQVCACCESS and click Change Role.
3. On the User tab, enter the name of the user(s) created above.
4. Click User comparison.
5. Click Complete comparison.
6. Click Save.

## Testing SQL statements

The /n/QTQVC/SQL transaction allows testing of SQL SELECT statements. After installing the transports and creating a user, test that everything has been correctly installed.

Do the following:

1. Log on with the newly created user and test transaction /n/QTQVC/SQL.

   ![Test of SQL Statements dialog](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_Testing-statements2.png)
2. Enter the SQL statement.
3. Click Open Stream to start the job.

Then either:

1. Click Fetch Stream to display one page of the result. Click Close Stream to end the job.

   or:
2. Click all Data to execute the complete job and get the run-time statistics.
