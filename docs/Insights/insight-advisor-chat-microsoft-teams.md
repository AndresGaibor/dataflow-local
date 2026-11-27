---
title: "Exploring application content with conversational analytics in Microsoft Teams"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/insight-advisor-chat-microsoft-teams.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring applications with conversational analytics", "Accessing Insight Advisor Chat through external collaboration platforms"]
---

# Exploring application content with conversational analytics in Microsoft Teams

Integrate conversational analysis of Qlik Cloud application data into your Microsoft Teams workspace using Insight Advisor Chat. Using Microsoft Teams as an external collaboration channel, you and your team can easily explore and interact with data in personal and group chat interactions.

The Qlik chatbot app for Microsoft Teams allows you to collaboratively harness the power of automated analytics generation, using simple commands and natural language.

Interaction with a Qlik Sense application in Microsoft Teams

![Message bar in personal Microsoft Teams chat with the Qlik chatbot, showing how the interface prompts the user with the available commands.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SaaSMSTeams_overview.png "Click to view full size")

When you interact with the Qlik Cloud tenant through Microsoft Teams, you are using Qlik's Insight Advisor Chat service, which is also available in the Insights and Analytics [activity centers](#glossary-0 "Glossary term").
For more information about Insight Advisor Chat, see [*Exploring applications with conversational analytics*](insights-chat.htm).

Information noteThis help topic discusses accessing conversational analytics for analytics content in Qlik Cloud. For information about how to access Qlik Sense Enterprise on Windows environments through Microsoft Teams, see [Configuring Qlik Insight Advisor Chat for external channels](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Administer_QSEoW/QlikInsightsAdvisorChat/insights_externalChannels.htm).

## Terminology

Please note the distinctions between the following terms when reading this help content.

Terminology for conversational analytics in Microsoft Teams

| Term | Definition |
| --- | --- |
| Microsoft Teams | An external collaboration platform for team interactions. Users can interact with Qlik Sense application content within this platform. |
| Qlik chatbot app | The Microsoft Teams app that allows interactions with Qlik Sense application content through Insight Advisor Chat. |
| Qlik Sense application | The analytics application that contains the data which users will interact about, either in Qlik Cloud Analytics activity centers or through an external collaboration platform. |
| Insight Advisor Chat | The underlying Qlik service which allows conversational interactions between users and Qlik Sense application content. The same service is used in both Qlik Cloud Analytics and external collaboration platforms. |

## When to use Insight Advisor Chat in Microsoft Teams

The Qlik chatbot for Microsoft Teams can improve your team's efficiency by integrating the analytical power of Qlik Sense into a collaboration platform. It could be used in the following scenarios:

- Business analysts who primarily communicate over Microsoft Teams, but rely on Qlik Cloud to combine and aggregate the various enterprise data sources they use to track business needs.
- Agents and administrators in a technical support department, who might interact with clients and colleagues over Microsoft Teams, but frequently use Qlik Cloud to track their progress on incidents and tickets.
- Data analysts who use Qlik Cloud for machine learning and statistical analysis, but also need to collaborate with colleagues through Microsoft Teams.

## Prerequisites and setup

To use the Qlik chatbot app, users must have a Qlik account. Contact [Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) for assistance.

Before you can start, the following requirements must be met.

### Subscription requirements and cross-region inference

Insight Advisor Chat in Microsoft Teams is only available in tenants without a Qlik Answers license, or alternatively in tenants where cross-region inference is turned off.

Feature availability of Insight Advisor Chat in Microsoft Teams

| Scenario | Insight Advisor Chat available in Microsoft Teams |
| --- | --- |
| Qlik Answers licensed, cross-region inference turned on | No |
| Qlik Answers licensed, cross-region inference turned off | Yes (subject to tenant permission defaults) |

### Administration activity center requirements for Qlik Cloud administrators

Before you can use Microsoft Teams to interact with your Qlik Sense applications, your Qlik Cloud tenant administrator must complete the following actions:

- Add the Microsoft 365 tenant as a collaboration channel in the Administration activity center.
  For more information, see [*Adding connections to external collaboration platforms*](../Admin/mc-collaboration-platforms.htm).
