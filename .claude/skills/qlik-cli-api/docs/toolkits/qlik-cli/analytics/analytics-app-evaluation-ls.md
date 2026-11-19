---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-app-evaluation-ls/
last_updated: 2026-10-14T09:59:57Z
---

# analytics app evaluation ls

## qlik analytics app evaluation ls

List app evaluations

### Synopsis

Returns a paginated list of historical evaluations for the specified app. Use
the `next` and `prev` cursor values from the response links to navigate through
pages of results.

```
qlik analytics app evaluation ls [flags]
```

### Options

```
      --all             When ˋtrueˋ, includes full evaluation details in each result. When ˋfalseˋ, detail fields are omitted.
      --appId string    (Required) The unique identifier of the app.
      --fileMode        When ˋtrueˋ, adds file download headers to the response.
      --format string   The output format for the response. Accepts ˋjsonˋ or ˋxmlˋ.
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --next string     A cursor token for fetching the next page of results.
      --prev string     A cursor token for fetching the previous page of results.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     The field to sort results by. Prefix with ˋ-ˋ for descending order or ˋ+ˋ for ascending.
                        Allowed values: "started", "+started", "-started"
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
