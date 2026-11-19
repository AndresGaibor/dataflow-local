---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-link-ls/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-link ls

## qlik analytics odag-link ls

List ODAG links

### Synopsis

A Link object defines an on-demand data navigation path between a selection Analytics Application and a template Analytics Application including the set of properties that control how that data access occurs and under what conditions access is permitted. The set of links returned by this method have properties that match the combination of conditions defined by any supplied query parameters.

```
qlik analytics odag-link ls [flags]
```

### Options

```
  -h, --help                    help for ls
      --includeCharts           Determines whether master charts of the template Analytics Application are included in the response.
      --interval int            Duration in seconds to wait between retries, at least 1 (default 1)
      --optOwner string         Use ˋoptOwnerˋ to filter results by link owner user ID. If supplied, only links owned by that user are returned. If not supplied, returns all links the current user can access.
  -q, --quiet                   Return only IDs from the command
      --raw                     Return original response from server without any processing
      --retry int               Number of retries to do before failing, max 10
      --selectionAppID string   Filter the list by the selection Analytics Application ID.
      --type string             The type of the links to query. Defaults to ˋlinkˋ.
                                Allowed values: "link", "view", "all"
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
