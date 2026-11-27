---
title: "Configuring SSO for the Cloudera Impala connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ClouderaImpala/Configure-Cloudera-for-SSO.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Cloudera Impala"]
---

# Configuring SSO for the Cloudera Impala connector

With a single sign-on (SSO) solution, you can minimize the number of times a user has to log on to access apps and websites.

Information noteWhen using Qlik Cloud Analytics, this section is only relevant if you are using Direct Access gateway 1.7.13 or later and have selected the Single Sign-On authentication mechanism.

When you set up Cloudera Impala as a data source, you can configure Cloudera Impala for SSO. You store the Direct Access gateway user credentials and define a trusted relationship so that the system passes the Direct Access gateway credentials to Cloudera Impala.

To configure SSO for Cloudera Impala, you must:

- Create the Cloudera Manager Principal.
- Set up a "Kerberized" Cloudera cluster.
- Install and configure Ranger.
- Test the configuration.

## Creating the Cloudera Manager Principal

Do the following:

1. Create an Organizational Unit (OU) in your Active Directory setup where all the principals used by your CDH cluster will reside.
2. Add a new user account to Active Directory to be used as the Cloudera Manager Principal.

   The password should be set to never expire.
3. Use Active Directory's Delegate Control wizard to allow this new user to Create, delete, and manage user accounts.

## Setting up a "Kerberized" Cloudera cluster

Do the following:

1. Use the Cloudera Kerberos wizard to set up Kerberos authentication for the Cloudera cluster running Impala.
2. Configure the cluster so that the generic Cloudera Impala ODBC driver can connect using Kerberos principal authentication and can delegate connection to other users.

See the Cloudera documentation for details: [Cloudera documentation](http://www.cloudera.com/documentation/enterprise/5-16-x/topics/cm_sg_s4_kerb_wizard.html)

## Install and configure Ranger

Ranger must be used for authorization.

Do the following:

1. Install and configure the Ranger package.
2. Verify that the Ranger service has been added to the Cloudera cluster.
3. Configure Cloudera Impala to use Ranger.

[Ranger documentation](https://ranger.apache.org/index.html)

## Testing the configuration

On the system where Direct Access gateway is installed, create a connection to Cloudera Impala using the generic Cloudera ODBC driver.

If the connection works with the generic Cloudera ODBC driver, then connections made with the Cloudera Impala Connector in the ODBC Connector Package will also work.
