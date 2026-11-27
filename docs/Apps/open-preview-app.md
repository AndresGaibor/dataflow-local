---
title: "Opening and previewing applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/open-preview-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Understanding applications"]
---

# Opening and previewing applications

You can open or preview applications from your activity centers. Applications, especially large or complex ones that take longer to load, may offer a preview as an alternative to opening the application. This loads a sheet selected by the application creator for you to use while the application finishes loading in the background.

Application preview is useful when you need to quickly verify information in an application or make a fast decision without waiting for the entire application to load. When you preview an application, the preview sheet displays with the latest data from the application. You cannot make selections in a preview.

Information note

Preview is not available in the following regions:

- il-central-1
- eu-west-3
- eu-north-1

## Opening an application

Do the following:

1. In an activity center, locate the application.
2. Click the application.

   If both Open application and Open preview appear when you hover over the application, click Open application.

   Alternatively, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Open in new tab.

## Opening an application without data

In some cases, you may want to open an application without loading its data, for example when there are large amounts of data that would take a long time to load.

When you open an application without data, visualizations will not work, as they are not connected to the data source. Additionally, the data manager and the data model viewer will not be available.

Do the following:

1. In an activity center, locate the application.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Tools > Open without data.

   The application opens without loading its data.

The application opens, and you can access the data load editor to update the load script, and view or work with the layout of sheets and stories.

You can work with the layout of sheets and stories, to reorganize the content, for example, but you will only see representations of the visualizations. You cannot update measures or dimensions. You can make changes to the data load script, if you want to. Once you run the script in the data load editor successfully, the application visualizations will work as intended and will be ready to be used for data analysis.

## Previewing an application

You can preview an application from an activity center when the application creator has configured a preview sheet. The options that appear depend on how the creator configured the application preview. For more information, see [*Configuring application previews*](set-preview-sheet.htm).

The preview renders as sheet in the application for you to look at while the rest of the application loads. This can be useful when working with large applications with longer load times. Visualizations in the preview sheet are rendered as snapshots with limited interactivity or as images.

Do the following:

1. In an activity center, locate the application.
2. Hover over the application, and then click Open preview.

   Alternatively, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Preview.

   The preview sheet opens with updated data.

Information noteThe Open preview option appears only when the application creator has configured a preview sheet and selected an opening behavior that includes the preview.

### Viewing application details from a preview

You can view the details of an application without leaving the preview.

Do the following:

- In the preview, click Show details.

  The application details display.

### Opening the full application from a preview

You can open the application from the preview. An Application loaded indicator confirms when the application has finished loading.

Do the following:

- In the preview, click Open application.

  The full application opens.

## Learn more

- [*Configuring application previews*](set-preview-sheet.htm)
- [*Opening the application*](open-the-app.htm)
- [*Setting a default bookmark to create an application landing page*](../Bookmarks/set-default-bookmark.htm)
