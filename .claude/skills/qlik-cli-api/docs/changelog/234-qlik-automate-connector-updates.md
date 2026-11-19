---
source: https://qlik.dev/changelog/234-qlik-automate-connector-updates/
last_updated: 2026-07-02T14:13:27+01:00
---

# Block updates - Qlik Automate connectors

Updates have been made to
[Qlik Automate](https://qlik.dev/toolkits/no-code/) connectors and blocks.

### Amazon Bedrock connector \{#234-amazon-bedrock-connector}

**New blocks**:

- `Do Chat Completion`: Invokes an Amazon Bedrock model to run
  chat completion inference using the messages you provide.

### Azure OpenAI connector \{#234-azure-openai-connector}

**Updated blocks**:

- `Do chat completion`: Added `response_format`, `max_completion_tokens`,
  and `temperature` inputs for structured output and generation control.

### BitBucket connector

- All blocks: removed the requirement for the `read_registry` and `write_registry`
  scopes when authenticating the connector. These were removed in response to
  customer feedback.

### Google Sheets connector \{#234-google-sheets-connector}

**Updated blocks**:

- `get file info`: Updated to use the Google Drive v3 API endpoint.

### Microsoft Teams connector \{#234-microsoft-teams-connector}

**Updated blocks**:

- `list replies`: Updated to use the Microsoft Graph v1.0 API endpoint
  instead of the beta endpoint.

### Qlik Reporting connector \{#234-qlik-reporting-connector}

**Removed blocks**:

- `get chart image (deprecated)`: This deprecated block has been removed.
- `Get PixelPerfect Report (deprecated)`: This deprecated block has been
  removed.
- `get tabular report (deprecated)`: This deprecated block has been removed.

### Salesforce connector \{#234-salesforce-connector}

**Updated blocks**:

- `delete contact`: Updated to use Salesforce REST API version 67.0.

### ServiceNow connector \{#234-servicenow-connector}

**Updated blocks**:

- All blocks: Corrected the API URL pattern to remove an extra
  `.com` from the domain, fixing connectivity for ServiceNow instances
  that use a custom domain format.
