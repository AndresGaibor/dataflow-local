---
title: "Viewing table and field transformation details in Data manager"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/viewing-table-field-details.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager"]
---

# Viewing table and field transformation details in Data manager

You can view the operations and transformations performed on tables and fields in [Data manager](#glossary-0 "Glossary term") using the Details dialog. The Details dialog is available in the Associations and Table views for tables and in the data table editor for fields.

Details displays the current operations and transformations made to the selected table or [field](#glossary-1 "Glossary term") in the order they are applied in the generated data [load script](#glossary-2 "Glossary term"). This enables you to easily see the source of a table or field, the current changes that have been made, and the sequence in which the changes have been applied. You can use Details, for example, to easily see which tables were concatenated or if a field was reordered.

The information displayed in Details varies depending if you are viewing a table or field. Table Details displays:

- Source tables for the selected table.
- Transformations used on the table, such as unpivoting and concatenation.

Field Details displays:

- Source tables and fields for the selected field.
- Field type changes.
- Transformations used on the fields, such as from the data profiling card or from concatenation.

## Viewing table details

Do the following:

- In Data manager, select a table, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and click View details.

The Details dialog opens.

## Viewing field details

Do the following:

1. In Data manager, select a table and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. Click ![Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) above a field heading and click View details.

The Details dialog opens.
