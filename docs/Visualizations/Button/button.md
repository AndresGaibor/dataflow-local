---
title: "Button"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Button/button.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Dashboard objects"]
---

# Button

You can use buttons to:

- Add quick links for easy selection and navigation in your application
- Reload data
- Run automations

## When to use the button

The button is useful when you want to help the application user by providing:

- predefined [selections](#glossary-1 "Glossary term") or selection controls
- navigation links to other [sheets](#glossary-2 "Glossary term"), [stories](#glossary-3 "Glossary term"), or websites
- reload data functionality in an application
- the ability to run an automation from an application.

You can reload data in an application that you own. App users need edit permissions. For more information, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../../Spaces/managing-managed-spaces.htm).

Example of buttons in use on a sheet

![Four buttons as they appear in Qlik Sense. They are labelled Reload Data, Clear Selections, Previous Sheet, and Next Sheet.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/buttons.png "Click to view full size")

## Mobile limitations

In the Qlik Analytics mobile app, the button is a natively rendered visualization. Natively rendered visualizations have better performance compared to visualizations rendered in WebView. If a natively rendered visualization is wrapped inside a Container object, it will be rendered in an embedded WebView.

While natively rendered visualizations have greater performance, they do not support the full breadth of object styling (general styling or theme-based styling) when viewed in the Qlik Analytics mobile app. If styling of objects is important for mobile analysis, the application developer can place the object inside a Tab container, Container, or Layout container. This forces the WebView presentation and preserves styling.

## Learn more

- [*Creating buttons*](create-buttons.htm)
