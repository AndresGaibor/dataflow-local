---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-data-quality-fields-structure/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance data-quality fields-structure

## qlik data-governance data-quality fields-structure

Assign types to dataset fields

### Synopsis

Fields structures define the standard or semantic type assigned to each field in a dataset. Use this group to assign types to one or more fields; fields not included in the request keep their current assigned structure.

```
qlik data-governance data-quality fields-structure [flags]
```

### Options

```
  -h, --help   help for fields-structure
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
