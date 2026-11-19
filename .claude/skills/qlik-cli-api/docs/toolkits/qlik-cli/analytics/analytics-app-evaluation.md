---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-app-evaluation/
last_updated: 2026-10-14T09:59:57Z
---

# analytics app evaluation

## qlik analytics app evaluation

Manage app evaluations

### Synopsis

App evaluations measure performance and scalability of analytics applications, including object response times, CPU usage, document size, and data model metrics.

```
qlik analytics app evaluation [flags]
```

### Options

```
  -h, --help   help for evaluation
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
