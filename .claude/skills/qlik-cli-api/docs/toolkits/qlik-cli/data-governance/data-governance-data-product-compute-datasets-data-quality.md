---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-product-compute-datasets-data-quality/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance data-product compute-datasets-data-quality

## qlik data-governance data-product compute-datasets-data-quality

Trigger data quality computation for the data-product's datasets

### Synopsis

Triggers a full data quality computation for all datasets in the data product, running profile calculation followed by data quality
assessment. Returns a `batchComputationId` that can be used to track overall progress via the batch computation status endpoint
(`GET /api/data-governance/data-qualities/batch-computations/{batchComputationId}`). The computation runs asynchronously.
Poll the status endpoint until `status` is `FINISHED`.

```
qlik data-governance data-product compute-datasets-data-quality <data-productId> [flags]
```

### Options

```
  -h, --help           help for compute-datasets-data-quality
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
