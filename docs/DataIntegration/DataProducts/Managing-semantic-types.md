---
title: "Managing semantic types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Managing-semantic-types.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog", "Assessing data quality"]
---

# Managing semantic types

The semantic type of a field corresponds to the data type that can be found in it, such as names, ZIP codes, or phone numbers.

Semantic types help you enhance the data quality of your datasets. The more your data are valid against the assigned semantic type, the better the quality is.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

Information noteYou need the permission to manage semantic types.

A semantic type is automatically assigned to each field of your datasets. Some semantic types are predefined and available by default. For more information, see [Predefined semantic types](#Predefined-types).

If the predefined types do not fulfill your requirements, you can create your own semantic types:

- Dictionary: The data must be conform to the values from the dictionary. For more information, see [Creating a dictionary-based semantic type](#Creating-dictionary-based).
- Pattern: The data must be conform to a regular expression. For more information, see [Creating a pattern-based semantic type](#Creating-pattern-based).
- Compound: The data must be conform to the values from different semantic types that form the compound semantic type. For more information, see [Creating a compound semantic type](#Creating-compound).

To enhance the data quality of your datasets, the semantic types can be included in the data quality computation. For more information, see [Using the semantic types for validation](#Validation).

Information noteYou can save up to 20MB of semantic types per tenant.

## Semantic types discovery

The data discovery calculates how many values in a field match each semantic type and, if the result is greater than 40%, it assigns the semantic type to the field.

The score is displayed in the right panel when assigning a semantic type. For more information, see [Assigning another semantic type](#Assigning-semantic-type).

### How is the percentage calculated?

This percentage is the sum of two percentages:

- One percentage represents the number of values matching the semantic type; up to 100% allocated. To determine if a value matches a semantic type, the data discovery depends on the type of the semantic type:

  - Dictionary: Does the value match a value from the dictionary? Punctuation, case, spaces, and accents are ignored.
  - Pattern: Does the value match the regular expression? The case is ignored but the accents are not.
  - Compound: is the value discovered into at least one child?

    A compound type is a group of existing semantic types, called children.

    Only active children are considered. If you deactivate a child, the compound type ignores it during discovery.

  If the answer is positive, the value is considered valid.
- The other percentage represents the similarity between the field name and the name of the semantic type; up to 10% allocated.

  To compare the names:

  - The Levenshtein algorithm is used. It calculates the minimum number of edits (insertion, deletion, or substitution) required to transform one string into another.
  - The case and accents are ignored.
  - If the strings contain spaces, the word order is ignored. For example, US Phone and Phone US are considered identical.

  The maximum percentage is 100%. If all values match a semantic type and the field name is identical to the name of the semantic type, the result still is 100%.

### Data types discovery

Instead of semantic types, native data types can also be assigned. If no semantic type obtains more than 40%, the data discovery automatically assigns a data type.

To determine of which type is a value, the data discovery follows an order:

1. Is the value empty?
2. Is the value of type Boolean? true and false are the only values considered of type Boolean.
3. Is the value of type integer?
4. Is the value of type decimal?
5. Is the value of type date?
6. If the value is not of one of the above types, it is considered a text value.

As the verification is incremental, a value is only of one type. For example, the value 5 is of type integer. It will not be considered of type text.

## Assessing the values

You can see the percentage of invalid, empty, and valid values in the quality bar of each field. The percentage is calculated on all data of the field, not on the sample only.

Information noteThe quality bar includes the results for the semantic types and the validation rules. For more information, see [Working with validation rules](Working-with-validation-rules.htm).

1. Open the dataset.
2. Select the Data Preview tab.
3. To display the percentage, hover over a color in the quality bar.
   You can see up to three colors from left to right:- Red: Invalid values. This includes not executable values from rules.
   - Black: Empty or null values.
   - Green: Valid values. This includes not applicable values from rules.![Quality bar of a field.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data-products-quality-bar.png)
4. For more details about each color, click it. The right panel opens and you can see the semantic type and the percentage for the validation rules.

The invalid values are marked with a red bar on the left.

![Invalid value marked in red.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data-products-invalid-value.png)

For more details about the error, click the red bar. The error may come from a validation rule, the semantic type, or both.

## Activating and deactivating a semantic type

When you do not want a semantic type to be assigned to any field, you can deactivate it. Some semantic types are deactivated by default.

You can activate and deactivate semantic types at any time.

When you deactivate a semantic type, it is no longer available for discovery, manual assignment, or validation rules. If the type is already assigned to a field, refresh the dataset to apply the change. Compound types also ignore deactivated children.

1. Before you deactivate a semantic type, check if it is used in datasets. For more information, see [Is the semantic type being used?](#semantic-type-used-in).

   After you deactivated the semantic type, you need to refresh the datasets in which it was used.
2. Open Data quality. You are in the Semantic types tab.
3. From the list, click the semantic type or ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png).
4. Click Edit. The Edit semantic type window is open.
5. Either:

- Click Activate at the top of the window.
- Click Deactivate in the bottom-left corner of the window.

  The semantic type is deactivated and marked as such in the Semantic types tab.

  ![Deactivated from the semantic types tab](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/semantic-types-deactivated.png)

  If the semantic type is used in datasets, a message is displayed in the field.

  !['Missing semantic type' message](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/semantic-types-missing.png)

  To assign another semantic type, see [Assigning another semantic type](#Assigning-semantic-type).

## Assigning another semantic type

The semantic types are automatically assigned to fields but you can assign another one.

1. Open the dataset.
2. Select the Data Preview tab.
3. Click the field you want to update.
4. In the right panel, click the Edit icon of the Data type section.

   ![Edit icon of Data type section in the right panel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qcdi-edit-icon-right-panel.png)
5. Search for the semantic type you want to assign to the field and click it.

   To help you choose the best semantic type for the field, each semantic type has a score in percentage. It represents the values of the sample that are valid against the semantic type. If you have the update permission, you can update the scores by clicking Refresh in the right panel.

   To create a semantic type and automatically assign it to the field, click Create from field. For more information, see [Creating a semantic type from a field](#Creating-from-field).
6. Click Refresh above the right panel to apply your changes.

## Creating a dictionary-based semantic type

You can create a semantic type based on a closed dictionary. You define each value to which your data must correspond.

Information noteThe maximum size of a dictionary-based semantic type is 10MB.

1. Open Data quality. You are in the Semantic types tab.
2. If you have no semantic types, click Add. Otherwise, click Create semantic type.
3. Enter a name.
4. Enter a description. This is optional but recommended to describe the purpose of the semantic type.
5. If you want the semantic types to be included in the quality computation, turn on the toggle Use for validation.
6. Select Dictionary.
7. Enter the values or import a text file by clicking ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png).
8. To automatically open the semantic type when it has been created, select the Open semantic type check box.
9. Click Create. The semantic type is created.
10. To assign the new semantic type to fields that match it, go to Catalog, open a dataset and click Compute or Refresh.

## Creating a pattern-based semantic type

You can create a semantic type based on a regular expression.

1. Open Data quality. You are in the Semantic types tab.
2. If you have no semantic types, click Add. Otherwise, click Create semantic type.
3. Enter a name.
4. Enter a description. This is optional but recommended to describe the purpose of the semantic type.
5. If you want the semantic types to be included in the quality computation, turn on the toggle Use for validation.
6. Select Pattern.
7. Enter or paste the regular expression. The maximum length is 350 characters.

   For security reasons, a few regular expressions cannot be used, especially the backreferences. For more information, see the [RE2/J documentation](https://github.com/google/re2j).
8. To automatically open the semantic type when it has been created, select the Open semantic type check box.
9. Click Create. The semantic type is created.
10. To assign the new semantic type to fields that match it, go to Catalog, open a dataset and click Compute or Refresh.

## Creating a compound semantic type

You can create a group of semantic types. For example, if the datasets contains customers all around the world, you can create a compound semantic type to group all Postal code semantic types.

Information noteYou can create compound semantic types from dictionary or pattern semantic types. A compound semantic type cannot contain other compound semantic types.

1. Open Data quality. You are in the Semantic types tab.
2. If you have no semantic types, click Add. Otherwise, click Create semantic type.
3. Enter a name.
4. Enter a description. This is optional but recommended to describe the purpose of the semantic type.
5. If you want the semantic types to be included in the quality computation, turn on the toggle Use for validation.
6. Select Compound.
7. Select the semantic types to be added from the drop-down list.

   When Use for validation is turned on, you can only select semantic types that are also used for validation. If you cannot find a semantic type in the list, make sure that Use for validation is turned on.
8. To automatically open the semantic type when it has been created, select the Open semantic type check box.
9. Click Create. The semantic type is created.
10. To assign the new semantic type to fields that match it, go to Catalog, open a dataset and click Compute or Refresh.

## Creating a semantic type from a field

You can a create semantic type from a dataset. You do not need to go to the Semantic types tab.

1. Open the dataset.
2. Select the Data Preview tab.
3. Click the field you want to update.
4. In the right panel, click the Edit icon of the Data type section.

   ![Edit icon of Data type section in the right panel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qcdi-edit-icon-right-panel.png)
5. Click Create from field. The Create semantic type window opens. The type Dictionary is already selected.
6. Enter the values or import a text file by clicking ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png).
7. To automatically open the semantic type when it has been created, select the Open semantic type check box.
8. Click Create. The semantic type is created. You are back to the dataset.
9. Click Refresh above the right panel to apply your changes.

### Detecting classification

Detected semantic types can help you identify fields that might require classification or regulatory review. For example, fields detected as email addresses, phone numbers, and national identifiers can indicate sensitive data.

After semantic type discovery, review each sensitive field and:

- Confirm the detected semantic type is correct.
- Apply required classifications and tags to the field.
- Assign another semantic type when the detected type is incorrect. For more information, see [Assigning another semantic type](#Assigning-semantic-type).
- Refresh dataset quality to apply the changes.

## Configuring classifications

You can apply classifications to datasets to identify private and sensitive information in your data.

You can see which classifications apply to which semantic types from Data quality > Semantic types.

You can view classification details from the dataset's:

- Overview tab: in the Schema section.
- Profile and Data preview tabs: click a field to view its classifications in the right panel.

### Editing classifications of a semantic type

1. Open Data quality > Semantic types.
2. Click the three dots menu icon next to the semantic type you want to edit, and then click Edit. The Edit semantic type window is open.
3. Click the drop-down menu to add or remove classifications. You can select as many classifications as needed.

   ![Edit classifications from semantic type](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/classifications-from-semantic-type.png)
4. Click Save. The change applies to all datasets using the edited semantic type.

### Editing classifications for a dataset

You can edit a dataset's classifications directly from the dataset. The semantic type is not modified, the change is only for the dataset.

Information noteThis option is available in all subscriptions, not only in the subscriptions including the semantic types.

1. Open the dataset, and then go to the Profile or Data preview tab.
2. Click a field. The right panel is open.
3. From the Classifications section, click the edit icon.

   ![Edit classifications from dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/classifications-from-dataset.png)
4. Click the drop-down menu to add or remove classifications. You can apply as many classifications as needed. The classifications are automatically applied to the field.

   Some classifications may be marked as Auto classified. They are detected using the semantic types. It is recommended to keep them applied but you can remove them.

   ![Auto classified label](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/classifications-label.png)

## Configuring regulations

Regulations represent data-protection and compliance frameworks, such as GDPR or CCPA, that govern how specific types of data must be handled.

By linking regulations to datasets, you can track which compliance requirements apply across a data product and identify datasets that contain data subject to regulatory obligations.

Regulations are linked to semantic types. When data discovery detects a semantic type in a dataset field, regulations are associated with that semantic type and surfaces them as applicable to the dataset.

For example, a field detected as a national identifier or email address can trigger associations with regulations that govern personal data. This link between field-level semantic types and their corresponding regulations makes it possible to automatically surface compliance implications at both the dataset and data product level.

Regulations are suggested but not automatically applied to datasets. You need to apply them manually.

You can view regulation details in the right panel of the dataset's Overview tab.

When a data product contains datasets with regulations, the regulations are automatically aggregated and displayed at the data product level.

Information noteThis option is available in all subscriptions, not only in the subscriptions including the semantic types.

To edit regulations:

1. Open the dataset.
2. Click the three dots action menu > Edit.
3. In the Details section, click the drop-down menu to select the regulations. You can apply as many regulations as needed.

   ![Edit regulations in dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/regulations-dataset.png)

   Depending on the classifications of the data, different regulations may be marked as Suggested.
4. Click Save. The regulations are applied to the dataset and are displayed in the right panel of the Overview tab.

## Is the semantic type being used?

Before you edit, deactivate, or delete a semantic type, check which datasets and fields use it. The number of datasets using the semantic type is displayed:

- In the Used in column from the Semantic types tab.
- In the right panel of the Edit semantic type window.

The total includes all the datasets, even the datasets to which you do not have access.

1. Open Data quality. You are in the Semantic types tab.
2. Click the Used in count of the semantic type.

   A window opens. It lists the datasets from the spaces that you can access. For each dataset, you can see the space, the owner, the fields that use the semantic type, and the average quality of these fields against the semantic type.

   The datasets from the spaces that you cannot access are not listed. Only their number is displayed at the end of the list.

   When no fields are displayed, check the dataset connection.
3. To open a dataset, click its name. The dataset opens in a new tab.

Opening the Used in count from the Edit semantic type window shows the same information.

## Editing a semantic type

You can rename a semantic type, add, edit, and remove values.

You cannot change the type of a semantic type. You must create a new one.

1. Before you edit a semantic type, check if it is used in datasets. For more information, see [Is the semantic type being used?](#semantic-type-used-in).

   After you edited the semantic type, you need to refresh the datasets in which it is used.
2. Open Data quality. You are in the Semantic types tab.
3. From the list, click the semantic type or ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png).
4. Click Edit. The Edit semantic type window is open.
5. Edit as needed.
6. Click Save.

When the semantic type is used in datasets, a message is displayed above the dataset to inform you to refresh.!['Click Refresh' message in a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/semantic-types-refresh.png)

## Deleting a semantic type

You can delete a semantic type even if it is assigned to fields in one or more datasets.

1. Before you delete a semantic type, check if it is used in datasets. For more information, see [Is the semantic type being used?](#semantic-type-used-in).

   After you deleted the semantic type, you need to refresh the datasets in which it was used.
2. Open Data quality. You are in the Semantic types tab.
3. From the list, click the semantic type or ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png).
4. Click Delete.
5. Confirm the deletion.

   If the semantic type is used in datasets, a message is displayed in the field.

   !['Missing semantic type' message](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/semantic-types-missing.png)
6. To assign another semantic type, see [Assigning another semantic type](#Assigning-semantic-type).

## Importing and exporting semantic types

You can export semantic types from one tenant and import them into another tenant to support migration and multi-tenant setup workflows.

You can perform these actions from the user interface, and you can also use the public Semantic Types API to automate semantic types management. For API details, see [Import and export semantic types](https://qlik.dev/manage/data-governance/import-export-semantic-types/).

### Exporting semantic types

1. Open Data quality. You are in the Semantic types tab.
2. Click Export.
3. Save the exported file to reuse the semantic types in another environment.

### Importing semantic types

1. Open Data quality. You are in the Semantic types tab.
2. Click Import.
3. Select the semantic types file to import.

Information noteThe semantic types file can be exported from Qlik or Talend.

4. In the Review import dialog, review the imported semantic types organized by status:
   - **Identical semantic types:** Semantic types with the same name and definition as existing ones. These are ignored during import.
   - **New semantic types:** Semantic types that do not exist in your tenant. These are created during import.
   - **Conflicting semantic types:** Semantic types with the same name as existing ones but with different definitions. For each conflicting type, choose a resolution option:
     - Ignore — Keep your existing semantic type; the imported one is not added.
     - Update — Replace your existing semantic type with the imported version.
     - Keep both — Import the semantic type with a modified name (e.g., a numeric suffix) so both versions exist in your tenant.
   - **Failing semantic types:** Semantic types with errors that prevent import. These must be fixed in the source file before they can be imported.
5. Click Import to apply your conflict resolutions and import the semantic types.
6. Review the import confirmation dialog to see the results:
   - Number of semantic types created
   - Number of semantic types ignored
   - Summary of conflicting and failed semantic types if applicable

## Using the semantic types for validation

As the semantic types are part of the dataset quality, they are part of the data quality computation but you can turn off this functionality.

1. In Data quality, create or update a semantic type.
2. In the configuration window, turn off the toggle Use for validation.
3. Click Save.

Turning on or off this toggle does not impact the usage of the semantic type. When a semantic type is assigned to a field, the values of the field are always validated against the semantic type.

For example, 89% of the values of a field are valid againt a semantic type:

- If the toggle is turned off, the dataset quality is not impacted by this good percentage.
- If the toggle is turned on, the dataset quality is better.

Tip noteWhen the semantic types lower the quality score, turn off the toggle while you are cleaning up your data.

## Predefined semantic types

The predefined semantic types are split into two categories:

- Data types: The standard types (text, integer, etc.).
- Semantic types: Groups of defined values.

The tables below list and describe each data type and semantic type.

Description of each data type.

| Data type | Description |
| --- | --- |
| Text | String text |
| Integer | Numeric value |
| Decimal | Decimal numeric value |
| Date | Date including day, month, and year |
| Time | Time of the day |
| Timestamps | Date and time |
| Boolean | Answers with the value `True` or `False` |

Description of each semantic type and the origin of data.

| Semantic type | Description | Origin of data |
| --- | --- | --- |
| Academic and professional suffix | Academic and professional suffix | Qlik |
| Academic and professional title | Academic and professional title | Qlik |
| Address Line | Street number and name | Qlik |
| Airport | Airport | Qlik |
| Amex Card | American Express card | Qlik |
| Animal | Animal | Qlik |
| Answer | Answers with the value True or False | Qlik |
| AT VAT Number | Austrian VAT number | Qlik |
| Bank Routing Transit Number | Bank routing transit number | Qlik |
| BE Postal Code | Belgian postal code | Qlik |
| Beverage | Type of beverage | [YAGO](https://yago-knowledge.org/) |
| BG VAT Number | Bulgarian VAT number | Qlik |
| CA Province Territory | Canadian province | [Statoids](http://www.statoids.com/) |
| CA Province Territory Code | Canadian province code | [Statoids](http://www.statoids.com/) |
| Christian religious title | Christian religious title | Qlik |
| City | City name | Qlik |
| Civility | Civility | Qlik |
| Color Hex Code | Color hexadecimal code | Qlik |
| Company | Company name | [YAGO](https://yago-knowledge.org/) |
| Continent | Continent name | Qlik |
| Continent Code | Continent code | Qlik |
| Country | Country name | [ISO](https://www.iso.org/obp/ui/#search) |
| Country Code ISO2 | 2-letter country code | [ISO](https://www.iso.org/obp/ui/#search) |
| Country Code ISO3 | 3-letter country code | [ISO](https://www.iso.org/obp/ui/#search) |
| Currency Code | Currency code | [ISO](https://www.iso.org/iso-4217-currency-codes.html) |
| Currency Name | Currency name | [ISO](https://www.iso.org/iso-4217-currency-codes.html) |
| Data URL | URL starting with the word data | Qlik |
| DE Bundesländer | German federal states | Qlik |
| DE Postal Code | German postal code | Qlik |
| DE Phone | German phone number | Qlik |
| Email | Email address | Qlik |
| EN Month | Month in English | Qlik |
| EN Month Abbrev | English month abbreviation | Qlik |
| EN Weekday | Week day or their abbreviation | Qlik |
| First Name | First name | Qlik |
| File URL | File URL | Qlik |
| Formal title | Formal title | Qlik |
| FR Commune | French municipality | Insee |
| FR Departement | French department | Insee |
| FR Insee Code | French Insee code of cities with Corsica and colonies | Insee |
| FR Postal Code | French postal code | Qlik |
| FR Phone | French phone number | Qlik |
| FR Region | French region | Insee |
| FR Region Legacy | Former French regions, prior to the 2016 territorial reform. | Insee |
| FR Social Security Number | French social security number | Qlik |
| FR VAT Number | French VAT number | Qlik |
| Gender | Gender | Qlik |
| Generic URL | Generic URL (Web, HDFS, MailTo, data, file) | Qlik |
| Geographic Coordinate | Geographic coordinate, longitude, or latitude coordinates with at least meter precision | Qlik |
| Geographic Coordinates | Geographic coordinates, Google Maps style GPS Decimal format | Qlik |
| Geographic Coordinates (degree) | Geographic coordinates (degrees), Latitude, and longitude coordinates separated by a comma in the form: N 0:59:59.99,E 0:59:59.99 | Qlik |
| HDFS URL | HDFS URL | Qlik |
| HR Department | HR department | Qlik |
| IBAN | International Bank Account Number | Qlik |
| Industry | Industry name | Qlik |
| Industry Group | Industry group | Qlik |
| Inherited suffix | Inherited suffix | Qlik |
| IPv4 Address | IPv4 address | Qlik |
| IPv6 Address | IPv6 address | Qlik |
| ISBN-10 | International standard book number 10 digits | Qlik |
| ISBN-13 | International standard book number 13 digits | Qlik |
| Islamic religious title | Islamic religious title | Qlik |
| Job Title | Job title | Qlik |
| Judaic religious title | Judaic religious title | Qlik |
| Language | Language | Wikipedia |
| Language Code ISO2 | 2-letter language code | Wikipedia |
| Language Code ISO3 | 3-letter language code | Wikipedia |
| Last Name | Last name | [United States Census Bureau](http://www.census.gov/) |
| MAC Address | MAC address | Qlik |
| MailTo URL | MailTo URL | Qlik |
| MasterCard | Mastercard credit card | Qlik |
| Measure Unit | Measure unit | Qlik |
| Military suffix | Military suffix | Qlik |
| Money Amount (EN) | Amount of money in English format | Qlik |
| Money Amount (FR) | Amount of money in French format | Qlik |
| Month | Month | Qlik |
| Museum | Museum name | [YAGO](https://yago-knowledge.org/) |
| MX Estado | Mexican state | [Statoids](http://www.statoids.com/) |
| MX Estado Code | Mexican state code | [Statoids](http://www.statoids.com/) |
| Name Suffix | Name suffix (Inherited, academic, professional, or military) | Qlik |
| North American state | US state and Canadian province | Qlik |
| North American state code | US state code and Canadian province code | Qlik |
| Organization | Organization | [YAGO](http://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/) |
| Passport | Passport number | Qlik |
| Phone number | Phone number (DE, FR, UK, US) | Qlik |
| Religious title | Religious title (Christian, Islamic, Judaic) | Qlik |
| SE Social Security Number | Swedish person number | Qlik |
| Sector | Sector | Qlik |
| SEDOL | Stock exchange daily official list | Qlik |
| Street Type | Street type | Qlik |
| Title | Title (Civility, academic, professional, formal, religious) | Qlik |
| UK Phone | UK phone number | Qlik |
| UK Postal Code | UK postal code | Qlik |
| UK Social Security Number | National identification number, national identity number, or national insurance number generally called NI number | Qlik |
| US Phone | US phone number | Qlik |
| US Postal Code | US postal code | Qlik |
| US Social Security Number | US social security number | Qlik |
| URL | Web site URL | Qlik |
| US County | US county name | Wikipedia |
| US State | US states | Qlik |
| US State Code | US state code | Qlik |
| Visa Card | Visa credit card | Qlik |
| Web Domain | Web site domain | Qlik |
| Weekday | Day of the week | Qlik |
