---
title: "Navigating analytic content"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCloudNavigation/navigating-activity-center-content.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Cloud Analytics activity centers"]
---

# Navigating analytic content

Qlik Cloud Analytics [activity centers](#glossary-0 "Glossary term") offer a range of analytic content.

Click the content to open it. Activity center content displays the name, owner, and the modification date.
You can view the tags applied to the content by hovering your cursor over an application. On a touch device, you can view the tags by tapping ![Arrow Up](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_up.svg) on the application.

In addition, different content types may have additional options available by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the content.

What content types are available to you depends on which activity center you are in.

Content types by activity center

| Content type | Insights activity center | Analytics activity center |
| --- | --- | --- |
| Charts | Yes | Yes |
| Applications | Yes | Yes |
| Data | No | Yes |
| Scripts | No | Yes |
| Data flows | No | Yes |
| Table recipes | No | Yes |
| Notes | Yes | Yes |
| Links | Yes | Yes |
| Automations | No | Yes |
| ML deployments | No | Yes |
| ML experiments | No | Yes |
| Glossaries | No | Yes |
| Assistants | Yes | Yes |
| Knowledge bases | No | Yes |
| Skills | No | Yes |
| Data products | No | Yes |

## Charts (Insights and Analytics)

Charts are application visualizations that have been made available in activity centers. You can add visualizations from applications as charts in your activity center. This lets you to closely monitor important visualizations without opening applications. For more information, see [*Monitoring visualizations*](../Hub/monitor-charts-hub.htm).

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the chart including:

Chart options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this chart only or add them to the space with a chosen role. | - |
| Share > Copy link | Copy a link to the chart. | - |
| Share > Manage access | Manage user access to this chart or space the chart is in. | - |
| View in application | View the chart in the application it came from. | - |
| Details | You can view the owner and other metadata for the chart. | - |
| Manage > Favorite | Add the chart to your Favorites. | - |
| Manage > Add to collection | You can add the chart to one of your collections. | - |
| Manage > Edit details | You can change the chart name, description, and tags. | - |
| Copy as image | Copy the chart as a PNG to paste into another application. |  |
| Save as image | Save the chart as a PNG. |  |
| Delete | You can delete the chart. | - |

## Applications (Insights and Analytics)

Applications are task-specific, purpose-built applications that contain data loaded from data sources that are interpreted through visualizations.

In the Insights activity center, you can view applications. In the Analytics activity center, you can create new applications, duplicate existing applications, or upload applications. You can upload applications exported from your activity centers or other versions of Qlik Sense. You can keep your applications private or you can share them with other users. To learn more about Qlik Sense applications, see [*Working with applications*](../Visualizations/create-apps-visualizations.htm).

Each application displays the application name, owner, and the modification date.
You can view the type of application and tags applied to the application by hovering your cursor over an application. On a touch device, you can view the application type and tags by tapping ![Arrow Up](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_up.svg) on the application. You can click on the application to open it. If the application creator has configured an application preview, you can click Open preview to see the preview sheet. You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the application including:

Application options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this application only or add them to the space with a chosen role. | [*Sharing applications with users who are not space members*](../Spaces/sharing-content-with-non-space-members.htm) |
| Share > Copy link | Copy a link to the application.  Warning noteIf the application is in an [anonymous access](#glossary-1 "Glossary term") tenant and anonymous access is turned on for the application, the application link can be opened by anyone. |  |
| Share > Manage access | Manage user access to this application or space the application is in. | [*Sharing applications with users who are not space members*](../Spaces/sharing-content-with-non-space-members.htm) |
| Open in new tab | You can open your application in a new tab. | [*Opening an application*](../Apps/open-preview-app.htm#Opening) |
| Preview | Open the application preview.  Information notePreview is only available if the application creator has set up a preview sheet. | [*Opening and previewing applications*](../Apps/open-preview-app.htm) |
| Details | You can view the application type and owner, as well as relevant date information for the application. Additionally, you can view the application size. This page also shows the tags applied to the application and who can access the application. You can also see reload history and performance evaluations related to the application. | - |
| Manage > Favorite | Add this application to your Favorites. | - |
| Manage > Add to collection | You can add the application to one of your collections. |  |
| Manage > Edit details | You can change the application name, description, and tags. | [*Editing application details*](../Apps/edit-app-cloud-hub.htm) |
| Manage > Notification settings | Set notification preferences for this application. You can receive notifications when reloads and performance evaluations succeed or fail. You can also receive notifications if a scheduled reload for an application failed, stopped, or was disabled. You must be assigned to the reload schedule to receive this notification. You will not receive notifications if an application is reloaded in the [Data manager](#glossary-2 "Glossary term") or Data load editor. Reload notifications are sent if an application is reloaded in activity centers or on a schedule. | [*Notifications*](../Introduction/profile-settings.htm#Notifica) |
| Manage > Publish to space | Publish the application to a managed space. | [*Publishing applications*](../Apps/publish-app-cloud-hub.htm) |
| Manage > Published copies | View and managed the published copies of the application. | [*Publishing applications*](../Apps/publish-app-cloud-hub.htm) |
| Manage > Move to space | You can move the application to a different space. | [*Moving applications between spaces*](../Spaces/managing-apps-in-spaces.htm#Moving) |
| Manage > Duplicate | You can create a copy of the application. | [*Creating applications and adding data*](../Apps/create-app-cloud-hub.htm#Duplicat) |
| Manage > Duplicate as script | You can duplicate the application and convert it to a script. The application's load script is used as the script. | [*Converting applications to scripts*](../Apps/convert-app-to-script.htm) |
| Reload > Reload now | You can reload the application data manually. | [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm) |
| Reload > Schedule | You can create tasks to schedule reloads of application data. | [*Scheduling reloading application data*](../Apps/reloading-apps-cloud-hub.htm#Scheduli) |
| Reload > History | View the reload history of the application. | [*Viewing reload history for an application*](../Apps/reloading-apps-cloud-hub.htm#Viewing) |
| Tools > Lineage | Lineage represents the history of a [field](#glossary-3 "Glossary term") or [dataset](#glossary-4 "Glossary term"), back through applications and transforms, to the original data source. | [*Analyzing lineage in Analytics*](../Catalog/lineage.htm) |
| Tools > Impact analysis | Impact analysis shows a downstream view of a data element’s dependencies - which databases, applications, scripts, files, or links would directly or indirectly be impacted if the value or structure of that particular field was changed. | [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm) |
| Tools > Performance evaluation | You can run a tailored evaluation as you develop your application and presents simple and understandable metrics such as response times for public [sheets](#glossary-5 "Glossary term") and objects. | [*Application performance evaluation*](../Apps/app-performance-evaluation.htm) |
| Tools > Open without data | You can open your application without data. This is helpful if you need to troubleshoot your [load script](#glossary-6 "Glossary term"). When you open an application without data, [visualizations](#glossary-7 "Glossary term") will not work, as they are not connected to the data source. Additionally, the data manager and the data model viewer will not be available. | [*Opening an application without data*](../Apps/open-preview-app.htm#Opening2) |
| Download > Download | You can download applications as .qvf files. | [*Downloading applications*](../Apps/export-apps-cloud-hub.htm) |
| Download > Download without data | You can downlaod the application without any data. This only the sheets and [stories](#glossary-8 "Glossary term") of the application. | [*Downloading applications*](../Apps/export-apps-cloud-hub.htm) |
| Delete | You can delete the application. | [*Deleting applications*](../Apps/delete-app-cloud-hub.htm) |

You can also add QlikView applications to Qlik Cloud. QlikView applications can only be viewed and have different options than Qlik Sense applications in the activity centers.

## Data (Analytics)

Datasets are data files containing tables of data. You can view datasets in the Analytics activity center from the spaces to which you have access.

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the application including:

Application options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Use in > Application | Create a new application using this dataset. | - |
| Use in > Table recipe | Create a new table recipe using this dataset. | - |
| Use in > Data flow | Create a new data flow using this dataset. | - |
| Use in > Script | Create a new script using this dataset. | - |
| Share > Invite | Give a user access to this dataset by adding them to the space with a chosen role. | - |
| Share > Copy link | Copy a link to the dataset. | - |
| Share > Manage access | Manage user access to this dataset or space the dataset is in. | - |
| Open in new tab | You can open your dataset in a new tab. | - |
| Details | View metadata about the dataset, including owner, space, the last time its profile was refreshed, and its file size.  From Details, you can also open the dataset in the catalog. When you open a dataset, you can access more details, such as an overview of the dataset, additional metadata, the data profile, lineage information, and impact analysis. | - |
| Manage > Favorite | Add this dataset to your Favorites. | - |
| Manage > Add to collection | You can add the dataset to one of your collections. | - |
| Manage > Edit details | You can change the dataset name, description, and tags. | - |
| Tools > Lineage | Lineage represents the history of a field or dataset, back through applications and transforms, to the original data source. | [*Analyzing lineage in Analytics*](../Catalog/lineage.htm) |
| Tools > Impact analysis | Impact analysis shows a downstream view of a data element’s dependencies - which databases, applications, scripts, files, or links would directly or indirectly be impacted if the value or structure of that particular field was changed. | [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm) |

## Scripts (Analytics)

Scripts are Qlik Cloud applications for loading, transforming, and exporting data.

In the Analytics activity center, you can create new scripts, duplicate existing scripts, or upload scripts. You can upload exported scripts. You can keep your scripts private or you can share them with other users. To learn more about scripts, see [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm).

Each script in the Analytics activity center displays the script name, owner, and the modification date.
You can view the type of script and tags applied to the script by hovering your cursor over a script. On a touch device, you can view the script tags by tapping ![Arrow Up](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_up.svg) on the script. You can click on the script to open it. You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the script including:

Script options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this script by adding them to the space with a chosen role. | [*Sharing scripts*](../ScriptEditor/managing-scripts.htm#Sharing) |
| Share > Copy link |  | - |
| Share > Manage access | Manage user access to this application or space the application is in. | [*Sharing scripts*](../ScriptEditor/managing-scripts.htm#Sharing) |
| Open in new tab | You can open your script in a new tab. | - |
| Details | You can view the script owner, as well as relevant date information for the script. Additionally, you can view the script size. This page also shows the tags applied to the script and who can access the script. You can also see reload history and performance evaluations related to the application. | - |
| Manage > Favorite | Add this dataset to your Favorites. | - |
| Manage > Add to collection | You can add the script to one of your collections. | - |
| Manage > Edit details | You can change the script name, description, and tags. | [*Moving scripts*](../ScriptEditor/managing-scripts.htm#Moving) |
| Manage > Notification settings | Set notification preferences for this script. You can receive notifications when reloads and performance evaluations succeed or fail. You can also receive notifications if a scheduled reload for a script failed, stopped, or was disabled. You must be assigned to the reload schedule to receive this notification. You will not receive notifications if a script is reloaded in Script. Reload notifications are sent if a script is reloaded in an activity center or on a schedule. | - |
| Manage > Publish to space | Publish the script to a managed space. | [*Publishing scripts*](../ScriptEditor/publishing-scripts.htm) |
| Manage > Published copies | View and managed the published copies of the script. | [*Publishing scripts*](../ScriptEditor/publishing-scripts.htm) |
| Manage > Move to space | You can move the script to a different space. | [*Editing script details*](../ScriptEditor/managing-scripts.htm#Renaming) |
| Manage > Duplicate | You can create a copy of the script. | [*Duplicating scripts*](../ScriptEditor/managing-scripts.htm#Duplicat) |
| Manage > Duplicate as application | You can convert the script to an application. The script will be used as the application's load script. | [*Converting scripts to applications*](../ScriptEditor/managing-scripts.htm#Converti) |
| Run > Run now | You can run the script manually. | [*Running scripts*](../ScriptEditor/reloading-scripts.htm) |
| Run > Schedule | You can create tasks to schedule runs of the script. | [*Running scripts*](../ScriptEditor/reloading-scripts.htm) |
| Run > History |  | - |
| Tools > Lineage | Lineage represents the history of a field or dataset, back through applications and transforms, to the original data source. | [*Analyzing lineage in Analytics*](../Catalog/lineage.htm) |
| Tools > Impact analysis | Impact analysis shows a downstream view of a data element’s dependencies - which databases, applications, scripts, files, or links would directly or indirectly be impacted if the value or structure of that particular field was changed. | [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm) |
| Download | You can export scripts as .qvf files. | [*Exporting scripts*](../ScriptEditor/managing-scripts.htm#Exportin) |
| Delete | You can delete the script. | [*Deleting scripts*](../ScriptEditor/managing-scripts.htm#Deleting) |

## Data flows (Analytics)

A data flow is an intuitive no-code experience that allows you to create a visual flow to prepare data. Place your source on the canvas, and use a variety of processors to combine and shape your data in order to produce clean datasets for your analytics applications or ML experiments.

For more information, see [*Loading and preparing data with Data flow*](../DataFlow/loading-preparing-with-data-flow.htm).

Data flow options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this data flow by adding them to the space with a chosen role. | [*Sharing data flows*](../DataFlow/managing-data-flows.htm#Sharing) |
| Share > Copy link | Copy a link to the data flow. | - |
| Share > Manage access | Manage user access to this data flow or space the data flow is in. | [*Sharing data flows*](../DataFlow/managing-data-flows.htm#Sharing) |
| Open in new tab | You can open your data flow in a new tab. | - |
| Details | You can view the data flow owner, as well as relevant date information for the data flow. Additionally, you can view the data flow size. This page also shows the tags applied to the data flow and who can access the data flow. You can also see run history. | [*Seeing data flow details*](../DataFlow/managing-data-flows.htm#Seeing) |
| Manage > Favorite | Add this data flow to your Favorites. | - |
| Manage > Add to collection | You can add the data flow to one of your collections. | [*Adding data flows to collections*](../DataFlow/managing-data-flows.htm#Adding) |
| Manage > Edit details | You can change the data flow name, description, and tags. | [*Editing data flow details*](../DataFlow/managing-data-flows.htm#Editing) |
| Manage > Notification settings | Set notification preferences for this data flow . You can receive notifications when runs succeed or fail. You can also receive notifications if a scheduled run for a data flow failed, stopped, or was deactivated. You must be the owner of the scheduled task to receive this notification. You will not receive notifications if a data flow is run from the data flow interface. Run notifications are sent if a data flow is run in an activity center or on a schedule. | [*Configuring data flows notifications*](../DataFlow/managing-data-flows.htm#Configur) |
| Manage > Move to space | You can move the data flow to a different space. | [*Moving data flows*](../DataFlow/managing-data-flows.htm#Moving) |
| Manage > Duplicate | You can create a copy of the data flow. | [*Duplicating data flows*](../DataFlow/managing-data-flows.htm#Duplicat) |
| Manage > Duplicate as script | You can convert the data flow to a script. | [*Converting data flows to script*](../DataFlow/managing-data-flows.htm#Converti) |
| Manage > Publish to space | Publish the data flow to a managed space. | [*Publishing data flows*](../DataFlow/managing-data-flows.htm#Publishi) |
| Run > Run now | You can run the data flow manually. | [*Running data flows*](../DataFlow/managing-data-flows.htm#Reloadin) |
| Run > Schedule | You can create tasks to schedule runs of the data flow. | [*Scheduling data flows runs*](../DataFlow/managing-data-flows.htm#Scheduli) |
| Run > History |  | - |
| Tools > Lineage | Lineage represents the history of a field or dataset, back through applications and transforms, to the original data source. | [*Viewing lineage*](../DataFlow/managing-data-flows.htm#Viewing) |
| Tools > Impact analysis | Impact analysis shows a downstream view of a data element’s dependencies - which databases, applications, scripts files, links, or other content would directly or indirectly be impacted if the value or structure of that particular field was changed. | [*Viewing impact analysis*](../DataFlow/managing-data-flows.htm#Viewing2) |
| Download | You can download data flows as .dfw files. | [*Exporting data flows*](../DataFlow/managing-data-flows.htm#Exportin) |
| Delete | You can delete the data flow. | [*Deleting data flows*](../DataFlow/managing-data-flows.htm#Deleting) |

## Table recipes (Analytics)

A table recipe allows you to easily prepare tabular datasets within a no-code, spreadsheet-like interface. Iteratively explore, clean, and transform data through a series of reusable steps to produce a recipe.

For more information, see [*Loading and preparing data with Table recipe*](../TableRecipe/loading-preparing-with-table-recipe.htm).

Table recipe options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this table recipe by adding them to the space with a chosen role. | [*Sharing table recipes*](../TableRecipe/managing-table-recipes.htm#Sharing) |
| Share > Copy link | Copy a link to the table recipe. |  |
| Share > Manage access | Manage user access to this table recipe or space the table recipe is in. | [*Sharing table recipes*](../TableRecipe/managing-table-recipes.htm#Sharing) |
| Open in new tab | You can open your table recipe in a new tab. | - |
| Details | You can view the table recipe owner, as well as relevant date information for the data flow. Additionally, you can view the table recipe size. This page also shows the tags applied to the table recipe and who can access the data flow. You can also see run history. | [*Seeing table recipe details*](../TableRecipe/managing-table-recipes.htm#Seeing) |
| Manage > Favorite | Add this table recipe to your Favorites. | - |
| Manage > Add to collection | You can add the table recipe to one of your collections. | [*Adding table recipes to collections*](../TableRecipe/managing-table-recipes.htm#Adding) |
| Manage > Edit details | You can change the table recipe name, description, and tags. | [*Editing table recipe details*](../TableRecipe/managing-table-recipes.htm#Editing) |
| Manage > Notification settings | Set notification preferences for this table recipe. You can receive notifications when runs succeed or fail. You can also receive notifications if a scheduled run for a table recipe failed, stopped, or was deactivated. You must be the owner of the scheduled task to receive this notification. You will not receive notifications if a table recipe is run from the table recipe interface. Run notifications are sent if a table recipe is run in an activity center or on a schedule. | - |
| Manage > Move to space | You can move the table recipe to a different space. | [*Moving table recipes*](../TableRecipe/managing-table-recipes.htm#Moving) |
| Manage > Publish to space | Publish the table recipe to a managed space. | - |
| Manage > Duplicate | You can create a copy of the table recipe. | [*Duplicating table recipes*](../TableRecipe/managing-table-recipes.htm#Duplicat) |
| Manage > Duplicate as data flow | You can convert the table recipe to a data flow. | [*Converting table recipes to a data flow*](../TableRecipe/managing-table-recipes.htm#Converti2) |
| Manage > Duplicate as script | You can convert the table recipe to a script. | [*Converting table recipes to script*](../TableRecipe/managing-table-recipes.htm#Converti) |
| Run > Run now | You can run the table recipe manually. | [*Running table recipes*](../TableRecipe/managing-table-recipes.htm#Running) |
| Run > Schedule | You can create tasks to schedule runs of the table recipe. | [*Scheduling table recipes runs*](../TableRecipe/managing-table-recipes.htm#Scheduli) |
| Run > History |  |  |
| Tools > Lineage | Lineage represents the history of a field or dataset, back through applications and transforms, to the original data source. | [*Viewing a table recipe lineage*](../TableRecipe/managing-table-recipes.htm#Viewing) |
| Tools > Impact analysis | Impact analysis shows a downstream view of a data element’s dependencies - which databases, applications, scripts files, links, or other content would directly or indirectly be impacted if the value or structure of that particular field was changed. | [*Viewing a table recipe impact analysis*](../TableRecipe/managing-table-recipes.htm#Viewing2) |
| Download | You can download table recipes as .dfw files. | [*Exporting table recipes*](../TableRecipe/managing-table-recipes.htm#Exportin) |
| Delete | You can delete the table recipe. | [*Deleting table recipes*](../TableRecipe/managing-table-recipes.htm#Deleting) |

## Notes (Insights and Analytics)

Notes are text commentary added by users. To learn more about notes, see [*Working with notes*](../Notes/notes-using.htm).

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the notes including:

Note options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this note by adding them to the space with a chosen role. | - |
| Share > Copy link | Copy a link to the chart. | - |
| Share > Manage access | Manage user access to this note or space the note is in. | - |
| Open in new tab | You can open your note in a new tab. | - |
| Details | You can view metadata for the note, including owner, space, and relevant dates. | - |
| Manage > Favorite | Add this note to your Favorites. | - |
| Manage > Add to collection | You can add the note to one of your collections. | - |
| Manage > Edit details | You can change the note name, description, and tags. | - |
| Manage > Notification settings | Set notification preferences for this note. | - |
| Delete | You can delete the note. | - |

## Links (Insights and Analytics)

Links are hyperlinks, typically to external content, added to activity centers. To learn more about links, see [*Adding links in the Analytics activity center*](../Hub/links.htm).

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the links including:

Link options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this link by adding them to the space with a chosen role. | [*Adding links in the Analytics activity center*](../Hub/links.htm) |
| Share > Copy link | Copy the link. | - |
| Share > Manage access | Manage user access to this link or space the link is in. | - |
| Open in new tab | You can open your link in a new tab. | - |
| Details | You can view metadata for the link, including owner, space, and relevant dates. | - |
| Manage > Favorites | Add this link to your Favorites. | - |
| Manage > Add to collection | You can add the link to one of your collections. | - |
| Manage > Edit details | Edit the link. | - |
| Manage > Move to space | Move the link to another space. | - |
| Delete | You can delete the link. | - |

## Automations (Analytics)

Automations are automated analytics and data workflows, such as workflows that collect information from one application and pass it to another. To learn more about automations, see [*Qlik Automate*](../../Sense_QlikAutomation/introduction/home-automation.htm).

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the automations including:

Automation options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Copy link | Copy a link to the automation. | - |
| Open in new tab | You can open your automation in a new tab. | - |
| Details | You can view metadata for the automation, including owner, space, and relevant dates. | - |
| Manage > Favorite | Add this automation to your Favorites. | - |
| Manage > Add to collection | You can add the automation to one of your collections. | - |
| Manage > Edit details | You can change the automation name, description, and tags. | - |
| Manage > Notification settings | Set notification preferences for this notification. You can receive notifications when runs fail. | - |
| Manage > Move to space | Move the automation to another space. | - |
| Manage > Duplicate | Duplicate the automation. | - |
| Delete | You can delete the automation. | - |

## ML deployments (Analytics)

ML deployments are machine-learning models that have been deployed to make predictions. To learn more about ML deployments, see [*Working with ML deployments*](../AutoML/working-with-deployments.htm).

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the ML deployment including:

ML deployment options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this ML deployment by adding them to the space with a chosen role. | [*Sharing ML deployments*](../AutoML/deploying-models.htm#Sharing) |
| Share > Copy link | Copy a link to the ML deployment. | - |
| Share > Manage access | Manage user access to this ML deployment or space the ML deployment is in. | [*Sharing ML deployments*](../AutoML/deploying-models.htm#Sharing) |
| Open in new tab | You can open your ML deployment in a new tab. | - |
| Details | You can view metadata for the ML deployment, including owner, space, and relevant dates. | - |
| Manage > Favorite | Add this ML deployment to your Favorites. | - |
| Manage > Add to collection | You can add the ML deployment to one of your collections. | - |
| Manage > Edit details | You can change the ML deployment name, description, and tags. | - |
| Manage > Move to space | Move the ML deployment to another space. | - |
| Tools > Lineage | You can analyze the upstream elements from which the ML deployment was created. | [*Analyzing lineage for machine learning content*](../Catalog/lineage.htm#MLLineage) |
| Tools > Impact analysis | You can analyze downstream elements that are created from, and are possibly dependent on, the ML deployment. | [*Impact analysis for machine learning content*](../Catalog/impact-analysis2.htm#MLImpact) |
| Delete | You can delete the ML deployment. | - |

## ML experiments (Analytics)

ML experiments are machine-learning experiments where data has been loaded to train a model to analyze and predict a business problem. To learn more about ML experiments, see [*Working with experiments*](../AutoML/working-with-experiments.htm).

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the ML experiments including:

ML experiment options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this ML experiment by adding them to the space with a chosen role. | [*Sharing experiments*](../AutoML/creating-experiments.htm#Sharing) |
| Share > Copy link | Copy a link to the ML experiment. | - |
| Share > Manage access | Manage user access to this ML experiment or space the ML experiment is in. | [*Sharing experiments*](../AutoML/creating-experiments.htm#Sharing) |
| Open in new tab | You can open your ML experiment in a new tab. |  |
| Details | You can view metadata for the ML experiment, including owner, space, and relevant dates. | - |
| Manage > Favorites | Add this ML experiment to your Favorites. | - |
| Manage > Add to collection | You can add the ML experiment to one of your collections. | - |
| Manage > Edit details | You can change the ML experiment name, description, and tags. | - |
| Manage > Move to space | Move the ML experiment to another space. | - |
| Tools > Lineage | You can analyze the upstream elements from which the ML experiment was created. | [*Analyzing lineage for machine learning content*](../Catalog/lineage.htm#MLLineage) |
| Tools > Impact analysis | You can analyze downstream elements that are created from, and are possibly dependent on, the ML experiment. | [*Impact analysis for machine learning content*](../Catalog/impact-analysis2.htm#MLImpact) |
| Delete | You can delete the ML experiment. | - |

## Glossaries (Analytics)

Glossaries are tools for standardizing terms and definitions in Qlik Cloud. To learn more about glossaries, see [*Working with business glossaries*](../Catalog/BusinessGlossary/Working-business-glossaries.htm).

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the glossary including:

Glossary options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this glossary by adding them to the space with a chosen role. | [*Sharing business glossaries*](../Catalog/BusinessGlossary/Working-business-glossaries.htm#Sharing) |
| Share > Copy link | Copy a link to the glossary. | - |
| Share > Manage access | Manage user access to this glossary or space the glossary is in. | [*Sharing business glossaries*](../Catalog/BusinessGlossary/Working-business-glossaries.htm#Sharing) |
| Open in new tab | You can open your glossary in a new tab. | - |
| Details | You can view metadata for the glossary, including owner, space, and relevant dates. | - |
| Manage > Favorites | Add this glossary to your Favorites. | - |
| Manage > Add to collection | You can add the glossary to one of your collections. | - |
| Manage > Edit details | You can change the glossary name, description, and tags. | - |
| Manage > Move to space | Move the glossary to another space. | - |
| Delete | You can delete the glossary. | - |

## Assistants (Insights and Analytics)

Qlik Answers assistants are AI-based assistants that provide an interface for interacting with data sources through natural language questions. To learn more about using assistants, see [*Answering questions with Qlik Answers*](../QlikAnswers/answering-questions-qlik-answers.htm). To learn more about creating assistants, see [*Working with assistants*](../QlikAnswers/Assistants/assistants.htm)

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the assistant including:

Assistant options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this assistant by adding them to the space with a chosen role. | [*Sharing assistants*](../QlikAnswers/Assistants/managing-assistants.htm#Sharing) |
| Share > Copy link |  | - |
| Share > Manage access | Manage user access to this assistant or space the assistant is in. | [*Sharing assistants*](../QlikAnswers/Assistants/managing-assistants.htm#Sharing) |
| Open in new tab | You can open your assistant in a new tab. | - |
| Details | You can view metadata for the assistant, including owner, space, and relevant dates. | - |
| Manage > Favorites | Add this assistant to your Favorites. | - |
| Manage > Add to collection | You can add the assistant to one of your collections. | - |
| Manage > Edit details | You can change the assistant name, description, and tags. | - |
| Manage > Move to space | Move the assistant to another space. | - |
| Delete | You can delete the assistant. | - |

## Knowledge bases (Insights and Analytics)

Qlik Answers knowledge bases are collections of structured data used by Qlik Answers assistants to answer questions. To learn more about working with assistants, see [*Working with assistants*](../QlikAnswers/Assistants/assistants.htm)

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the assistant including:

Knowledge base options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Invite | Give a user access to this knowledge base by adding them to the space with a chosen role. | [*Sharing knowledge bases*](../QlikAnswers/KnowledgeBases/managing-knowledge-bases.htm#Sharing) |
| Share > Copy link |  | - |
| Share > Manage access | Manage user access to this knowledge base or space the knowledge base is in. | [*Sharing knowledge bases*](../QlikAnswers/KnowledgeBases/managing-knowledge-bases.htm#Sharing) |
| Open in new tab | You can open your knowledge base in a new tab. |  |
| Details | You can view metadata for the knowledge base, including owner, space, and relevant dates. | - |
| Manage > Favorites | Add this knowledge base to your Favorites. | - |
| Manage > Add to collection | You can add the knowledge base to one of your collections. | - |
| Manage > Edit details | You can change the knowledge base name, description, and tags. | - |
| Manage > Move to space | Move the knowledge base to another space. | - |
| Delete | You can delete the knowledge base. | - |

## Skills (Analytics)

Qlik Answers skills are catalog items that teach Qlik Answers how to handle specific topics and tasks. Skills can be added to both applications and assistants. For more information, see [*Working with skills*](../QlikAnswers/Skills/working-with-skills.htm).

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the skill.

Skill options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Share > Copy link | Copy a link to the skill. | - |
| Open in new tab | You can open your skill in a new tab. | - |
| Download | You can download skills as .md files. | - |
| Details | You can view the skill description and owner, as well as relevant date information for the skill. This page also shows the tags applied to the skill. | - |
| Manage > Favorite | Add this skill to your Favorites. | - |
| Manage > Add to collection | You can add the skill to one of your collections. | - |
| Manage > Edit details | You can change the skill name, description, and tags. | - |
| Manage > Move to space | You can move the skill to a different space. | - |
| Manage > Duplicate | You can create a copy of the skill. |  |
| Delete | You can delete the skill. | - |

## Data products (Analytics)

Data products are highly trusted, re-usable, and consumable data assets. They are curated collections of productized datasets and business-approved metadata and domain logic designed to solve domain-specific business outcomes. To learn more about working with data products, see [*Working with data products*](../DataIntegration/DataProducts/Data-products.htm)

You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the data product including:

Data product options in activity centers

| Option | Description | Further reading |
| --- | --- | --- |
| Use in > Application | Create a new application using this data product. | [*Loading data from the data marketplace*](../DataIntegration/Marketplace/loading-data-from-marketplace.htm) |
| Use in > Table recipe | Create a new table recipe using this data product. | [*Loading data from the data marketplace*](../DataIntegration/Marketplace/loading-data-from-marketplace.htm) |
| Use in > Data flow | Create a new data flow using this data product. | [*Loading data from the data marketplace*](../DataIntegration/Marketplace/loading-data-from-marketplace.htm) |
| Use in > Script | Create a new script using this data product. | [*Loading data from the data marketplace*](../DataIntegration/Marketplace/loading-data-from-marketplace.htm) |
| Use in > ML Experiment | Create a new ML experiment using this data product. | [*Loading data from the data marketplace*](../DataIntegration/Marketplace/loading-data-from-marketplace.htm) |
| Share > Invite | Give a user access to this data product by adding them to the space with a chosen role. | - |
| Share > Copy link |  | - |
| Share > Manage access | Manage user access to this data product or space the data product is in. | - |
| Open in new tab | You can open your data product in a new tab. | - |
| Details | You can view metadata for the data product and other options. | - |
| Manage > Favorites | Add this data product to your Favorites. |  |
| Manage > Add to collection | You can add the data product to one of your collections. | - |
| Manage > Edit details |  | - |
| Manage > Move to space |  | - |
| Tools > Lineage | Lineage represents the history of a field or dataset, back through applications and transforms, to the original data source. | [*Analyzing lineage in Analytics*](../Catalog/lineage.htm) |
| Tools > Impact analysis | Impact analysis shows a downstream view of a data element’s dependencies - which databases, applications, scripts, files, or links would directly or indirectly be impacted if the value or structure of that particular field was changed. | [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm) |
| Delete | You can delete the data product. | - |
