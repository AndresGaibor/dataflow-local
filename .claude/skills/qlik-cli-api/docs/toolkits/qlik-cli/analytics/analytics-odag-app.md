---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-app/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-app

## qlik analytics odag-app

List ODAG analytics applications

### Synopsis

ODAG (On-Demand App Generation) applications are categorized as selection apps (entry points), template apps (source for generation), or generated apps (created via ODAG requests).

```
qlik analytics odag-app [flags]
```

### Options

```
  -h, --help   help for odag-app
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
