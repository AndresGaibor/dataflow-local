---
title: "Loading new and updated records with incremental load"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/use-QVD-files-incremental-load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---

# Loading new and updated records with incremental load

If your application contains a large amount of data from database sources that are continuously updated, reloading the entire data set can be time consuming. In this case, you want to load new or changed records from the database. All other data should already be available in the application. Incremental load using [QVD](#glossary-1 "Glossary term") files, makes it possible to achieve this.

The basic process is described below:

1. Load new or updated
   data from the database source table.

   This is a slow process, but only a limited
   number of records are loaded.
2. Load
   data that is already available in the application from the QVD file.

   Many records are loaded, but this is a much faster process.
3. Create a new QVD file.

   This is the file you will use the next time you do an incremental load.
4. Repeat the procedure for every table loaded.

The following examples show cases where incremental load is used. However, a more complex solution might be necessary, depending on the source database structure and mode of operation.

- Insert only (no update or delete)
- Insert and update (no delete)
- Insert, update and delete

You can read QVD files in either optimized mode or standard mode. (The method employed is automatically selected
by the Qlik Sense engine depending on the complexity of the operation.)
Optimized mode is about 10 times faster than standard mode, or about 100 times faster than loading the database
in the ordinary fashion.

For more information, see [*Working with QVD files*](../Scripting/work-with-QVD-files.htm).

## Insert only (no update or delete)

If the data resides in a database other than a simple log file, the append approach will not work. However, the problem can still be solved with
a minimum amount of extra work. The following conditions apply:

- The data source can be any database.
- Qlik Sense loads records inserted
  in the database after the last script execution.
- A ModificationTime [field](#glossary-2 "Glossary term") (or similar)
  is required for Qlik Sense to recognize which records are new.

Example:

QV\_Table:

SQL SELECT PrimaryKey,
X, Y FROM DB\_TABLE

WHERE ModificationTime
>= #$(LastExecTime)#

AND ModificationTime <
#$(BeginningThisExecTime)#;

Concatenate LOAD PrimaryKey, X, Y FROM [lib://DataFiles/File.QVD];

STORE QV\_Table INTO [lib://DataFiles/File.QVD];

The hash signs in the SQL WHERE clause define the beginning and end of a date. Check your database manual for the correct date syntax for your database.

## Insert and update (no delete)

The next case is applicable when data in previously loaded records may
have changed between script executions. The following conditions apply:

- The data source can be any database.
- Qlik Sense loads records inserted
  into the database or updated in the database after the last script execution.
- A ModificationTime field (or similar)
  is required for Qlik Sense to recognize which records are new.
- A primary key field is required
  for Qlik Sense to sort out updated records from the QVD file.
- This solution will force the reading
  of the QVD file to standard mode (rather than optimized), which is still considerably faster than loading the entire
  database.

Example:

QV\_Table:

SQL SELECT PrimaryKey,
X, Y FROM DB\_TABLE

WHERE ModificationTime
>= #$(LastExecTime)#;

Concatenate LOAD PrimaryKey,
X, Y FROM [lib://DataFiles/File.QVD]

WHERE NOT Exists(PrimaryKey);

STORE QV\_Table INTO [lib://DataFiles/File.QVD];

## Insert, update and delete

The most difficult case to handle is when records are actually deleted
from the source database between script executions. The following conditions
apply:

- The data source can be any database.
- Qlik Sense loads records inserted
  into the database or updated in the database after the last script execution.
- Qlik Sense removes records deleted
  from the database after the last script execution.
- A field ModificationTime (or similar)
  is required for Qlik Sense to recognize which records are new.
- A primary key field is required
  for Qlik Sense to sort out updated records from the QVD file.
- This solution will force the reading
  of the QVD file to standard mode (rather than optimized), which is still considerably faster than loading the entire database.

Example:

Let ThisExecTime = Now(
);

QV\_Table:

SQL SELECT PrimaryKey,
X, Y FROM DB\_TABLE

WHERE ModificationTime
>= #$(LastExecTime)#

AND ModificationTime <
#$(ThisExecTime)#;

Concatenate LOAD PrimaryKey,
X, Y FROM [lib://DataFiles/File.QVD]

WHERE NOT EXISTS(PrimaryKey);

Inner Join SQL SELECT
PrimaryKey FROM DB\_TABLE;

If ScriptErrorCount =
0 then

STORE QV\_Table INTO [lib://DataFiles/File.QVD];

Let LastExecTime = ThisExecTime;

End If

Related learning:

- [How do I process current records using incremental load?](/lnk/How_process_current_records_incremental_load)
