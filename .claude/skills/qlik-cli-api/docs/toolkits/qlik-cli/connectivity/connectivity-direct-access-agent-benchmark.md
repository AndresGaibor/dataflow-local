---
source: https://qlik.dev/toolkits/qlik-cli/connectivity/connectivity-direct-access-agent-benchmark/
last_updated: 2026-10-14T09:59:57Z
---

# connectivity direct-access-agent benchmark

## qlik connectivity direct-access-agent benchmark

Manage direct-access-agent benchmarks

### Synopsis

Benchmarks measure the throughput and latency of a Direct Access agent as a background task. Use this group to start a benchmark and list the status and results of previous benchmark runs.

```
qlik connectivity direct-access-agent benchmark [flags]
```

### Options

```
  -h, --help   help for benchmark
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
