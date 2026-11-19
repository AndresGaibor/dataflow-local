---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-quality-fields-structure-update/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance data-quality fields-structure update

## qlik data-governance data-quality fields-structure update

Assign types to fields

### Synopsis

Assigns a standard or semantic type to one or more fields in a dataset. This is a partial update:
only the fields included in the request are modified; any field not included in the request keeps
its current assigned structure unchanged.

```
qlik data-governance data-quality fields-structure update [flags]
```

### Options

```
      --datasetId string                    (Required) The ID of the dataset
      --fields-name string                  The name of the field.
      --fields-type-kind string             The kind of the field type.
                                            Allowed values: "STANDARD", "SEMANTIC"
      --fields-type-name string             The name of the standard type (if applicable).
      --fields-type-precision string        The precision of the type (e.g., for date/time fields).
                                            Allowed values: "timestamp-millis", "timestamp-micros", "time-millis", "time-micros", "date"
      --fields-type-semanticTypeId string   The ID of the semantic type (if applicable).
  -f, --file file                           Read request body from the specified file
  -h, --help                                help for update
      --interval int                        Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                               Return only IDs from the command
      --raw                                 Return original response from server without any processing
      --retry int                           Number of retries to do before failing, max 10
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
