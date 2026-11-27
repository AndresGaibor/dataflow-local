---
title: "Creating assistants"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Assistants/create-assistants.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with assistants"]
---

# Creating assistants

Create your assistants and add content, such as applications and knowledge bases, as data sources.

## Creating new assistants

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-0 "Glossary term") and select Assistant.

   You can also create assistants from Answer in Analytics or by clicking Create new > Assistant in Catalog.

   In a knowledge base, you can also click Create assistant.
2. After Name, enter a name for the assistant.
3. Optionally, after Description, enter a description for the assistant.
4. After Space, select the destination space.
5. Optionally, after Tag, enter any tags you want to apply to the knowledge base.
6. Click Create.

## Managing content

In the Content tab, you can add and remove structured and unstructured data sources for your assistant to use to answer questions.

### Managing applications

Each assistant can have a maximum of five applications added as data sources. The assistant can use the structured data within the applications to answer questions. Users with the appropriate permissions can also generate sheets for the applications.

Before being added to an assistant, an application must first be made available to Qlik Answers and finished indexing. For more information, see [*Making applications available for Qlik Answers*](../Applications/working-with-apps-in-qlik-answers.htm#Making).

#### Adding applications

Do the following:

1. In the Content tab, click Add content > Add application.
2. Select an application and click Add.

#### Reloading applications

Do the following:

- Click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Reload application.

### Managing knowledge bases

Assistants can have a maximum of five knowledge bases. You can manually index knowledge bases from Overview. You can also open knowledge bases in a new tab.

#### Adding knowledge bases to assistants

Do the following:

1. In the Content tab, click Add content > Add knowledge base.
2. Select the knowledge bases to add.
3. Click Select.

#### Indexing knowledge bases from assistants

Do the following:

- In the Content tab, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the knowledge base you want to index and then click Index all files.

#### Removing knowledge bases from assistants

Do the following:

1. In the Content tab, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the knowledge base you want to delete and then click Remove.
2. Click Remove.

## Managing skills

In the Skills tab, you can add and remove skills for your assistant. Skills teach Qlik Answers how to handle specific topics and tasks, drawing on that knowledge automatically when relevant. You can add a maximum of five skills to an assistant. You can only add or remove skills that are in a space you have access to.

For more information, see [*Adding skills to applications and assistants*](../Skills/adding-skills.htm).

## Adding conversation starters

Conversation starters help users understand what they can ask Qlik Answers, enabling them to get the most out of your assistant.

Conversation starters are available at the start of the chat. Selecting a starter asks the assistant that question. Conversation starters allow you to add a curated list of questions available to your assistant's users. These questions help show your users what is possible with your assistant.

You can add a maximum of five conversation starters to your assistant.

Do the following:

1. In the Conversation starters tab, click Create conversation starter.
2. Under Question, enter a question and press Enter.

## Customizing assistant settings

You can customize additional chat settings for your assistant in Settings, including the avatar icon and error message text.

### Customizing assistant details

Under Assistant details, you can change the following:

- Name: The assistant name.
- Description: The assistant description.
- Tags: Add or select tags to apply to the assistant.

### Customizing chat settings

Under Chat settings, you can modify the following settings:

- Avatar icon: Add a custom avatar icon for the assistant. Images must be PNG files and 1 MB or smaller.
- Welcome message: Add a welcome message to your chat.
- Error messages: Customize the error message text for the following errors:

  - Question included prompt injection: This error appears when a question or knowledge file contains language intended to insert additional instructions or rules into the prompt.
