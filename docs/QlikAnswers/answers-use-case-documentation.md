---
title: "Qlik Answers use case: Documentation assistant"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/answers-use-case-documentation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Qlik Answers use case: Documentation assistant

Qlik Answers knowledge assistants can be used for a variety of purposes within Qlik Cloud in an organization. This use case looks at how Qlik Answers can be used to provide a documentation assistant to Qlik Cloud users.

A documentation team in an organization has been tasked with providing an assistant that can draw on information from their product's helpsite.

The target audience is internal users, such as Support and Product Management, who need to quickly find information. These users need to be able to ask questions and get answers from helpsite content as well as get summaries of helpsite information

Additionally, the documentation team has identified this as an opportunity to get feedback from internal users on the documentation that can then be used to drive improvements.

To accomplish this, the documentation team decides to send a copy of their helpsite files to an Amazon S3 bucket whenever the helpsite is built. Using an Amazon S3 V2 connection in Qlik Cloud, the files can then be made available to a Qlik Answers assistant.

## User roles in this use case

For this project, the documentation team involves the following users:

- Documentation engineer: The documentation engineer outputs the documentation content to an Amazon S3 bucket for use in a knowledge base.
- Tenant administrator: The tenant administrator sets the user role permissions to allow the creation and consumption of the assistant and knowledge base.
- Assistant owner: The assistant owner creates, configures, and manages the assistant and knowledge base.
- Audit administrator: The audit administrator reviews the feedback from the assistant.
- Assistant users: The intended audience for the documentation assistant.

Information noteDepending on the organization and the distribution of responsibilities, some of these users can be the same user.

## Creating the documentation assistant

To create the documentation assistant, the team does the following:

- Prepare the helpsite to exporting to storage
- Prepare roles in Administration
- Prepare spaces in Qlik Cloud
- Create the documentation knowledge base
- Create the documentation assistant
- Test the assistant
- Share the assistant available with other users
- Review user feedback

Additionally, the Tenant administrator monitors usage for the documentation assistant and other assistants in the organization using the Answers Analyzer for Qlik Cloud application.

### Preparing the helpsite to export to storage - Documentation Engineer

The first step is setting up the helpsite to export content into online storage for use in the knowledge base.

The Documentation Engineer modifies the helpsite publishing workflow to export the helpite topics to an Amazon S3 bucket every time the helpsite is built and released. This ensures that the source files for the knowledge base will always be up-to-date.

### Preparing roles in Administration - Tenant administrator

In Administration, the Tenant administrator manages roles to allow:

- The Assistant owner to create assistants and knowledge bases

  The Assistant owner requires the following permissions:

  - Content types > Manage assistants: Allowed
  - Content types > Knowledge bases > Manage knowledge bases: Allowed
  - Content types > Knowledge bases > Index knowledge bases: Allowed
  - Content types > Knowledge bases > Search knowledge bases: Allowed
- The Assistant users to use the assistant.

  The Assistant users require the following permissions:

  - Content types > Knowledge bases > Search knowledge bases: Allowed
- The Audit administrator to view and review assistant feedback.

  The Audit administrator requires the following permissions:

  - Content types > Manage assistants: View assistants
  - Content types > Knowledge bases > Search knowledge bases: Allowed
  - Content types > Knowledge bases > Manage knowledge bases: Allowed

  Additionally, the Audit administrator requires the Audit Admin user role.

The Tenant Administrator has can either create custom roles, change the defaults for all roles, or use a combination of both.

### Preparing spaces in Qlik Cloud - Assistant owner

Next, spaces must be prepared for the assistant and knowledge bases. As a best practice for assistants shared with other users, the assistant and knowledge base will be kept in separate spaces. This provides more fine-grained access control to the knowledge base data and the assistant itself.

From Create, the Assistant owner creates the following spaces:

- Assistant Data, a managed space.

  The connection to the data will be added to this space.
- Assistants, a managed space.

  The documentation assistant will be added to this space.

When the assistant is ready, the Assistant users and Audit administrator will be added to the spaces.

### Creating the documentation knowledge base - Assistant owner

