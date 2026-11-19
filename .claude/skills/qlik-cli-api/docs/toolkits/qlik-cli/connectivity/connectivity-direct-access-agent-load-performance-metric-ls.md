---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-direct-access-agent-load-performance-metric-ls/
last_updated: 2026-10-14T09:59:57Z
---

# connectivity direct-access-agent load-performance-metric ls

## qlik connectivity direct-access-agent load-performance-metric ls

Get load performance metrics

### Synopsis

Retrieves performance metrics for loads processed by the gateway, either for all loads or a filtered subset. Use these metrics to evaluate reload throughput, connector latency, and concurrent reload activity. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Load performance recording is disabled by default and is controlled by the `BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED` configuration property. Available in Direct Access Gateway V1.7.17+.

```
qlik connectivity direct-access-agent load-performance-metric ls <direct-access-agentId> [flags]
```

### Options

```
      --filter string   SCIM style filter string as defined in RFC 7644 section 3.4.2.2
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --page int        The page number
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     The field to sort by with +/- prefix indicating sort order
                        Allowed values: "-benchmarkStartTime", "+benchmarkStartTime", "benchmarkStartTime", "-benchmarkEndTime", "+benchmarkEndTime", "benchmarkEndTime", "-dataTransmissionStartTime", "+dataTransmissionStartTime", "dataTransmissionStartTime", "-dataTransmissionEndTime", "+dataTransmissionEndTime", "dataTransmissionEndTime"
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
