---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-app-evaluation-compare/
last_updated: 2026-10-14T09:59:57Z
---

# analytics app evaluation compare

## qlik analytics app evaluation compare

Compare app evaluations

### Synopsis

Compare two app evaluations to detect performance regressions after app changes or engine upgrades. Both evaluations must belong to the same app.

```
qlik analytics app evaluation compare [flags]
```

### Options

```
  -h, --help   help for compare
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
