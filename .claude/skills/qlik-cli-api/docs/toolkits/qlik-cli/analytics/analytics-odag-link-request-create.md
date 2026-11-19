---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-link-request-create/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-link request create

## qlik analytics odag-link request create

Submit an ODAG request

### Synopsis

Submits a new Analytics Application generation request with the current selection state from a selection Analytics Application. The request is validated against link properties before queuing.  On success, returns a request object that you must monitor for completion using the status endpoint.  Validation failures return detailed error information.

```
qlik analytics odag-link request create <odag-linkId> [flags]
```

### Options

```
      --actualRowEst int                                  The current row estimate value calculated by the link's ˋrowEstExprˋ property in the context of the selection Analytics Application.
      --bindSelectionState-selectedSize int               The actual number of selected values. Not used for ˋbindSelectionStateˋ.
      --bindSelectionState-selectionAppParamName string   The name of a variable or field that corresponds to one or more bindings having a matching ˋselectAppParamNameˋ used to generate Analytics Applications.
      --bindSelectionState-selectionAppParamType string   The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that ˋExcludeˋ is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0).
                                                          Allowed values: "Field", "Variable", "Property", "Exclude", "BDI"
      --bindSelectionState-values-numValue string         The list of values in the selection state for this field.
      --bindSelectionState-values-selStatus string        The valid set of selection states that a specific field value can be in. One of: ˋSˋ (selected), ˋOˋ (optional), or ˋXˋ (excluded).
                                                          Allowed values: "S", "O", "X"
      --bindSelectionState-values-strValue string         The list of values in the selection state for this field.
      --clientContextHandle string                        An opaque handle to a client-side object that contains the reference to the link being used.
  -f, --file file                                         Read request body from the specified file
  -h, --help                                              help for create
      --interval int                                      Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                                             Return only IDs from the command
      --raw                                               Return original response from server without any processing
      --retry int                                         Number of retries to do before failing, max 10
      --selectionApp string                               (Required) The system-assigned ID for an Analytics Application.
      --selectionState-selectedSize int                   The actual number of selected values. Not used for ˋbindSelectionStateˋ.
      --selectionState-selectionAppParamName string       The name of a variable or field that corresponds to one or more bindings having a matching ˋselectAppParamNameˋ used to generate Analytics Applications.
      --selectionState-selectionAppParamType string       The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that ˋExcludeˋ is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0).
                                                          Allowed values: "Field", "Variable", "Property", "Exclude", "BDI"
      --selectionState-values-numValue string             The list of values in the selection state for this field.
      --selectionState-values-selStatus string            The valid set of selection states that a specific field value can be in. One of: ˋSˋ (selected), ˋOˋ (optional), or ˋXˋ (excluded).
                                                          Allowed values: "S", "O", "X"
      --selectionState-values-strValue string             The list of values in the selection state for this field.
      --sheetname string                                  The name of the sheet from which the request is being made.
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
