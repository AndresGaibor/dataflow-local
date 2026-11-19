---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-semantic-type-patch/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance semantic-type patch

## qlik data-governance semantic-type patch

Update a semantic type

### Synopsis

Partially updates an existing semantic type identified by its ID. Only the fields included in the request payload are modified; omitted fields keep their current values.

```
qlik data-governance semantic-type patch <semantic-typeId> [flags]
```

### Options

```
  -f, --file file                   Read request body from the specified file
  -h, --help                        help for patch
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --op string                   
                                    Allowed values: "replace"
      --path string                 
                                    Allowed values: "/label", "/description", "/useForValidation", "/activated", "/config/validationContent", "/config/validationPattern", "/config/validationCriteria", "/config/values", "/config/children"
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --value string|bool|unknown   The new value to apply at the given ˋpathˋ. The accepted type depends on the target path: a string for ˋ/labelˋ, ˋ/descriptionˋ, ˋ/config/validationContentˋ, ˋ/config/validationPatternˋ, and ˋ/config/validationCriteriaˋ; a boolean for ˋ/useForValidationˋ and ˋ/activatedˋ; an array for ˋ/config/valuesˋ and ˋ/config/childrenˋ.
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
