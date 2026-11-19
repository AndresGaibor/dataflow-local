---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-link-cancreate-get/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-link cancreate get

## qlik analytics odag-link cancreate get

Check create link permission

### Synopsis

Checks whether the current user has permission to create new ODAG links. Optionally verify permissions for a specific template Analytics Application or selection Analytics Application context. Returns a boolean indicating create permission status.

```
qlik analytics odag-link cancreate get [flags]
```

### Options

```
  -h, --help                          help for get
      --interval int                  Duration in seconds to wait between retries, at least 1 (default 1)
      --optDenyIfSelAppNotUpdatable   When ˋtrueˋ, deny permission if the selection Analytics Application cannot be updated. This parameter is ignored unless ˋoptSelectAppIdˋ is also supplied.
      --optSelectAppId string         An optional parameter for specifying the ID of a selection Analytics Application.
      --optTemplateAppId string       An optional parameter for specifying the ID of a template Analytics Application.
  -q, --quiet                         Return only IDs from the command
      --raw                           Return original response from server without any processing
      --retry int                     Number of retries to do before failing, max 10
```

### Options inherited from parent commands

```
  -c, --config string            path/to/config.yml where parameters can be set instead of on the command line
      --context string           Name of the context used when connecting to Qlik Associative Engine
      --headers stringToString   HTTP headers to use when connecting to Qlik Associative Engine (default [])
      --insecure                 Allow connecting to hosts with self-signed certificates
      --json                     Returns output in JSON format, if possible. Disables verbose and traffic output
  -s, --server string            URL to Qlik Cloud or directly to a Qlik Associative Engine
      --server-type string       The type of server you are using: cloud, Windows (Enterprise on Windows) or engine
  -v, --verbose                  Log extra information
```
