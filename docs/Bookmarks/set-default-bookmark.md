---
title: "Setting a default bookmark to create an application landing page"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Bookmarks/set-default-bookmark.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Bookmarking selections"]
---

# Setting a default bookmark to create an application landing page

You can select a [sheet](#glossary-0 "Glossary term") to be the landing page of your application by setting a default [bookmark](#glossary-2 "Glossary term"). When you open the application, the layout state and the selection state of the default bookmark are used.

If you do not set a default bookmark, the application overview is displayed when the application is opened.

Consider the following when using default bookmarks.

- You can only set one default bookmark for an application.
- You can clear the selection of the default bookmark when viewing a sheet. However, the bookmark will be applied when you re-open or reload the sheet.
- When you duplicate an application, the default bookmark is duplicated with the application.
- If you have the same application open in an active session in another tab, the default bookmark will not override the selections made in the other tab.

For more information about bookmarks, see [*Bookmarking selections*](keep-track-of-important-data.htm).

You can use a default bookmark in conjunction with the Always one selected value for a field to highlight specific selections for your application consumer. For more information about the Always one selected value, see [*Always one selected value*](../DataSource/select-single-value.htm).

Information noteIn previous versions of Qlik Sense, the default bookmark would only apply the selection state of the bookmark.

## Set a default bookmark

Do the following:

1. In a sheet, click Bookmarks in the asset panel.
2. Right-click an existing bookmark, and then click Set as default bookmark.
3. Click the bookmark. The bookmark is now listed as default and the selections are shown in the application.
4. To test that the default bookmark is working properly, close and then reopen the application. The default bookmark sheet and selections should be shown.

To remove a bookmark as the default, open the Bookmarks window in an unpublished application, and then right-click the default bookmark. Click Remove as default bookmark. The next time you open the application, the application overview is shown.

For more information about creating bookmarks, see [*Creating bookmarks*](create-bookmark.htm).
