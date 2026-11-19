---
source: https://qlik.dev/changelog/12-qlik-cli-update/
last_updated: 2025-07-02T17:28:24+02:00
---

# qlik-cli 2.5.x released

The latest version of `qlik-cli` allows better windows support, support for
new APIs and notifications.

Here are the updates.

## Chocolatey

qlik-cli is now back to Chocolatey

To install using `choco`:

`choco install qlik-cli`

To upgrade qlik-cli using chocolatey:
`choco upgrade qlik-cli`

If you see an error like below:

Error retrieving packages from [source](https://www.nuget.org/api/v2)
The combination of parameters provided to this OData endpoint is no longer
supported. Please refer to the this
[URL](https://aka.ms/nuget/odata-deprecation) for more information about this
deprecation.

Then first run:
`choco source list`

Then remove the one matching nuget.org:
`choco source rm --name=nuget.org`

Another way to fix a failing upgrade is to uninstall and reinstall.

```bash
 choco uninstall qlik-cli
 choco install qlik-cli
```

## in v2.5.0 / v2.5.1

New - Added support for outbound proxy: you can now set the operating system environment
variables called `HTTPS_PROXY/HTTP_PROXY` with the hostname or IP address of
the proxy server.

> Note: HTTPS_PROXY takes precedence over HTTP_PROXY for https requests.
> Qlik CLI supports only Basic Authentication.

Fix - Improve --limit flag descriptions

Fix - Updated the included latest Qlik Cloud API-specifications

## in v2.4.0

### Updated Commands

Commands have been updated to reflect the latest API changes.

### Notifications

Users to be notified when a new version of qlik-cli is available. The
notification message contains URL with detailed changelog of the latest
release.

### Self Update CLI

The self update command enables users to update to the latest version of
qlik-cli by simply running `qlik update`.

### OpenAPI specs support

The latest qlik-cli update provides support for OpenAPI specs that define
parameters at the path level. In this case, the parameters are inherited by
all operations under that path.

### Progress Bar

The animated progress bar displayed when uploading an app is now based on
estimated upload time.

### Support for unix-like Windows terminals

The latest version of qlik-cli provides better support for unix-like Windows
terminals (such as MinGW, MSYS2, and Cygwin).

### Fix

The latest version of qlik-cli also includes bug fixes and minor improvements.

## in v2.3.0

### Support for identity-providers endpoint

The `identity-providers` service is used for managing identity providers.
In this version of qlik-cli the support for identity-providers endpoint is provided.

### Support for questions endpoint

The `questions` endpoint lets user ask natural language questions against
Qlik Sense apps enabled for conversational analytics. This version of qlik-cli
provides support for this endpoint.

```bash
qlik question ask --app-id <appId> --text="new cases by department over time"

#returns a QueryResponse object containing conversational response
{
  ...
  "conversationalResponse": {
    ...
    "responses": [
      {
        "imageUrl": "/api/v1/temp-contents/6139c949f0ccf200019a09e2?inline=1",
        "sentence": {
          "text": "new cases by department over time"
        },
        "type": "chart"
      },
      {
        "narrative": {
          "text": "* New Cases is 180.\n* There were 18 of New Cases not associated to a Department. This may indicate a data quality issue."
        },
        "sentence": {
          "text": "new cases by department over time"
        },
        "type": "narrative"
      }
    ],
    "sentenceWithMatches": "**new cases** by **department** over time"
  },
```

### Progress bar for Downloads

The latest version of qlik-cli also shows an animated progress during app
download.

### Spinner feedback

A new spinner feedback is added when users are waiting for server response
using qlik-cli.
