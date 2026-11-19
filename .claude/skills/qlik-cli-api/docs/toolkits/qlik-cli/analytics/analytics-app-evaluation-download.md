---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-app-evaluation-download/
last_updated: 2026-10-14T09:59:57Z
---

# analytics app evaluation download

## qlik analytics app evaluation download

Download an app evaluation log

### Synopsis

Downloads the evaluation log for the specified app evaluation, defaulting to XML
format. Use the `Accept` header to request JSON output instead.

```
qlik analytics app evaluation download <evaluationId> [flags]
```

### Options

```
  -h, --help           help for download
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
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
