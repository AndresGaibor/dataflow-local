---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-semantic-type-dataset-field-ls/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance semantic-type dataset-field ls

## qlik data-governance semantic-type dataset-field ls

List dataset fields affected by a semantic type

### Synopsis

Returns a paginated list of datasets and their field names that are associated with the specified semantic type. Data is pre-computed from the dataset relationship collection and populated lazily when data quality events are processed.

```
qlik data-governance semantic-type dataset-field ls <semantic-typeId> [flags]
```

### Options

```
  -h, --help           help for ls
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int      The total number of resources to retrieve.
      --page int       Page number for pagination (1-based).
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --sort string    Optional resource field name to sort on. Can be prefixed with +/- to determine order, defaults to (+) ascending. In URLs, "+" should be percent-encoded as "%2B".
                       Allowed values: "+datasetId", "-datasetId"
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
