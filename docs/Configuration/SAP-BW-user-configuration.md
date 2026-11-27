---
title: "SAP BW Connector user configuration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Configuration/SAP-BW-user-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector configuration"]
---

# SAP BW Connector user configuration

A user profile transport is supplied for Business Warehouse systems.

Authorizations are required to use the BW Connector. Qlik provides three roles that contain the necessary authorizations. You can assign different roles to different users, depending on need, or all roles can be assigned to one user:

- The QTQVCADMIN role is required for users who perform Qlik transactions in the SAP GUI.
- The QTQVCACCESS role is used by a connector back-end user who performs extraction jobs from Qlik.
- The QTQVCBWACCESS role is to be used by OLAP, DSO/ODS, and BW connectors back-end users for doing extraction jobs on an SAP BI/BW system.

After the transports have been installed in the system, create one or more users as needed. You can also assign the roles to existing users.

Do the following:

1. In the SAP system, go to transaction SU01.
2. Click Create (F8).
3. Give the new user a user a name and a password.
4. For an existing user, enter the User ID and click Change (Shift + F6).
5. On the Logon data tab, assign new users to User Type: Service.
6. On the Roles tab, add the desired roles.
7. Click Save.

If the installation is an upgrade from a previous version and the role QTQVCBWACCESS has been updated, update all users assigned to the role.

Do the following:

1. Go to transaction PFCG.
2. Enter the role name QTQVCBWACCESS.
3. Click Change Role.
4. On the User tab, enter the name of the user(s) created above.
5. Click User comparison.
6. Click Complete comparison.
7. Click Save.

This role is intended only for use in a Development environment. As part of the development process, you should create a more restricted role for the Production environment.
