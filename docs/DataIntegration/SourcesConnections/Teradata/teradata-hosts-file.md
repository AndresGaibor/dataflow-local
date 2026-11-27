---
title: "Editing the hosts file"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Teradata/teradata-hosts-file.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Teradata"]
---

# Editing the hosts file

The user who is working with the Teradata Database must be registered as a user in the Teradata Database. This is the user that is entered in the User name field in the connector definition. You must grant Teradata Database access to this user before configuring the database in Qlik Talend Cloud Data Integration.

To enable the Data Movement gateway to access the Teradata Database, add the Teradata Database machine IP address or hostname and the database mapping to the Windows or Linux hosts file.

To add the Teradata Database mapping to the hosts file:

1. Open the hosts file on the Data Movement gateway machine.

   On Windows, the default path is:

   C:\Windows\System32\drivers\etc\hosts

   On Linux, the default path is:

   /etc/hosts
2. Add the following line (note the cop1 suffix after the database name):

   <Teradata Database IP address/hostname> <Teradata Database name>cop1

   Example:

   123.123.123.1 teradatadbonecop1

   Information note

   Make sure the database name added to the hosts file matches the value in Default database.
3. Save the file.
