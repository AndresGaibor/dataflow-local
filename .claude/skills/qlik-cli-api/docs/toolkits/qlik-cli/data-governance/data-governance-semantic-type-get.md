---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-semantic-type-get/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance semantic-type get

## qlik data-governance semantic-type get

Get a semantic type

### Synopsis

Returns the definition of a single semantic type identified by its ID, including its configuration (regex, dictionary, or compound rules).

```
qlik data-governance semantic-type get <semantic-typeId> [flags]
```

### Options

```
      --fields string   A comma-separated list of fields to include in the response. The ˋidˋ field is always returned regardless of this filter.
  -h, --help            help for get
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
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
