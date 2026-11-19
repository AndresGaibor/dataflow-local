---
source: https://qlik.dev/changelog/42-qlik-cli-update/
last_updated: 2023-11-29T15:53:15+01:00
---

# Qlik-Cli Update-May 2023

## Qlik-Cli (v2.20.4)

feat: Added `qlik app insight-analyse` command for Insight Advisor analyses.
Documentation for the API can be
found [here](https://qlik.dev/apis/rest/apps#%23%2Fentries%2Fv1%2Fapps%2F-appId%2Finsight-analyses-get)

feat: Added command for changing owner of an object.
Documentation for the API can be found [here](https://qlik.dev/changelog/2023-05-09-2)

```bash
# Change owner for a specific object
qlik app object change-owner --appId <app-id> --objectId <object-id> --ownerId <owner-id>
```

feat: add `publish` & `unpublish` commands for Bookmarks, Dimensions and Measures.

```bash
# Publish a bookmark
qlik app bookmark publish <bookmark-id> --app <app-id>
# Unpublish a bookmark
qlik app bookmark unpublish <bookmark-id> --app <app-id>
# Publish a dimension
qlik app dimension publish <dimension-id> --app <app-id>
# Unpublish a dimension
qlik app dimension unpublish <dimension-id> --app <app-id>
# Publish a measure
qlik app measure publish <measure-id> --app <app-id>
# Unpublish a measure
qlik app measure unpublish <measure-id> --app <app-id>
```

fix: `qlik context` commands are no longer `experimental`

fix: `qlik-cli` is now based on Golang v1.20.4 to resolve security vulnerabilities.

fix: added missing body parameters for `qlik qrs` commands.
This issue was reported on qlik-oss [here](https://github.com/qlik-oss/qlik-cli/issues/32)
