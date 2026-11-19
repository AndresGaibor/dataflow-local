---
source: https://qlik.dev/toolkits/qlik-cli/alerting/alerting-sharing-task-task-execution/
last_updated: 2026-10-14T09:59:57Z
---

# alerting sharing-task task-execution

## qlik alerting sharing-task task-execution

Examine sharing-task executions

### Synopsis

Task executions record the execution history of a sharing task. Use this group to list completed executions of a sharing task or retrieve a specific execution by ID. Executions that are in progress are not included.

```
qlik alerting sharing-task task-execution [flags]
```

### Options

```
  -h, --help   help for task-execution
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
