---
title: "Creating an API with AI Assistant"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/CreatingANewApiWithAiAssistant.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API design"]
---

# Creating an API with AI Assistant

You can create an API by interacting with an AI model using natural language.
This option might help you to create the required API more rapidly.

Information noteNote: For help on how to create a new empty API or work with an API example, see [Working with a new API](WorkingWithNewApi.htm).

- A Talend tenant user must create a secure connection with Qlik Cloud by following the procedure in [Configuring Qlik Cloud Authentication](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/configuring-qlik-cloud-authentication).
- At least one user account must be assigned to a role that has the API
  Designer - Administrate permission enabled. This setting is
  "tenant-wide", which means other tenant users with the API
  Designer role will then also have access to the feature. For
  further information about user accounts, roles, and permissions, see [*Administering Qlik Cloud*](../../Introduction/administer-deployment.htm).

1. On the API Contracts homepage, click New API.
2. Select New API and click AI
   Assistant.

   ![AI Assistant dialog box.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/create_api_ai_assistant.png)

   Information noteNote: If the AI Assistant icon is not visible, a user
   with the API Contracts - Administrate permission must
   enable the Generative AI-based features setting. They
   do this by clicking their user name in the top right corner of the API Contracts homepage, clicking API Contracts settings, and then
   selecting the Generative AI-based features check
   box.
3. In the Describe the API you want to generate field, use
   natural language to describe the API you want to create, then click
   Generate.

   The generated API is displayed in the Preview
   panel.
4. Repeat the previous step to refine your description, if required.

   If you make multiple iterations, you can step backwards and forwards through
   each iteration by clicking the < and
   > buttons above the description field. You can do
   this only during the current session.
5. When the generated API satisfies your requirements, click
   Save below the Preview panel.

The generated API is saved and is added to the list of APIs on the API Contracts
homepage.
