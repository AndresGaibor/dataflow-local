---
title: "IBM DB2 for iSeries"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-iseries/IBM4DB2-iseries-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# IBM DB2 for iSeries

This section explains how to set up an IBM DB2 for iSeries source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](prereq-idb2.htm), set up the [*Required permissions*](../../../../Global_Common/Content/SharedReplicateHDD/IBM4DB2-iseries/required_permissions_iseries.htm), and familiarized yourself with the [*Limitations and considerations*](../../../../Global_Common/Content/SharedReplicateHDD/IBM4DB2-iseries/iseries_limitations.htm).

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the IBM DB2 for iSeries source connector and then provide the following settings:

### Data source

- Data gateway

Select a Data Movement gateway to use for moving your data.

For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

- Server: The IP address or host name of the IBM DB2 for iSeries server.

### Account properties

- User name: The user name required to access the IBM DB2 for iSeries server.
- Password: The password required to access the IBM DB2 for iSeries server.

### Database properties

- Use table and schema system names: The IBM DB2 for iSeries
  source connector lands tables based on their SQL names (unlimited length). If your IBM
  DB2 for iSeries database does not use SQL names, it's likely that you'll want to keep the
  system names.
- Relative Record Number (RRN):
  See [*Adding the RRN Column to Target Tables*](#top) below.

### CDC properties

- Journal name: The name of the journal containing the source tables.

  See also: [*CDC prerequisites*](prereq-idb2.htm#CDC)
- Journal library: The name of the library where the journal is located.

  See also: [*CDC prerequisites*](prereq-idb2.htm#CDC)
- Skip journal validation when a task starts: From IBM DB2 for iSeries 7.3, Qlik Talend Data Integration automatically validates the specified journal. This involves checking that the journal exists and that it contains the tables selected for landing. When numerous tables are selected for landing, this process may take some time.
  In such cases, if you are sure that the specified journal exists and that it contains the correct tables, you may want to skip the validation phase.
- For information about the following options, see [*Using the R4I UDTF for Change Capture*](#Using) below:
  - Enable UDTF capturing
    - CDC reader UDTF name
    - UDTF result set size (MB)
- Check for changes every (sec): How often to check the source database for changes.

### Override CCSID mapping to code page

In the CCSID to character set mapping field enter the CCSID(s) and code page(s) in the following format (separated by commas with no spaces):

CCSID1,codepage1,CCSID2,codepage2,...

The Character set (code page) must be specified in the proper format (e.g. ibm-1148\_P100-1997). For a list of valid formats, see [the ICU Converter Explorer](http://demo.icu-project.org/icu-bin/convexp).

#### Converting to a custom code page

Perform the following procedure if the source datasets are defined with an incorrect CCSID and the correct definition is actually in a UCM file.

1. On the Data Movement gateway machine:

   1. If the ICU package is not installed, open a shell prompt and install the [ICU package](https://icu.unicode.org/home).
   2. Change the working directory to <product\_dir>/bin

      The default <product\_dir> is /opt/qlik/gateway/movement
   3. Create a mapping data file with the file extension **.ucm**.

      Information note

      If you edit an existing UCM file, you must also change the values of the <code\_set\_name> and <icu:alias> properties. If the file does not contain an <icu:alias> property, then you only need to change the value of the <code\_set\_name> property.
   4. Create a CNV file for the UCM file by running the following command:

      `makeconv -v <file_name>.ucm`

      Example:

      `makeconv -v 1047_EX.ucm`

      This will create a CNV file with the same name as the UCM file (for example, 1047\_EX.cnv).
   5. Create a new subfolder named icudt<XX>l under <product\_dir>/bin where the XX is the same as the number in the libicudata.so.<XX> file name.

      For example, If the shared object file name is libicudata.so.69, create a new subfolder named icudt69l.
   6. Copy the CNV file to the subfolder you just created (<product\_dir>/bin/icudt69l in the example above).
2. In the connector dialog's CCSID to character set mapping field, enter the original source CCSID number followed by the CNV file name without the extension.

   Example:

   1047,1047\_EX
3. On the Data Movement gateway machine, restart the Data Movement gateway service with the following command:

   sudo systemctl restart repagent

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.

## Adding the RRN Column to Target Tables

Source tables that do not have a primary key, a unique index, or a combination of columns that can be used as a unique index, must be registered using the relative record numbers (RRN).

Select one the following options:

- Add RRN column to target tables without a primary key or unique index. The RRN column will automatically become the primary key of the target table.
- Add RRN column to all target tables
- Do not add RNN column to target tables

To support DELETE operations in auto-commit mode for tables journaled with \*AFTER images, do the following:

1. Enable the Add RRN column to all target tables option.
2. Mark the new RRN column on the target as the table's sole Primary Key (using a transformation).

   Note that adding an RRN column without marking it as a Primary Key will result in the table being suspended if a DELETE operation is performed.

When you select one of the "Add RRN columns" options, both the Change Tables and the target tables will have an extra column, ATTREP\_RRN of type INTEGER, which contains a unique value for each row. This column contains the RRN that corresponds to each source table row.

Information note

The IBM DB2 for iSeries RRN values represent the exact position of the row in the file structure that holds the table data. When a table is reorganized, the table is rebuilt resulting in *new* RRNs being allocated to each row. Consequently, reorganization of tables where the RRN is being used as a target key should be avoided whenever possible. If such reorganization is unavoidable, you should immediately reload the reorganized table to prevent unpredictable behavior when changes are applied to the target (e.g. failed DELETEs, duplicate INSERTs, and so on).

## Using the R4I UDTF for Change Capture

By default, changes captured from IBM DB2 for iSeries are filtered on the Data Movement gateway machine using the standard display\_journal function. When there is a high volume of changes, this may impact Change Processing performance.

Installing the R4I UDTF on IBM DB2 for iSeries enables captured changes to be filtered on IBM DB2 for iSeries instead of on the Data Movement gateway machine, significantly improving CDC performance.

Warning noteThe R4I UDTF can capture up to 300 tables per task. If you need to capture more than 300 tables per task, do not use this option.

To set up change capture using the R4I UDTF:

1. Go to [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).
2. Select Qlik Data Integration.
3. Scroll down the Product list and select Replicate.
4. In the Download Link column, click the QlikReplicate\_\_R4I.zip link to start your download.
5. Install the R4I UDTF on the IBM DB2 for iSeries server.
6. Select the Enable UDTF capturing option.
7. If you changed the default CDC reader UDTF name during the R4I installation, specify the new name in the CDC reader UDTF name field.
8. In the UDTF result set size (MB) field, you can set the maximum size of the result-set buffer returned by the R4I UDTF.
   A larger result set will usually improve performance, but will also impact DB2 memory consumption. Therefore, If you want to increase the result-set size, best practice is to run the task in a test environment first as insufficient memory on DB2 might result in data inconsistency on the target (due to partial records being captured).
