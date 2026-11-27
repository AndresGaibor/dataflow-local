---
title: "Workday Reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Workday-Reports-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Workday Reports

Workday is a cloud-based enterprise resource planning (ERP) platform that provides human capital management, financial management, and analytics capabilities. Workday Reports (Report-as-a-Service) is a Workday feature that exposes custom reports as web service endpoints, making report data available for external consumption via API.

Workday Reports integration replicates data using the [Workday RaaS Public Web Services API](https://community.workday.com/api). Each report you configure becomes its own dataset in the destination.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

The connector supports three authentication methods:

- JWT Bearer Token (default): Use a private key to sign in as a Workday integration system user.
- Basic Auth: Use a Workday user name and password.
- Authorization Code: Use the OAuth browser-based sign-in flow to authorize the connection.

To set up your Workday Reports account, you need:

- A Workday tenant with one or more custom reports to replicate.
- Each report must be enabled as a web service in Workday.
- A Workday user with permission to run each report. For JWT Bearer Token authentication, use an integration system user.
- The web service URL for each report.

To enable a report as a web service:

1. Log into your [Workday](https://www.workday.com/en-us/signin.html) account.
2. Search for and run the Edit Custom Report task for the report you want to replicate.
3. Open the Advanced tab.
4. Select Enable As Web Service.
5. Save the report.

To register the Workday API client for Authorization Code authentication:

1. Log into your [Workday](https://www.workday.com/en-us/signin.html) account.
2. Search for and run the Register API Client task.

   Use the Register API Client task, not Register API Client for Integrations. Only the first task supports the redirection URI required by the Qlik sign-in flow.
3. Enter a Client Name, such as Qlik Talend Cloud.
4. Set Client Grant Type to Authorization Code Grant.
5. Set Access Token Type to Bearer.
6. Set Redirection URI to https://connector.qlik.com/auth/oauth/v3.htm.
7. Select the Scope (Functional Areas) that cover the data you intend to replicate. Select the functional areas corresponding to the Workday modules that you need. If you do not grant a scope, the matching tables are excluded from discovery.
8. Save the task. Workday displays the Client ID and Client Secret once. Copy and paste them into a secured file.

### Set up JWT Bearer Token authentication

JWT Bearer Token authentication uses a private key to prove the connection can sign in as an integration system user. A Workday administrator must register the matching certificate and API client.

When the connector starts, it sends a signed assertion to the Workday token endpoint to obtain an access token. The assertion expires after five minutes. During a long run, the connector requests a new access token about once an hour. The token acts as the integration system user and is limited to the API client's scope. The connector does not save an access token or refresh token between runs.

To create a private key and certificate, run this OpenSSL command:

```
openssl req -x509 -newkey rsa:2048 -sha256 -nodes -days 730 \
-keyout workday-reports-key.pem -out workday-reports-cert.pem \
-subj "/CN=Qlik Workday Reports"
```

This command creates a private key file and a certificate file. Register the certificate in Workday; keep the private key secure because anyone with it can sign in as the integration system user within the API client's scope.

The private key must be an RSA key in PEM format without a passphrase. The `-days` value sets the certificate's expiration date. Choose a duration that meets your security policy and record the expiration date.

1. Choose or create an integration system user. Note the user name exactly as Workday displays it, without `@` or the tenant name.
2. Share each report with the user, and ensure the user can access each report's data source and fields. The connector returns only the rows the user is permitted to see.
3. Enable each report as a web service as described above.
4. Run Create x509 Public Key. Enter a name, paste the complete contents of `workday-reports-cert.pem` into Certificate, and save.
5. Run Register API Client and set the following values:
   - Client Name: Enter a name without parentheses.
   - Client Grant Type: Select JWT Bearer Token.
   - Access Token Type: Select Bearer.
   - x509 Certificate: Select the certificate you registered.
   - Integration System User: Select the user from step 1.
   - Grant Administrative Consent and Include Workday Owned Scope: Select Yes.
   - Scope (Functional Areas): Include Tenant Non-Configurable, Integration, and the functional areas that secure each report's data source. To find these areas, run View Security for Securable Item on the data source.
6. Save the API client. Copy its Client ID and Token Endpoint exactly as Workday displays them.

You do not need to run Configure Web Service Security when the integration system user is specified on the API client.

To get the report URL:

From the report's related actions in Workday, click Web Service > View URLs, then copy the JSON URL. It has the following form:

`https://<host>/ccx/service/customreport2/<tenant>/<owner>/<Report_Name>`

The host must use HTTPS and end in `workday.com` or `myworkday.com`. For example:

- https://wd2-impl-services1.workday.com/ccx/service/customreport2/mytenant/owner/MyReport
- https://wd5-services1.myworkday.com/ccx/service/customreport2/mytenant/owner/MyReport

To renew the certificate before its expiration date:

1. Create a new RSA private key and certificate, then register the certificate with Create x509 Public Key.
2. Edit the API client and set x509 Certificate to the new certificate.
3. Edit the connection and replace Private Key with the new private key.

Information note

Connections cannot sign in between updating the API client and replacing the private key. Make both changes between scheduled runs. To avoid a gap, register a second API client with the new certificate, update the connection's Client ID and Private Key, then retire the old client.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm).  Optional. |
| Start Date | Required by the form. The connector reads each report in full on every run, so this date does not limit the rows it returns. |
| Authentication Method | Select JWT Bearer Token (default), Basic Auth, or Authorization Code. |
| Hostname | Enter the Workday API hostname, such as wd2-impl-services1.workday.com, without https:// or a path. For JWT Bearer Token authentication, use lowercase. The hostname must end in workday.com or myworkday.com. |
| Tenant | Enter your Workday tenant name. For JWT Bearer Token authentication, use the part of the token endpoint after `/ccx/oauth2/`. For example, if the endpoint is `https://wd2-impl-services1.workday.com/ccx/oauth2/acme/token`, enter `acme`. The Hostname and Tenant values together form `https://<hostname>/ccx/oauth2/<tenant>/token`. |
| Client ID | Enter the Client ID from the Workday API client. For JWT Bearer Token authentication, copy it exactly as Workday displays it. |
| Client Secret | Client secret for Authorization Code authentication. |
| Integration System User | For JWT Bearer Token authentication, enter the Workday user name without `@tenant`. |
| Private Key | For JWT Bearer Token authentication, paste the complete contents of the RSA private key in PEM format, including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines. Do not use a passphrase-protected key. The connection stores the key encrypted. |
| Username | User name for Basic Auth authentication. |
| Password | Password for Basic Auth authentication. |
| Report Name | Enter one or more reports to replicate. Add a row per report; each row requires the following fields:   - Report Name (required): A unique name for the report within this connection. The report name is used as the dataset name in the destination. - Report URL (required): The JSON web service URL for the report.   Information note If a report's name changes, the change is not reflected in an existing task. Create a new task to replicate the report under the new name. |

## Limitations and considerations

- Use JWT Bearer Token authentication on a new connection. Existing connections keep the connector version they were created with, which might not support this authentication method.
- If the configured Workday account loses access to a report or its underlying data, that report will return fewer columns, return no rows, or fail.
- Reports that are not enabled as a web service in Workday cannot be replicated.

Information note

Do not change the authentication method for a connection associated with an active task. Create a new task with the other authentication method instead.

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

For every report you configure, the available fields are determined by the data points defined in the Workday report. If a field you expect is missing, verify that the report in Workday includes that field.

- **Datasets and columns are generated dynamically.** Because Workday reports are customer-defined, there is no consistent output across reports or tenants.
- **Reload only.** Incremental replication is not available.
- **A primary key is required.** Qlik Talend Cloud does not assign a primary key automatically. You must designate a primary key for each report before you prepare and run the task, or the storage task fails.
