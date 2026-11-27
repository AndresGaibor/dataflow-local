---
title: "Working with InfoProviders using a SAP BW connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Clients/Working-with-InfoProviders.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector clients", "Using the SAP BW Connector"]
---

# Working with InfoProviders using a SAP BW connection

You can connect to five types of InfoProviders in SAP BW:

- InfoCube (CUBE)
- MultiProvider (MPRO)
- DataStore Object (Advance) (ADSO)
- CompositeProvider (HCPR)
- Open ODS View (FBPA)

The connector extracts the characteristic key values and the measures that constitute the InfoProvider. Data is extracted in packages, and there is no limit to the amount of data that can be extracted at one time.

The connector adds RowNum as a row-number counter to the fields that can be selected by the connector. In addition to counting the rows (starting at 1), the RowNum counter ensures that the extracted rows are unique.

The functionality resembles the functionality of the transaction LISTCUBE in SAP BW or the Display Data functionality in SAP BW and HANA Studio. Fields or InfoObjects that are not extractable through these interfaces will not be extractable either.

## Select and load data

Once a connection to an SAP InfoProvider has been established, you can select data and load it into a Qlik Sense application.

Do the following:

1. Select the SAP BW Connector from the list of data connections.
2. Define the extraction parameters for the desired  InfoProvider.
3. Select Load texts to load the Text Table of the InfoObjects.

   When this property is selected, a script for loading the Text Table of the InfoObjects included in the InfoProvider is created. All available text fields of an InfoObject are included in the generated script and the fields are named:

   - <InfoObject Name>\_TEXT\_SH (for short texts)
   - <InfoObject Name>\_TEXT\_MD (for medium-length texts)
   - <InfoObject Name>\_TEXT\_LG (for long texts)

   If an InfoObject is configured to have text but no text has been loaded to the InfoObject in SAP BW, the script for that InfoProvider will be commented.
4. Select Load attributes to load the Attribute View of the InfoObjects.

   When this property is selected, a script for loading the Attribute View of the InfoObjects included in the InfoProvider is created. No check is performed to verify that Attribute data has been loaded in SAP BW. All available Attribute fields of an InfoObject are included in the generated script, and the name of the fields is <InfoObject Name>\_<Attribute Name>.

   Information noteTime-dependent Texts and Attributes are extracted with a condition to extract the current value of the text or attribute. The condition has the form DATEFROM <= SY-DATUM AND DATETO >= SY-DATUM.
5. Select Show friendly names if you want to see descriptions.
6. Select Provider Types.

   You can connect to five types of InfoProviders in SAP BW:

   - InfoCube (CUBE)
   - MultiProvider (MPRO)
   - DataStore Object (Advance) (ADSO)
   - CompositeProvider (HCPR)
   - Open ODS View (FBPA)

   You can select multiple provider types.
7. Select BW Objects. Select the InfoProviders whose data you want to load.

   You can filter the InfoProviders list using the search field ![Search](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/Icons/ic_search.svg) above the list. Select one InfoProvider at a time. If you intend to load data from more than one InfoProvider, you must complete the selection from the first InfoProvider and then reopen the data selection dialog to select data from the next InfoProvider.

   Clicking on the InfoProvider name causes all of its fields to be displayed.
8. Select Include LOAD statement, if not already checked, to create a LOAD statement before the SELECT statement.

   The LOAD statement before the SELECT statement allows the LOAD statement to use the SELECT statements as input. Basically, it is a LOAD statement that loads from the LOAD or SELECT statement below, without specifying a source qualifier, such as From or Resident, as you would normally. You can stack any number of LOAD statements this way. The statement at the bottom will be evaluated first, then the statement above, and so on until the top statement has been evaluated. Another advantage of the LOAD preceding SELECT is that you can keep a calculation in one place and reuse it in LOAD statements placed above. For example, when you load data from a database using a SELECT statement, you cannot use Qlik Sense functions to interpret data in the SELECT statement. The solution is to add a LOAD statement and perform data transformations above the SELECT statement.

   The LOAD statement created in the script panel is a simple load.
9. Select Metadata.

   Information noteIt is recommended to start the extraction configuration with the Metadata selection and the Conditions definition. For very large queries, you may want to set some granular filters through conditions before accessing the Preview window.
10. Select the fields whose data you want to load.

    You can filter the fields shown by using the search field ![Search](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/Icons/ic_search.svg) above the list of fields. When selecting fields, you can click the Metadata button to see which fields are primary key fields.
11. Select Conditions. You can also set conditions for each field by clicking ![Expression](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/Icons/ic_expression.svg). Conditions are set to include by default, but the Exclude option can be selected to use the condition for excluding rather than including values. The available conditions are:

    - Equals
    - Greater than or equal to
    - Less than or equal to
    - Greater than
    - Less than
    - Not equal to
    - Between

    The drop-down list of values in the Conditions for field dialog is populated with a maximum of 10,000 characteristic values. If the value you want to enter is not in the list of the first 10,000 rows, you can still enter the value manually in the entry field to the left of the drop-down list.

    Information noteThe InfoProvider Connector adds RowNum as a row-number counter to the fields that can be selected by the connector. In addition to counting the rows (starting at 1), the RowNum counter ensures that the extracted rows are unique. If RowNum is excluded from the selection, the output will not be handled correctly in Qlik Sense or QlikView. To calculate Sales Quantity per 0CALYEAR, the measure would have to be aggregated in Qlik Sense and QlikView.
