---
source: https://qlik.dev/changelog/37-qlik-cli-update/
last_updated: 2023-11-29T15:53:15+01:00
---

# Qlik-Cli Update-February 2023

## Qlik-Cli (v2.19.0)

feat: commands for managing script versions in an app

```bash
# List script versions in an app
qlik app script version ls --appId=<appId>

# Create a version of a script
qlik app script version create --versionMessage="Version1" --script="Load RecNo() as N autogenerate(100);" --appId=<appId>

# Get the current version of a script
qlik app script version get current --appId=<appId>

# Get a specific version of a script. The scriptId is returned when listing script versions.
qlik app script version get <scriptId> --appId=<appId>

# Remove a specific version of a script
qlik app script version rm <scriptId> --appId=<appId>

```

feat: additional support for rows and json output for the `qlik app eval` command.

```bash
# By default the eval command will only return maximum 20 rows of data
qlik app eval <expression> --app=<appId>

# If additional data is wanted the number of rows can now be specified using the --rows parameter
qlik app eval <expression> --rows=5000 --appId=<appId>

# It is also possible to get the hypercube data pages in raw json
qlik app eval <expression> --rows=5000 --appId=<appId> --json
```

chore: Documentation updates:

- [Qlik App Eval](https://qlik.dev/toolkits/qlik-cli/app/app-eval)

- [Qlik App Script](https://qlik.dev/toolkits/qlik-cli/app/app-script)
