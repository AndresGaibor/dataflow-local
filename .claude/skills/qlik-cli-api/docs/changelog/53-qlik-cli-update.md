---
source: https://qlik.dev/changelog/53-qlik-cli-update/
last_updated: 2023-11-29T15:53:15+01:00
---

# Qlik-Cli Update - August 2023

## Qlik-Cli v2.22.0

### feat: Intake of the brands API

This API allows you to manage the branding of a tenant.
For example, you can customize logos and favicons with your brand.
You can activate this by using the command:

```bash
qlik brand create --name=<name> --file-logo=<logo.png> --file-favIcon=<icon.ico>
qlik brand activate <brand-id>
```

### feat: Intake of group-create

The group-create command is a command used for creating groups.
It can be used for managing access control for multiple users
at the same time. For example, you can create a group
called developers with the "Developer" role assigned.

```bash
qlik group create --name=developers --assignedRoles='[{"name":"Developer"}]'
```

You can get a complete list of roles using the command `qlik role ls`.
`--assignedRoles` accepts either an ID or the name of a role.

### feat: Tenant-edit command

The tenant-edit command now allows you to update your tenant-configuration
in a command-line-editor of your choice.

- docs: Edit-commands are no longer experimental
- docs: The identity-provider commands are no longer experimental
- fix: Bug when providing required body parameters from a file using the `--file` flag.
