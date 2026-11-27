---
title: "Associating data in the table editor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/managing-associations-table-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Associating data in the table editor

You can create custom associations to fields in other tables with Associate in the field menu of the [Data manager](#glossary-0 "Glossary term") table editor.

In many cases it is easier to manage to your associations in the Associations view.

Typically, these are the most common cases where you need to create a custom association instead of following the recommendations:

- You know which fields to associate the tables with, but the score for this table pair is too low to show in the list of recommendations.

  Create an association based on a single [field](#glossary-1 "Glossary term") in each table.
- The tables contain more than one common field, and they need to be used to form the association.

  Create a compound key.

## Creating an association using a single field

If the two tables contain related data, but the association does not show up as recommended, you can define a custom association in the table editor. This creates a key field to associate the tables.

Do the following:

1. From the data manager overview, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) on one of the tables you want to associate.

   The table editor opens.
2. Select Associate from the field menu of the field you want to use in the key field.

   The Associate tables editor opens, with a preview of the field you selected in the left table. Now you need to select which field to associate this with in the right hand table.
3. Click Select table and select the table to associate with.
4. Click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) and select the field to associate with.

   The right hand table will show preview data of the field you selected. Now you can compare the left table with the right to check that they contain matching data. You can search in the tables with ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg) to compare them more easily.
5. Enter a name for the key field that will be created in Name.

   It's not possible to use the same name as an existing field in either of the tables.
6. Click Associate.

The tables are now associated by the two fields you selected, using a key field. This is indicated with ![Associate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_associate.svg). Click ![Associate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_associate.svg) to display options to edit or break the association.

## Creating a compound key

If two tables contain more than one common field that would create an association, Qlik Sense creates a [synthetic key](#glossary-2 "Glossary term") to handle the association. The recommended way of fixing this is to create a compound key. This can be achieved by creating a custom association containing all fields that should be associated.

Do the following:

1. From the data manager overview, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) on one of the tables you want to associate.

   The table editor opens.
2. Select Associate from the field menu of one of the fields you want to include in the compound key field.

   The Associate tables editor opens, with a preview of the field you selected in the left table.
3. Click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) to add the other fields you want to include in the compound key field.

   The preview is updated with the compound key data.

   Now you need to select which fields to associate this with in the right hand table.
4. Click Select table and select the fields you want to include in the compound key field.
5. Click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) and select the field to associate with. You need to select them in the same order as in the left hand table.

   To make it easier to interpret the data in the key you can also add delimiter characters.

   The right hand table will show preview data of the field you selected.

   Now you can compare the left table with the right to check that they contain matching data. You can search in the tables with ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg) to compare them more easily.
6. Enter a name for the key field that will be created in Name.
7. Click Associate.

The tables are now associated by the fields you selected, using a compound key field.

### Limitations

There are some limitations to the use of compound keys.

- It is not possible to create a compound key in a concatenated table.
- If you use a calculated field in a compound key, the calculated field expression is expanded in the compound key expression. There is no reference to the calculated field, that is, if you edit the calculated field, the compound key is not updated.

## Editing an association

You can edit an association to rename it, or change the associated fields.

Do the following:

1. Click ![Associate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_associate.svg) to show the association menu.
2. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) to edit the association.

The Associate tables editor opens, and you can rename the association or change the associated fields.

## Breaking an association

If you have a created an association between two tables that is not needed, you can break it.

Do the following:

1. Click ![Associate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_associate.svg) to show the association menu.
2. Click ![Break association](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_break_association.svg) to break the association.

The tables are now not associated anymore.
