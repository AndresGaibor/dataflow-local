---
source: https://qlik.dev/changelog/17-qlik-cli-update/
last_updated: 2025-07-08T16:09:30Z
---

# qlik-cli 2.6.0 released

## 2.6.0

- New: Added `qlik edit` command - you can now easily update resources without
  worrying about the complicated JSON Patch calculations. Based on the `EDITOR`
  environment variable, the edit command starts your preferred editor
  automatically and once your changes are saved, all `PUT`/`PATCH` operations are
  automatically done.

  *If you want to see communication details for your edit call, you can use
  the `--verbose` flag. It displays all HTTP operations that are
  performed including payloads for requests.*

  example:

  ```bash
  qlik webhook edit <webhookId>
  # this command launches your preferred editor containing the resource in json format
  # changing, for example, the description parameter is the equivalent of doing
  # a patch request with payload:
  # [
  #   {
  #       "op": "replace",
  #       "path": "/description",
  #       "value": "my new description"
  #   }
  # ]
  ```

- New: Added `qlik spec get` provides more detailed information about added
  external specs, most notably the path to the added specification.

- New: The auto-generated usage documentation now get automatically published to
  [qlik-cli](https://qlik.dev/toolkits/qlik-cli) upon new releases.

- Fix: Improved robustness in handling of array subtypes - missing types
  now return errors.
  Any included schema is thus required to have proper types defined. Previously,
  it defaulted to string if the type was missing.