12. Select Preview. Based on your configuration under Conditions the connector will try to fetch a preview for the desired InfoProvider. The preview will consist of 50 rows and will include the total number of rows.
13. Select Script Preview. This shows the load script built from the selections made.
14. Select Insert Script to load the data.

## Restrict access

The SAP connector roles contain the authorization objects that are checked when using the connectors. Authorization objects may be checked both in the SAP connector code and in standard SAP code called from the Qlik code. It is not necessary to import and use the Qlik roles. You can create your own authorizations, as well as copy or modify the Qlik roles.

### Role QTQVCBWACCESS

The role QTQVCBWACCESS is used for extraction jobs from SAP BI/BW system from Qlik. It is used with BEx query, InfoProvider, DSO and OLAP.

The role QTQVCBWACCESS contains authorization objects that can be used to restrict which InfoProviders a user can access. If users should have different access, update the authorization objects in copies of the role QTQVCBWACCESS and assign the relevant copy to each user. It is suggested that you copy the role QTQVCBWACCESS and use the copy. If the role QTQVCBWACCESS is updated in a future connector release, InfoProvider authorizations in that role will be overwritten.

The default behavior in the Qlik role QTQVCBWACCESS is to allow the usage of all InfoProviders.

### How to restrict usage for all types of InfoProviders

There are five different authorization objects in role QTQVCBWACCESS, which can be used to restrict usage of different types of InfoProviders. Each authorization object is described in the table below:

Authorization objects

| Authorization object | Description | Field | Value | Comment |
| --- | --- | --- | --- | --- |
| S\_RS\_ADSO | Defines access to Advanced DataStore objects. | RSOADSONM (Advanced DataStore object) | If set to \* then all DataStore objects are allowed. | Replace \* in the Value field with a list of Advanced DataStore objects that the user can access. |
| S\_RS\_HCPR | Defines access to HANA CompositeProviders. | RSHCPR (HANA CompositeProvider) | If set to \* then all HANA CompositeProviders are allowed. | Replace \* in the Value field with a list of HANA CompositeProviders that the user can access. |
| S\_RS\_ICUBE | Defines access to InfoCubes. | RSINFOCUBE (InfoCube) | If set to \* then all InfoCubes are allowed. | Replace \* in the Value field with a list of InfoCubes that the user can access. |
| S\_RS\_MPRO | Defines access to MultiProviders. | RSMPRO (MultiProvider) | If set to \* then all MultiProviders are allowed. | Replace \* in the Value field with a list of MultiProviders that the user can access. |
| S\_RS\_ODSV | Defines access to Open ODS Views. | RSFBPNAME (Open ODS View) | If set to \* then all Open ODS Views are allowed. | Replace \* in the Value field with a list of Open ODS Views that the user can access. |

The following example shows the default setup for the authorization object S\_RS\_ICUBE (InfoCube). In this setup the \* after InfoCube indicates that all InfoCubes are allowed access:

![Example infocube setup with an asterisk in the InfoCube field](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_setup-SAP-infocubeexample1.png)

Replacing \* with a list of the InfoCubes, restricts access to the InfoCubes listed:

![Example InfoCube setup with a list of InfoCubes in the InfoCube field](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_setup-SAP-infocubeexample2.png)

After listing the allowed InfoCubes, save, generate, and assign the role used to the SAP user ID. Use the SAP transaction PFCG to display and maintain authorization objects in a role.

## Limitations and workarounds

To extract ADSOs, CompositeProviders, and Open ODS Views, the SAP BW system needs to be at least on basis level 7.4 SP9 and the database needs to be HANA. Cubes and MultiProviders are supported from basis level 7.0 and any database.

### InfoCube (CUBE)

The Qlik SAP InfoProvider Connector does not connect semantically partitioned cubes. Copies of the cube are generated, and it is those generated cubes that appear in the list of InfoProviders in the selection dialog.

### MultiProvider (MPRO)

MultiProviders that have VirtualProviders as part providers are not supported by the connector.

### DataStore Object (Advanced) (ADSO)

Only the fields that are available for reporting can be extracted by the connector. For more information, see SAP Note 2185212. To extract fields that are not available for reporting, use the Qlik SAP SQL Connector and extract the Active Table of the ADSO. The table name is /BI0/A<Name\_of\_ADSO>1 or /BIC/A<Name\_od\_ADSO>1.

### CompositeProvider (HCPR)

Only Central CompositeProviders (Object type HCPR) are supported. Local and Ad-Hoc CompositeProviders (Object type COPR) are not supported by the connector. For CompositeProviders with ambiguous joins, there is a risk that the extracted key figure values will be incorrect. For more information see SAP Note 2372430. You can extract the data through a BW query using the Qlik SAP BW Connector instead.

### Open ODS View (FBPA)

Open ODS Views build on SAP BW DataSources are not supported.

Conditions on fields that use System-Wide Unique Name will cause preview and reload to fail. You can manually change the script and replace the field name in the WHERE clause with the System-Wide Unique Name of the same field.
