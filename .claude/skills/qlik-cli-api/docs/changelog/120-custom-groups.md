---
source: https://qlik.dev/changelog/120-custom-groups/
last_updated: 2025-02-03T13:41:21Z
---

# Updated API - The Groups API now supports custom groups

Custom Groups are a powerful new capability designed to give enterprise customers greater flexibility and control over
user and group management.

With Custom Groups, organizations that do not rely on Identity Provider (IdP) groups for access control can now create
and maintain user-to-group relationships directly in Qlik Cloud. This enables seamless group-based provisioning for both
administrative access and product feature controls.

### Use Cases Solved

- **Public Sector Flexibility**: Manage group memberships within Qlik Cloud to streamline resource access without
  relying on IdP-provided groups, simplifying integration with third-party applications.
- **Enterprise Autonomy**: Gain full control over user and group assignments without being tied to IT-managed Active
  Directory groups, empowering teams to adapt quickly to evolving needs.
- **Embedded Analytics**: With qlik-embed and OAuth2 Machine-to-Machine impersonation, use Custom Groups to handle
  user group membership using only REST APIs and the qlik-api framework, reducing complexity.

Custom Groups offer enhanced usability and autonomy, making access management easier and more aligned with your unique
organizational structure.

### API example: Create a custom group

Here's an example of how to create a custom group and assign a role to it using the [Groups API](https://qlik.dev/apis/rest/groups/):

```bash
curl -L "https://<TENANT>/api/v1/groups" ^
-X POST ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "{\"name\": \"<GROUP_NAME>\", \"status\": \"active\", \"providerType\": \"custom\", \"assignedRoles\": [{\"name\": \"<ROLE_NAME>\"}]}"
```

> **Note:** This is a non-breaking addition to the Groups API. Group creation requests sent without a `providerType`
> will continue to be created as an `IdP` group.

For more information, see [Managing groups](https://qlik.dev/manage/manage-groups).
