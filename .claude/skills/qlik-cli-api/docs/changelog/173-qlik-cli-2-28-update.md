---
source: https://qlik.dev/changelog/173-qlik-cli-2-28-update/
last_updated: 2025-10-16T09:20:48+02:00
---

# qlik-cli 2.28.0 - October 2025

A new release of [qlik-cli](https://qlik.dev/toolkits/qlik-cli/) has been published, which expands the set of covered APIs
to include additional published [REST APIs](https://qlik.dev/apis/rest/), and fixes bugs.

## New commands \{#new-commands-2025-10}

qlik-cli now supports the following commands:

- `qlik automation change-owner` - Changes the owner of an automation to another user.
- `qlik automation change-space` - Changes the space of an automation by specifying a new space.
- `qlik di-project di-task runtime state-datasets` - Returns dataset-level runtime state for a data task.
- `qlik direct-access-agent connector file allowed-paths` - Manages direct-access-agent connector file allowed-paths.
- `qlik direct-access-agent connector file custom-data-type-mappings` - Manages connector type mapping configuration.
- `qlik ml experiment recommend-models` - Returns model recommendations for a specified experiment.
- `qlik report output` - Lists report request outputs.
- `qlik sharing-task executions` - Manages sharing-task executions.

## Breaking changes \{#breaking-changes-2025-10}

- The commands `qlik data-connection patch` and `qlik data-credential patch` no longer support the flags
  `--patchData-op` and `--patchData-path`, which are respectively replaced by `--op` and `--path`.

## Bug fixes \{#bug-fixes-2025-10}

The following issues have been fixed:

- `version` command not returning the version information.
- `value` flag used with a `patch` command is ignored.
- qlik-cli crashes when assigning several roles to a group or a user in a space.
