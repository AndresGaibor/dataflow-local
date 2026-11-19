---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-semantic-type-create/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance semantic-type create

## qlik data-governance semantic-type create

Create a semantic type

### Synopsis

Creates a new semantic type for the current tenant. A semantic type can be defined as a regular expression, a dictionary of values, or a compound of other semantic types, as specified by the `type` field in the request body.

```
qlik data-governance semantic-type create [flags]
```

### Options

```
      --activated                          
      --config-children strings            A coumpound of multiple kinds of semantic types
      --config-validationContent string    one of ANY_CHARACTER / ALPHABETIC / NUMERIC,
                                           ANY_CHARACTER: validates all characters,
                                           ALPHABETIC: validates only alphabetic content,
                                           NUMERIC: validate only number
                                           Allowed values: "ANY_CHARACTER", "ALPHABETIC", "NUMERIC"
      --config-validationCriteria string   one of EXACT_VALUE / IGNORE_CASE_AND_ACCENTS,
                                           EXACT_VALUE: matches only the exact values in dictionary,
                                           IGNORE_CASE_AND_ACCENTS: case and accents are ignored
                                           Allowed values: "EXACT_VALUE", "IGNORE_CASE_AND_ACCENTS"
      --config-validationPattern string    Regular expression
      --config-values strings              A semantic type for words matching a value in the list of values
      --description string                 
  -f, --file file                          Read request body from the specified file
  -h, --help                               help for create
      --interval int                       Duration in seconds to wait between retries, at least 1 (default 1)
      --label string                       
  -q, --quiet                              Return only IDs from the command
      --raw                                Return original response from server without any processing
      --retry int                          Number of retries to do before failing, max 10
      --type string                        
      --useForValidation                   
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
