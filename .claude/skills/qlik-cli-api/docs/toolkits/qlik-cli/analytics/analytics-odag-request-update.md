---
source: https://qlik.dev/toolkits/qlik-cli/analytics/analytics-odag-request-update/
last_updated: 2026-10-14T09:59:57Z
---

# analytics odag-request update

## qlik analytics odag-request update

Perform action on ODAG request

### Synopsis

Performs actions on ODAG requests such as pausing, resuming, or canceling them. Cancel actions are effective only before the data loading phase. For multi-application generation requests, actions apply only to sub-requests that have not yet started loading. Automatic acknowledgment  option simplifies state transitions.

```
qlik analytics odag-request update <odag-requestId> [flags]
```

### Options

```
      --action string     (Required) The action to perform on the request. One of: (1) ˋcancelˋ a pending or in-flight request; (2) ˋpauseˋ a request that has not started (still in the ˋqueuedˋ state); (3) ˋresumeˋ a paused request; (4) acknowledge a prior cancellation; or (5) acknowledge a prior failure.
                          Allowed values: "cancel", "pause", "resume", "ackcancel", "ackfailure"
      --autoAck           Optional flag used with the ˋcancelˋ action. When ˋautoAckˋ is ˋtrueˋ, a canceled request automatically transitions to the ˋcanceledAckˋ state after cancellation completes. When ˋautoAckˋ is ˋfalseˋ, the request transitions to ˋcanceledˋ, and you must call this endpoint again with ˋaction=ackcancelˋ to acknowledge the cancellation.
      --delGenApp         Optional flag that deletes the generated Analytics Application after an ˋactionˋ of ˋcancelˋ (with ˋautoAck=trueˋ), ˋackcancelˋ, or ˋackfailureˋ.
  -h, --help              help for update
      --ignoreSucceeded   Optional flag used with the ˋcancelˋ action. When ˋtrueˋ, the API does not return an error if the request reaches the ˋsucceededˋ state while the cancellation request is in progress.
      --interval int      Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet             Return only IDs from the command
      --raw               Return original response from server without any processing
      --retry int         Number of retries to do before failing, max 10
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
