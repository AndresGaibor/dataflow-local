---
source: https://qlik.dev/changelog/10-qlik-cli-update/
last_updated: 2025-03-11T11:54:24Z
---

# qlik-cli 2.2.0 released

The latest version of qlik-cli adds resumable uploads for large Qlik Sense
applications and bug fixes to improve overall usability. Here are the updates.

## New feature highlights

### Import large Qlik Sense apps

You can now upload large apps to SaaS tenants using qlik-cli using the `qlik app import` command. Use the `--resumable`
switch to instruct the cli to handle the upload as a large file.

When you upload an app using qlik-cli, a nice animated bar appears displaying
the progress.

### File piping

File piping allows you to combine commands where the output of one may be used
as the input of the next command you issue.

### Command aliases

Aliases enable you to create shorthand commands for hard to remember long
commands. For example, say you run a command frequently to find the guid of an
application in your tenant, `$(qlik item ls --resourceType app --name`. You can
use the alias command to create a shortcut it into something like
`qlik getAppGuid consumer+sales`. This returns the complete JSON object for the
consumer+sales resource in the items collection.

### Limit flag added for listing apps

The `--limit` switch enables you to return a number of app resource objects per
page ranging from 1 to 100.

### Identifying experimental flags and switches in commands

Command switches and flags that are experimental features are labeled as such
for your information.

## Fixes worth mentioning

### Temporary Upload Service

Use of the temporary upload service in qlik-cli caused problems with large app
uploads and resumability. This problem has been fixed and implemented through
the resumable switch in the `qlik app import` command.

### Updated response from reload get command

In prior CLI versions, `qlik reload get` was not sending a correct response.
This issue has been resolved.

## Bullet list of all features and fixes in qlik-cli 2.2.0

- feature: add limit flag when listing apps

- feature: Support resumable uploads

- feature: add status for qseow

- feature: Support big apps

- feature: show if a flag or command is experimental

- feature: Add progress-bar

- feature: add support for command aliases

- feature: Add Patch description

- feature: support for files piping

- fix: Solve temporary upload service store issues

- fix: Add timeout to Establish TCP connection

- fix: append experimental to long description with leading newline

- fix: Honor optional request bodies

- fix: handle empty stdin

- fix: omit cookie header

- fix: updated response for reload get

Update qlik-cli today by using brew if you use a Mac, or download the
redistributable from
[here](https://github.com/qlik-oss/qlik-cli/releases/tag/v2.2.0).
