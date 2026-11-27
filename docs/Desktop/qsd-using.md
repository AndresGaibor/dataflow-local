---
title: "Using Qlik Sense Desktop"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Desktop/qsd-using.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Sense Desktop"]
---

# Using Qlik Sense Desktop

Use Qlik Sense Desktop to create [visualizations](#glossary-0 "Glossary term"), [charts](#glossary-1 "Glossary term"), interactive dashboards and analytics applications for local and offline usage in a contained environment, that is your local computer, before uploading them to Qlik Cloud.

## Starting Qlik Sense Desktop

You start Qlik Sense Desktop from the Start menu under the Qlik Sense program group.

Before you can start using Qlik Sense Desktop, you need to authenticate yourself against a Qlik Sense Enterprise server. You need to have a working network connection to enable authentication.

After you have been authenticated once, internet access is not required to continue using Qlik Sense Desktop. However, you have to re-authenticate yourself if thirty days have passed since you last authenticated, if you have logged out, or if your administrator has revoked your user access for Qlik Sense Enterprise server. If you are using SAML authentication and close the browser, the session ends and the cookie is deleted so you must re-authenticate yourself to start a new session.

Information noteQlik Sense Desktop runs in the language of your operating system and the language cannot be altered, unless you open and run Qlik Sense Desktop in a web browser.

## Opening Qlik Sense Desktop in a web browser

By default, Qlik Sense Desktop runs in a window of its own. But you can also open it in a web browser.

You must log in using Qlik Sense Desktop before you can open it in a web browser.

Do the following:

1. Start Qlik Sense Desktop from the start menu.
2. Open a (supported) web browser.
3. Type http://localhost:4848/hub in the browser address bar.

Qlik Sense Desktop opens in the web browser, showing the hub with all your applications.

## The Qlik Sense Desktop hub

When Qlik Sense Desktop starts up, you arrive at the hub. The hub is where you find all your applications. Click an application in the hub to open it in a separate tab.

The Qlik Sense Desktop hub with the Work view open

![Qlik Sense Desktop hub view.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Hub_dt3.png "Click to view full size")

### A: Toolbar

The toolbar contains the global menu and other useful commands.

Toolbar options

| UI item | Description |
| --- | --- |
| Menu | Toggle on and off the navigation menu |
| Search | You can search to easily find a specific application. |
| More | Global menu with options Dev Hub, Help and About.  You can click the Client authentication link to enable using Qlik Sense Desktop.  To learn more about Dev Hub, see [Dev Hub](/en-US/sense-developer/November2026/Subsystems/Dev-Hub/Content/Sense_Dev-Hub/dev-hub-at-a-glance.htm). |

### B: Login information

Login information options

| UI item | Description |
| --- | --- |
| User | Your login information is displayed when you are logged in. Depending on how the Qlik Sense system has been set up, you may have to log in by clicking the Log in button.  When logged in, you can click User and then click User in the pop-up menu, to open the Profile dialog with the following information: User ID and User directory. |
| Log out | Click User and then click Log out in the pop-up menu to log out. |

### C: Create new application

Application options

| UI item | Description |
| --- | --- |
| Create new app | Create a new application. The button is only available if you have permission to create applications.  To learn more about creating an application, see [Creating applications and adding data](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/create-app-cloud-hub.htm). |
| Sort ascending | You can sort the applications alphabetically, by created date, or by published date, descending or ascending. |
| Grid View List View | Toggle between grid view and list view of the hub, depending on what kind of overview you prefer. |

### D: Work

Personal with all your own applications under Work.

### E: Main area

All your applications are displayed in the main area.

### F: Getting started

Go to the Qlik Sense Desktop webpage to learn more about how to get started with Qlik Sense Desktop.

## Opening an application in Qlik Sense Desktop

With Qlik Sense Desktop, you can open applications from the hub, or from a file location.

### Opening an application from the hub

You open an application from the hub by clicking it.

### Opening an application from outside the hub

With Qlik Sense Desktop, you can open an application that is not in the hub. You can do this in two ways.

- Navigate to where you keep your application, and drag it to the hub.
- You can also copy the application using Ctrl+C, and then open it in the hub using Ctrl+O.

Tip noteIf you want the application to be part of your hub content, you can move the application file (with extension .qvf) to the application directory, typically <user>\Documents\Qlik\Sense\Apps.

## Disabling Insight Advisor in Qlik Sense Desktop applications

Insight Advisor can be disabled in an application by adding a variable.

Do the following:

1. In the sheet edit mode, in the assets panel, click ![Variables](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg).
2. Click Create new.
3. In Name, type DISABLE\_INSIGHTS.
4. In Definition, type any value.
5. Click Close.
6. Refresh the application.

Related learning:

- [Getting started with Qlik Sense](/lnk/Getting_started_QS)
