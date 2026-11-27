---
title: "Uploading image files to media library"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/MediaLibrary/MediaLibrary-upload.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Uploading image files to media library

You can upload images to the media library. Because of limitations in the web browsers supported by Qlik Sense, it is recommended to keep the height and width as well as the file size of the images as small as possible. The maximum file size is 5 MB.

The following formats are supported: .png, .jpg, .jpeg, and .gif.When using Qlik Sense in Qlik Cloud, you upload images to the In app folder in the media library.

You can open the media library in several ways:

- From the application details area. Do the following:

  1. In an application, click the application name in the navigation bar at the top of the screen.
  2. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Edit details.
  3. Click ![Select image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the application thumbnail.
- When editing a sheet. For example:

  - Add an Image object to the sheet. In the properties, select Media library as the Image source.
  - Double-click a Text & image visualization on the sheet and click ![Select image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg).
  - Click the title area on a [sheet](#glossary-0 "Glossary term"). Next, in the properties panel, click ![Select image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) under Thumbnail.
  - Follow the procedure for adding a background image to a chart or sheet, then click ![Select image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg).

    Example, for bar chart: [*Customizing the background*](../Visualizations/Bar-Chart/create-bar-charts.htm#CustomBackground)

    Example, for sheet: [*Adding a background color or image*](../Sheets/styling-sheets.htm#CustomBackground)
- In Storytelling view, click ![Select image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) in the toolbar.

The Media library dialog opens and now you can upload images.

Do the following:

1. Select New upload.
2. Do one of the following:

   - Drop one or more image files onto the designated area.
   - Click the designated area to open the upload dialog, browse and select images, and click Open.
   - Paste an image from your clipboard (Ctrl+V) while the Media library dialog is open.

   An upload indicator is displayed while the image file is being uploaded. You can cancel an ongoing upload by clicking on ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg) on the image.

   Information noteYou cannot upload a file if its file name already exists in the media library.

   Tip noteYou can also add images to the media library without opening the media library. Simply paste an image from your clipboard onto the sheet. The image is automatically added to the media library and to the sheet.

Now you have added images to the media library. Click the image and select ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) to insert the image.

## Permissions and visibility of media library content

In Qlik Cloud, access to the media library is controlled by user entitlement and space permissions. Without sufficient privileges, you cannot see or manage the content in an application's media library. However, media library content that is used in thumbnails, public sheets, and public stories can be seen by all application consumers.

### Entitlement and permissions

This section lists the entitlements and permissions users need to access media library content.

For more information, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)

#### Viewing media library content

Any user meeting the requirements in the list below can view the media library content of an application in Storytelling.

- Professional user entitlement (applies only to user-based subscriptions).
- Applications in [shared spaces](#glossary-1 "Glossary term"): Owner, Can manage, Can edit data in applications, Can edit, or Can view role in the space.
- Apps in [managed spaces](#glossary-2 "Glossary term"): Owner, Can manage, Can contribute, Can view, Has restricted view, or Can operate role in the space.

#### Creating and managing media library content

Any user meeting the requirements in the list below can create, edit, and delete the media library content in an application.

- Professional user entitlement (applies only to user-based subscriptions).
- Applications in [shared spaces](#glossary-3 "Glossary term"): Owner, Can manage, Can edit data in applications, or Can edit role in the space.
- Applications in [managed spaces](#glossary-4 "Glossary term"): Owner, Can manage, or Can operate role in the space.

### Exported applications

When an application is exported and re-uploaded into Qlik Cloud, the user who re-uploads it can access all media library content.

### Administrator access

Tenant and analytics administrators can access the media library content for an application in any shared or managed space, but they must add themselves to the space first.

Tenant administrators can access the media library content in any application in another user's personal space, but they need to change the application owner first.

## Learn more

- [*Changing the thumbnail of an application*](../Apps/change-thumbnail-app.htm)
- [*Text & image*](../Visualizations/TextAndImage/text-image.htm#Adding)
- [*Adding images to a slide*](../StoryTelling/Media/add-image-to-slide.htm)
- [*Styling an application*](../Apps/style-app.htm)
