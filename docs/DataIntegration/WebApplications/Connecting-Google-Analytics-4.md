---
title: "Google Analytics 4"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Google-Analytics-4.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Google Analytics 4

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

Google Analytics 4 is an analytics service that enables you to measure traffic and engagement across your websites and apps. You can use Google Analytics 4 custom reports as a data source when landing or replicating data.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your Google Analytics 4 custom reports, you need to authenticate the connection with your account credentials.

1. Go to https://console.cloud.google.com/apis/library/analytics.googleapis.com and click Enable.
2. Go to https://console.developers.google.com/apis/api/analyticsdata.googleapis.com/overview and click Enable.
3. Go to https://console.developers.google.com/apis/api/analyticsreporting.googleapis.com/overview and click Enable.
4. Click Credentials.
5. Click Create credentials.
6. Click OAuth client ID, and select Web application.
7. Add https://connector.qlik.com/auth/oauth/v3.htm as an Authorized redirect URI.
8. Click Create.

You can now see Client ID and Client Secret that you need to copy to the connection settings.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

## Custom reports

You can use up to ten Google Analytics 4 custom reports.

1. Go to https://ga-dev-tools.web.app/query-explorer, and make sure it is set to GA4.
2. Select your metrics and dimensions.
3. Click the copy icon next to Request JSON at the bottom of the page to copy the value.

   Warning noteDo not try to copy any other way than using the copy icon.
4. Paste the copied text to a custom report field in the connection.

Information note Start and end dates from the report are not used. Instead, the Start Date set in the connection is used.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Provide a name for the connection in Connection name.
5. Select Open connection metadata to define metadata for the connection when it has been created.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Client ID | Client ID for Google Analytics GA4 OAuth authentication. |
| Client Secret | Client secret for Google Analytics GA4 OAuth authentication. |
| Custom Report One | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Two | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Three | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Four | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Five | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Six | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Seven | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Eight | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Nine | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Custom Report Ten | Custom report JSON.  For more information, see [*Custom reports*](#Custom). |
| Start Date | Start date in the format `YYYY-MM-DD`.  Example: 2020-10-01  Information noteStart and end dates from the report are not used. |
| Property ID | Google Analytics 4 property identifier.  For more information, see <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>. |
