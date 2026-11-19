---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-direct-access-agent-load-performance-metric/
last_updated: 2026-10-14T09:59:57Z
---

# connectivity direct-access-agent load-performance-metric

## qlik connectivity direct-access-agent load-performance-metric

View direct-access-agent load performance metrics

### Synopsis

Load performance metrics describe reload throughput, connector latency, and concurrent reload activity for loads processed by a Direct Access gateway. Use this group to evaluate gateway performance for all loads or a filtered subset.

```
qlik connectivity direct-access-agent load-performance-metric [flags]
```

### Options

```
  -h, --help   help for load-performance-metric
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
