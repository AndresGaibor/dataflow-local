---
title: "Tutorial - Designing sheets for PowerPoint reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/designing-and-creating-PowerPoint-reports.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with sheets"]
---

# Tutorial - Designing sheets for PowerPoint reports

Subscriptions and Qlik Automate reports can be generated in PowerPoint format. This tutorial will show you how to use custom background images and layouts, so your [sheets](#glossary-0 "Glossary term") look professional in PowerPoint slides.

## What you will learn

Once you have completed this tutorial, you will know how to design sheets that look great in PowerPoint reports. You will understand how to customize grid size and add background images to sheets.

## Who should complete this tutorial

Users who are familiar with designing applications in Qlik Cloud Analytics. You know how to make [charts](#glossary-2 "Glossary term") in edit mode.

## What you need to do before you start

You need:

- Access to Qlik Cloud Analytics.
- If you have a user-based subscription, you need Professional user entitlement. To find out what type of user you have, contact your tenant administrator. For more information, see [*Managing user entitlements*](../Admin/SaaS-user-allocations.htm).
- Two Qlik Cloud Analytics applications. Download this package and unzip it:

  [Tutorial - Designing PowerPoint Reports](/en-US/cloud-services/tutorials/DesigningPPTReports.zip)

The zip file contains two Qlik Cloud Analytics applications. Both applications already contain data and test images:

- Tester - Customer relationship management (CRM) dashboard: For users who want to complete this tutorial. This application has [visualizations](#glossary-3 "Glossary term") but the layout is unprofessional, and there are blank sheets. All the sheets in this application are set to private, so they can be edited.
- Final - Customer relationship management (CRM) dashboard: For users who want to see the final result of the tutorial. You can use this application to test subscriptions or report automations. All the sheets in this application are set to public.

## Uploading the tutorial applications

Before you start, you need to upload both applications to your [personal space](#glossary-4 "Glossary term") in Qlik Cloud Analytics. Your personal space is your own private work area in Qlik Cloud Analytics.

Do the following:

1. Log in to Qlik Cloud Analytics.
2. Go to the Create page of the Analytics [activity center](#glossary-5 "Glossary term") and select Upload.
3. Select App.
4. Drag and drop the two Qlik Cloud Analytics applications onto the dialog.
5. Make sure the space is set to Personal.
6. Click Upload.

Both applications are now in your personal space.

## First sheet: Intro

If you want to follow along with this tutorial, open Tester - Customer relationship management (CRM) dashboard. Double-click the Intro sheet.

Information noteAll of the sheets in this application are set to landscape layout. Portrait layout is not supported for sheets that will be outputted to subscriptions or automations in PowerPoint format. Sheets set to portrait layout will be converted to landscape. However, you can use portrait layout if you are using the Qlik Reporting Service API. For more information about using the API to create reports, see the [Developer Portal documentation](https://qlik.dev/apis/rest/reports).

This first sheet is meant to be the title page of a PowerPoint report. Right now, it is just black text on a white background.

Intro sheet

![Intro sheet before editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_IntroSheetTester.png "Click to view full size")

Do the following:

1. Click Edit sheet.
2. In the properties panel, click on ![styling palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling. The sheet background settings will display.
3. Under Background image, click the first drop down and select Image from media library.
4. Click ![Image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the default thumbnail.

   The Media library opens.
5. Select Q4 Title\_1920\_1080.png. A preview is displayed. Select Insert.
6. You can change the size and orientation of the background image. For this image, select Original size and Position - top left.
7. The text is too dark to read. Double-click on the text object, and change the font color to white.
8. From Charts, under Legacy, drag a Text & image object onto the sheet. You will add an expression that shows when the application was last updated.
9. In the Text & image object, type "Last updated:".Make the font color white.
10. In the properties panel, click Data > Add measure. Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg).

    The expression editor opens.
11. In the expression editor, insert: =Date(now())
12. Click Apply.
13. The expression will change whenever the application is reloaded, to show the current date.

    You can format the style of the expression the same as if it were plain text. For example, you can make the font white or make the text larger.

The first sheet now looks like the intro slide in a PowerPoint deck. You can move to the second sheet, Trends.

## Second sheet: Trends

This sheet has some interesting charts, but they are not aligned properly. This sheet has no corporate branding.

Trends sheet

![Trends sheet before editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_TrendsSheetTester.png "Click to view full size")

Do the following:

1. In the properties panel, click on ![styling palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling. The sheet background settings will display. Ensure that the toggle is set to Custom .
2. Under Background image, click the first drop down and select Image from media library.
3. Click ![Image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the default thumbnail.

   The Media library opens.
4. Select Side Panel.png. A preview is displayed. Select Insert.
5. You can change the size and orientation of the background image. For this image, select Fit to Width and Position - top left.
6. Our background image is overlapping with some of the charts. Because the grid spacing is set to wide, it is difficult to align the charts properly.
7. Go to Grid spacing, and select Custom in the drop down.
8. Move the slider all the way to the right to make the grid squares as small as possible.
9. Adjust the size of the charts so they line up evenly.

This sheet is now organized and has a background image set as a side panel. Move to the next sheet, Revenues.

## Third sheet: Revenues

This sheet has a KPI in red text displaying how much revenue has been earned. There is a lot of white space. Adding a background image will make it seem like the KPI is part of the image.

Revenues sheet

![Revenues sheet before editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_RevenuesSheetTester.png "Click to view full size")

Do the following:

1. In the properties panel, click on ![styling palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling. The sheet background settings will display.
2. Under Background image, click the first drop down and select Image from media library.
3. Click ![Image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the default thumbnail.

   The Media library opens.
4. Select Revenue background 1980x1080.png. A preview is displayed. Select Insert.
5. Change the size to Stretch to Fit.

This single KPI now has a dynamic background. Move to the next sheet, Revenue by Industry.

## Fourth sheet: Revenue by Industry

This sheet has several charts, but a lot of white space. Let's add an image as a border.

Revenue by Industry sheet

![Revenues by Industry sheet before editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_RevenuesIndustrySheetTester.png "Click to view full size")

Do the following:

1. In the properties panel, click on ![styling palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling. The sheet background settings will display.
2. Under Background image, click the first drop down and select Image from media library.
3. Click ![Image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the default thumbnail.

   The Media library opens.
4. Select Q4 Background Slide\_1920\_1080.png. A preview is displayed. Select Insert.
5. Change the size to Stretch to Fit.

The sheet now has a bar of color on the top and bottom. Move to the next sheet, The end.

## Fifth sheet: The end

This sheet is meant to let the audience know that the PowerPoint presentation is over. Right now it is blank. You will add an animated .gif as a background image.

The end sheet

![The end sheet before editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_TheEndSheetTester.png "Click to view full size")

Do the following:

1. In the properties panel, click on ![styling palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling. The sheet background settings will display.
2. Under Background image, click the first drop down and select Image from media library.
3. Click ![Image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the default thumbnail.

   The Media library opens.
4. Select Qlik\_Outro\_Presentation.gif. A preview is displayed. Select Insert.
5. Change the size to Always fill and Position - top left.

The sheet now has a large animation. The .gif will be animated in the sheet or a PowerPoint report, but not in a PDF.

Move to the next sheet, Thank you.

## Sixth sheet: Thank you

This sheet is meant to let the audience know they can ask questions. Right now it is black text on a white background. You will add the same background image used in the first sheet. This way, the first and last PowerPoint slides have the same image.

Thank you sheet

![Thank you sheet before editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ThankYouSheetTester.png "Click to view full size")

Do the following:

1. In the properties panel, click on ![styling palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling. The sheet background settings will display.
2. Under Background image, click the first drop down and select Image from media library.
3. Click ![Image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the default thumbnail.

   The Media library opens.
4. Select Q4 Title\_1920\_1080.png. A preview is displayed. Select Insert.
5. You can change the size and orientation of the background image. For this image, select Original size and Position - top left.
6. The text is too dark to read. Double-click on the text object, and change the font color to white.

You now have six sheets that look like a professional PowerPoint deck. Click Edit sheet to stop editing.

Intro sheet

![Intro sheet after editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_IntroSheetFinal.png "Click to view full size")

Trends sheet

![Trends sheet after editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_TrendsSheetFinal.png "Click to view full size")

Revenues sheet

![Revenues sheet after editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_RevenuesSheetFinal.png "Click to view full size")

Revenue by Industry sheet

![Revenue by Industry sheet after editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_RevenueIndustrySheetFinal.png "Click to view full size")

The end sheet

![The end sheet after editing. This is a decorative animated gif that shows the Qlik logo.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Qlik_Outro_Presentation.gif "Click to view full size")Replay animation

Thank you sheet

![Thank you sheet after editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ThankYouSheetFinal.png "Click to view full size")

## Next steps

Your application is now ready to be added to a [subscription](#glossary-6 "Glossary term") or report automation.

Subscriptions are a good choice if you need to apply section access to your reports. For more information, see [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm).

Reporting automations allow you to created more complex reports, such as reports with looping. For more information, see [*Creating a report using Qlik Automate*](../Reporting/Automations/Create-automations-report.htm).

If you are creating an automated report that will run on a schedule, you should make sure your application data is also reloading on a schedule. For more information, see [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm).
