---
title: "Sharing visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Share/sharing-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Sharing and downloading application content"]
---

# Sharing visualizations

You can share [visualizations](#glossary-0 "Glossary term") with your current [selections](#glossary-1 "Glossary term") with others. This enables you to share insights you have discovered.

You can share a visualization as an image, link, or embedded HTML.

Do the following:

1. Right-click on the visualization or click the hover menu ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
2. Select Share. Then choose:
   - Image: Qlik Sense creates an image of your a visualization with the current selections. You then select recipients and Qlik Sense sends them your visualization.

     Information note

     Sharing by email is enabled by your [tenant administrator](#glossary-2 "Glossary term"). If this option is not available in your application, it may be disabled for apps in your Qlik Cloud tenant.
   - Copy link. Copy and share the generated URL to the visualization.
   - Embed link: create a link that can be embedded in emails and HTML

## Limitations

When sharing a visualization, shadows applied to the chart object are not shown in the output.

Consider the following limitations that apply to sharing visualizations. These limits are checked when you click Share. If these limits are exceeded, you will see an error message. If this issue occurs, contact a user with Can edit permission in the application.

The specific limitations are listed below:

- Maximum number of fields in the selections: 125
- Maximum number of field values in the selections: 150,000 total field values across one or many fields
- Maximum number of alternate states: 125

  [*Using alternate states for comparative analysis*](../Visualizations/alternate-states-comparative-analysis.htm)
- Maximum number of patches: 100

  Patches are properties or styling applied in the application. For example: Adding a sort to a table column.
- Maximum number of variables: 1,100

  [*Using variables in expressions*](../Variables/work-with-variables.htm)
- Maximum number of sheets in the subscription: 10
- Maximum image size: 4,000 x 4,000 pixels
- Minimum image size: 5 x 5 pixels for charts and 20 x 20 pixels for sheets

## Learn more

- [*Enabling and disabling reporting, subscriptions, and sharing features*](../Admin/mc-enable-reporting-features.htm)
- [How do I email Qlik Sense charts?](/lnk/How_email_Qlik_Sense_charts)

Related learning:

- [How do I email Qlik Sense charts?](/lnk/How_email_Qlik_Sense_charts)
