---
title: "Reusing assets with master items"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Assets/work-with-master-items.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Reusing assets with master items

When you create and build your [visualizations](#glossary-0 "Glossary term"), you can save assets to reuse in other visualizations and on other [sheets](#glossary-1 "Glossary term"). You can save visualizations, [dimensions](#glossary-2 "Glossary term"), and [measures](#glossary-3 "Glossary term") as master items. When your application gets published these master items will be available to others as ready-to-use visualizations, dimensions, and measures.

Any updates you make to the master item are applied everywhere the master item is used. For example, you could use a master measure in as many of your visualizations as you like while only having to update it in a single instance to update all instances of the measure in your visualizations.

One of the purposes with creating and maintaining master items is for other users to explore their own ways and directions in the data, on top of what you have provided in the application as pre-made sheets with visualizations. The users will be able to create their own visualizations with your pre-made master dimensions and master measures, for example.

## Permissions for working with master items

In shared and managed spaces within Qlik Cloud Analytics, you need specific permissions to work with the master items in an application. The sections below outline the user requirements for working with master items.

For more information, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)

### Viewing master items in an application

To view the master items in an application, you need the following:

- Professional user entitlement (applies only to user-based subscriptions).
- Applications in [shared spaces](#glossary-5 "Glossary term"): Owner, Can manage, Can edit data in applications, or Can edit role in the space.
- Applications in [managed spaces](#glossary-6 "Glossary term"): Owner, Can manage, or Can contribute role in the space. Alternatively, you can view master items if you have Can contribute access to only the application.

### Creating, editing, and deleting master items

To create, edit, and delete master items in an application, you need the following:

- Professional user entitlement (applies only to user-based subscriptions).
- Applications in [shared spaces](#glossary-7 "Glossary term"): Owner, Can manage, Can edit data in applications, or Can edit role in the space.

You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Learn more

- [*Reusing dimensions with master dimensions*](../Dimensions/create-master-dimension.htm)
- [*Reusing measures with master measures*](../Measures/create-master-measure.htm)
- [*Reusing visualizations with a master visualization*](../Visualizations/create-master-visualization.htm)
