---
source: https://qlik.dev/toolkits/qlik-cli/data-governance/data-governance-semantic-type-import/
last_updated: 2026-10-14T09:59:57Z
---

# data-governance semantic-type import

## qlik data-governance semantic-type import

Import semantic types

### Synopsis

Imports semantic types from a JSON file. Supports Qlik Cloud format (`QlikSemanticTypesExport`) and Talend legacy format (`DQDictionaryImportExport`). Format is auto-detected from the `exportFormat` field in the payload.

**Conflict handling** is controlled by the `skipConfirmation` flag and the optional `conflictResolutions` array:

- **Preview** (`skipConfirmation` false/absent, no `conflictResolutions`):
  the file is analysed but nothing is imported. Returns `200` with a
  per-type conflict/summary body. Re-submit with `skipConfirmation=true`
  or `conflictResolutions` to actually apply the import.

- **One-shot** (`skipConfirmation=true`, no `conflictResolutions`):
  if real conflicts or in-file duplicates exist, returns `200` with the
  conflict body and imports nothing; otherwise the import is applied and
  `201` is returned with the import report.

- **Resolved** (`conflictResolutions` provided): the import is applied using
  the per-label strategies, falling back to `defaultConflictStrategy`
  (defaults to `SKIP`) for unlisted labels. Returns `201` in both cases
  (conflicts present or not), with the import report.

Import is best-effort: each type is processed independently. Failures are logged in the response report without blocking other types.

```
qlik data-governance semantic-type import [flags]
```

### Options

```
      --conflictResolutions-label string      Label of the conflicting semantic type.
      --conflictResolutions-strategy string   ˋOVERWRITEˋ: replace the existing type with the version from the file. ˋSKIPˋ: keep the existing type unchanged, do not import. ˋKEEP_BOTHˋ: keep the existing type and create the version from the file with a deduplicated label.
                                              Allowed values: "OVERWRITE", "SKIP", "KEEP_BOTH"
      --defaultConflictStrategy string        Fallback strategy applied to conflicting types not listed in ˋconflictResolutionsˋ. Defaults to ˋSKIPˋ.
                                              Allowed values: "OVERWRITE", "SKIP", "KEEP_BOTH"
      --file unknown                          (Required) The export file payload as-is. Format is detected from the ˋexportFormatˋ field. Accepts ˋQlikSemanticTypesExportˋ (Qlik native) or ˋDQDictionaryImportExportˋ (Talend legacy).
  -h, --help                                  help for import
      --interval int                          Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                                 Return only IDs from the command
      --raw                                   Return original response from server without any processing
      --retry int                             Number of retries to do before failing, max 10
      --skipConfirmation                      Controls preview vs. one-shot import when no ˋconflictResolutionsˋ are supplied. When ˋfalseˋ (default) the call is a **preview**: the file is analysed and a per-type conflict/summary body is returned (HTTP 200) without importing anything. When ˋtrueˋ the import is attempted **one-shot**: if real conflicts or in-file duplicates exist the conflict body is returned (HTTP 200) and nothing is imported; otherwise all types are imported (HTTP 201). Ignored when ˋconflictResolutionsˋ are provided (those always apply the import).
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
