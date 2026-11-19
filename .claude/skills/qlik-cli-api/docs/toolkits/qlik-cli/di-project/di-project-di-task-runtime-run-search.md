---
source: https://qlik.dev/toolkits/qlik-cli/di-project/di-project-di-task-runtime-run-search/
last_updated: 2026-10-14T09:59:57Z
---

# di-project di-task runtime run search

## qlik di-project di-task runtime run search

Search task run history

### Synopsis

Returns a paginated list of historical run instances for the specified data task, filtered by the provided criteria.

```
qlik di-project di-task runtime run search [flags]
```

### Options

```
      --di-projectId string       (Required) Identifier of the data project.
      --di-taskId string          (Required) Identifier of the data task.
  -f, --file file                 Read request body from the specified file
      --filters-field string      The run-history field to filter on.
                                  Allowed values: "ID", "STATUS", "SUB_STATUS", "PERIOD"
      --filters-operator string   Filter operator.
                                  - ˋINˋ / ˋNOT_INˋ: exact match against the values list (recommended for ID, STATUS, SUB_STATUS).
                                  - ˋBETWEENˋ: only valid with the ˋPERIODˋ field. The ˋvalueˋ list must contain two ISO-8601 timestamps (start, end).
                                  Allowed values: "IN", "NOT_IN", "BETWEEN"
      --filters-value strings     Values to match. For ˋBETWEENˋ on ˋPERIODˋ, supply exactly two ISO-8601 timestamps.
  -h, --help                      help for search
      --interval int              Duration in seconds to wait between retries, at least 1 (default 1)
      --lastId string             Cursor for paging. Pass the ˋrunIdˋ of the last item from the previous response to fetch the next page; omit on the first request.
      --limit int                 Maximum number of runs to return.
  -q, --quiet                     Return only IDs from the command
      --raw                       Return original response from server without any processing
      --retry int                 Number of retries to do before failing, max 10
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
