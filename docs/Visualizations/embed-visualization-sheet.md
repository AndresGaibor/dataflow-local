---
title: "Embedding a visualization or a sheet in a web page"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/embed-visualization-sheet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Sharing and downloading application content"]
---

# Embedding a visualization or a sheet in a web page

You can integrate Qlik Sense [visualizations](#glossary-0 "Glossary term") or [sheets](#glossary-1 "Glossary term") into your web applications using [qlik-embed](https://qlik.dev/embed/qlik-embed/). This could for example be a web page on your intranet. You select which visualization or sheet to embed, and adjust appearance and interaction settings. Then you can copy the embed code and add it to your web content.

For more information about using qlik-embed to embed visualizations and sheets, see:

- [qlik-embed overview](https://qlik.dev/embed/qlik-embed/)
- [Authentication options](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/)
- [Explore a code example](https://qlik.dev/embed/qlik-embed/examples/quickstart-webcomponent-complete/)
- [Customizing UIs and parameters](https://qlik.dev/embed/qlik-embed/parameters/)

## Access control

The embedded object will be subject to the same access rules as the original object and application. This means that anyone who wants to view the embedded object must have:

- Access to Qlik Sense.
- Access to the application. If the application is in your personal space, you are the only one with access.
- Access to the sheet. If the sheet is not public, you are the only one with access.
- Access to any bookmark used for selection. Private bookmarks will be applied for you, but not for anyone else.
- Same access to the data used in the selection as you, if section access is used to restrict data access.

## Embedding a sheet

You can embed a sheet in your web page.

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Embed sheet.
2. Select a Theme and UI type to use for the embedded sheet.
3. Under Embed code, click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg).

   Tip noteIn this dialog, you can also view and copy the application and object IDs, and inspect the object type. This makes it easy to work with your own code, and also to retrieve this information for other purposes—for example, for use in script and chart expressions.

You now have the embed code of the sheet in your clipboard, ready to add to your web page or application using qlik-embed.

## Embedding a visualization

You can embed a visualization in your web page.

Do the following:

1. Right-click on the visualization or click the hover menu ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
2. Select Share. Then choose Embed.
3. Under Embed code, click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg).

   Tip noteIn this dialog, you can also view and copy the application and object IDs, and inspect the object type. This makes it easy to work with your own code, and also to retrieve this information for other purposes—for example, for use in script and chart expressions.

You now have the embed code of the visualization in your clipboard, ready to add to your web page or application using qlik-embed.

## Limitations of embedded objects

- On devices with a small screen, the embed modal will not be available via context menus.
- The sheet title is not included when embedding sheets, unless using [classic/app UI](https://qlik.dev/embed/qlik-embed/parameters/#classicapp).
- The Copy cell value option is not available for embedded tables, unless using [classic/app UI](https://qlik.dev/embed/qlik-embed/parameters/#classicapp).
