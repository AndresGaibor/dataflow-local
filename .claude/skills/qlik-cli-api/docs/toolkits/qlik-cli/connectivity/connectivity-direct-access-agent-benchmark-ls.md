---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-direct-access-agent-benchmark-ls/
last_updated: 2026-10-14T09:59:57Z
---

# connectivity direct-access-agent benchmark ls

## qlik connectivity direct-access-agent benchmark ls

List benchmark statuses

### Synopsis

Retrieves paginated statuses for benchmarks run by the specified Direct Access agent. Use the filters and sort order to find benchmark runs and review their progress or completed results. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.17+.

```
qlik connectivity direct-access-agent benchmark ls <direct-access-agentId> [flags]
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
