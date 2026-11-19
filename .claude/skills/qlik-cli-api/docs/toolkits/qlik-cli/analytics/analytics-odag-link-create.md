---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-link-create/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-link create

## qlik analytics odag-link create

Create an ODAG link

### Synopsis

Creates a new link that enables ODAG navigation from a designated selection Analytics Application to a generated Analytics Application that is created by copying the designated template Analytics Application, injecting values for bind variables harvested from the selection Analytics Application and dynamically loaded with data using those bindings. The Bindings will be initialized by searching the load script of the template Analytics Application for patterns of the form `$(od_FIELDNAME)[M-N]` where `FIELDNAME` is the name of a field in the model of the selection Analytics Application and the optional pattern `[M-N]` identifies the lower bound `M` and the upper bound `N` for the number of values for that field which must be in the active selection state of the selection Analytics Application for binding to occur.  The active selection state defaults to `selected` (i.e. green) unless the `od` prefix is immediately followed by some combination of the letters `s`, `o`, or `x`, in that order, specifically designating the `selected`, `optional` (i.e. white) and/or `excluded` (i.e. gray) groups of values to be harvested from the selection Analytics Application's selection state. The bindings in the `bindings` array in the request payload override the properties of the corresponding field bindings found in the script of the template Analytics Application.

```
qlik analytics odag-link create [flags]
```

### Options