- Assign permissions to allow users and groups to access the Qlik Cloud content in Microsoft Teams. Users need at least one of the following:

  - The Collaboration Platform User built-in security role. See:

    - [*Assigning security roles and custom roles*](../Admin/SaaS-roles-capacity-model.htm) (capacity-based subscriptions)
    - [*Assigning security roles and custom roles*](../Admin/SaaS-roles.htm) (user-based subscriptions)
    - [*Assigning security roles and custom roles*](../Admin/SaaS-roles-anonymous.htm) (Qlik Anonymous Access subscriptions)
  - The Insight Advisor in Microsoft Teams permission set to Allowed through the default permissions or a custom security role. See:

    - [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm) (capacity-based subscriptions)
    - [*Default permissions and custom roles*](../Admin/permissions-scopes.htm) (user-based subscriptions)
    - [*Default permissions and custom roles*](../Admin/permissions-scopes-anonymous.htm) (Qlik Anonymous Access subscriptions)

  Without one of these permissions, users cannot ask questions and use the available commands when interacting with the Qlik chatbot app. They might still be able to view interactions between other tenant members and the Qlik Sense applications.

  Information note

  It is also recommended that you assign In-app content download permissions accordingly for these users. For full access to application content in Microsoft Teams, users need the In-app content download permission set to No data or Allowed. This permission is set when configuring default permissions and custom roles. See:

  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes-capacity-model.htm#InApp) (capacity-based subscriptions)
  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes.htm#InApp) (user-based subscriptions)
  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes-anonymous.htm#InApp) (Qlik Anonymous Access subscriptions)

### Adding the Qlik chatbot app for Microsoft Teams

You interact with your Qlik Sense application content through the Qlik chatbot in Microsoft Teams. This chatbot is available as an app in Microsoft Teams.

The setup process for the Qlik chatbot app will vary depending on your organization's Microsoft 365 tenant configuration. For the application to be available for use or installation (for example, from the application store in Microsoft Teams), your Microsoft 365 tenant administrator might have to install and enable it for the tenant's users.

In some cases, the Qlik chatbot app will be installed and pre-configured for all or some users in the Microsoft 365 tenant once the application is enabled by their administrator. In other cases, you might need to add the app yourself. For information about the possible requirements from your Microsoft 365 tenant administrator, see [*Availability of the Qlik chatbot app in Microsoft Teams*](../Admin/microsoft-365-tenant-apps.htm).

