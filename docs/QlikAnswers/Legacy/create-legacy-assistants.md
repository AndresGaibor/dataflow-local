---
title: "Creating legacy assistants"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Legacy/create-legacy-assistants.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Qlik Answers legacy experience", "Working with legacy assistants"]
---

# Creating legacy assistants

Create your legacy assistants and add knowledge bases to them.

## Creating new legacy assistants

Do the following:

1. Go to the Create page of the Analytics[activity center](#glossary-0 "Glossary term") and select Assistant.

   You can also create assistants from Answer in Analytics or by clicking Create new > Assistant in Catalog.

   In a knowledge base, you can also click Create assistant.
2. After Name, enter a name for the legacy assistant.
3. Optionally, after Description, enter a description for the legacy assistant.
4. After Space, select the destination space.
5. Optionally, after Tag, enter any tags you want to apply to the knowledge base.
6. If you are using the agentic experience, select Legacy assistant.
7. Click Create.

## Managing legacy assistant knowledge bases

Manage legacy assistant knowledge bases in Overview.

In the Overview tab, you can add and remove knowledge bases. Legacy assistants can have a maximum of five knowledge bases. You can manually index knowledge bases from Overview. You can also open knowledge bases in a new tab.

### Adding knowledge bases to legacy assistants

Do the following:

1. In the Overview tab, click Add knowledge base.

   You can create a new knowledge base to add by clicking Create knowledge base.
2. Select the knowledge bases you want to add.
3. Click Select.

### Indexing knowledge bases from legacy assistants

Do the following:

- In the Overview tab, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the knowledge base you want to index and click Index all files.

### Removing knowledge bases from legacy assistants

Do the following:

1. In the Overview tab, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the knowledge base you want to delete and click Remove from assistant.
2. Click Remove.

## Adding conversation starters

Conversation starters help your assistant direct conversations, helping users get the most out of your legacy assistant.

Conversation starters are available at the start of the chat. Selecting a starter asks the legacy assistant that question. Conversation starters allow you to add a curated list of questions available to your legacy assistant's users. These questions help show your users what is possible with your legacy assistant.

You can add a maximum of five conversation starters to your legacy assistant.

Do the following:

1. In the Conversation starters tab, click Create conversation starter.
2. Under Question, enter a question and press Enter.

## Customizing legacy assistant settings

You can customize additional chat settings for your legacy assistant in Settings, including the avatar icon and error message text.

### Customizing legacy assistant details

Under Assistant details, you can change the following:

- Name: The legacy assistant name.
- Description: The legacy assistant description.
- Tags: Add or select tags to apply to the legacy assistant.

### Customizing legacy assistant chat settings

Under Chat settings, you can modify the following settings:

- Avatar icon: Add a custom avatar icon for the legacy assistant. Images must be PNG files and must be 1 MB or smaller.
- Welcome message: Add a welcome message to your chat.
- Error messages: Customize the error message text for the following errors:

  - Question outside bounds of knowledge: This error occurs when the knowledge base does not have enough information to answer a question.
  - Question included prompt injection: This error appears when a question or knowledge file contains language intended to insert additional instructions or rules into the prompt.
  - Question is too complex: This error occurs when a question consists of too many parts, which makes it difficult to identify a clear answer.
