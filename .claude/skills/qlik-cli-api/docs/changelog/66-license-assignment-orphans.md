---
source: https://qlik.dev/changelog/66-license-assignment-orphans/
last_updated: 2026-01-19T14:21:00Z
---

# The Licenses API adds support for filtering on assignment orphans

The query parameter `orphans` has been added to the Licenses API to help identify
licenses assigned to users who do not exist in the tenant upon which the call is
made.

Assignment of licenses is keyed on the user `subject`, which is a unique string
provided by the Identity Provider. These assignments are handled separately to users
in the tenant, since a single entitlement can support more than one Qlik Cloud tenant,
or Qlik Sense Enterprise Client-managed site. This means that calls to the `users` API
on a tenant will return only users on that tenant, while a call to `licenses/assignments`
returns all global assignments to that entitlement.

In use cases where you have only 1 tenant, and want to track down and remove
assignments not linked to users, you can leverage the below API call, or automation
snippet to return a list of these assignments.

To call via code:

```bash
curl --get --location 'https://<TENANT>.<REGION>.qlikcloud.com/api/v1/licenses/assignments?orphans=true' ^
--header 'Authorization: Bearer <API_KEY>'
```

To call via an automation, and output a table of assignments, review
the [find orphaned assignments example](https://qlik.dev/manage/automate/find-orphaned-license-assignments).

Review the [license assignments endpoint](https://qlik.dev/apis/rest/licenses/#%23%2Fentries%2Fv1%2Flicenses%2Fassignments-get)
specification for further information.
