---
source: https://qlik.dev/changelog/245-qlik-automate-connector-updates/
last_updated: 2026-09-02T14:19:24Z
---

# Block updates - Qlik Cloud Services, Qlik Platform Operations & GitHub connectors

Updates have been made to
[Qlik Automate](https://qlik.dev/toolkits/no-code/) connectors and blocks.

### GitHub connector \{#245-github-connector}

**New blocks**:

- `Delete Branch`: Deletes a branch from a repository.

### Qlik Cloud Services connector \{#245-qlik-cloud-services-connector}

**New blocks**:

- `Add space role to member by name`: Retrieves the member's current roles in the space, verifies
  the target role is assignable in that space type, and assigns it if not already present.
- `Create Data Connection`: Creates a new connection object from an automation connector.
- `Duplicate data connection`: Duplicates a connection.
- `Update data connection`: Updates the specified properties of a connection.
- `Get IP policy`: Returns details for a specific IP policy by policy ID.
- `Create IP policy`: Creates a new IPv4 IP policy in the tenant.
- `List IP policies`: Returns a list of IP policies present in the tenant.
- `Update IP policy`: Updates the IP policy.
- `Delete IP policy`: Deletes an IP policy by ID.
- `Do app evaluation`: Queues an app evaluation.
- `Get app evaluation`: Retrieves the result of an app evaluation.
- `List evaluations`: Lists app evaluations for an app.
- `Get Tenant Banner`: Retrieves the announcement banner configuration for the tenant.
- `Set Tenant Banner`: Sets the content and action links for the tenant-wide announcement banner.
- `Remove space role from member by name`: Retrieves the member's current roles and removes the
  specified role if assigned.
- `Get ODAG Settings`: Retrieves ODAG settings, including feature enablement status.
- `Update ODAG Settings`: Updates the ODAG settings.
- `List ODAG Apps`: Returns a list of all ODAG apps.
- `Create ODAG Link`: Creates an On-Demand App Generation (ODAG) link in the tenant.
- `Get ODAG Link`: Retrieves an ODAG link by ID.
- `List ODAG Links`: Returns a list of ODAG links.
- `Sync ODAG Links`: Registers the ODAG links referenced by a selection app and returns those the user can access.
- `Update ODAG Link`: Updates an ODAG link in the tenant.
- `Create ODAG Link Request`: Creates an ODAG link request.
- `Get ODAG Link Request`: Retrieves information about an ODAG link request by ID.
- `List ODAG Link Requests`: Returns a list of ODAG link requests.
- `Update ODAG Link Request Action`: Performs actions on ODAG requests, such as pausing, resuming, or canceling them.

**Updated blocks**:

- `Create group`: Added an optional parameter to assign roles to the group on creation.
- `Raw API request`: Fixed an issue where DELETE requests with an empty request body incorrectly
  returned a "Request body must be empty" error.

### Qlik Platform Operations connector \{#245-qlik-platform-operations-connector}

**New blocks**:

- `Add space role to member by name`: Retrieves the member's current roles in the space, verifies
  the target role is assignable in that space type, and assigns it if not already present.
- `Create IP policy`: Creates a new IPv4 IP policy in the tenant.
- `Delete IP policy`: Deletes an IP policy by ID.
- `Get IP policy`: Returns details for a specific IP policy by policy ID.
- `List IP policies`: Returns a list of IP policies present in the tenant.
- `Duplicate Analytics Data Connection`: Duplicates an existing analytics data connection.
- `Update Analytics Data Connection`: Updates an existing analytics data connection.
- `List members from space - for lookup`: Lists members of a space for use in lookup fields.
- `Remove space role from member by name`: Retrieves the member's current roles and removes the
  specified role if assigned.
- `Get Tenant Banner`: Retrieves the announcement banner configuration for the tenant.
- `Set Tenant Banner`: Sets the content and action links for the tenant-wide announcement banner.
- `List ODAG Apps`: Returns a list of all ODAG apps.
- `Get ODAG Settings`: Retrieves ODAG settings, including feature enablement status.
- `Update ODAG Settings`: Updates the ODAG settings.
- `Create ODAG Link`: Creates an On-Demand App Generation (ODAG) link in the tenant.
- `Get ODAG Link`: Retrieves an ODAG link by ID.
- `List ODAG Links`: Returns a list of ODAG links.
- `Sync ODAG Links`: Registers the ODAG links referenced by a selection app and returns those the user can access.
- `Update ODAG Link`: Updates an ODAG link in the tenant.
- `Update ODAG Link Request Action`: Performs actions on ODAG requests, such as pausing, resuming, or canceling them.
- `Create ODAG Link Request`: Creates an ODAG link request.
- `Get ODAG Link Request`: Retrieves information about an ODAG link request by ID.
- `List ODAG Link Requests`: Returns a list of ODAG link requests.

**Updated blocks**:

- `Create group`: Added an optional parameter to assign roles to the group on creation.

**Removed blocks**:

- `Get Tenant Name and Region`
