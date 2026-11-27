---
title: "Uploading and managing visualization extensions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-extensions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Uploading and managing visualization extensions

Extensions add custom visualization capabilities to Qlik Cloud applications. You can upload and manage extensions in the Administration activity center.

Qlik Cloud Government noteThird-party extensions are supported in Qlik Cloud Government. Using them may require approval as part of an Agency Authority to Operate, depending on your organization's security and compliance requirements.

## Using extensions

Visualization extensions in Qlik Cloud add new visual components beyond the standard visualizations. Use them to tailor how you present and explore data.

For more information, see [Qlik Developer: Extending Qlik](https://qlik.dev/extend/). For a visual demo, see [Using third-party visualization extensions in Qlik Cloud](https://share.vidyard.com/watch/kq8gkpB6jfLuVDWERgAgXE?) and [Extensions and API keys](https://share.vidyard.com/watch/KzZMkq1RDQVcnWc8ShfYje?).

## Required roles

To upload and manage extensions, you must have one of the following roles:

- Tenant administrator
- Analytics administrator
- Custom role with the Manage extensions permission set to Allowed

## File requirements and limits

Follow these rules to ensure your extension uploads and works correctly.

### File limits

Extension ZIP files have these limits:

- Maximum ZIP file size: 30 MB
- Maximum size for any single file in the ZIP: 30 MB
- Maximum number of files in the ZIP: 500
- Maximum total uncompressed size: 100 MB

### Required base files for an extension

Ensure your extension ZIP file includes the following files:

- .qext: Metadata file
- .js: JavaScript code
- .html: HTML rendering code
- .css: Custom styling

### File naming rules

Each file in the extension must have a file name and a file extension. Files that do not comply are ignored. Examples of ignored files include .gitignore and README.

### Best practices

- Minify your code files.
- Include only the files your extension needs to run.
- Review the extension and its code before you upload it.

### External resources and CSP

#### Host image files externally

Do not include image files (such as GIF, PNG, JPG) in the extension ZIP file. Instead, host images externally (for example, on an application server, an S3 bucket, or a public content management system), and reference them from your extension code.

#### Reference external code and content

To reference external code or content in your extension, configure a tenant Content Security Policy (CSP) and allowlist the external origins your extension needs to access.

If an origin is not allowlisted, your extension will not render.

For more information, see [*Managing Content Security Policy (CSP)*](mc-administer-content-security-policy.htm).

### Unsupported file formats

For security reasons, extensions can't include files with disallowed MIME types. MIME types (Multipurpose Internet Mail Extensions) indicate a file's format. If your extension contains a disallowed MIME type (for example, an executable file or a ZIP file), the upload fails.

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

### Unsupported features

The following features are not supported:

- Bundled extensions: ZIP files containing other extension ZIP files are not supported.
- QVF and QVD files: These files are not accessible from the extension service.

To upload QVF or QVD files, use one of the following methods:

- Upload an application from the Create page in the Analytics [activity center](#glossary-1 "Glossary term").
- Upload an application by using qlik-cli.
- Upload a QVD from the Create page in the Analytics activity center.
- Upload a QVD by using Qlik DataTransfer.

## Managing extensions

Extensions are managed on the Extensions page in the Administration activity center.

### Extensions table information

- Name: Metadata name in the QEXT file
- QEXT version: Metadata version
- QEXT filename: Unique identifier for the extension definition file
- Status: Migration status of the extension

### About migration status

Qlik has moved extensions from legacy storage to the service used to manage extensions. Migration status indicates the current migration state of an extension.

Migration status values:

- Migrated: The extension has been successfully migrated and is available.
- Unavailable: The extension is no longer available and cannot be migrated. Delete the extension from the Administration activity center.

## Adding extensions

Do the following:

1. In the Administration activity center, go to Extensions.
2. Click Add.
3. Click Browse to select an extension file, or drop a file in the designated area.
4. Optionally, add tags.
5. Click Publish.

Information noteYou cannot upload an extension with the same QEXT filename as an existing one.

## Editing extensions

Do the following:

1. In the Administration activity center, go to Extensions.
2. On the extension you want to edit, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
3. Use the editing panel to replace the extension or update tags.
4. Save your changes.

## Downloading extensions

Use this to back up an extension before editing it or to move it to another tenant.

Do the following:

1. In the Administration activity center, go to Extensions.
2. On the extension you want to download, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Download.
3. Save the ZIP file.

## Deleting extensions

Deletion of extensions can impact all resources, affecting all users within the tenant.

Do the following:

1. In the Administration activity center, go to Extensions.
2. Select the extensions you want to delete.
3. Click Delete.
