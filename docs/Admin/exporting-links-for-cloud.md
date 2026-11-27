---
title: "Importing application links from Qlik Sense Enterprise on Windows to Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/exporting-links-for-cloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources", "Creating and managing generic links"]
---

# Importing application links from Qlik Sense Enterprise on Windows to Qlik Cloud

As a tenant administrator, you can export application links from your Qlik Sense Enterprise on Windows environment and import them into Qlik Cloud. By using CSV files, you can efficiently import large numbers of links.

Use the Operations Monitor application within your Qlik Sense Enterprise on Windows hub to export a spreadsheet with relevant application information. Format this sheet into a CSV file, including the required columns for importing into the Administration activity center.

Do the following:

Export links

1. In the Qlik Sense Enterprise on Windows hub Monitoring apps stream, open the Operations Monitor application.
2. Navigate to the Export Links for Cloud sheet.
3. Apply relevant filters to refine the data as needed.
4. Right-click the Export Links table, select Export, and then select Export data.
5. Download the generated data file, which will be in spreadsheet format.
6. Open the downloaded file using Microsoft Excel.

Convert to CSV format

1. Once opened in Excel, save the file in CSV (.csv) format.

   Information note

   Ensure that the file is saved with UTF-8 encoding, as Qlik Sense only supports this encoding for generic link CSV files.

Import to Qlik Cloud

1. In the Qlik Cloud Administration [activity center](#glossary-0 "Glossary term"), go to Generic links.
2. In the upper-right corner, click Upload CSV file.
3. Select and upload the CSV file containing the exported application links.

For more information, see [*Creating and managing generic links*](mc-administer-generic-links.htm).
