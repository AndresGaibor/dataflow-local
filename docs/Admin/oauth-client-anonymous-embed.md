---
title: "Creating an OAuth client for anonymous embeds of application content"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/oauth-client-anonymous-embed.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system", "Creating and managing OAuth clients"]
---

# Creating an OAuth client for anonymous embeds of application content

To embed application content for anonymous access using qlik-embed, you need to create an OAuth client with a type specifically designed for this use case.

Information note
This functionality is only available with a Qlik Anonymous Access subscription. For more information, see [*Qlik Anonymous Access subscriptions*](subscription-options-anonymous.htm).

Do the following:

1. In the Administration [activity center](#glossary-0 "Glossary term"), go to the OAuth section.
2. Click Create new.
3. In the Client type dropdown menu, select Anonymous embed.
4. Enter a Name and optionally a Description for the OAuth client.
5. Under Allowed origins, enter each origin that you need to authorize. These are the domains that will be accessing the Qlik Cloud tenant to retrieve the information for the embedded analytics.

   Click Add after inserting each URL.
6. When you are done, click Create.
7. Click Copy to clipboard to save the client ID for later use. It will be needed when the application content is embedded with qlik-embed.
8. Click Done.
