---
title: "Configuring your packages"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Tutorial/tutorial-configuring-packages.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Tutorial – Customizing how Insight Advisor interprets data"]
---

# Configuring your packages

The next step is to start working with the other elements of the [logical model](#glossary-0 "Glossary term"), starting with packages.

Packages are collections of groups that should be used together in analysis. This ensures only relevant fields are used together by [Insight Advisor](#glossary-1 "Glossary term"). Groups can belong to multiple packages. Packages are an optional part of the logical model.

## Why create packages?

Packages define the scope of which groups should be used together in analysis. For example, your logical model may have groups that cover different areas of an organization. Mixing these may not always be desirable for your Insight [charts](#glossary-2 "Glossary term").

For example, the tutorial app has data related to the handling of support calls, which is not related to the sales and supplier data. If you navigate to Sheet and select AverageCallSatisfaction from the Insight Advisor Assets panel, you get results where the support call data is mixed with sales data fields.

By using packages, you can keep the sales and supplier data together for analysis and keep the support call data together for analysis, preventing Insight Advisor from trying to use the data together.

## Creating packages

You are going to create packages for the sales-related groups and support-related groups. Both will include the relevant Employees and Offices groups.

### Creating the Support package

Do the following:

1. Navigate to Packages.
2. Click Create package.
3. For Package name, enter Support.
4. Add the following groups to the package:

   - SupportCalls
   - SupportDate
   - Employees
   - Offices
5. Click Create.

### Creating the Sales package

Do the following:

1. Navigate to the Packages section.
2. Click Create package.
3. For Package name, enter Sales.
4. Add the following groups to the package:

   - Categories
   - Customer
   - Employees
   - Offices
   - Products
   - Sales
   - Sales\_OrderDate
   - SalesCity
   - SalesCountry
   - Suppliers
5. Click Create.

## Results

Go to Sheet in the app navigation menu and click ![Insight Advisor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg). In the assets panel, select AverageCallSatisfaction.
Now, none of the generated Insight Advisor analyses use fields from groups that are not part of the Support package.
