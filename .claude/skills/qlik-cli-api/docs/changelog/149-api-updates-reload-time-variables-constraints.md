---
source: https://qlik.dev/changelog/149-api-updates-reload-time-variables-constraints/
last_updated: 2025-06-25T08:30:14Z
---

# Updated API - The Reloads API supports reload-time variable updates, and the Engine API supports constraints

To support dynamic reload workloads, reload-time variable updates and variable
constraints have been added for Analytics apps.

### Reload-time variable update

Using the new `variables` property on the [Reloads API](https://qlik.dev/apis/rest/reloads/#post-v1-reloads),
you can set variables directly in a reload request, enabling dynamic app behavior
without editing the load script. This reduces complexity, improves deployment
automation, and brings parity with QlikView-style task-driven customization.

Example request using reload-time variable update:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/reloads" \
  -X POST \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-type: application/json" \
  -d '{
        "appId": "your-app-id",
        "variables": {
          "customerId": "123",
          "region": "EMEA",
          "daysHistory": "30"
        }
      }'
```

These variables will be applied before any load script, and will be overwritten
by any LET or SET calls for these variables during script execution, so ensure
you validate state of each variable prior to overwriting.

Use cases include:

- Injecting customer-specific configuration at reload time, such as customer IDs,
  customer names, or specific customer mappings.
- Injecting situation-specific configuration at reload time, such as reconfiguring
  the number of days of history to load into the app in case of break-glass incidents.
- Supporting central control over app behavior across many apps or tenants.
- Migrating QlikView tasks that used variable configuration, and Qlik Sense Enterprise
  client-managed tasks which leveraged custom properties to pass configuration
  to apps.

### Variable constraints

To prevent accidental or unauthorized overrides, you can now constrain variables
in the load script. This ensures that certain variables must meet specified
criteria even when passed dynamically.

Example usage:

```txt
CONSTRAIN a = {"valuesnum": [2,3,4]}; // Require variable a to be a number of 2, 3, or 4
CONSTRAIN b = {"minnum": "3000"};     // Require variable b to be greater than 3000
CONSTRAIN c = {"maxnum": "4000"};     // Require variable c to be lesser than 4000
CONSTRAIN d = {"minnum": "3000", "maxnum": "4000"};           // Require variable c to be greater than 3000 and lesser than 4000
CONSTRAIN e = {"valuestext": ["Dept A", "Dept B", "Dept C"]}; // Require variable e to be text of `Dept A`, `Dept B`, or `Dept C`
```

This protects your app from:

- Malicious or malformed variable input that might break app logic or SQL queries.
- Unintended overrides in templated apps.

### Use them separately or together

Reload-time variable updates can be used alone to streamline deployments.
Constraints can be used independently to validate variable values.

Together, they form a secure and flexible configuration model for large-scale,
multi-tenant, or dynamic deployments.

For more information on passing variables, refer to the [Reloads API reference](https://qlik.dev/apis/rest/reloads/#post-v1-reloads).

To learn about setting constraints, see the [Constrain reference](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Constrain.htm)
on help.qlik.com and the [`GenericVariableConstraints` schema](https://qlik.dev/apis/json-rpc/qix/schemas/#genericvariableconstraints).
