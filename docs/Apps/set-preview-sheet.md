---
title: "Configuring application previews"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/set-preview-sheet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Configuring application previews

In the settings for an application, you can control how the application opens from an activity center and which [sheet](#glossary-1 "Glossary term") users see when they preview the application.

Application preview is useful when you have a large or complex application that can take longer to open. Adding a preview to the application lets your application users quickly verify information or make a fast decision without waiting for the entire application to load.

Information note

Any selections you currently have in the application when you select a sheet are included in the preview.

Information note

Only public sheets can be used as the preview sheet. If your application has no public sheets, you cannot configure a preview.

Information note

Preview is not available in the following regions:

- il-central-1
- eu-west-3
- eu-north-1

## Configuring application preview

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
2. In the settings, click Application preview.
3. From When I click the application, select the opening behavior:

   - Open application: The full application opens. This is the default.
   - Open preview: The preview opens.
   - Both options: Both Open application and Open preview appear on the application card.
4. From Preview sheet, select a public sheet.

   Your current selections are applied to the preview.
5. Click Apply changes.

The selected sheet appears when users preview the application.

## Limitations

Application previews have the following limitations:

- Preview is not supported for applications using Section Access.
- The following visualizations do not display in previews:

  - Animator
  - Date picker
  - Trellis container
  - Variable input

## Learn more

- [*Opening and previewing applications*](open-preview-app.htm)
- [*Styling an application*](style-app.htm)
- [*Setting a default bookmark to create an application landing page*](../Bookmarks/set-default-bookmark.htm)
