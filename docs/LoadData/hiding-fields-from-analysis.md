---
title: "Hiding fields from analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/hiding-fields-from-analysis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Hiding fields from analysis

You can hide data fields that you do not want available when building [visualizations](#glossary-0 "Glossary term") in [sheet](#glossary-1 "Glossary term") view or in [Insight Advisor](#glossary-2 "Glossary term").

You might, for example, have [fields](#glossary-3 "Glossary term") that are only used for calculating another field. You can hide these fields in [Data manager](#glossary-4 "Glossary term") so that they are not available in the assets panel of [sheets](#glossary-5 "Glossary term") or from Insight Advisor but remain available in Data manager and [Data load editor](#glossary-6 "Glossary term"). This can be used to remove information that may be redundant or unnecessary to your current analysis or insights, including only relevant information and making it easier to read and analyze.

When hiding a field, all existing relationships the field has, such as associations or use in calculations, will be maintained. If a field is currently in use, such as in a [master item](#glossary-7 "Glossary term") or in an existing [chart](#glossary-8 "Glossary term"), it will continue to be available there, but will not be available for use in new master items or visualizations until it is shown again.

Information note

You can view all your hidden fields in Data manager by going into Data load editor and opening the auto-generated section. All hidden fields will be listed as TAG FIELD <field name> WITH '$hidden';

## Hiding a field from analysis

Do the following:

1. Click on ![Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) above the field heading.
2. Click Hide in Analysis.

The field is now hidden in sheet view and in Insight Advisor. Hidden fields have ![View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view.svg) added above the field heading.

## Showing a hidden field

Do the following:

1. Click on ![Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) or ![View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view.svg) above the field heading.
2. Click Show in Analysis.

The field is now available in sheet view and in Insight Advisor. The ![View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view.svg) above the field heading will be removed.
