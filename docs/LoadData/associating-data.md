---
title: "Managing data associations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/associating-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager"]
---

# Managing data associations

Qlik Sense can profile your data to help you create associations between tables. You can make associations by choosing from Qlik Sense Insight Advisor's analysis-based recommendations, or you can create your own.

If you want to associate your data, we recommend that you use the Add data option with data profiling enabled. This is the default option. You can verify this setting by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the Add data button in the lower right corner of the Add Data page.

In the Associations view of the [Data manager](#glossary-0 "Glossary term"), your data is illustrated using bubbles, with each bubble representing a data table. The size of the bubble represents the amount of data in the table. The links between the bubbles represent the associations between tables. If there is an association between two tables, you can click the button in the link to view or edit the association.

Associations view in Data manager

![Associations view of the Data manager.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-data-manager_saas.png "Click to view full size")

Tip note

In most cases it is easier to edit table associations in the model view, but you can also edit a single table's associations using the Associate option in table edit view.

For more information, see [*Associating data in the table editor*](managing-associations-table-editor.htm).

## Associating tables using the Recommended associations panel

In many cases, Qlik Sense Insight Advisor will recommend associations between data tables. The Recommended associations panel lets you view and apply these recommendations.

The Recommended associations panel will open by default if any tables are present. It can be closed by and re-opened by clicking on the ![Effects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_effects.svg).

If the panel is closed and recommendations exist, you will see a badge on top of the ![Effects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_effects.svg) showing the number of recommendations.

Open recommended associations

![Associations view with five bubbels and the icon Recommended associations to the right.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_data_association_rec_panel_badge_saas.png "Click to view full size")

Do the following:

1. Click ![Effects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_effects.svg) in the upper right corner of the associations view, if the Recommended associations panel is closed.

   The panel appears on the right.
2. You will see the following information:
   - Total tables: the total number of tables.
   - Unassociated tables: the total number of tables that have no associations.
   - Recommendations: the total number of recommended associations.
   - Recommended association details: showing the name of the recommended association, and then table and field names separated by colons
3. Click on a single recommendation to preview it in dark blue.
4. To accept only some of the recommendations, click the Apply button for the specific recommendation you need.
5. Click Preview all to see how all the recommended associations will affect your data tables. Associations being previewed are highlighted.

   Recommended associations panel

   ![ Recommended associations panel open and the Associations view displaying the recommended associations.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_data_association_rec_panel_preview_saas.png "Click to view full size")
6. Click Apply all to apply every recommended association. Associations that have been accepted are highlighted in light grey.

   You can click ![open bottom panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_toggle_bottom.svg) at the bottom of the screen to see how your tables have changed.

You can now start making [visualizations](#glossary-1 "Glossary term") with your data.

## Associating tables manually

You can associate tables manually, by dragging them together. When you drag table bubbles towards each other, they will be marked with a green, orange, or red stripe.

- Green: the Data manager is very confident about which fields to associate. For example, if two tables have fields labeled "Sales Region", the Data manager assumes they should be associated.
- Orange: the Data manager is fairly confident that these tables can be associated. For example, if two different fields have different labels, but contain single digit data, the Data manager will flag them as orange, because the data types are similar.
- Red: the Data manager does not know how to associate these tables. You will have to choose which tables and fields go together in the Associate tables editor.

I want to manually associate tables that are green or orange

Do the following:

1. Drag a table to one of the tables marked with green or orange.
2. The association is automatically applied.

The tables are now associated using the recommended fields.

I want to manually associate a tables that are red

You can associate the tables by creating a custom association.

Do the following:

1. Drag a table to one of the tables marked with red.

   The Associate tables editor opens.
2. In the left table, select which fields to use in the association.

   You choose a single [field](#glossary-2 "Glossary term") or multiple fields. You can also add delimiter characters to make it easier to interpret the data, or to match a field that already exists. You can see what the association data looks like in the preview.
3. In the right table, select which fields to use to match the selections you made in the left table.
4. Enter a name for the key field that will be created in Name.

   This new field name cannot be the same as an existing field name in either table.
5. Click Associate.

The tables are now associated using your custom association.

## Breaking associations

There are two ways of breaking associations that are not a good fit for your data model.

Do the following:

- Click one of the associated tables, and drag it away from the other table until the association breaks. Or you can:
- Click on the link between the two bubbles, and then click the Delete button in the bottom panel.

The two tables are no longer associated.

## Editing associations

You can edit an existing association between two tables if you need to adjust the data model.

Do the following:

1. Click the circle between the associated tables to open the data panel.

   The panel opens with a preview of data in the associated fields.
2. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).

   You will see one or more buttons, each marked with green, orange, or red. Green means the Data manager is very confident in the association, orange means somewhat confident, and red means unsure. The current association is marked with grey.
3. Click one of the association buttons:

   - Click a recommended association to select it.
   - Click an existing custom association ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) to edit which fields to use in the association.
   - Click Custom association to create a new association.

     This button is only available if there is a recommended association for the table pair.

     Custom associations can contain a single field or multiple fields.

You have now changed the association between the table pair.

## Previewing data

You can preview tables in the associations view to get a better understanding of the data.

Do the following:

1. Select a table.
2. Click ![open bottom panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_toggle_bottom.svg) at the bottom of the view.

The preview pane is displayed with the table data.

## Synthetic keys

When two or more data tables have two or more fields in common, this suggests a composite key relationship. Qlik Sense handles this by creating synthetic keys automatically. These keys are anonymous fields that represent all occurring combinations of the composite key.

For more information, see [*Synthetic keys*](../Scripting/synthetic-keys.htm).

If adding a table results in any of the following cases, you can only add data with profiling enabled:

- A synthetic key containing more than five fields is created.
- More than ten synthetic keys are created.
- Nested synthetic keys are created, that is, synthetic keys containing other synthetic keys.

These cases indicate that you need to adjust the data tables to resolve the issues.

## Limitations

There are some cases where association recommendations are not provided, due to the structure of the loaded tables and the data in the tables. In these cases, you need to adjust the associations in the table editor.

- Many-to-many relationships.
- Field pairs with data does not match well in both directions. This may be the case when you have a small table with a few field values that match a field in a large table 100%, while the match in the other direction is significantly smaller.
- Compound key associations.

For more information about how to edit a table, see [*Editing a table*](editing-table.htm).

If your application contains more than 500 fields, the recommended associations list might be more limited than for an application with fewer than 500 fields.

Additionally, the Data manager will only analyze tables that were added with Add data. Tables added using the data [load script](#glossary-4 "Glossary term") are not included in the association recommendations, unless they have been synchronized into Data manager.

For more information, see [*Synchronizing scripted tables in Data manager*](synchronizing-scripted-tables.htm).

## Applying changes and reloading data

Changes that you have made in the Data manager will not be available in the application until you have reloaded data. When you reload data, the changes are applied and any new data that you have added is loaded from the external data sources. Data that you loaded previously is not reloaded.

You can reload all the data from the external data sources by using the ![reload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sync.svg) button in the Data manager footer.

![Data manager footer.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DataManagerDataReload_revised.png)

The ![reload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sync.svg) button reloads all the data for the selected table. It does not reload all the data for all the tables in the application.

If the data in Data manager is out of sync with the application data, the Load data button is green. In the Associations view, all new or updated tables are indicated with \*, and deleted tables are a lighter color of gray. In the Tables view, all new, updated, or deleted tables are highlighted in blue and display an icon that shows the status of the table:

- Tables marked with Pending delete ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) will be deleted.
- Tables marked with Pending update ![reload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sync.svg) will be updated with fields that have been added, renamed, or removed, or the table will be renamed.
- Tables marked with Pending add ![Checkmark ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg) will be added.

### Applying changes

Do the following:

- Click Load data to load the changes in the application.

The application data is now updated with changes you made in Data manager.

Related learning:

- [Introduction to the data manager](/lnk/Intro_Data_Manager_QS)
- [Associating Tables and Transforming Data](/lnk/Assoc_tables_transform_data_QS)
- [Data manager associations, concatenations and joins](/lnk/Data_Manager_Assocs_Concats_Joins_QS)
- [How do I define associations between tables?](/lnk/How_define_associations_between_tables)
