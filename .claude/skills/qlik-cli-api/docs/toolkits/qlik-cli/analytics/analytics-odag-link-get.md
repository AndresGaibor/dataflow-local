---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-link-get/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-link get

## qlik analytics odag-link get

Get ODAG link details

### Synopsis

Retrieves details of a specific ODAG link, including bindings, properties, status, and template Analytics Application charts. Use this to review link configuration or verify permissions before generating Analytics Applications.

```
qlik analytics odag-link get <odag-linkId> [flags]
```

### Options

```
  -h, --help            help for get
      --includeCharts   Determines whether master charts of the template Analytics Application are included in the response.
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
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
