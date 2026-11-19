---
source: https://qlik.dev/toolkits/qlik-cli/direct-access-agent/direct-access-agent-benchmark-cancel/
last_updated: 2026-10-14T09:59:57Z
---

# direct-access-agent benchmark cancel

## qlik direct-access-agent benchmark cancel

Request benchmark cancellation

### Synopsis

Requests cancellation of a running benchmark for the specified agent. The request is asynchronous. Use the returned status URL to monitor when cancellation completes. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

```
qlik direct-access-agent benchmark cancel [flags]
```

### Options

```
      --benchmarkId string             (Required) The benchmark ID
      --direct-access-agentId string   (Required) The agent ID
  -h, --help                           help for cancel
      --interval int                   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                          Return only IDs from the command
      --raw                            Return original response from server without any processing
      --retry int                      Number of retries to do before failing, max 10
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
