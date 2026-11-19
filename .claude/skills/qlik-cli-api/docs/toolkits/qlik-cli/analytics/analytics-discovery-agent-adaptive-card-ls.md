---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-discovery-agent-adaptive-card-ls/
last_updated: 2026-10-14T09:59:57Z
---

# analytics discovery-agent adaptive-card ls

## qlik analytics discovery-agent adaptive-card ls

List Adaptive Cards

### Synopsis

Retrieves Adaptive Cards for in-app metrics. Supports fetching a single card by metric ID or multiple cards by a list of metric IDs. Supports filtering by app IDs, measures, dimensions, categories, breakdown dimensions, analysis types, and triggered time range. When filtering by measures, use the `appIds` parameter to scope results to specific apps, as the same measure expression can exist across multiple apps.

When called without any filter parameters, only the top-ranked result per metric is returned. When any filtering parameter is supplied (`metricIds`, `dimensions`, `measures`, `appIds`, `breakdowns`, `analysisTypes`, `comparisonPeriods`, `timeRangeStart`, `timeRangeEnd`), ranking is not applied and all matching results are returned.

```
qlik analytics discovery-agent adaptive-card ls [flags]
```

### Options

```
      --analysisTypes strings       Filter by analysis type. Repeat the parameter to include multiple types. When this parameter is present, all matching results are returned regardless of ranking.
                                    Allowed values: "recordHigh", "recordLow", "aboveModel", "belowModel", "spikesUp", "spikesDown", "newBaseLine", "trendChanges"
      --appIds strings              Filter by app ID(s). Use this to scope results to specific apps. When combined with measures, returns only cards matching BOTH criteria (AND logic). Repeat the parameter to supply multiple app IDs (OR logic within appIds).
                                    
                                    **Recommendation:** Use consistent parameter order for better HTTP cache hit rates:
                                    1. appIds (if present)
                                    2. measures (if present)
                                    3. other filters
                                    4. pagination (limit, next, prev)
                                    
                                    **Example - One app, multiple measures:**
                                    ˋ?appIds=app-123&measures=Sum(Sales)&measures=Avg(Revenue)&measures=Count(Orders)ˋ
                                    
                                    **Example - Multiple apps, one measure:**
                                    ˋ?appIds=app-retail&appIds=app-wholesale&measures=Sum(Sales)ˋ
                                    
                                    **Example - Multiple apps, multiple measures:**
                                    ˋ?appIds=app-sales&appIds=app-hr&measures=Sum(Revenue)&measures=Avg(Salary)ˋ
      --breakdowns strings          Filter by one or more breakdown selections in the form ˋdimension:valueˋ (example ˋRegion:EMEAˋ). Values are selected from the UI dropdown — not free text — and should match available dimension/value pairs.
                                    Repeat the parameter to supply multiple breakdowns; results match any of the provided breakdown pairs.
      --categories strings          Filter by category IDs from the business glossary. Category filtering is not currently applied to the result set.
      --comparisonPeriods strings   Filter by comparison period. Example values: ˋDˋ, ˋWˋ, ˋMˋ, ˋQˋ, ˋYˋ. When this parameter is present, all matching results are returned regardless of ranking.
                                    Allowed values: "D", "W", "M", "Q", "Y"
      --dimensions strings          Filter by dimension(s). Matching is case-sensitive; leading and trailing whitespace will be trimmed. Repeat the parameter to supply multiple dimensions.
  -h, --help                        help for ls
      --interval int                Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int                   The total number of resources to retrieve.
      --measures strings            Filter by measure(s). Matching is case-sensitive; leading and trailing whitespace will be trimmed. Repeat the parameter to supply multiple measures.
      --metricIds strings           Filter by metric ID. Repeat the parameter to supply multiple IDs. When omitted, returns cards for all metrics visible to the caller.
      --next int                    The numeric offset to the next page of resources. Provide either the next or prev parameter, but not both.
      --prev int                    The numeric offset to the previous page of resources. Provide either the next or prev parameter, but not both.
  -q, --quiet                       Return only IDs from the command
      --raw                         Return original response from server without any processing
      --retry int                   Number of retries to do before failing, max 10
      --sort string                 The field to sort by, with +/- prefix indicating sort order
                                    Allowed values: "creationTime", "+creationTime", "-creationTime"
      --timeRangeEnd string         Exclusive upper bound for filtering by analysis result end time. Use ISO 8601 format.
      --timeRangeStart string       Inclusive lower bound for filtering by analysis result end time. Use ISO 8601 format.
      --type string                 Filter by Adaptive Card category. When omitted, cards from all categories are returned.
                                    Allowed values: "measures", "dimensions", "breakdowns"
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