For full details, refer to the [Microsoft 365 documentation](https://learn.microsoft.com/en-us/microsoft-365/?view=o365-worldwide). Try a search such as enabling chatbot app.

### Making Qlik Sense applications available in Microsoft Teams

For users to be able to interact with a Qlik Sense application in Microsoft Teams, the application must be made available in Insight Advisor Chat.

To turn Insight Advisor Chat on and off for an application in a collaborative space, you need the following roles in the space:

- Shared space: Can edit or higher permissions. See [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm).
- Managed space: Can manage, Can operate, or higher permissions. See [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm).

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

In Qlik Sense, open the application you would like to enable for exploration in Microsoft Teams.

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Settings.
2. In the menu, switch to the Capabilities tab.
3. Turn on Enable application for Insight Advisor Chat in activity centers.

For additional information, see [*Making applications available in Insight Advisor Chat*](insight-advisor-available-chat.htm).

## Adding the Qlik chatbot to a Microsoft Teams conversation

After the Qlik chatbot app has been added to your Microsoft Teams environment, you can interact with it in several conversation settings. To use the chatbot in group conversations and team channels, add it to the chat or channel. Depending on your organization's Microsoft Teams configuration, this action might have to be completed in the settings for the Qlik chatbot app. Refer to the Microsoft help documentation for more information.

## Supported conversation types

You can interact with the chatbot in the following conversation settings:

- Personal chat between you and the Qlik application
- Group chats between you and one or more other users
- In a team channel

### Interacting via personal chat

You can interact with the Qlik chatbot in your one-on-one chat with it. Open the personal chat, and type or select a command or question into the message bar. Insight Advisor Chat will return responses to your requests.

### Interacting via group chats and channels

The Qlik chatbot can be used in interactions between you and one or more other users. Before the users in the conversation can use conversational analytics with the Qlik Cloud tenant, the chatbot application must be added to the chat or channel. For more information, see [*Adding the Qlik chatbot to a Microsoft Teams conversation*](#Adding2).

For other users in the conversation to interact with the same Qlik Sense application, they must have permissions to the application and select the application in the chat by using the apps command.

To receive a response from the Qlik chatbot app, tag it in your message and select a command, or type a natural language question and send your message.

Warning noteIn group or team conversations, the generated responses are viewable by any chat members who do not have direct access to the Qlik Sense application or Qlik Cloud tenant. Always respect your organization's security policies. For more information, see [*Data security considerations*](#Data).

Do the following:

1. In the Microsoft Teams message bar, start typing @Qlik and select the Qlik application from the available options. This tags the Qlik chatbot in the message.

   A suggestion menu appears with a list of commands you can use.
2. Select one of the suggested commands or enter any text, and send the message.

Using the Qlik chatbot in team channels

![Example of how the Qlik Microsoft Teams bot can be used in a team channel for group interactions with data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SaaSMSTeams_team_channel1.png "Click to view full size")

## Data security considerations

### Security considerations for group conversations

For interactions with the Qlik chatbot in Microsoft Teams, the only credentials that are checked are those of the user making the request. This means that in group chats and channels, Insight Advisor Chat's responses could be viewable by users without access to the applications and Qlik Cloud tenant you are referencing, as well as users outside your organization.

In the same way, responses regarding application data protected by section access are viewable to users in the chat who do not have the required access to the data and the environment.

It is important to respect your organization's security policies when interacting with the Qlik chatbot in group conversations. You should only make requests if the requests and responses are acceptable to be shared with all users in the chat (and others who may be added to it in the future).

### Section access considerations

To interact with a Qlik Sense application that uses section access, users must have the required data access defined in the section access script. However, users without access to the application as per the section access script will still be able to see application names, field names, and master item names for applications they do not have access to. For more information, see [*Using Section Access and Insight Advisor Chat*](../Scripting/Security/manage-security-with-section-access.htm#Section).

Additionally, in group conversations, responses regarding application data protected by section access are viewable to any users in the chat who do not have the required access to the data.

## Logging in

To interact with the Qlik chatbot in Microsoft Teams (for example, clicking an interactive card in the chat or using commands yourself), you must be logged in individually with a Qlik account. The Qlik account you log in with does not have to be associated with your Microsoft 365 user account.

You are prompted to log into Qlik Cloud if you are not logged in and send a message or command to the Qlik application. The delivery of this prompt varies slightly, depending on whether you are interacting in a personal chat, group chat, or channel.

After you have been sent the login prompt, the chatbot will not respond to your questions or commands for the next three minutes, or until you have logged in.

After logging into the Qlik Cloud tenant in Microsoft Teams, your session is active for 30 days. When you log in, you are assigned an access token, which is automatically re-validated on a periodic basis until your session expires.

Information noteIf the Block passing 'offline\_access' scope to identity provider setting is turned on in your Qlik Cloud tenant's identity provider configuration, you will need to log in every six hours. See [*Configuring an identity provider (IdP)*](../Admin/mc-creating-idp.htm).

### In your personal conversation with the chatbot

Do the following:

1. In Microsoft Teams, open your personal, one-on-one chat with the Qlik chatbot.
2. Type any text into the message bar and send it. Alternatively, use the suggestions menu to select a command, and send it.
3. Click Sign In in the sign-in card that appears in the chat.

   Alternatively, find a sign-in card that is already in the chat and click Sign In.
4. In the window that opens, enter your Qlik Cloud tenant's Hostname, and select a region from the drop down list.

   These details can be found in your Qlik Cloud tenant URL.
5. Complete the remaining login steps in the window, using the login flow configured for your tenant.

### In a group conversation or team channel

Do the following:

1. In Microsoft Teams, open a group conversation or channel where you want to ask questions to the Qlik application.
2. In the message bar, start typing @Qlik. Select the Qlik application from the available options.

   This tags the Qlik application in the message.
3. With the Qlik application tagged in your message, type any text into the message bar and send it. Alternatively, use the suggestions menu to select a command, and send it.
4. Click Sign In in the sign-in card that appears in the chat.

   Alternatively, find a sign-in card that is already in the chat and click Sign In.
5. In the window that opens, enter your Qlik Cloud tenant's Hostname, and select a region from the drop down list.

   These details can be found in your Qlik Cloud tenant URL.
6. Complete the remaining login steps in the window, using the login flow configured for your tenant.

## Using commands and asking questions

You interact with the chatbot in the same way you interact with Insight Advisor Chat. For full details, see [*Exploring applications with conversational analytics*](insights-chat.htm).

You can use commands when interacting with the Qlik chatbot in Microsoft Teams. The available commands are shown as suggestions as you prepare your message. Commands allow you to make basic requests to the Insight Advisor Chat service, such as identifying the dimensions and measures in a Qlik Sense application.

You can also enter your questions to Insight Advisor Chat as natural language. You can enter the commands for the Qlik application as natural language (for example, by typing a question such as apps). Natural language can also be used to make more advanced requests using specific combinations of measures, dimensions, and filters from the application's data model.

For example, to aggregate a measure called Sales by a dimension called Product Category, applying a time filter to show results only for the year 2022, you could type show me total sales by product category for 2022.

You, and other users in the conversation with access to the Qlik Sense application, can ask follow-up questions which draw from a similar combination of parameters as the question that was last asked.

For example, if you ask a question such as show me dairy sales in UK, you or another user in the conversation can ask a follow-up question like what about USA. This question references the same measure (Sales) and dimensions (Product Category and Region), but applies different filters on the dimensions used.

For additional information about asking natural language questions, see [*Using natural language questions*](insights-chat.htm#Using).

### Available commands

To view and select from available options, use the apps, dimensions, and measures commands. The dimensions and measures commands display corresponding master items from an application. If an application has no master items, dimension and measure fields are displayed instead.

The following table contains a list of the available commands that you can use within the Qlik chat application for Microsoft Teams. Additional information about each of these commands can be found in subsequent sections on this page.

Available commands for Insight Advisor Chat in Microsoft Teams

| Command | Description |
| --- | --- |
| apps | Lists all available applications that the user can interact with. |
| dimensions | Lists all available dimensions in the currently selected application. |
| measures | Lists all available measures in the currently selected application. |
| questions | Displays the example questions that have been added to the Qlik Sense application by its developers. |
| clear | Clears the application that is selected as the subject of the chat. |
| clear entity context | Clears the dimensions and measures that have been selected in the conversation. The application context is kept. |
| language | Lists available languages and their two-letter language codes. |
| language <two-letter language code> | Sets the language to the specified value (for example, language en for English). |
| language clear | Resets the language. For information about default language used, see [*Changing the language*](#Changing). |
| help | Displays information to help guide you on using Insight Advisor Chat. |
| revoke token | Deletes the access token record that was generated when the user logged in. |
| logout | Logs the user out of the Qlik Cloud tenant. This does not delete the record of their access token. |

### Using commands and asking questions in the personal conversation

Do the following:

1. In Microsoft Teams, open your personal, one-on-one chat with the Qlik chatbot app.
2. Click the message bar, or Tab to it using your keyboard.

   A suggestion menu appears with a list of commands you can use. If the menu does not appear, try pressing the Space bar.
3. Select one of the available commands or type a question, and send the message.

   Alternatively, enter the command text as natural language, and send the message.

The Qlik chatbot responds with its response to your command. Depending on your request, additional interactions with the chatbot's response might be needed to generate insights and charts.

Suggestions menu in Microsoft Teams chat showing available commands for use in personal chat with the chatbot

![Message bar in personal Microsoft Teams chat with the Qlik chatbot, showing how the interface prompts the user with the available commands.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SaaSMSTeams_commands_personal.png "Click to view full size")

### Using commands and asking questions in a group conversation or team channel

Do the following:

1. In Microsoft Teams, open a group conversation or channel.
2. In the message bar, start typing @Qlik. Select the Qlik chatbot from the available options.

   This tags the Qlik chatbot in the message.
3. Select one of the suggested commands or type a question, and send the message.

The Qlik chatbot responds with its response to your command. Depending on your request, additional interactions with the chatbot's response might be needed to generate insights and charts.

Information noteFor other users in the conversation to interact with the same Qlik Sense application, they must have permissions to the application and select the application in the chat by using the apps command.

Suggestions menu in Microsoft Teams chat showing available commands for use in group chat

![Message bar in group Microsoft Teams chat featuring the Qlik chatbot, showing how the interface prompts the user with the available commands.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SaaSMSTeams_commands_group.png "Click to view full size")

This image shows how the chatbot can be used in team channels.

Using the Qlik chatbot in team channels

![Example of how the Qlik Microsoft Teams bot can be used in a team channel for group interactions with data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SaaSMSTeams_team_channel2.png "Click to view full size")

### Listing applications

Use the apps command to list the applications you have access to in the Qlik Cloud tenant. After an application has been selected, questions and commands can be asked and entered about the application data.

If you would like to ask questions about a different application, enter the apps command again and select a different application. Alternatively, use the clear command to reset the application context. See [*Clearing the application*](#Clearing2).

### Listing dimensions

After you have selected a Qlik Sense application, use the dimensions command to see a list of available dimensions in the application.

Selecting a dimension generates insights and analyses which use that dimension, as well as other dimensions or measures you may have selected in previous interactions. For information about resetting the selected dimensions and measures in the chat, see [*Clearing dimensions and measures*](#Clearing).

### Listing measures

After you have selected a Qlik Sense application, use the measures command to see a list of available measures in the application.

Selecting a measure generates insights and analyses which use that measure, as well as other dimensions or measures that you may have selected in previous interactions. For information about resetting the selected dimensions and measures in the chat, see [*Clearing dimensions and measures*](#Clearing).

### Asking for assistance

The help and questions commands are available for requesting assistance with interacting with the chatbot and Qlik Sense application data.

#### The help command

The help command displays general information about interacting with Insight Advisor Chat.

#### The questions command

Qlik Sense application developers can add helpful sample questions to their applications, which are presented to users in Insight Advisor and Insight Advisor Chat. Use the questions command to list these questions in the chat.

For more information about adding example questions to an application, see [*Adding example questions to Insight Advisor*](../BusinessLogic/business-logic-vocabulary-questions.htm).

### Changing the language

The language used in a conversation with the chatbot is unique to each user in the chat. A group conversation can include multiple users interacting with the same chatbot in their respective languages.

The language command is available to help you adjust the language in which you interact with Insight Advisor Chat in Microsoft Teams.

The language that is initially used in the Microsoft Teams chat, or when you reset the language, is determined by the following hierarchy:

- By default, the language of your interactions with the Qlik chatbot will be the language configured for use in Microsoft Teams.
- If the language configured in Microsoft Teams is not a language supported by Qlik's Insight Advisor Chat, the language of the chat defaults to the language set in your Qlik Cloud personal settings.
- If neither the Microsoft Teams language nor the Qlik Cloud profile language are supported by Insight Advisor Chat, the chat defaults to English.

The following command variants are available:

- language: Lists available languages and their two-letter language codes.
- language <two-letter language code> (for example, language en for English): Sets the language to the specified value.
- language clear: resets the language.

The language clear command resets any customizations you have made to the language in the conversation with the chatbot. If you start a chat with the bot, then later switch your Microsoft Teams language, use the language clear command to make the chatbot adjust to the updated Microsoft Teams language.

For a list of available languages in Insight Advisor Chat, see [*Supported languages*](insights-chat.htm#Supporte).

### Logging out and revoking your access token

When you log into the Qlik Cloud tenant in a chatbot conversation, a token is applied, which is automatically refreshed for 30 days. After this 30-day period, you are logged out and require a new token.

Use the logout command to log out of the Qlik Cloud tenant in the chat. This command logs you out, but maintains your token in case you log in again within a short time interval.

In a circumstance where you will not need the chatbot service for more than 30 days, you can revoke your token so it is deleted before the 30-day mark. To do this, use the revoke token command.

### Clearing the application or entity context

The clear command has two variants:

- clear: clears the application selected as the subject of users' questions and commands.
- clear entity context: clears the dimensions and measures that have been selected in the conversation. The application context is kept.

#### Clearing the application

After a Qlik Sense application has been selected in a chat, requests made to Insight Advisor Chat are assumed to be about that particular application.

Use the clear command to reset the application that was previously selected for exploration through the chatbot.

#### Clearing dimensions and measures

Insight Advisor Chat automatically remembers dimensions, measures, and filters that have been selected and applied within interactions about a Qlik Sense application. For example, if you select a dimension called Region and a measure called Margin in the chat, then later select a different dimension called Product Type, Insight Advisor Chat could recommend analyses and insights combining both of these dimensions, as well as the measure.

Use the clear entity context command to clear the context of the application you are interacting with the chatbot about. This allows you to generate recommendations for a new combination of dimensions, measures, and filters.

## Additional data exploration options

You can further explore and analyze your data using several other interactive elements in responses by the Qlik chatbot.

### Info

The Info button shows details about how your request was interpreted by Insight Advisor Chat as it generated the selected analysis. Dimensions, measures, and filters on field values are highlighted to demonstrate how the request was parsed. The Qlik Sense application is also shown.

Info button on a response in Microsoft Teams

![Interactive response card in Microsoft Teams showing expanded 'Info' button and how it demonstrates the parsing of the user request.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SaaSMSTeams_response_info.png "Click to view full size")

### Explore this further

Clicking Explore this further on a recommendation opens Insight Advisor in the Qlik Sense application, where you can explore the data further.

Information noteIf the link is blocked by your browser's firewall or other security features, you will not be able to open the Qlik Sense application. You also need access to the Qlik Sense application.

Depending on the request and entities referenced in it, the original natural language question might populate in the search bar. If the recommendation is a chart, you can add it directly to a sheet in your Qlik Sense application.

### Suggested analysis

Click Suggested analysis on a response card to display other similar recommendations. Click a suggestion to view it in the chat.

Suggested analysis button on a response in Microsoft Teams

![Interactive response card in Microsoft Teams, showing how the 'Suggested analysis' option can generate new analysis recommendations for deeper data exploration](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SaaSMSTeams_suggested_analysis.png "Click to view full size")

## Insight Advisor Chat and business logic

A Qlik Sense application's logical model controls how users interact with Insight Advisor using conversational analytics. Activating a custom logical model can alter the visibility and names of fields when interacting with the application through Insight Advisor Chat and external collaboration platforms such as Microsoft Teams. For more information, see [*Building logical models for Insight Advisor with Business logic*](../BusinessLogic/business-logic-logical-models.htm).

## Permissions

Whether you are using Insight Advisor Chat from an activity center or through an external collaboration platform, your access is affected by administrator-assigned privileges (in the form of security roles and permissions) and space roles.

If your Qlik Cloud tenant is licensed for Qlik Answers and has turned on cross-region inference, Insight Advisor Chat will not be available. Use Qlik Answers with your application instead to explore your data and create sheets and visualizations.

### Administrator-assigned

Consider the following:

- To access Insight Advisor Chat within Qlik Cloud, a tenant administrator must assign you specific permissions. See:

  - [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm) (capacity-based subscriptions)
  - [*Default permissions and custom roles*](../Admin/permissions-scopes.htm) (user-based subscriptions)
  - [*Default permissions and custom roles*](../Admin/permissions-scopes-anonymous.htm) (Qlik Anonymous Access subscriptions)
- If you are accessing Insight Advisor Chat through an external collaboration platform, a tenant administrator needs to assign specific permissions to you. For more information, see [*Administration activity center requirements for Qlik Cloud administrators*](#MCAdmin).
- Administrator-assigned permissions—in particular, permissions for content download—can affect your access to Insight Advisor Chat. See:

  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes-capacity-model.htm#InApp) (capacity-based subscriptions)
  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes.htm#InApp) (user-based subscriptions)
  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes-anonymous.htm#InApp) (Qlik Anonymous Access subscriptions)

### Space roles

For applications in collaborative spaces, space roles further govern your access to Insight Advisor Chat. For more information, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)

## Limitations

The following limitations apply to using Insight Advisor Chat in Microsoft Teams:

- Qlik Cloud Government does not support conversational analytics with Insight Advisor Chat in Microsoft Teams.
- In the Qlik Cloud Analytics hub, tenant administrators can see and interact with any application in the Qlik Cloud tenant that has been made available for Insight Advisor Chat. However, in Microsoft Teams, Qlik Cloud tenant administrators can only see and interact with the Insight Advisor Chat-enabled applications to which they have access (via the space or application sharing).

For a full list of limitations which apply to Insight Advisor Chat, see [*Limitations*](insights-chat.htm#Limitati).

## Learn more

- [*Accessing Insight Advisor Chat through external collaboration platforms*](insight-advisor-chat-external.htm)
- [Chat with a bot in Microsoft Teams](https://support.microsoft.com/en-gb/office/chat-with-a-bot-in-microsoft-teams-9c7bab5e-b1a2-4e35-801a-80d076e26f3f)
- [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id)
- [Add an application to Microsoft Teams](https://support.microsoft.com/en-us/office/add-an-app-to-microsoft-teams-b2217706-f7ed-4e64-8e96-c413afd02f77)
- [*Exploring applications with conversational analytics*](insights-chat.htm)
- [*Availability of the Qlik chatbot app in Microsoft Teams*](../Admin/microsoft-365-tenant-apps.htm)
