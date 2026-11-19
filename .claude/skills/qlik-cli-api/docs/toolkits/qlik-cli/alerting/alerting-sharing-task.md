---
source: https://qlik.dev/toolkits/qlik-cli/alerting/alerting-sharing-task/
last_updated: 2026-10-14T09:59:57Z
---

# alerting sharing-task

## qlik alerting sharing-task

Inspect sharing tasks

### Synopsis

Sharing tasks define when scheduled reports, data alerts, subscriptions, and other tasks execute, and associate each task with its execution conditions. The alerting namespace provides access to the execution history of sharing tasks.

```
qlik alerting sharing-task [flags]
```

### Options

```
  -h, --help   help for sharing-task
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
