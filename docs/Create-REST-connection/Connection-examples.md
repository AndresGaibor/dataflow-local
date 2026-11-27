---
title: "Setting up selected REST sources for data loading"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/Create-REST-connection/Connection-examples.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "REST data sources", "Create a REST connection"]
---

# Setting up selected REST sources for data loading

The following procedures explain how to acquire the connection requirements for selected social networking platforms:

- Facebook
- LinkedIn

You use the developer interface for each platform to get credentials and query parameters for the specific application or service you intend to collect data from.

Warning noteThe procedures below are accurate for the particular requests illustrated. The procedures for alternative requests may differ from those illustrated. Also, social networking platforms used in the illustrated procedures may change their interface or the other details of the procedure. When that happens, the procedures below will not be completely accurate.

## Connecting to Facebook

Do the following:

1. Sign into your Facebook account at:

   [Facebook for developers](https://developers.facebook.com/)
2. Create a new application.

   The registration and validation process for the application takes time, so the application may not be available as soon as you add it. If you have an application that was written previously, you can access that immediately, but it must be an application created with a developer account.
3. Navigate to the developer explorer page at:

   [Facebook for developer tools: select Graph API Explorer](https://developers.facebook.com/tools)
4. Select the application.
5. Select Get Access Token.

   The objective is to provide access to data. Get Access Token is currently the interface label Facebook uses. Even if that label changes, there must be a means of getting an access token.
6. Generate an API method.
7. Submit.
8. Go to the connection dialog in the REST Connector.
9. In the URL field, enter the URL from your Facebook application.

   The URL contains the API method that determines the type of response the data source returns. For example:

   https://graph.facebook.com/+'me?fields=albums.limit(5),posts.limit(5)'
10. Add a parameter in the Query parameters field for the access token you received for the application.

    For example:

    ![Query parameters field with the name specified as access_token and the value being the Access Token supplied by the API](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/ex_Facebook-access-token.PNG)

    The access token authenticates your access to the Facebook data. You do not need Windows authentication nor do you need to provide your Facebook credentials in the User name and Password fields.
11. Complete the remaining fields and selections in the connection dialog.

    [*Create a REST connection*](Create-REST-connection.htm)

## Connecting to LinkedIn

Do the following:

1. Sign into your LinkedIn account at:

   [Linkedin](https://www.linkedin.com/)
2. Navigate to the developer page at:

   [Linkedin Developers](https://www.linkedin.com/developer/apps)
3. Create a new application.

   The registration and validation process for the application takes time, so the application may not be available as soon as you add it. If you have an application that was written previously, you can access that immediately.
4. Follow the LinkedIn instructions for setting up OAuth 2.0 authentication and acquiring an access code: [Authenticating with OAuth 2.0 Overview](https://docs.microsoft.com/en-us/linkedin/shared/authentication/authentication)
5. Go to the connection dialog in the REST Connector.
6. In the URL field, enter the URL generated for your LinkedIn application.
7. Enter your LinkedIn credentials in the User name and Password fields.
8. Add a parameter in the Query parameters field for the access token you received for the application.

   For example:

   ![Query parameters field with the name specified as oauth2_access_token and the value being the Access Token supplied by the API](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/ex_LinkedIn-access-token.PNG)
9. Complete the remaining fields and selections in the connection dialog.

   [*Create a REST connection*](Create-REST-connection.htm)