In the Assistant Data managed space, the Assistant owner can create their knowledge base. They create a knowledge base and a connection to the Amazon S3 bucket. They then use dynamic rules to get all files from the folders.

Do the following:

1. In the Analytics activity center, go to the Answer mini-home.
2. Click Create new > Knowledge base.
3. After Name, enter Documentation KB.
4. After Space, select Assistant Data.
5. With Open knowledge base selected, click Create.

   Now, you can create the connection.
6. Click Use connection.
7. Click Create connection and configure a connection to the Amazon S3 bucket using an Amazon S3 V2 connector.
8. Select the connection and click Next.
9. Select Dynamic rules.
10. Change the folder depth to cover the depth of the helpsite folder structure.

    In this use case, as the helpsite has a deep folder hierarchy, the Assistant owner selects 20.
11. Click Select.
12. Click Index all.
13. When the index is complete, click ![Source options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Set schedule.
14. Turn on Daily index schedule and set a start time and timezone.
15. Click Save.

### Creating the assistant - Assistant owner

The Assistant owner now creates the assistant in the Assistants managed space. They add the Documentation KB knowledge base and customize the assistant conversation starters and settings.

Do the following:

1. In the Analytics activity center, go to the Assistants mini-home.
2. Click Create new > Assistant.
3. After Name, enter Documentation Assistant.
4. After Space, select Assistants.
5. Click Create.
6. In Overview, click Add knowledge base.
7. Select Documentation KB and click Select.
8. In Conversation starters, add three to five conversation starters to help users understand the kinds of questions they can ask the assistant.
9. In Settings, customize the assistant's Avatar icon and Welcome message.
10. Optionally, customize the error messages for the assistant.

The assistant is now ready for testing.

### Testing the assistant

The Assistant owner tests the assistant to confirm that it provides the expected answers and subject matter coverage. They use questions to which they know the answer to validate the assistant's responses. The Assistant owner tracks incorrect or unhelpful responses and see if can resolve them with adjustments to the source material.

Once testing is complete, the assistant is ready to be shared with other users.

### Sharing the assistant with other users - Assistant owner

The Assistant owner now can share the documentation assistant with other users. They need to add the members of their tenant to their shared and managed spaces:

- In the Assistant Data managed space, as they want all tenant users to be able to ask question of the data, in Members, after Anyone at <name> tenant, select Can consume data.
- In the Assistants managed space, in Members, after Anyone at <name> tenant, select Can consume data and Has restricted view.

Once added to both spaces, users can ask the assistant questions and get responses using the helpsite content.

### Reviewing user feedback - Audit administrator

Once the documentation assistant is live, the Audit administrator can review feedback in the Review. The Audit administrator reviews feedback once a week and creates tasks for the documentation team.

- For positive feedback, the Audit administrator examines the responses and potentially creates tasks for the Documentation team to use the responses when creating FAQs or even to add to the documentation.
- For negative feedback, the Audit administrator triages it, reviewing the conversation, responses, and any included comments. Where there are actionable issues, the Audit administrator creates tasks for the Documentation team to investigate or resolve the issue.
- For unanswered questions, the Audit administrator examines the questions to see if they were within the scope of the assistant. If they are, the Audit administrator logs a task for the Assistant owner to investigate the sources in the knowledge base. There may be gaps in the source files.
- For questions not in scope of the assistant, the Audit administrator can assess if some of the assistant details, description, or sample questions can be adjusted to make the scope of the assistant clearer for the users.

The Audit administrator also exports the feedback as CSV files and adds them to an analytics app to track trends, such as which sources have the most positive and negative feedback.

### Managing Qlik Answers usage - Tenant administrator

The Tenant administrator tracks Qlik Answers usage across the tenant using the Qlik Cloud Answers Analyzer application, available through Qlik Automate. Qlik Cloud Answers Analyzer helps the Tenant administrator track Qlik Answers usage in Documentation Assistant and knowledge base, as well as with other assistants and knowledge bases in the organization.

For more information, see [*Monitoring Qlik Answers usage*](administering-qlik-answers.htm#Monitori).
