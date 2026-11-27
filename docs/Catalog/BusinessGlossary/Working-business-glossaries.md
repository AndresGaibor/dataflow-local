---
title: "Working with business glossaries"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/BusinessGlossary/Working-business-glossaries.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data"]
---

# Working with business glossaries

A business glossary is a tool that helps you to standardize terms and definitions within your Qlik Cloud platform. A shared understanding of terminology is essential for data discovery and collaboration across departments. Business glossaries are a resource type in Qlik Cloud. They consist of logical categories populated with terms. The terms are described in clear language that everyone across an organization can refer to and understand.

A business glossary:

- Helps app designers find standardized definitions and related datasets
- Helps business analysts find and understand answers to business questions
- Instills confidence in linked datasets and apps by providing context and background
- Facilitates deeper communication and collaboration across lines of business

An organization may have multiple glossaries for various functional areas that support targeted lines of business. Qlik Cloud Catalog provides the additional benefit of being able to link business terms to datasets and apps for valuable metrics and [visualizations](#glossary-1 "Glossary term") providing deeper context and data-driven validation.

## Required permissions

Business glossaries requires one of the following permissions assigned by an administrator to your user role:

- Manage glossaries and approve terms:

  - Allowed
  - Read and collaborate on terms only
  - Manage only

If you cannot use business glossaries, contact your administrator.

## Business glossary structure and components

A business glossary has a Name , Description, and Terms that are organized into Categories. Additional details like abbreviations, relations to other terms, and links to supporting assets add value to each term entry.

Business glossaries are a resource type that display in Qlik Cloud

![Business glossary is a resource type in Qlik Cloud](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_BizGlossaryCatalog-rev.png "Click to view full size")

## Creating and editing business glossaries

A glossary owner, also known as the steward, has the permission Manage glossaries and approve terms set to Allowed in their user role in the Administration activity center. This user is responsible for ensuring that terms are accurate and the glossary meets the needs of its consumers. This permission role is required to create, update, and delete a glossary as well as edit or delete the term in the Verified state and change the term status to Verified.

Information note

The Allowed setting for Manage glossaries and approve terms is the equivalent of the Steward global role that previously was used to administer business glossaries. The Steward role is still supported, but will eventually be replaced by the user role permissions.

Users that have the permission Manage glossaries and approve terms set to Manage only or Read and collaborate on terms only in their user role can interact with business glossaries, depending on their space permissions. Users that have Can view access to the space can view the Terms in the glossary. Users that have Can manage and Can edit [permissions](#glossary-2 "Glossary term") in the space can add and edit unapproved terms. The business glossary owner receives [notifications](#glossary-3 "Glossary term") that terms have been added and term Stewards receive notifications when terms have been changed. The glossary owner approves edits to terms and categories by changing status to Verified.

A user with any one of the following permissions: Owner, Can manage, Can edit data in applications, or Can edit can create, edit, delete categories.

For detailed information on access permissions for business glossaries, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../../Spaces/managing-managed-spaces.htm).

If the source for a glossary is maintained and updated externally, the Qlik Cloud glossary should be placed in a space where users, except for the steward, only have Can view permissions. When there are updates made to the external glossary, the steward imports it using Import and update glossary to update terms, categories, and metadata. Stewards can set up the import to delete terms removed from the source and that should no longer exist in the glossary. Other users can associate the glossary terms to master items in apps to provide explanations of terminology.

Tip noteYou can use business glossaries in data products to make the terms available more widely when the data product is activated. For more information, see [*Adding business glossaries to a data product*](../../DataIntegration/DataProducts/Adding-business-glossaries.htm).

## Glossary actions by user role permission

Your user role's setting for the permission Manage glossaries and approve terms determines what actions you can take with business glossaries.

Glossary actions by Manage glossaries and approve terms permission setting

| Action | Allowed | Manage only | Read and collaborate on terms only |
| --- | --- | --- | --- |
| List glossaries in the space | Yes | Yes | Yes |
| Open a glossary (details page only) | Yes | Yes | Yes |
| View glossary and terms | Yes | Yes | Yes |
| Move glossary from this space | Yes | Yes | No |
| Move glossary to this space | Yes | Yes | No |
| Create a glossary | Yes | Yes | No |
| Edit glossary settings and page | Yes | Yes | No |
| Delete a glossary | Yes | Yes | No |
| Add a term in glossary | Yes | Yes | Yes |
| Edit term not in Verified state | Yes | Yes | Yes |
| Edit term in Verified state | Yes | No | No |
| Delete term not in Verified state | Yes | Yes | Yes |
| Delete term in Verified state | Yes | No | No |
| Change state of a term to/from Verified | Yes | No | No |
| Change state of a term between states other than Verified | Yes | Yes | Yes |
| Create, edit, delete categories | Yes | Yes | Yes |
| Link glossary terms to master items in apps | Yes | Yes | No |
| Can export glossaries and terms | Yes | Yes | No |

### Sharing business glossaries

You can share a business glossary by inviting a user, group, or everyone in your tenant to the space where it is stored.

Do the following:

1. In the catalog, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the item to be shared and select Share > Invite.
2. Search for users or groups by name or email address.
3. Select space permissions for the users or groups.
4. Or, select permissions for Anyone at <your tenant name> from the dropdown list.
5. Click Done.

The users receive access to the shared item and all other content in the space.

## Working with business glossaries in Qlik Answers

You can also work with business glossaries from the agentic Qlik Answers experience. In the Glossary context, you can create and maintain business glossaries from chat.

For more information, see [*Managing business glossaries with Qlik Answers*](../../QlikAnswers/glossary-agent.htm).

## Notifications

Business glossary users can subscribe to glossary notifications to be informed when a new glossary term is created, deleted, or updated. The owner of the glossary receives the notifications of added terms and the stewards of a term receive the notifications of changed terms.

Do the following:

1. Go to Settings>Notifications.
2. Expand options for notifications under Glossaries and select whether you would like to be notified in the event of term creation, deletion, and update by either browser notifications, push notifications in Qlik Sense Mobile, email, or daily email digest.

Information note

Web notifications are available for 90 days, after which they are deleted.

## Learn more

- [*Managing business glossaries with Qlik Answers*](../../QlikAnswers/glossary-agent.htm)
