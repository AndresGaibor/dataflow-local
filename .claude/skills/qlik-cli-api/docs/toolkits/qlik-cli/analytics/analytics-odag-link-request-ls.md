---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-link-request-ls/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-link request ls

## qlik analytics odag-link request ls

List requests for an ODAG link

### Synopsis

Retrieves all Analytics Application generation requests for a specific ODAG link, with optional filtering by pending status (`pending`), selection Analytics Application (`selectionAppId`), sheet context (`selectionAppSheet`), or client context (`clientContextHandle`). Use this to track generation history or monitor in-flight requests.

```
qlik analytics odag-link request ls <odag-linkId> [flags]
```

### Options

```
      --clientContextHandle string   An opaque handle to a client-side object that contains the reference to the link being used.
  -h, --help                         help for ls
      --interval int                 Duration in seconds to wait between retries, at least 1 (default 1)
      --pending                      Pass ˋtrueˋ if only pending requests should be returned.
  -q, --quiet                        Return only IDs from the command
      --raw                          Return original response from server without any processing
      --retry int                    Number of retries to do before failing, max 10
      --selectionAppId string        The ID of the selection Analytics Application.
      --selectionAppSheet string     The name (or ID) of the sheet to filter qualifying ODAG requests for a selection Analytics Application.
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
