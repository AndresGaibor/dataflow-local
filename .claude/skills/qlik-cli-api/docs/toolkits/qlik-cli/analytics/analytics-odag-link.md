---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-link/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-link

## qlik analytics odag-link

Manage ODAG links

### Synopsis

ODAG links define on-demand data navigation paths between a selection app and a template app. They control how data access occurs and under what conditions access is permitted.

```
qlik analytics odag-link [flags]
```

### Options

```
  -h, --help   help for odag-link
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
