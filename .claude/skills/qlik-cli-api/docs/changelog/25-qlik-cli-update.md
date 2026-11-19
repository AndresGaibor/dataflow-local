---
source: https://qlik.dev/changelog/25-qlik-cli-update/
last_updated: 2025-07-08T16:09:30Z
---

# qlik-cli 2.15.0 released

### Changes in v2.15.0

- Support for the new automation API with the `automation` command

  ```bash
  # get an automation
  qlik automation get <automationId>
  # list automation runs
  qlik automation run ls --automationId <automationId>
  ```

  See the command documentation [here](https://qlik.dev/toolkits/qlik-cli/automation/automation)

- Fix: Fail before request on missing path parameter

  ```bash
  qlik item update itemId --file ./my_file
  # now output an explicit error message about required parameters
  Error: required flag(s) "resourceType" not set
  ```

- Fix: correct output when using the `--json` for errors

  ```bash
  qlik extension get don_t_exists --json
  # now outputs json ready to be parsed
  {
      "status": 404,
      "title": "Not found"
  }
  ```
