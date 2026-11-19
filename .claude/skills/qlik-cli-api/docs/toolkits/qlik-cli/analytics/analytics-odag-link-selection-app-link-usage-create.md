---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-link-selection-app-link-usage-create/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-link selection-app-link-usage create

## qlik analytics odag-link selection-app-link-usage create

List ODAG links used by a selection Analytics Application

### Synopsis

Registers the current set of ODAG links referenced by a selection Analytics Application and returns only those links the current user can access. Call this when a selection Analytics Application is opened or after modifying its ODAG link references. The response is an array of objects, where the `id` identifies the requested link and `link` contains the link state when accessible. Use `GET /analytics/odag-links/{linkId}` for full details.

```
qlik analytics odag-link selection-app-link-usage create [flags]
```

### Options

```
  -f, --file file          Read request body from the specified file
  -h, --help               help for create
      --includeCharts      When ˋtrueˋ, include master charts from the template Analytics Application in the response.
      --interval int       Duration in seconds to wait between retries, at least 1 (default 1)
      --linkList strings   An array of Link IDs.
  -q, --quiet              Return only IDs from the command
      --raw                Return original response from server without any processing
      --retry int          Number of retries to do before failing, max 10
      --selAppId string    (Required) The ID of a selection Analytics Application.
      --type string        The type of the links to query. Defaults to ˋlinkˋ.
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
