---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-quality-field-quality-filter/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance data-quality field-quality filter

## qlik data-governance data-quality field-quality filter

Retrieve field qualities for multiple datasets

### Synopsis

Retrieves the latest computed field quality metrics for a list of datasets. The maximum number of datasets is 100.
When a dataset has been analyzed through multiple connections, the response returns the result from the most recently computed connection.

```
qlik data-governance data-quality field-quality filter [flags]
```

### Options

```
      --datasets-datasetId string   The ID of the dataset
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for filter
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
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
