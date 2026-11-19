---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-direct-access-agent/
last_updated: 2026-10-14T09:59:57Z
---

# connectivity direct-access-agent

## qlik connectivity direct-access-agent

Manage connectivity direct-access-agents

### Synopsis

Connectivity direct-access-agents expose performance diagnostics for Direct Access gateways. Use this group to run benchmarks against an agent and review load performance metrics for reloads processed by the gateway.

```
qlik connectivity direct-access-agent [flags]
```

### Options

```
  -h, --help   help for direct-access-agent
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
