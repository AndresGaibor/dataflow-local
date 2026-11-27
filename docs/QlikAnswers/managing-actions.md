---
title: "Managing assistant actions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/managing-actions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with assistants"]
---

# Managing assistant actions

Actions allow your assistants to run automations.

Each assistant can have up to five automations available as actions. You can add:

- Automations in shared spaces in which you have a Can edit or greater space permission.
- Automations in your personal space.

For information about preparing automations for use with Qlik Answers, see [*Working with automations in Qlik Answers*](working-with-automations.htm)

## User access to actions

Automations are filtered based on user permissions. Users only see and can run automations to which they have access. Users must have the following permission in their user role to use shared automations:

- Automations > Shared Automations: Allowed.

Users must also have Can edit or greater space permission in the shared space containing the automation to run the automation.

## Adding actions

Actions can be configured to require user confirmation at the start or run automatically. Requiring user confirmation provides the users with the automation name and description. This is helpful if there is potential overlap between automations. Running automations automatically is useful when automations have clear purposes for users and there are not overlaps between automations in the assistant.

Do the following:

1. In the Actions tab of an assistant, click Add action > Add automation.

   If you want to create a new automation and add it, click Add action > Create automation.
2. Select an automation and click Next.
3. Optionally, decide if you want users to confirm they want to run the automation.

   Ask users to confirm before running an automation is turned on by default.

   Information noteWhen this confirmation is disabled and the automation does not require user input, the automation runs without input. If the automation requires an input, it will ask for user input when required.
4. Click Add.

## Editing actions

Do the following:

- Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit action.

## Removing actions from assistants

Do the following:

1. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Remove.
2. Click Remove.

## Limitations

Actions have the following limitations:

- Only the first input block in an automation is displayed in Actions. Automations can have multiple input blocks and all inputs are visible based on the automation workflow.
- Automations run sequentially, not in parallel. If multiple automations are needed for a question, they run one after another.
- Automations must complete within 5 minutes. If an automation takes longer, it continues running in the background, but the assistant will not receive the output.
- Automations can only return text content. Charts and images are not supported.
- Users cannot ask new questions in the same conversation thread while an automation is waiting for confirmation.
- If a user loses permission to an automation after it has been added to the assistant, the automation will not appear or run for that user.
- Automations are not supported for users in fast mode.
