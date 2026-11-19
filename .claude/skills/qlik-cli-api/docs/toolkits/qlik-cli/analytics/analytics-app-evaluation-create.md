---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-app-evaluation-create/
last_updated: 2026-10-14T09:59:57Z
---

# analytics app evaluation create

## qlik analytics app evaluation create

Queue an app evaluation

### Synopsis

Queues a performance and scalability evaluation for the specified app, scheduling
it for execution by the evaluation engine. The evaluation measures object response
times, CPU usage, document size, and data model metrics. Once queued, use the
returned `id` with the retrieval operations to poll for results.

```
qlik analytics app evaluation create [flags]
```

### Options

```
      --appId string            (Required) The unique identifier of the app to evaluate.
      --engineSizeHint string   Overrides the automatic engine size calculation with the supplied number of GiB.
                                The value is forwarded to the engine session request when acquiring an engine.
                                Optional.
  -f, --file file               Read request body from the specified file
  -h, --help                    help for create
      --interval int            Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet                   Return only IDs from the command
      --raw                     Return original response from server without any processing
      --retry int               Number of retries to do before failing, max 10
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
