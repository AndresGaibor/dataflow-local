---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-semantic-type-export/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance semantic-type export

## qlik data-governance semantic-type export

Export semantic types

### Synopsis

Exports semantic types from the current tenant as a downloadable JSON file. Supports optional filtering by type IDs, category, creator, or search term.  Without filters, all types (user-created and Qlik defaults) are exported.

```
qlik data-governance semantic-type export [flags]
```

### Options

```
      --createdBy string   Filter by creator user ID. When provided, only types created by this user are included.
  -f, --file file          Read request body from the specified file
  -h, --help               help for export
      --ids strings        List of semantic type IDs to export. When provided, only these types are included.
      --interval int       Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet              Return only IDs from the command
      --raw                Return original response from server without any processing
      --retry int          Number of retries to do before failing, max 10
      --search string      Case-insensitive substring search on label and description fields. Returns only semantic types where the label or description contains the search term. Special regex characters are automatically escaped for literal matching. Maximum length: 500 characters. Empty string returns no results.
      --types strings      Filter by semantic type categories. Supports multiple values for OR logic. When provided, only types matching the specified categories are included.
                           Allowed values: "REGEX", "DICTIONARY", "COMPOUND"
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
