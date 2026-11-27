---
title: "Importing and exporting glossaries"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/BusinessGlossary/exporting-glossaries.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with business glossaries"]
---

# Importing and exporting glossaries

You can import categories and terms into your glossary. You can also export your glossary as a backup or to import it into a different environment.

## Importing terms from glossary files

You can import terms, categories, and metadata into your glossary from a glossary file. Glossaries can be imported from

- Other Qlik Cloud environments in the Qlik glossary JSON format.
- JSON files in Atlan and Apache Atlas glossary formats.
- Microsoft Excel and CSV (Comma-Separated Value) files.

  Using column headers in the file will make it easier to map fields to properties in the glossary.

  Information noteMicrosoft Excel files in the legacy .XLS format are not supported.

You can import from multiple files into your glossary to build your glossary. You can also import repeatedly from a single glossary file, updating the glossary in Qlik Cloud with any new changes to that file.

When importing a file, you can choose to optionally also update metadata such as the glossary overview and glossary details.

You can view import logs under Import log files. Logs show the terms, categories, and metadata changed in each import.

### Importing a JSON file

Do the following:

1. In a glossary, click Glossary details.
2. Click Import & export.
3. If you are reimporting a glossary, click Download glossary to export a backup of the glossary.
4. Click Import and update glossary.
5. Select Update glossary metadata if you want to update the glossary overview and glossary details.
6. Optionally, to delete all terms and categories not in the import file, select Delete terms and categories in this glossary that do not existing in the imported glossary.
7. Optionally, click Import test to test the import and view the log. You can download the log as a TXT file.
8. Click Import.

The glossary items are now imported from the selected file to your glossary.

### Importing an Excel or CSV file

1. In a glossary, click Glossary details.
2. Click Import and update glossary.
3. Select which glossary file to import.
4. Select glossary format in File format.
5. Select Update glossary metadata if you want to update the glossary overview and glossary details.
6. Optionally, to delete all terms and categories not in the import file, select Delete terms and categories in this glossary that do not existing in the imported glossary.
7. Select Include headers: If the first row contains header information.
8. Set Skip rows: If you want to skip a number of the first rows.
9. If you are importing a CSV file, set the format options that apply to your CSV file for:

   - Delimiter: Which delimiter is used to separate fields.
   - Encoding: Text encoding that is used.
   - Quoting: Symbol used to mark quoting.
10. Optionally, click Import test to test the import and view the log. You can download the log as a TXT file.
11. Click Import.

    Mapping preview is displayed.
12. Map the fields in your file that contain glossary items to categories in your business glossary.

    If you are importing an Excel file with more than one worksheet, you can select which sheet to use in the left panel.
13. Click Import when you are happy with your field mappings.

The glossary items are now imported from the selected file to your glossary.

## Exporting glossaries

Download copies of your business glossary in Export. The glossary file is then available for import into a different environment. You can also export glossaries to archive different versions of your glossaries.

You can download the glossary in Qlik Cloud glossary format as a JSON file , or to an Microsoft Excel file.

Do the following:

1. In a glossary, click Glossary details.
2. Click Import & export.
3. Select Download glossary to save the business glossary to your Downloads directory.

   You can select to download the file in JSON or Excel format.

The glossary file is now available for import into environments such as a different space or different Qlik Cloud tenant.
