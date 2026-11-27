---
title: "Include"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/Include.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---

# Include

The Include/Must\_Include variable specifies
a script that contains text that should be included in the script and evaluated as script code. It is not used to add data. You can store parts of your script code in a separate text file and reuse it in several applications. This is a user-defined variable.

Syntax:

$(Include=filename)

$(Include=script ID)

$(Must\_Include=filename)

$(Must\_Include=script ID)

There are two versions of the variable:

- Include does not generate an error if the script cannot be found, it will fail silently.
- Must\_Include generates an error if the script cannot be found.

If working with files, if you do not specify a path, the filename will be relative to the Qlik Sense application working directory. You can also specify an absolute file path, or a path to a lib:// folder connection. Do not put a space character before or after the equal sign. If working with other scripts, you can specify the script with by following script:// with the script ID.

Information noteThe construction set Include =filename is not applicable.

Examples:

$(Include=abc.txt);

$(Include=script://a01b2c34-5de6-789f-g0hi-1j2k3l45m6n7);

$(Must\_Include=lib://DataFiles/abc.txt);

## Permissions for inserting scripts

Multiple script formats can be inserted into your scripts. QVF and QVS formats are recommended and offer a graphical user interface to generate the Include statement syntax automatically.

Depending on the format of the script you are inserting, you require different permission levels for the script that you are inserting. These permissions may be required for using the graphical interface for script insertion, reloading scripts, or both.

Space permissions for inserted scripts

| Format of inserted script | Required role in space containing the inserted script |
| --- | --- |
| QVF (standalone script asset) | - Shared space: Can edit, Can edit data in applications, Can manage, or Owner - Managed space: Can operate, Can manage, or Owner |
| QVS or other text format | - Shared space: Can consume data, Can edit, Can edit data in applications, Can manage, or Owner - Managed space: Can consume data, Can operate, Can manage, or Owner |

## Limitations

### Limited cross-compatibility between UTF-8 encoded files under Windows versus Linux.

It is optional to use UTF-8 with BOM (Byte Order Mark). BOM can interfere with the use of UTF-8 in software that does not expect non-ASCII bytes at the start of a file, but that could otherwise handle the text stream.

- Windows systems use BOM in UTF-8 to identify that a file is UTF-8 encoded, despite the fact that there is no ambiguity in the byte storage.
- Unix/Linux use UTF-8 for Unicode, but does not use the BOM as this interferes with the syntax for command files.

This has some implications for Qlik Sense.

- In Windows any file that begins with an UTF-8 BOM is considered a UTF-8 script file. Otherwise ANSI encoding is assumed.
- In Linux, the system default 8 bit code page is UTF-8. This is why the UTF-8 works although it does not contain a BOM.

As a result, portability cannot be guaranteed. It is not always possible to create a file on Windows that can be interpreted by Linux and vice versa. There is no cross compatibility between the two systems regarding UTF-8 encoded files due to different handling of the BOM.

For more information, see [Byte order mark](https://en.wikipedia.org/wiki/Byte_order_mark)

## Inserting QVS code from spaces in Qlik Cloud Analytics

In Qlik Cloud Analytics, when loading data from a data file within a load script, you can use a LOAD statement or insert QVS code. In both cases, hierarchical space folder structures can be referenced in your script statement. Follow the rules for [valid space folder paths](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#PathRules). Additionally, the file and all referenced folders need to already exist in the specified location. Otherwise, the reload fails.

Example: Referencing QVS file at the top-level path of a space

In this example, the file test.qvs is referenced in the load script. The file is located in the space TeamSharedSpace. The file is not located within any specific folder, but instead is located at the top-level path in the space.

```
$(Must_Include=lib://TeamSharedSpace:DataFiles/test.qvs)
```

Example: Referencing QVS file in a specific folder path within a space

In this example, the file test.qvs is referenced in the load script. The file is located in the folder SalesData within the space TeamSharedSpace.

```
$(Must_Include=lib://TeamSharedSpace:DataFiles/SalesData/test.qvs)
```

For more information about referencing space folder structure in load scripts, see [*Referencing space folder structure in application and script development*](../../Spaces/manage-data-files-spaces.htm#FolderStructureRefExamples).
