---
title: "Reusing sheets and sheet content"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/reusing-sheets-and-sheet-content.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with sheets"]
---

# Reusing sheets and sheet content

You can reuse content on [sheets](#glossary-0 "Glossary term") and duplicate sheets.

## Copying, replacing and moving items on sheets

You can copy, replace, and move items on a sheet and between sheets. You can do this in the following ways:

- Using the edit bar on the sheet (![Cut](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cut.svg), ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) and ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg)).
- By right-clicking and selecting Cut, Copy and Paste.
- With the keyboard shortcuts Ctrl+C, Ctrl+X and Ctrl+V.

## Duplicating a sheet

You can duplicate any sheet, regardless of whether it is a sheet that belongs to the application or a sheet you have created yourself. The purpose of duplicating sheets is to save time by reusing content, and to allow you to modify the duplicate so that it fits your needs better. A duplicated sheet contains the same visualizations as the original sheet, and is linked to the same master items. The duplicated sheet is a standalone sheet with no connection to the original sheet. Duplicated sheets appear under My own in application overview and in Sheets in the assets panel.

You can duplicate a sheet in the following ways:

- Click Duplicate in the shortcut menu of a sheet in the application overview or in the sheet navigator.
- Click Duplicate sheet in the global menu in the application overview or in sheet view.

## Copying and pasting sheets

You can copy and paste sheets. Copying and pasting makes it easy to create copies of content, and enhances collaboration.

You can copy and paste sheets from the Assets panel in sheet view, or in the application overview.

Do the following:

1. Open the application containing the sheet to copy.
2. In sheet view, expand the Assets panel and open Sheets.
3. Right-click the sheet and click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) Copy.
4. In the target application (or in the same application), expand the Assets panel and open Sheets.
5. Under My own, right-click a blank area and click ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg) Paste.

### Copying and pasting sheets between two different applications

You can copy and paste sheets between applications. For example, you might have duplicated an application and want to update the original application with a newly created sheet.

The following considerations apply:

- To copy sheets between applications, the two applications must exist in the same Qlik Cloud [tenant](#glossary-1 "Glossary term").
- You cannot copy and paste sheets between different environment types (for example, between an application in Qlik Cloud Analytics and an application in Qlik Sense Desktop).
- For the visualizations on the sheet to populate with data, the dimensions and measures used in the sheet visualizations must exist in the target application. The custom styling applied to the sheet, and to its visualizations, will be transferred regardless of whether or not the data matches.

## Permissions

To paste a copied sheet into an application, you need:

- Professional user entitlement (applies only to user-based subscriptions).
- Applications in [shared spaces](#glossary-2 "Glossary term"): Owner, Can manage, Can edit data in applications, or Can edit role in the space.
- Applications in [managed spaces](#glossary-3 "Glossary term"): Owner or Can manage , or Can contribute role in the space.

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)

As with any other sheet content, when you paste a sheet and make it public, other users with sufficient permissions can perform actions such as:

- Copying and pasting the sheet.
- Duplicating the sheet.
- Deleting the sheet.
- Making the sheet private.
