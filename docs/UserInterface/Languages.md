---
title: "Changing language in Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Introducing Qlik Cloud", "Qlik Cloud interface overview"]
---

# Changing language in Qlik Cloud

By default, Qlik Cloud tries to automatically detect your language preferences from your system settings, browser settings, or administrator-configured IdP settings. You can manually set your preferred language. If you are an application or script creator, you can also set the preferred regional settings for your apps and scripts.

Qlik Cloud is available in the following languages:

- English
- German
- Spanish
- French
- Italian
- Japanese
- Dutch
- Brazilian Portuguese
- Russian
- Swedish
- Simplified Chinese
- Polish
- Turkish
- Korean
- Traditional Chinese

Information note
Language settings in browser-based Qlik Cloud are separate from language settings for the Qlik Analytics mobile app. For more information, see [*Setting your preferred language for the Qlik Analytics mobile app*](../Mobile/qsmsaas-using.htm#Setting).

## How the language is detected

By default, Qlik Cloud selects your language from one of two settings:

- From your organization's IdP settings.
- From your browser or system settings.

If your browser or IdP language is not a supported by Qlik Cloud, Qlik Cloud will use English.

The following table lists how Qlik Cloud detects in which language to display content based on browser or system settings.
Some examples of common and supported web browsers and operating systems are listed.

Language detection in common and supported web browsers and operating systems

| Web browser | Operating system | Language setting detected |
| --- | --- | --- |
| Google Chrome | Windows | Browser language preference |
| Safari | macOS | Operating system locale |
| Safari | iOS | Operating system locale |
| Mozilla Firefox | Windows | Preferred content language |
| Microsoft Edge | Windows | Operating system language |

Information noteThe user interface language only influences in which language Qlik Cloud is displayed.

## Setting your preferred language in Qlik Cloud

You can set your preferred language in your personal settings. This will overrule the detected language in Qlik Cloud.

Do the following:

1. Click your user profile and select Settings.
2. Select Language and regions.
3. Under Preferred language, select your language.

## Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics

You can set the default regional settings for the apps and scripts you create.
Regional settings include formatting for money, dates, and decimals as well as the localization of names of days and months. You can view and edit your application regional settings in Data load editor. For information on editing these settings, see [*Modifying regional settings for applications and scripts*](../Apps/regional-settings-in-apps.htm). Regional settings do not change the language for users accessing the application or script aside from the settings that are localized to the selected region, such as day names.

If you do not set a preferred regional setting, your apps and scripts will use English (United States).

Do the following:

1. Click your user profile and select Settings.
2. Select Language and regions.
3. Under Regional settings for creating apps and scripts, select your preferred region.

## Setting the application reading order in Qlik Cloud Analytics

The default reading order in a Qlik Sense application is left to right. You can change the reading order to right-to-left in your application preferences, for example, if your data or labels are in a right-to-left language such as Arabic or Hebrew. For more information, see [*Right-to-left reading order in apps*](rtl.htm).
