---
source: https://qlik.dev/toolkits/qlik-cli/di-project/di-project-import/
last_updated: 2026-10-14T09:59:57Z
---

# di-project import

## qlik di-project import

Import a project (JSON zip)

### Synopsis

Imports a data integration project synchronously from a legacy JSON-based `.zip` file.
This endpoint only accepts zips that contain JSON project files (the legacy format). The import is processed synchronously and completes before the response is returned.
Submitting a YAML-based zip to this endpoint returns `400`. To import a YAML-based zip, use `POST /di-projects/{projectId}/actions/import-async` instead.

```
qlik di-project import <di-projectId> [flags]
```

### Options

```
  -h, --help           help for import
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
      --zip file       
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
