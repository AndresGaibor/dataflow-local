---
source: https://qlik.dev/toolkits/qlik-cli/qlik/qlik/
last_updated: 2026-10-14T09:59:57Z
---

## qlik

qlik is a tool for working with Qlik Cloud

### Synopsis

qlik is a Command Line Interface for Qlik Cloud.

It gives you access to all public APIs which enables you to administrate your tenant and apps,
develop and manage apps, migrate data and much more.

Sending quotes in the body requires a different syntax for some Windows terminals.
Powershell: qlik ... --body '\[\{"op":"replace","path":"/name","value":"abc"}]'
CMD.exe: qlik ... --body \[\{"op":"replace","path":"/name","value":"abc"}]

```
qlik [flags]
```

### Options

```
  -c, --config string            path/to/config.yml where parameters can be set instead of on the command line
      --context string           Name of the context used when connecting to Qlik Associative Engine
      --headers stringToString   HTTP headers to use when connecting to Qlik Associative Engine (default [])
  -h, --help                     help for qlik
      --insecure                 Allow connecting to hosts with self-signed certificates
      --json                     Returns output in JSON format, if possible. Disables verbose and traffic output
  -s, --server string            URL to Qlik Cloud or directly to a Qlik Associative Engine
      --server-type string       The type of server you are using: cloud, Windows (Enterprise on Windows) or engine
  -v, --verbose                  Log extra information
```
