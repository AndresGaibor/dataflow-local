---
title: "Configuring SSO for the Apache Hive connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ApacheHive/Configure-Apache-hive-for-SSO.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Apache Hive"]
---

# Configuring SSO for the Apache Hive connector

Information noteWhen using Qlik Cloud Analytics, this section is only relevant if you are using Direct Access gateway 1.7.13 or later and have selected the Single Sign-On authentication mechanism.

With a single sign-on (SSO) solution, you can minimize the number of times a user has to log on to access apps and websites.

When you set up Apache Hive as a data source, you can configure Apache Hive for SSO. You store the Direct Access gateway user credentials and define a trusted relationship so that the system passes the Direct Access gateway credentials to Apache Hive.

To configure SSO for Apache Hive, you must:

- Create the Apache Hive Manager Principal.
- Set up a "Kerberized" hadoop cluster.
- Install and configure Sentry or Ranger for authorization.
- Test the configuration.

## Creating the Apache Hive Manager Principal

Do the following:

1. Create an Organizational Unit (OU) in your Active Directory setup where all the principals used by your CDH cluster will reside.
2. Add a new user account to Active Directory to be used as the Hive Manager Principal.

   The password should be set to never expire.
3. Use Active Directory's Delegate Control wizard to allow this new user to Create, delete, and manage user accounts.

## Setting up a "Kerberized" hadoop cluster

Do the following:

1. Use the Cloudera or Hortonworks Kerberos wizard to set up Kerberos authorization for the hadoop cluster.
2. Configure authorization on the cluster to allow the generic Apache Hive ODBC driver can connect using Kerberos authentication which can delegate connections to other users.

See the Apache Hive documentation for details: [Apache Hive documentation](https://cwiki.apache.org/confluence/display/Hive/Home#Home-HiveDocumentation)

## Install and configure Sentry or Ranger

Sentry or Ranger (for Cloudera) must be used for authorization.

Sentry and Ranger perform authorization, which different than authentication in hadoop.

- Authentication is the process of determining if someone is who they claim to be.
- Authorization is the function of specifying access rights to resources.

Authentication determines who the user is, and authorization determines what the user can do.

Do the following:

1. Install and configure the Sentry or Ranger package.
2. Verify that the Sentry or Ranger service has been added to the cluster.
3. Configure Apache Hive to use Sentry or Ranger.

[Sentry documentation](https://cwiki.apache.org/confluence/display/SENTRY/Sentry+Tutorial)

[Ranger documentation](https://docs.cloudera.com/HDPDocuments/HDP3/HDP-3.1.0/installing-ranger/content/installing_ranger_using_ambari.html)

## Testing the configuration

On the system where Direct Access gateway is installed, create a connection to Apache Hive using the generic Apache Hive ODBC driver.

If the connection works with the generic Apache Hive ODBC driver, then connections made with the Apache Hive Connector in the ODBC Connector Package will also work.
