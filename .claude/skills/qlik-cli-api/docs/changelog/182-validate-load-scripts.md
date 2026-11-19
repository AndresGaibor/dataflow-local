---
source: https://qlik.dev/changelog/182-validate-load-scripts/
last_updated: 2026-01-19T14:21:00Z
---

# Validate Analytics application load scripts using Apps API

For programmatic integrations using Qlik Automate or third-party services, updates to Qlik
Analytics application load scripts previously could not be validated after update without
running a trial data refresh of the application. With a new engine feature, validate script,
users can now send a load script to an endpoint for validation without needing to load it
into an application. This helps to improve the quality of programmatic deployments by
verifying load script rewrites before they are updated in applications, and reducing
reload failures caused by script issues.

### How to validate load scripts

You can validate load scripts using the Apps API by sending a POST request to the `/v1/apps/validatescript`
endpoint with the load script you wish to validate in the payload.

> **Note:** This initial release validates script syntax, which is where most errors occur. It will not validate
> availability of data connections required for the script to run successfully, this must still be validated
> via a trial reload in the target application.

### Example: Unexpected token error

```json
{
    "script": "SET Thousand Sep=',';",
  }
```

Will return the error:

```json
"errors" [
  {
    "msg": "Unexpected token: 'Sep', expected: '='",
    "Info": "",
    "Column": 0,
    "line": 0,
    "ch": 0
  }
],
"Warnings": []
```

For more information, see:

- [Apps API reference](https://qlik.dev/apis/rest/apps/)
- [validate load script examples](https://qlik.dev/manage/automate/validate-load-script/)
