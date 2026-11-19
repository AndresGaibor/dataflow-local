---
source: https://qlik.dev/changelog/7-qlik-cli-update/
last_updated: 2023-11-29T15:53:15+01:00
---

# qlik-cli 2.0.0 adds new commands and squashes bugs

## New commands

The `license` command in qlik-cli enables you to set license assignments for
users in addition to providing metrics related to your tenant's overall license
footprint.

The `evaluation` command enables you to trigger Qlik Sense app evaluations
through cli, retrieve the results, and perform additional commands based on the
feedback. A handy command for automating devops of Qlik Sense apps.

## New features

Flags that are deprecated in qlik-cli now show a warning message when used.

```bash
qlik api-key ls --sub="test"
"Flag --sub has been deprecated, please don't use it!"
```

***

A security enhancement has been made to remove session Ids from log messages

***

You can now add names to external specifications you sideload into qlik-cli.
Here's an example: `qlik spec add ./my-spec.json --name foo`

## Breaking change

The response on the `app` command has changed. Now it returns only information
from the Apps API.

```bash
#qlik app create command
app=$(qlik app create --attributes-name "example")
echo $app
#returns new response

{
  "attributes": {
    "_resourcetype": "app",
    "createdDate": "2021-02-15T07:01:43.930Z",
    "custom": {},
    "description": "",
    "dynamicColor": "",
    "encrypted": true,
    "hasSectionAccess": false,
    "id": "8be82d0f-02d2-4f0e-974c-08dc444384a7",
    "lastReloadTime": "",
    "modifiedDate": "2021-02-15T07:01:46.575Z",
    "name": "testttt2",
    "originAppId": "",
    "owner": "auth0|b96eb87010c7ad52667b2dc8b1ec0b12f97c43ae7848740874267b62aa45c856",
    "ownerId": "ffnbiWZyssMZ5ofRfLc1JzFdZrPvACFl",
    "publishTime": "",
    "published": false,
    "thumbnail": ""
  },
  "create": [...],
  "privileges": [...]
}

```

Instead of returning information from the items API.

```bash
#Breaking change

app=$(qlik app create --attributes-name "example")
echo $app
#returns old response

{
  "actions": [...],
  "collectionIds": [],
  "createdAt": "2021-02-15T08:15:57Z",
  "creatorId": "ffnbiWZyssMZ5ofRfLc1JzFdZrPvACFl",
  "id": "602a2dbd31d6bf3d1f471c31",
  "isFavorited": false,
  "meta": {...},
  "name": "testttt3",
  "ownerId": "ffnbiWZyssMZ5ofRfLc1JzFdZrPvACFl",
  "resourceAttributes": {...},
  "resourceCreatedAt": "2021-02-15T08:15:57Z",
  "resourceCustomAttributes": null,
  "resourceId": "22205ac6-406c-4484-b715-1da12219b044",
  "resourceReloadEndTime": "",
  "resourceReloadStatus": "",
  "resourceSize": {... },
  "resourceSubType": "",
  "resourceType": "app",
  "resourceUpdatedAt": "2021-02-15T08:15:57Z",
  "tenantId": "xrpC13FnjenBc-mhBG98ah2qNlfmwj8X",
  "thumbnailId": "",
  "updatedAt": "2021-02-15T08:15:57Z",
  "updaterId": "ffnbiWZyssMZ5ofRfLc1JzFdZrPvACFl"
}

```

From now on, to obtain the unique id referencing the app in the items API, you
need to issue a `qlik item ls` command after running `qlik app create`.

```bash
qlik item ls --resourceId $app --resourceType app
#returns item information formerly seen in the old response

```

## Bug fixes

- Fixed a bug with `qlik app ls` returning non-app resources.
- Fixed `qlik qrs task start by-id` which failed with `no such operation`
  message.
- Resolved runtime errors using qlik-cli on Windows computers.
