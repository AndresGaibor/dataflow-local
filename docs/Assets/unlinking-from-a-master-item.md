---
title: "Unlinking from a master item"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Assets/unlinking-from-a-master-item.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Unlinking from a master item

Unlink a [dimension](#glossary-0 "Glossary term") or [measure](#glossary-1 "Glossary term") in a [visualization](#glossary-2 "Glossary term") from its [master item](#glossary-3 "Glossary term") to edit only the current instance of the dimension or measure. Unlinking removes the connection to the master item, and the dimension or measure becomes independent. If you want to update all instances of a linked dimension or linked measure, you must edit the master item. For more information, see [*Editing a master dimension*](edit-master-dimension.htm) or [*Editing a master measure*](edit-master-measure.htm).

## Unlinking from the properties panel

Unlink from a master dimension or master measure in a visualization using the [properties](#glossary-4 "Glossary term") panel.

Do the following:

1. Click ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet.

   The properties panel opens on the right-hand side.
2. Select the visualization on the [sheet](#glossary-5 "Glossary term").

   The properties for the selected visualization are displayed in the properties panel.
3. Under Data, locate and click the dimension or measure.

   A linked dimension or measure is indicated by the symbol ![Unlink](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg).
4. Click ![Unlink](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg).

   A dialog is displayed that you are about to unlink from a master item
5. Click OK.

You can now edit the dimension or measure in the visualization without affecting any visualization that use the master items.

Information noteYou can only unlink from a single dimension, not a drill-down dimension.