```
      --bindings-formatting-delimiter string                 The character to use as a separator between two (or more) bound values when formatting the source values associated with this binding.  If this property is not supplied, a comma character will be used by default.  Use an empty string to indicate that no separator character should be used.
      --bindings-formatting-quote string                     The character to use for quote wrapping each of the bound values when formatting the source values associated with this binding.  If this property is not supplied, a single quote character (ˋ'ˋ) will be used by default.  Use an empty string to suppress quote wrapping the values.
      --bindings-numericOnly                                 Set to ˋtrueˋ to indicate that only numeric values from the selection Analytics Application source parameter should be used. The default value for this property, if left unspecified, is ˋfalseˋ. This is currently only settable in the template Analytics Application script and not when creating or updating a Link.
      --bindings-range-lowerBound int                        The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound.
      --bindings-range-upperBound int                        The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound.
      --bindings-selectAppParamName string                   The path (or name) of the selection Analytics Application field, variable, or property to obtain the list of values for this binding.
      --bindings-selectAppParamType string                   The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that ˋExcludeˋ is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0).
                                                             Allowed values: "Field", "Variable", "Property", "Exclude", "BDI"
      --bindings-selectionStates string                      A combination of the letters ˋSˋ and/or ˋOˋ to indicate which values from the selection states ˋselectedˋ or ˋoptionalˋ in the hypercube of the selection Analytics Application to harvest as bind values to inject into the script of the template Analytics Application at ODAG request submission time. This is currently only settable in the template Analytics Application script and not when creating or updating a Link.
      --bindings-templateAppVarName string                   A collection of Bindings.  Note that there can be multiple bindings having the same ˋtemplateAppFieldNameˋ in a binding collection to denote different usages of the field's selection state in the context of the data prep logic but they all must have the same value for their ˋrangeˋ property.
      --dynamicView                                          When ˋtrueˋ, the ODAG link is treated as a dynamic view. Analytics Application retention time is overridden to ˋ24 hoursˋ and the maximum number of generated Analytics Applications is set to ˋ1ˋ.
  -f, --file file                                            Read request body from the specified file
  -h, --help                                                 help for create
      --includeCharts                                        Determines whether master charts of the template Analytics Application are included in the response.
      --includeScript                                        Set to ˋtrueˋ to include the generated Analytics Application load script in the generated Analytics Application. The default value is ˋfalseˋ.
      --interval int                                         Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                                          (Required) The name of a link.
      --properties-appOpenMethod-context string              An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-appOpenMethod-openMethod string           The complete set of possible properties for a link and their associated user context/value pairings.
                                                             Allowed values: "Tab", "Window"
      --properties-appRetentionTime-context string           An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-appRetentionTime-retentionTime string     The complete set of possible properties for a link and their associated user context/value pairings.
      --properties-disable-context string                    An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-disable-disable                           The complete set of possible properties for a link and their associated user context/value pairings.
      --properties-genAppLimit-context string                An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-genAppLimit-limit int                     The complete set of possible properties for a link and their associated user context/value pairings.
      --properties-genAppName-context string                 An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-genAppName-formatString string            A string containing the base text of the name to use for the generated Analytics Application and optionally any number of placeholder patterns of the form ˋ{N}ˋ where ˋNˋ is an integer greater than or equal to ˋ0ˋ. The integer identifies the offset in the ˋparamsˋ array of an ˋAppNameParameterV2ˋ to evaluate at ODAG Request execution time to compute a fragment of the generated Analytics Application's name and insert it at the same position as its corresponding ˋ{N}ˋ placeholder.
      --properties-genAppName-params strings                 The complete set of possible properties for a link and their associated user context/value pairings.
                                                             Allowed values: "templateAppName", "userId", "curYear", "curMonth", "curDay", "curHr", "curMin", "curSec"
      --properties-limitPolicy-context string                An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-limitPolicy-limitPolicy string            The complete set of possible properties for a link and their associated user context/value pairings.
                                                             Allowed values: "Restrict", "AutoDelete"
      --properties-menuLabel-context string                  An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-menuLabel-label string                    The complete set of possible properties for a link and their associated user context/value pairings.
      --properties-overrideGenAppLimit-context string        An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-overrideGenAppLimit-overrideGenAppLimit   The complete set of possible properties for a link and their associated user context/value pairings.
      --properties-rowEstRange-context string                An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-rowEstRange-highBound int                 The maximum value for the row estimate to enable usage of the link. If the row estimate expression evaluates to a value larger than this value, the user will be prevented from submitting an ODAG request for this link.
      --properties-rowEstRange-lowBound int                  The minimum value for the row estimate to enable usage of the link to perform an ODAG request.  If the row estimate expression evaluates to a number lower than this value, the user will be prevented from submitting an ODAG request for this link.  If this value is not supplied, no minimum is required.
      --properties-targetSheet-context string                An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, ˋUser_*ˋ indicates that the link property setting applies to all users while ˋUser.name = joeˋ indicates the rule applies only to a specific user named ˋjoeˋ.
      --properties-targetSheet-sheetId string                The ID of the sheet to first navigate to when opening the generated Analytics Application from the selection Analytics Application.
      --properties-targetSheet-sheetName string              An optional, read-only property that is returned when retrieving a link if the ˋtargetSheetˋ setting exists for the current user in the link's ˋpropertiesˋ set and the sheet with that ID exists in the link's ˋtemplateAppˋ.
  -q, --quiet                                                Return only IDs from the command
      --raw                                                  Return original response from server without any processing
      --registerOnSelectionApp                               When true, ODAG also creates a generic object on the selection Analytics Application referencing the new link (ˋqType: odagapplinkˋ, or ˋdynamicappviewˋ for dynamic-view links), so the link shows up in the app's list of links. Idempotent on retry; must not be combined with a client-side registration of the same link.
      --retry int                                            Number of retries to do before failing, max 10
      --rowEstExpr string                                    The measure expression to be evaluated in the context of the selection Analytics Application for the link that estimates the number of records that will be qualified by the primary load query of the template Analytics Application. This expression must be valid in the context of the selection Analytics Application fields and update whenever the selection state of the selection Analytics Application changes.
      --selectionApp string                                  (Required) The system-assigned ID for an Analytics Application.
      --statusSetting string                                 The requested status transition to apply to a Link.
                                                             New links are always created with status ˋactiveˋ; ˋstatusSettingˋ is ignored.
                                                             When updating a Link, if ˋstatusSettingˋ is provided, the request updates the Link's ˋstatusˋ only (other fields in the payload are not applied). If omitted, the Link's status is not changed.
                                                             ˋstatusSettingˋ is an action, and it maps to the resulting ˋstatusˋ: - ˋactivateˋ sets ˋstatusˋ to ˋactiveˋ. - ˋdisableˋ sets ˋstatusˋ to ˋdisabledˋ. - ˋdecommissionˋ sets ˋstatusˋ to ˋdecommissionedˋ.
                                                             If ˋstatusSettingˋ has an unsupported value, the request returns an error and the Link is not updated.
                                                             Links with status ˋdecommissionedˋ cannot change status.
                                                             Allowed values: "activate", "disable", "decommission"
      --templateApp string                                   The system-assigned ID for an Analytics Application.
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
