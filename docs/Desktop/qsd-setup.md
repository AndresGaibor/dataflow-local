---
title: "Setting up Qlik Sense Desktop"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Desktop/qsd-setup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Sense Desktop"]
---

# Setting up Qlik Sense Desktop

This section describes how to install Qlik Sense Desktop on your computer.

## System requirements

To successfully install and run Qlik Sense Desktop, the requirements listed in this section must be fulfilled.

Qlik Sense Desktop requirements

|  |  |
| --- | --- |
| Operating system | Microsoft Windows 10 (64-bit version only)  Microsoft Windows 11 |
| Processors (CPUs) | Intel Core 2 Duo or higher recommended.  Advanced Vector Extensions (AVX) support. |
| Memory | 4 GB minimum (depending on data volumes, more may be required).  Information noteQlik Sense uses an in-memory analysis technology. The memory requirements are directly related to the amount of data being analyzed. |
| Disk space | 5.0 GB total required to install |
| .NET Framework | 4.8.1 or higher |
| Security | Local admin privileges needed to install. |
| Minimum screen resolution | - Desktops, laptops and tablets: 1024x768 - Small screens: 320x568 |
| Browser support | - Microsoft Edge - Google Chrome - Mozilla Firefox   Tip note By default, Qlik Sense Desktop runs in a window of its own. But you can also open it in a web browser.  For more information, see [Starting Qlik Sense Desktop](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/UserInterface/start-dt.htm).  Warning noteMozilla Firefox requires hardware acceleration, not supported in virtual environments. |

## Installing Qlik Sense Desktop

You can either perform a standard installation, where installation and storage locations are set to default options, or specify the locations in a custom installation.

### Qlik Sense Desktop standard installation

Do the following:

1. Double-click Qlik\_Sense\_Desktop\_setup.exe to start the installation.

   The welcome dialog is displayed.
2. Click Install if you want to perform a standard installation.

   The License agreement dialog is displayed.
3. Read the license agreement, select I accept the license agreement, and click Next.

   Tip noteYou also have the option to print the license agreement to a local printer.
4. On the Ready to install screen, optionally select to create a desktop shortcut. Click Install.
5. In the Extension bundles section, optionally select to install the extension bundles. Then, select which extension bundles you want to install from the list of those available for your Qlik Sense installation.

You can always add or remove extension bundles from your Qlik Sense installation at a later moment. See: [*Modifying extension bundles installation*](#Modifyin).

6. If you have chosen not to install the extension bundles, click Install. Otherwise, click Next.
7. If you are installing any of the extension bundles, accept the extension bundle license agreement. Then, click Install.
8. When the installation has completed, the Installation summary is displayed.

   Click Finish to close the Installation summary.

You have now successfully installed Qlik Sense Desktop on your computer.

### Qlik Sense Desktop custom installation

Do the following:

1. Double-click on Qlik\_Sense\_Desktop\_setup.exe to start the installation.

   The welcome dialog is displayed.
2. Click Custom Installation.

   The License agreement dialog is displayed.
3. Read the license agreement, select the I accept the license agreement check box, and click Next.

   Tip noteYou also have the option to print the license agreement to a local printer.
4. Type or browse to the location where you want to install Qlik Sense Desktop and click Next.

   Information noteQlik Sense Desktop cannot be installed in locations where administrator rights are required, for example C:\Program Files.
5. Type or browse to the location where you want Qlik Sense Desktop to store application content, and click Next.
6. On the Ready to install screen, optionally select to create a desktop shortcut. Click Install.
7. In the Extension bundles section of the Ready to install screen, optionally select to create a desktop shortcut. Then, select which extension bundles you want to install from the list of those available for your Qlik Sense installation.

You can always add or remove extension bundles from your Qlik Sense installation at a later moment. See: [*Modifying extension bundles installation*](#Modifyin).

8. If you have chosen not to install the extension bundles, click Install. Otherwise, click Next.
9. If you are installing any of the extension bundles, accept the extension bundle license agreement. Then, click Install.
10. When the installation has completed, the Installation summary is displayed.

    Click Finish to close the Installation summary.

You have now successfully installed Qlik Sense Desktop on your computer, using customized installation and storage locations.

Information noteTo silently install Qlik Sense Desktop, see [*Setting up Qlik Sense Desktop*](#Silent).

## Authenticating against Qlik Cloud (formerly Qlik Cloud)

Before you can start using Qlik Sense Desktop, you need to authenticate yourself against Qlik Cloud. To do so, you must generate an authentication link. You need to have a working network connection to enable authentication.

How to Authenticate Qlik Sense Desktop with Qlik Cloud (Qlik Cloud)

## Qlik Sense Desktop ports

Qlik Sense Desktop uses port 4848 by default.

## Qlik Sense Desktop storage

This section describes where the Qlik Sense applications are stored when running Qlik Sense Desktop.

### Default storage

By default, Qlik Sense stores applications in the local file system under C:\Users\{user}\Documents\Qlik\Sense.

### Portable format

A Qlik Sense application can be stored in the local file system in the proprietary .qvf format, which is a portable format.

A single application is stored as <AppName>.qvf, where <AppName> is the title of the application.

## Modifying extension bundles installation

You can add or remove extension bundles from your Qlik Sense Desktop installation at any moment.

Do the following:

1. In Control Panel, open Programs and Features.
2. In the list of programs, double-click the extension bundle that you want to modify.
3. The Extension Bundle Setup Wizard opens. Click Next.
4. Select Change.
5. On the Custom setup screen, click on the bundle icon to select how to modify the bundle installation:
   - If the bundle is installed, select Entire feature will be unavailable to uninstall it.
   - If the bundle is not installed, select Entire feature will be installed on local hard drive to install it.

   Then, click Next.
6. Click Change.
7. Click Finish to close the Extension Bundle Setup Wizard.

## Upgrading Qlik Sense Desktop

The upgrade option is available when Qlik Sense has been previously installed and a newer version of the setup file Qlik\_Sense\_Desktop\_setup.exe is executed.

Do the following:

1. Double-click on Qlik\_Sense\_Desktop\_setup.exe to start the installation.

   The welcome dialog is displayed.
2. Click UPGRADE.

   The License agreement dialog is displayed.
3. Read the license agreement and then tick the I accept the license agreement check box (if this is the case) and click Next.

   Tip noteYou also have the option to print the license agreement to a local printer.

   The Ready to install dialog is displayed.
4. Click Upgrade to start the installation.

   When the installation has completed, the Installation summary is displayed.
5. Click Finish to close the Installation summary

You have now successfully upgraded to a newer version of Qlik Sense Desktop.

Information noteTo silently upgrade Qlik Sense Desktop, see [*Setting up Qlik Sense Desktop*](#Silent).

### Application migration

After upgrading Qlik Sense Desktop, applications need to be migrated to ensure compatibility. In the hub, application thumbnails are not displayed before the application is migrated.

Migration is performed automatically when you open an application for the first time after an upgrade. Before an application is migrated, a backup copy is created in Users\{user}\Documents\Qlik\Sense\AppsBackup. You can use the backup copy if you want to open the application in a previous version of Qlik Sense Desktop.
