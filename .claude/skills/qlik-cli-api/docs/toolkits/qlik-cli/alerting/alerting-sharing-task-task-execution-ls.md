---
source: https://qlik.dev/toolkits/qlik-cli/alerting/alerting-sharing-task-task-execution-ls/
last_updated: 2026-10-14T09:59:57Z
---

# alerting sharing-task task-execution ls

## qlik alerting sharing-task task-execution ls

List sharing task executions

### Synopsis

Returns the execution history of a sharing task. Executions that are in progress are not included.

```
qlik alerting sharing-task task-execution ls [flags]
```

### Options

```
      --filter string           The filter for finding entries.
  -h, --help                    help for ls
      --interval int            Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int               The maximum number of entries to return.
      --offset int              The number of elements to skip for pagination.
      --page string             The cursor to the page of data.
  -q, --quiet                   Return only IDs from the command
      --raw                     Return original response from server without any processing
      --retry int               Number of retries to do before failing, max 10
      --sharing-taskId string   (Required) The sharing task identifier.
      --sort strings            Sort the returned result set by the specified field
                                Allowed values: "status", "-status", "+status", "startedAt", "-startedAt", "+startedAt"
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
