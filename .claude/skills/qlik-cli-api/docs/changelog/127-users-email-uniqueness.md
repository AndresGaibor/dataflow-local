---
source: https://qlik.dev/changelog/127-users-email-uniqueness/
last_updated: 2025-03-13T13:32:37Z
---

# API updates - Email uniqueness will be enforced for disabled and invited users

Qlik is announcing a change in behavior for the [Users API](https://qlik.dev/apis/rest/users/),
which will take effect no sooner than **March 31, 2025**.

The Users API currently allows you to create a new user with an email that is
already associated with a `disabled` user in the tenant, and to update a user's
email to the same address already associated to another `invited` or `disabled` user
in the tenant.

The Users API will be updated to enforce email uniqueness across all
user statuses (including: `active`, `invited`, `provisioned`, `disabled`).

Endpoints affected:

- POST `/v1/users`
- PATCH `/v1/users/{id}`
