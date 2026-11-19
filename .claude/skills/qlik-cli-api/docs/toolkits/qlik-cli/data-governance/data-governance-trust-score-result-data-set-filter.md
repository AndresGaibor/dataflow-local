---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-trust-score-result-data-set-filter/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance trust-score result data-set filter

## qlik data-governance trust-score result data-set filter

Retrieve Trust Scores in bulk

### Synopsis

Returns the current Trust Score for up to 100 datasets in a single request. Each result includes the overall score, per-axis breakdown (`weight`, `score`, `enabled` state), and per-metric details. Datasets with no computed Trust Score are omitted from the response. Requires `dataset:read` and `dataquality:read` permissions.

```
qlik data-governance trust-score result data-set filter [flags]
```

### Options

```
      --datasetIds strings   List of dataset IDs to retrieve Trust Scores for. Maximum 100 IDs per request.
  -f, --file file            Read request body from the specified file
  -h, --help                 help for filter
      --interval int         Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                Return only IDs from the command
      --raw                  Return original response from server without any processing
      --recomputeUsage       When true, refreshes the USAGE and TIMELINESS axes from source before returning the Trust Scores.
      --retry int            Number of retries to do before failing, max 10
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
