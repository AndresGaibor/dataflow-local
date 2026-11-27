---
title: "Best practices for in-application reporting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/InAppGeneral/reporting-best-practices.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics"]
---

# Best practices for in-application reporting

This page lists best practices you can follow for best results when working with in-application reporting in Qlik Cloud Analytics.

## Report task scheduling

Parallel report task execution will increase the processing time for report tasks. Running many report tasks concurrently puts the tasks at a higher risk for timeout or failure. Running many report tasks concurrently also increases the execution time for individual report tasks.

For optimal results:

- Avoid scheduling multiple report tasks at the same time. It is better to stagger the start time.
- When scheduling multiple report tasks for the same application, avoid scheduling these task runs at close to the same time as each other. It is recommended to stagger the start times so that one task execution clears its requests to the application before another task execution begins.

You should also try to avoid top-of-the-hour scheduling of a report task, as this is a peak request time for a tenant and region.

## Managing report task recipients

A report task configuration is flexible and allows you to add both individual users and groups of users as receivers of report output. When possible, a best practice is to use groups to add recipients to the report task. Groups are collections of recipients, and are defined in the [distribution list](#glossary-0 "Glossary term"). When you change the email address of a recipient who has been added to the task as part of a group, reports are generated and delivered to the updated email address.

On the other hand, adding individual recipients can be risky if there is a chance that the recipient's email address will change in the future. A best practice is to only add users individually when adding them as members of a group is not appropriate.

## Design considerations for applications used for reporting

Avoid using very large, interactive applications for reporting purposes. Instead, consider having a reporting application that maintains only the required data for reporting jobs if your application is very large.

## Designing Excel templates

### Arranging images and tabular data

In your Excel report template, a best practice is to organize different types of content in horizontal bands. You can place images side-by-side with tabular data, but it could result in image sizes being different than expected in the generated report.

Instead, place images in their own dedicated row in the template.

Consider arranging your report template in Excel with the structure shown in this image.

![The recommended way to structure an Excel report template. Images are contained in separate horizontal bands separate from the rows where tabular data is inserted](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_excel-template-recommended.png "Click to view full size")

## Best practices for effective object naming in Qlik Sense application development

When it comes to naming objects in Qlik Sense applications, it is important to follow certain best practices to ensure clarity, consistency, and maintainability. Object names are the chart and table tags that appear in your [report template](#glossary-1 "Glossary term").
Here are some recommendations for naming objects like tables, charts, and other elements in Qlik Sense:

- Use a unique name for each object. Avoid duplications that could generate confusion and cause you to add the wrong object.
- Use clear and descriptive names. Choose names that accurately reflect the purpose and content of the object. Avoid ambiguous or generic names that may confuse users.
- Be concise but informative. Keep the names concise while providing enough information to convey the object's function or data. Long and convoluted names can be cumbersome to work with.
- Use consistent naming conventions. Establish and follow a consistent naming convention across all objects in your application. This helps maintain a logical structure and makes it easier to search, identify, and manage objects.
- Avoid using special characters. Stick to alphanumeric characters and underscores in object names. Special characters can cause issues in scripting or expressions.
- Use camel case or underscores instead of spaces: Choose either camel case (myTable) or underscores (my\_table) to separate words in object names. This improves readability and makes the names more understandable.
- Avoid using reserved keywords. Qlik Sense has reserved keywords that should not be used as object names. These keywords are used in expressions, scripts, or the Qlik Sense environment. Examples include "if," "and," "or," "load", and so on.
- Use meaningful and intuitive names for dimensions and measures. When creating dimensions and measures within charts, use names that clearly describe the underlying data or calculations they represent. This enhances understanding and collaboration among developers and end-users.
- Document naming conventions. Maintain documentation that outlines the naming conventions used in your Qlik Sense applications. This helps new developers understand the naming conventions and ensures consistency when multiple developers are working on the same application.
- Regularly review and update object names. As your application evolves or requirements change, periodically review and update the object names to ensure they align with the current structure and functionality of the application.
