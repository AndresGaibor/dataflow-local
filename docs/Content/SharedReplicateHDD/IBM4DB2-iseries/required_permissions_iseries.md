---
title: "Required permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/IBM4DB2-iseries/required_permissions_iseries.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for iSeries"]
---

# Required permissions

The following permissions must be granted to the user specified in the General tab of the IBM DB2 for iSeries connector settings:

- USER CLASS = \*USER (default value)
- Special authority = \*NONE
- Full Load: Read permissions for the source tables.
- CDC: Read permissions for the journal defined for the IBM DB2 for iSeries connector and for the task's source tables.
- SELECT permission on the following tables:

  - QSYS2.SYSCOLUMNS
  - QSYS2.SYSTABLES

You must also set the following Authorities and Locks for the IBM DB2 for iSeries database:

- Journal Authority: \*USE
- Journal Library Authority: \*EXECUTE
- Journal Receivers Authority: \*USE
- Journal Receivers Library's Authority: \*EXECUTE
- File Authority (if specified): \*USE
- File Library Authority: \*EXECUTE
- Journal Lock: \*SHRRD
- Journal Receiver Lock: \*SHRRD
- File Lock (if specified): \*SHRRD

\*OBJEXIST is also required for the journal authority if any of the following are true:

- \*ALLFILE has been specified for the file key.
- Specified object does not exist on the system.
- \*IGNFILSLT or \*IGNOBJSLT is specified for the journal code selection value for any selected journal codes.

## DB2 server configuration

In rare situations, the following error might be encountered when using the IBM DB2 for iSeries endpoint in a moving task:

SQL0666N SQL query exceeds specified time limit or storage limit

To prevent this error from occurring, set the following attributes for the Qlik Talend Data Integration Job/UserID(s):

QRYSTGLMT=\*NOMAX

QRYTIMLMT=\*NOMAX

For more information, see <https://www.ibm.com/docs/en/i/7.4?topic=ssw_ibm_i_74/cl/chgqrya.htm>
