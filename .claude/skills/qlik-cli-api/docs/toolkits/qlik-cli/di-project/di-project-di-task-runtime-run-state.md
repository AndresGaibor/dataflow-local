---
source: https://qlik.dev/toolkits/qlik-cli/di-project/di-project-di-task-runtime-run-state/
last_updated: 2026-10-14T09:59:57Z
---

# di-project di-task runtime run state

## qlik di-project di-task runtime run state

View task run state

### Synopsis

Task run state shows the execution progress and any errors encountered during a specific run instance of a data task.

```
qlik di-project di-task runtime run state [flags]
```

### Options

```
  -h, --help   help for state
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
