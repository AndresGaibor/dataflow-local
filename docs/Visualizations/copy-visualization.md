---
title: "Copying a visualization from an existing visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/copy-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Copying a visualization from an existing visualization

You can copy a [visualization](#glossary-0 "Glossary term"):

- Within the same sheet.
- Between sheets in the same application.
- Between sheets belonging to different applications (see [*Considerations*](#Considerations) for more information).

Do the following:

1. Click on the item you want to copy.

   The item is highlighted.
2. Right-click the visualization and select ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) Copy.
3. To insert the item on another sheet, navigate to the sheet in the assets panel.
4. Right-click in the sheet and click ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg) Paste.

The copied item is added to the sheet.

Information note

Depending on what situation you are in, different things will happen when you paste the copied visualization on a sheet:

- If a visualization is selected, then the selected visualization will be replaced.
- If no visualization is selected, then the pasted visualization will be placed in the largest empty space.
- If there is no empty space, then the largest visualization on the sheet will be split in half to make space for the pasted visualization.

## Pasting text and images from your clipboard

In edit mode, you can also paste text and images directly from your system clipboard.

- Pasting text or formatted text into an empty area of a sheet creates a Text object.
- Pasting an image into an empty area of a sheet creates an Image object.
- If clipboard content contains both text and an image, the content is created as a Text object.
- If upload is not allowed for your role or the clipboard image format is not supported, the image is not added.
- Pasting images is not supported when using an iPad.

For more information, see [*Text*](DashboardBundle/text-object.htm), [*Image object*](Image/image-object.htm), and [*Uploading image files to media library*](../MediaLibrary/MediaLibrary-upload.htm).

## Considerations

- For a copied visualization to work in a different application, the same [dimensions](#glossary-2 "Glossary term") and [measures](#glossary-3 "Glossary term") have to be a part of the target application as well.
- When copying visualizations between two applications, the applications must be in the same Qlik Cloud [tenant](#glossary-4 "Glossary term").
- You cannot copy and paste visualizations between different environment types (for example, between an application in Qlik Cloud Analytics and an application in Qlik Sense Desktop).

## Permissions

To paste a copied visualization onto a sheet, you need:

- Permissions for editing the sheet. This means that the sheet needs to be private to you.
- Professional user entitlement (applies only to user-based subscriptions).
- Applications in [shared spaces](#glossary-5 "Glossary term"): Owner, Can manage, Can edit data in applications, or Can edit role in the space.
- Applications in [managed spaces](#glossary-6 "Glossary term"): Owner or Can manage , or Can contribute role in the space.

For more information about the required space roles, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)

As with any other sheet content, a visualization pasted onto a sheet that has been published or made public can be edited or deleted by any user who has permissions to make the sheet private.

## Copying sheets

You can also copy and paste entire sheets between applications. For more information, see [*Copying and pasting sheets*](../Sheets/reusing-sheets-and-sheet-content.htm#CopySheet).

## Learn more

- [*Keyboard navigation and shortcuts in apps*](../UserInterface/keyboard-navigation-and-shortcuts.htm)
