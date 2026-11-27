---
title: "ODBC (via Direct Access gateway)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ODBC-DrectAccess/ODBC.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# ODBC (via Direct Access gateway)

The ODBC  (via Direct Access gateway) connector allows you to access ODBC data stores that do not have an associated connector in Qlik Cloud. Connections can be configured by selecting ODBC (via Direct Access gateway) from the list of connectors in the Qlik Sense Add data connection or Data load editor dialogs.

Tip noteThe architecture, design, and technology stack of the ODBC (via Direct Access gateway) connector differ significantly from those of the legacy ODBC data source connections in Qlik Sense Client-Managed. As a result, the way fields are interpreted, typed, transformed, and optimized may vary. This can lead to differences in how fields behave, how they appear, and how quickly they load compared to the legacy connector. Consequently, direct comparisons between the two should be avoided.

Information note

- Requires Direct Access gateway 1.5.2 or later.
- Industry-accepted best practices must be followed when using or allowing access through the ODBC (via Direct Access gateway) connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.
- The ODBC (via Direct Access gateway) connector supports 64-bit Unicode (not ANSI) ODBC drivers based on ODBC 3.x standards only.
- MS Access requires Process Isolation to be enabled on the ODBC connector. For instructions, see [*Turning on process isolation or changing the number or concurrent reloads*](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm#Turning).
- When using Data Manager, ODBC drivers that cannot retrieve foreign keys from the database (for example, MS Access) are not supported.

## Unsupported or partially supported drivers

The following ODBC drivers are either not supported or
partially supported with the ODBC (via Direct Access gateway) connector:

- Oracle Instant Client
  - Not supported
- MongoDB Atlas SQL driver
  - Not supported
- MS Access ODBC driver - This driver is supported with process isolation only. To prevent errors when multiple users are trying to preview data or select tables concurrently, select the Metadata option in the process isolation settings.

  For more information on process isolation, see [Process isolation](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm#Process).

## Verifying the driver is installed

An ODBC driver for your ODBC data source
must be installed on the Qlik Data Gateway - Direct Access machine for Qlik Sense to be able to access your database. Best practice is to always install the latest driver. Please refer to the vendor's
documentation for download and installation instructions. You can verify which version is installed in the ODBC Data Source Administrator.

Tip noteThird-party ODBC drivers are supported on a best-effort basis.

To do this:

1. On the Direct Access gateway machine, open the ODBC Data Source Administrator by entering odbcad32.exe in the Type here to search box in the bottom left of your screen and pressing [Enter].
2. In the ODBC Data Source Administrator window (64-bit) dialog, select the Drivers tab and verify that the correct driver version is installed.

## Creating a System DSN

You can access your data source by specifying the System DSN or by selecting the driver and configuring a connection string. You can use the ODBC Data Source Administrator to create a System DSN if one does not exist for your data source.

Information noteUser DSNs are not supported.

### Before you begin

Obtain the following configuration information from your data source system administrator:

- The database server host name or IP address.
- The name of the database (and schema, if the database supports multiple schemas)
- A valid user name for accessing the system or data source
- A valid password for accessing the system or data source

### Procedure

To create a System DSN, do the following:

1. On the Direct Access gateway machine, open the ODBC Data Source Administrator by entering odbcad32.exe in the Type here to search box in the bottom left of your screen and pressing [Enter].
2. In the ODBC Data Source Administrator window (64-bit) dialog, select the System DSN tab.
3. Click Add.

   The Create New Data Source window opens.
4. Select your driver and click Finish.
5. In the Create a new Data Source to <you-data-source> wizard, configure the DSN and driver options.
6. Click Test DSN (the button name differs according to your data source) to attempt to establish a connection to your data source.
7. If the connection fails, review and correct your parameters and then try again.
8. Finish the data source configuration by closing any open configuration windows.

## Allowing only specific drivers and DSNs

When working with the ODBC (via Direct Access gateway) connector, you can allow only specific drivers and DSNs. For more information, see [Additional ODBC (via Direct Access gateway) connector settings](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm#Addition).

## Setting up custom SQL syntax

The default SQL syntax templates are stored in file C:\ProgramData\Qlik\Gateway\genericodbc\_database\_syntax.json. This file is created in C:\ProgramData\Qlik\Gateway the first time a connection using the ODBC (via Direct Access gateway) connector is established.

The SQL syntax templates are listed in the SQL syntax dropdown of the ODBC (via Direct Access gateway) connector dialog. You can edit an existing SQL syntax template or add new custom SQL syntax (that is supported by your ODBC driver), according to your needs.

To add custom SQL syntax:

1. On the Direct Access gateway machine, open C:\ProgramData\Qlik\Gateway\genericodbc\_database\_syntax.json as admin.

   Make a copy of the section:

   {
   "SyntaxId": "syntaxCustom",
   "DisplayName": "Custom SQL syntax",
   "DelimiterStart": null,
   "DelimiterEnd": null,
   "DataPreviewSelectTemplate": null,
   "DatabaseTerm": null,
   "OwnerTerm": null
   }
2. Replace the DisplayName value and the null values with your own custom values.
3. Save the file and restart the Qlik Data Gateway - Direct Access service.
