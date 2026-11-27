---
title: "Troubleshooting - Qlik Sense Desktop"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Troubleshooting/troubleshooting-dt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Sense Desktop"]
---

# Troubleshooting - Qlik Sense Desktop

This section describes problems that are specific to Qlik Sense Desktop.

## I cannot install Qlik Sense Desktop

Possible cause

The system requirements are not fulfilled, or you do not have local administrator privileges to install.

For more information, see [Setting up Qlik Sense Desktop](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Desktop/qsd-setup.htm).

## I cannot find the log files for Qlik Sense Desktop

The location of the log files in Qlik Sense Desktop depends on where you installed the application.

The default location is <user>\Documents\Qlik\Sense\Log.

## I cannot find the installation log files for Qlik Sense Desktop

If you click Cancel during installation, or the installation did not complete successfully, you can find detailed information in the installation log located in your temp folder accessed with the environment variable %temp%.

## My session expired

I was using Qlik Sense Desktop, logged in with my Qlik Sense Enterprise server credentials. Then I received the error message Your session has expired and now I cannot log in again.

Possible cause

You do not have user access or professional access on the Qlik Sense Enterprise server anymore.

Proposed action

Ask your administrator to give you user access or professional access.

## Application thumbnails are missing in the hub

Possible cause

You have upgraded Qlik Sense Desktop to a newer version. In the hub, application thumbnails are not displayed before the application is migrated.

Proposed action

Open the application. Migration is performed automatically when you open an application for the first time after an upgrade.

## Images are missing when moving an application

Possible cause

You have upgraded Qlik Sense Desktop to a newer version, and the application you want to move was created in a Qlik Sense Desktop installation prior to version 2.0.

Proposed action

Before moving the application to another computer, open the application with your new version of Qlik Sense Desktop. Make a change and save the application.

The images included in the application are now bundled together with the rest of the contents of the application.

## I dropped my qvw file onto the hub, and now I cannot find the qvw file, and my application is not available in the hub

Possible cause

You have dragged your QlikView document (qvw file) from a folder and dropped it onto the Qlik Sense Desktop hub, to open it as a Qlik Sense application.

When you make changes to the application and save the application, the following happens:

- The application is saved into the Qlik Sense format (qvf file) in the folder where your QlikView document (qvw file) was stored.
- Also, the QlikView document file (qvw) is removed from the folder and automatically converted into a backup file (qvw.backup) stored here: <user>\Documents\Qlik\Sense\AppsBackup.

Proposed action

If you want to open the backup file, you find it in this folder: <user>\Documents\Qlik\Sense\AppsBackup.

If the Qlik Sense application (qvf file) becomes stored in another folder than <user>\Documents\Qlik\Sense\Apps, move it to the Apps folder to make it available from the hub.

## I cannot open an application

When I try to open an application this error message is displayed: The object could not be saved.

Possible cause

The total path length for backing up the application exceeds the maximum of 260 characters.

The total path includes the backup directory, the product version and the timestamp of the backup date and the application name: <user>\Documents\Qlik\Sense\AppsBackup\<app name>

Proposed action

Rename the qvf file to shorten the total path. This will enable opening the application.

## I cannot download data from an object

When I try to download data from an object, using Qlik Sense Desktop, this error message is displayed: The object could not be saved.

Possible cause

The object's title length is too long. It exceeds the maximum of 174 characters.

Proposed action

Shorten the title of the object. This will enable download data.
