---
source: https://qlik.dev/changelog/48-qlik-cli-update/
last_updated: 2023-11-29T15:53:15+01:00
---

# Qlik-Cli Update - June 2023

## Qlik-Cli v2.21.0

- feat: Intake for note settings

```bash
qlik note settings update --toggledOn=true
```

- feat: Intake of the transports API

```bash
qlik transport email-config ls # list email configuration settings
qlik transport email-config validate # validate the config
```

- feat: Tenants API - updates

```bash
qlik tenant me # get current tenant information
qlik tenant patch <tenantId> 
```

- fix: make tcs default in data-file create and update by making resumable flag default true

```bash
# to set resumable to false
qlik data-file create  --name <fileName> --file <filePath>  --resumable=false
```

- docs: Explain quotes in body for Windows

- fix: remove deprecated app-evaluator endpoint

- fix: consistency in the data-file command now update use TCS
  like data-file create

- fix: checks if context already exists in init command

- fix: handle request bodies with a body property
