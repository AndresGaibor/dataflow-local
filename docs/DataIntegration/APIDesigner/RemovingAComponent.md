---
title: "Removing a component"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/RemovingAComponent.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with reusable components"]
---

# Removing a component

## Un-using a component

Remove a component from an element.

1. Go to the element from which you want to remove a component.
2. Click Delete.

Your component is no longer used in the element.

Information noteNote: This action does
not delete your component from the Components tab or from any
other entity in your API.

## Deleting a component

Delete a component and remove it from all elements that use it in your
API.

1. Go to the Components tab.
2. Click the trash icon to the right of the component that you want to
   delete.
3. Click Delete to confirm.

   If your component is used in any element of your API, a dialog box listing its
   dependencies is displayed. If you delete the component, it is removed from every
   element listed. If you delete a path variable component, the variable is inlined.![Confirmation dialog box.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/designer_delete_component.png)

Your component is deleted and removed from every API entity in which it was used,
unless it is a path variable. When a path variable component is deleted, the variable is
inlined in every resource that uses it.
