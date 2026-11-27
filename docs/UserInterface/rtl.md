---
title: "Right-to-left reading order in apps"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/rtl.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Right-to-left reading order in apps

Reading orders specify the direction of the characters in strings of text and numbers.

The default reading order in a Qlik Sense application is left to right. You can change the reading order to right-to-left in your application preferences, for example, if your data or labels are in a right-to-left language such as Arabic or Hebrew.

The reading order affects the whole application.

When the right-to-left reading order is turned on from application options it affects the application in the following ways:

- The [visualizations](#glossary-1 "Glossary term") are displayed from right to left.
- User-provided text, such as [sheet](#glossary-2 "Glossary term") titles, will always be right aligned, regardless of the language of the provided text.
- The reading order of the text is determined by the first strongly directional character in the string:

  - A string that starts with a strongly right-to-left character, will be displayed from right to left.
  - A string that starts with a strongly left-to-right character will be displayed from left to right.
- The main toolbar and the edit panels are not affected by this setting. For these, the language depends on the language setting of the web browser Qlik Sense is running in. For more information, see [*Changing language in Qlik Cloud*](Languages.htm).

A bar chart with the right-to-left reading order turned on.

![Bar chart with right-to-left reading order.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_BarChar_rtl.png "Click to view full size")

Information noteThe right-to-left reading order does not change the reading order of the radial gauge visualization because radial gauges are always viewed left to right.

## Activating right-to-left reading order

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
2. In the menu, switch to the Appearance tab.
3. Turn Right-to-left on or off.

Information noteIf a visualization is shared using Qlik Sense Charts, changing the reading order in the application will also affect the reading order in the shared chart. For more information, see  [*The reading order is incorrect in my shared chart*](../Troubleshooting/troubleshooting-navigate-interact.htm#Right-to).

### Visualization-specific settings

You might notice some visualizations in Qlik Sense can display right-to-left languages such as Arabic or Hebrew without right-to-left reading order being activated in the application. However, to guarantee that the right-to-left reading order is applied correctly at all times and to all visualizations in the application, you need to activate this setting in the application.
