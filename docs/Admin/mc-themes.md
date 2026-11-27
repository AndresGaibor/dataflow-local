---
title: "Uploading and managing themes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-themes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Uploading and managing themes

Add custom themes, including colors and backgrounds based on your company standards, to style your applications. You can upload and manage themes in the Administration activity center.

## What you can customize

With custom themes you can precisely style an application by:

- Changing the colors.
- Adding images and backgrounds.
- Specifying the font sizes and font colors globally or at a granular level.
- Defining color palettes.
- Customizing margins, padding, and spacing.

For information about how to create your own themes for applications, see [Qlik Developer: Custom themes](https://qlik.dev/extend/create-custom-themes/). For information about styling applications, see [*Styling an application*](../Apps/style-app.htm).

## Required roles

To upload and manage themes, you must have one of the following roles:

- Tenant administrator
- Analytics administrator
- Custom role with the Manage themes permission set to Allowed.

## File requirements and limits

Follow these rules to ensure your theme uploads and works correctly.

### Supported file formats

Themes only support the following file formats:

- HTML files
- CSS files
- JSON files
- Images (PNG, JPEG, GIF, and SVG)
- QEXT metadata files
- Font files

### File naming rules

Each file in the theme must have a file name and a file extension. Files that do not comply are ignored. Examples of ignored files include .gitignore and README.

### File size and count limits

Theme ZIP files have these limits:

- Maximum ZIP file size: 30 MB
- Maximum size for any single file in the ZIP: 30 MB
- Maximum number of files in the ZIP: 500
- Maximum total uncompressed size: 100 MB

### External resources and CSP

If your themes include links to external resources, the resource origins must be allowlisted in the Content Security Policy (CSP). For more information, see [*Managing Content Security Policy (CSP)*](mc-administer-content-security-policy.htm).

### Unsupported file formats

For security reasons, themes can't include files with disallowed MIME types. MIME types (Multipurpose Internet Mail Extensions) indicate a file's format. If your extension contains a disallowed MIME type (for example, an executable file or a ZIP file), the upload fails.

The following MIME types are not allowed:

- 'application/octet-stream'
- 'application/x-coredump'
- 'application/x-dosexec'
- 'application/x-executable'
- 'application/x-java-applet'
- 'application/x-object'
- 'application/x-sharedlib'
- 'application/zip'
- 'text/x-shellscript'
- 'text/x-awk'
- 'text/x-gawk'
- 'text/x-msdos-batch'
- 'text/x-nawk'
- 'text/x-php'

## Managing themes

Themes are managed on the Themes page in the Administration activity center.

### Themes table information

- Name: Metadata name in the QEXT file
- QEXT version: Metadata version
- QEXT filename: Unique identifier for the theme definition file
- Status: Migration status of the theme

### About migration status

Qlik has moved themes from legacy storage to the service used to manage themes. Migration status indicates the current migration state of a theme.

Migration status values:

- Migrated: The theme has been successfully migrated and is available.
- Unavailable: The theme is no longer available and cannot be migrated. Delete the theme from the Administration activity center.

## Adding themes

Do the following:

1. In the Administration activity center, go to Themes.
2. Click Add.
3. Click Browse to select a theme file, or drop a file in the designated area.
4. Optionally, add tags.
5. Click Publish.

Information noteYou cannot upload a theme with the same QEXT filename as an existing one.

## Editing themes

Do the following:

1. In the Administration activity center, go to Themes.
2. On the theme you want to edit, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
3. Use the editing panel to replace the theme or update tags.
4. Save your changes.

## Downloading themes

Use this to back up a theme before editing it or to move it to another tenant.

Do the following:

1. In the Administration activity center, go to Themes.
2. On the theme you want to download, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Download.
3. Save the ZIP file.

## Deleting themes

Deletion of themes can impact all resources, affecting all users within the tenant.

Do the following:

1. In the Administration activity center, go to Themes.
2. Select the themes you want to delete.
3. Click Delete.
