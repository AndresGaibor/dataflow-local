---
source: https://qlik.dev/toolkits/qlik-cli/app/app-reload/
last_updated: 2026-10-14T09:59:57Z
---

# app reload

## qlik app reload

Do a reload interactively and print the logs

### Synopsis

Reload and save the app in an interactive engine session, printing the reload log as it runs.

The reload runs on the engine serving the session and is subject to its memory limits. To reload large apps in Qlik Cloud, use 'qlik reload create' instead, which lets Qlik Cloud run the reload on a suitable engine.

```
qlik app reload [flags]
```

### Examples

```
qlik app reload --app myapp
```

### Options

```
  -a, --app string   Name or identifier of the app
  -h, --help         help for reload
      --limit int    Limit the number of rows to load
      --no-data      Open app without data
      --no-save      Do not save the app
      --partial      Perform a partial relaod
      --silent       Do not log reload output
  -t, --traffic      Log JSON websocket traffic to stderr
      --ttl string   The Engine session's time to live in seconds (default "0")
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
