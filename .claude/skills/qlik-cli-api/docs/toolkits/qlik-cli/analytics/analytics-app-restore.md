---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-app-restore/
last_updated: 2026-10-14T09:59:57Z
---

# analytics app restore

## qlik analytics app restore

Restore an application

### Synopsis

Restores a soft-deleted Qlik Cloud Analytics application to the same space with the same app ID, retaining the properties it had at the time of deletion.
This operation is available to the app owner and Tenant Admins. The app owner can restore the app only if the original space still exists and they still have delete permission in the space; otherwise, a 403 Forbidden error is returned.
Associated resources such as data alerts, subscriptions, collections, notes, and tags are deleted when the app is deleted and cannot be restored.

```
qlik analytics app restore <appId> [flags]
```

### Options

```
  -h, --help           help for restore
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
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
