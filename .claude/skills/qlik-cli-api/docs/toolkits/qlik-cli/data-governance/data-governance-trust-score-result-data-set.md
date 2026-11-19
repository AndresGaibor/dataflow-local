---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-trust-score-result-data-set/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance trust-score result data-set

## qlik data-governance trust-score result data-set

Retrieve trust scores for datasets

### Synopsis

Returns the current Trust Score for up to 100 datasets in a single request, including the overall score, per-axis breakdown, and per-metric details. Datasets with no computed Trust Score are omitted.

```
qlik data-governance trust-score result data-set [flags]
```

### Options

```
  -h, --help   help for data-set
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
