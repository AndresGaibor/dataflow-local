---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-quality-field-quality/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance data-quality field-quality

## qlik data-governance data-quality field-quality

Inspect field-level data quality

### Synopsis

Field qualities are the latest computed quality metrics for individual fields within a dataset. Use this group to retrieve field quality metrics for up to 100 datasets in a single request.

```
qlik data-governance data-quality field-quality [flags]
```

### Options

```
  -h, --help   help for field-quality
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
