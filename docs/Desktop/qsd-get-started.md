---
title: "Get started with Qlik Sense Desktop"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Desktop/qsd-get-started.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Sense Desktop"]
---

# Get started with Qlik Sense Desktop

Qlik Sense Desktop is an application you install on your local Windows computer. It is intended for you to try out and explore Qlik Sense, and it can also be used for creating [visualizations](#glossary-0 "Glossary term"), [charts](#glossary-1 "Glossary term"), interactive dashboards and analytics applications for local and offline usage in a contained environment, that is your local computer.

Applications you create in Qlik Sense Desktop can be exported and used in Qlik Cloud Analytics, Qlik Sense Enterprise, or by other Qlik Sense Desktop installations.

## Comparing Qlik Sense Desktop and Qlik Cloud Analytics

There are some differences between Qlik Sense Desktop and Qlik Cloud Analytics:

- You can only run Qlik Sense Desktop on your local Windows computer - use of multiple screens or tablets, for example, is not supported.
- Applications cannot be published in Qlik Sense Desktop, and because of this, there is no support for streams.
- Security functionality is not supported in Qlik Sense Desktop.
- There is no autosave function in Qlik Sense Desktop – you have to save your work manually by clicking Save in the toolbar. The application is automatically saved when reloading the script.
- Duplicating applications is not supported in Qlik Sense Desktop.
- Qlik Sense Desktop will run in the language of your operating system and the language cannot be altered.
- Dynamic views are not supported in Qlik Sense Desktop.

## Downloading the Qlik Sense Desktop installation files

Qlik Sense Desktop can be downloaded from Qlik Cloud or from the Qlik download site. Either of the two approaches gets the latest version of Qlik Sense Desktop onto your computer.

### Downloading from Qlik Cloud

Do the following:

1. Open Qlik Cloud.
2. Click your profile in the top right corner and select Settings.
3. Under Other, select Tools.
4. Under Qlik Sense Desktop, click Download to download Qlik Sense Desktop.
5. Install Qlik Sense Desktop.
6. Navigate back to Qlik Cloud.
7. Below the button you used to download Qlik Sense Desktop, click Authenticate to add a server authentication link to your Qlik Sense Desktop installation. You can then click on that link in Qlik Sense Desktop to authenticate.

### Downloading from the Qlik download site

Do the following:

1. Go to [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).
2. Select Qlik Data Analytics, and then select Qlik Sense Desktop from the Product list.
3. Optionally, use additional filters to narrow your list of possible downloads.
4. Click a download link to start the download.
5. Install Qlik Sense Desktop.
6. Click Authenticate to add a server authentication link to your Qlik Sense Desktop installation. You can then click on that link in Qlik Sense Desktop to authenticate.

### Authenticating against Qlik Cloud (formerly Qlik Cloud)

You can authenticate your Qlik Sense Desktop client against Qlik Cloud. To do so, you must generate an authentication link.

How to Authenticate Qlik Sense Desktop with Qlik Cloud (Qlik Cloud)

## What is included in Qlik Sense Desktop

### Desktop items and start menu items

After having completed your installation of Qlik Sense Desktop, a shortcut will be available from the desktop as well as from the Start menu (Start > All Programs):

- Shortcut to Qlik Sense Desktop

  The hub is the starting point when you run Qlik Sense. That is where you find all the Qlik Sense applications that you have created.

### Qlik Sense Desktop installation location

After having completed your installation of Qlik Sense Desktop, Qlik Sense Desktop is installed to Users\{user}\AppData\Local\Programs\Qlik.

You can also specify the installation location with the Custom Installation option.

### Examples, applications and logs

There are some example files included in the installation of Qlik Sense Desktop. These are installed to Users\{user}\Documents\Qlik\Examples. For example, a number of extension code examples are installed to the Extensions sub-folder.

The installation of Qlik Sense Desktop also comes with example applications. These are installed to Users\{user}\Documents\Qlik\Sense\Apps.

In your installation of Qlik Sense Desktop, logs are found in Users\{user}\Documents\Qlik\Sense\Log.

## Exploring the Qlik Sense Desktop hub

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
| Sort ascending | You can sort the applications alphabetically , by created date, or by published date, descending or ascending. |
| Grid View List View | Toggle between grid view and list view of the hub, depending on what kind of overview you prefer. |

### D: Work

Personal with all your own applications under Work.

### E: Main area

All your applications are displayed in the main area.

### F: Getting started

Go to the Qlik Sense Desktop webpage to learn more about how to get started with Qlik Sense Desktop.

Related learning:

- [Getting started with Qlik Sense](/lnk/Getting_started_QS)
