---
title: "Working with automations in Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/working-with-automations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Working with automations in Qlik Answers

Prepare automations for use with Qlik Answers assistants.

Assistants can run automations as actions. Automations can pull data from external systems or push information to external platforms. When you add an automation as an action to an assistant, the Qlik Answers can run the automation to help answer user questions or help them act on answers they have received.

Keep in mind the following best practices for using automations with Qlik Answers:

- Keep automations focused on single, well-defined tasks.
- Write clear names and descriptions to help Qlik Answers select the correct automation.
- Use output blocks to provide meaningful feedback to users.
- Test automations independently before adding them to assistants.
- Design for synchronous execution where results are returned immediately.
- Keep agent-supplied inputs at the beginning, and keep them independent of inputs computed by automation blocks.

For information on adding actions to assistants, see [*Managing assistant actions*](managing-actions.htm).

## Automation use cases in assistants

Automations in Qlik Answers assistants have two primary use cases in Qlik Answers:

- Pulling data from external systems.
- Pushing data to external systems.

### Pulling data from external systems

Use automations to retrieve information from external systems and bring it into the conversation. Examples include:

- Retrieving customer inquiries from databases.
- Fetching comments or issue details.
- Getting status updates from external services.

### Pushing data to external systems

Use automations to send information from the conversation to external platforms. Examples include:

- Sending email summaries with key insights.
- Posting messages to messaging platforms.
- Sharing structured or unstructured data with specific users.

## Preparing automations for Qlik Answers

When preparing automations for use with assistants, configure them to work effectively with AI-driven activation. The following elements are key for successfully adding automations to your Qlik Answers assistants:

- Clear names and descriptions
- Input blocks
- Output blocks
- Concurrent run limits

### Clear names and descriptions

The automation's name and description help Qlik Answers determine when to run the automation based on user requests. Qlik Answers users can also see the automation name and description.

When naming and describing automations:

- Use clear, descriptive names that indicate the automation's purpose.
- Write descriptions that help the agent understand what the automation does and when it should be used.
- Include keywords related to the automation's function in the description.

### Input blocks

Input blocks allow users to provide data to automations. Use input blocks to ask users for clarifications to use in blocks later in the workflow. The assistant uses conversational context to help narrow down inputs before running and requires confirmation before proceeding.

Input blocks are optional. Automations can run without requiring user input.

The following input types are supported:

- Single line
- Multiple line
- Dropdown

  Information noteDropdown inputs are limited to 10 options.
- Multi-select.

  Information noteMulti-select inputs are limited to 10 options.

Only the first input block is displayed in the assistant, though automations can have multiple input blocks.

### Output blocks

Output blocks are required for the assistant to receive and display automation results to the users. Without an output block, the assistant only confirms that the automation was triggered.

Always include an output block so the assistant can return text results back to users.

### Concurrent run limits

You must set higher concurrent run limits for automations used with assistants. Multiple users may trigger the same automation simultaneously, and higher limits help avoid concurrency issues.

### Automations availability

Ensure any automation you plan on adding to an assistant will be available to the assistant's users.

While you can add automations that are in a shared space where you have the Can edit permission or greater, or in your personal space, assistant users can only see and run automations they have permission to access. Make sure that the automations you add as actions are available to all your users.

If a user loses permission to an automation after it has been added to an assistant, the automation will not appear or run for that user.

## Limitations

Automations used as actions have the following limitations:

- Automations triggered from an assistant are synchronous. Execution of automation happens during the user conversation flow.

  If a user closes Qlik Answers while the agent is running the automation, the automation will either finish execution or will time out if no input is provided. Timeout is five minutes for each interaction.
- The per user conversation limit per automation run is 10.
- Supported input types are limited to:

  - Single line
  - Multiple line
  - Dropdown

    Information noteDropdown inputs are limited to 10 options.
  - Multi-select.

    Information noteMulti-select inputs are limited to 10 options.
- Only text can be shared from Qlik Answers. Chart images and visualizations are not supported.
- Only the first input block is displayed in the assistant.
- When multiple automations are invoked, they run one after another, not in parallel.
