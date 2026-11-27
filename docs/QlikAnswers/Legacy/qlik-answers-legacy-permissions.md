---
title: "Legacy Qlik Answers access and permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Legacy/qlik-answers-legacy-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Qlik Answers legacy experience", "Administering the legacy Qlik Answers experience"]
---

# Legacy Qlik Answers access and permissions

Access to the legacy Qlik Answers experience is controlled by your user role and space role permissions.

The legacy Qlik Answers experience has several points of access control. Access to Qlik Answers assistants and knowledge bases is controlled by user role permissions set in the Administration activity center. Access to individual assistants, knowledge bases, and the data sources used by the knowledge bases is controlled by space role permissions.

## User role permissions

User role permissions are set by administrators in the Administration activity center.
The following permissions are available:

- Manage assistants: Control what level of access users have with assistants. The following permissions are available:

  - View assistants: Users can view assistants and ask questions.
  - Allowed: Users can create, view, and manage assistants.
  - Not allowed: Users cannot access assistants.
- Manage knowledge bases: Control what level of access and interaction users have with knowledge bases. The following permissions are available:

  - View knowledge bases: Users can view knowledge bases.
  - Allowed: Users can create, view, manage, index, and search knowledge bases.
  - Not allowed: Users cannot access knowledge bases in Qlik Cloud.
- Index the contents of a knowledge base source: Control indexing rights with knowledge bases. The following permissions are available:

  - Allowed: Users can index knowledge bases and create a reindexing schedule.
  - Not allowed: Users cannot index knowledge bases.
- Search knowledge bases: Control search access to knowledge bases. Search allows users access to knowledge base contents when asking Qlik Answers questions. The following permissions are available:

  - Allowed: Users can search knowledge bases when asking questions of Qlik Answers assistants.
  - Not allowed: Users cannot search knowledge bases.

Additionally, to review conversations and view feedback in assistants, users require the audit admin user role.

Tip note

The minimum level of access for a consumer of assistants is:

- Managed assistants: View assistants
- Search knowledge bases: Allowed

## Spaces permissions and the legacy Qlik Answers experience

Your user permissions give you access to Qlik Answers, but your space roles control what you can do with Qlik Answers in different spaces. What space permissions you require depends on whether you are creating assistants or using Qlik Answers to answer your questions.

To use Qlik Answers assistants to answer questions, users need space access in:

- The space the assistant is in.

  - The minimum space roles in a shared space is Can view and Can consume data.
  - The minimum space role in a managed space is Has restricted view and Can consume data.
- The space the knowledge base is in.

  - The minimum space role in a shared space is Can consume data.
  - The minimum space role in a managed space is Has restricted view and Can consume data.
- The space the data sources are in.

  - The minimum space role in a shared space is Can consume data.
  - The minimum space role in a managed space is Can consume data.

Space permissions allow you to control which data sources are available to a user from a single assistant that uses knowledge bases and data sources in different spaces.

For example, an assistant in Managed space A has access to knowledge bases in Managed space B and Managed space C.

- User 1 has Has restricted view and Can consume data in Managed space A, Can consume data in Managed space B, and no access to Managed space C.
- User 2 has Has restricted view and Can consume data in Managed space A, no access to Managed space B, and Can consume data in Managed space C.

When User 1 asks a question, the assistant answers using data from Managed space B.

When User 2 asks the same question, the assistant answers using data from Managed space C.

### Shared space roles and legacy Qlik Answers experience permissions

Qlik Answers assistant actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chat with an assistant | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Create new assistants | Yes | Yes | Yes | Yes | No | No | No |
| Move assistants to the space | Yes | Yes | Yes | Yes | No | No | No |
| Move assistants to another space | Yes | Yes | Yes | Yes | No | No | No |
| Open an assistant | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Delete an assistant | Yes | Yes | Yes | Yes | No | No | No |
| Edit an assistant | Yes | Yes | Yes | Yes | No | No | No |
| View assistant knowledge bases | Yes | Yes | Yes | Yes | No | No | Yes |
| Add and remove knowledge bases | Yes | Yes | Yes | Yes | No | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | Yes | Yes | No | No | Yes |

Qlik Answers knowledge base actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Create knowledge bases | Yes | Yes | Yes | Yes | Yes | No | No |
| Move knowledge bases to the space | Yes | Yes | Yes | Yes | No | No | No |
| Move knowledge bases to another space | Yes | Yes | Yes | Yes | No | No | No |
| Open a knowledge base | Yes | Yes | Yes | Yes | No | No | Yes |
| Delete a knowledge base | Yes | Yes | Yes | Yes | No | No | No |
| Edit a knowledge base | Yes | Yes | Yes | Yes | No | No | No |
| Index sources | Yes | Yes | Yes | Yes | No | No | No |
| Set up an index schedule | Yes | Yes | Yes | Yes | No | No | No |
| Get answers from knowledge bases using an assistant | Yes | Yes | Yes | Yes | No | No | Yes |
| View sources from knowledge base | Yes | Yes | Yes | Yes | No | No | Yes |

Qlik Answers assistant actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Chat with an assistant  Can view also requires Can consume data to chat | Yes | Yes | Yes | Yes | Yes | No |
| Create new assistants | Yes | Yes | Yes | Yes | No | No |
| Move assistants to the space | Yes | Yes | Yes | Yes | No | No |
| Move assistants to another space | Yes | Yes | Yes | Yes | No | No |
| Open an assistant | Yes | Yes | Yes | Yes | Yes | No |
| Delete an assistant | Yes | Yes | Yes | Yes | No | No |
| Edit an assistant | Yes | Yes | Yes | Yes | No | No |
| Add and remove knowledge bases | Yes | Yes | Yes | Yes | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | Yes | Yes | No | No |

Qlik Answers knowledge base actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create knowledge bases | Yes | Yes | Yes | Yes | No | No |
| Move knowledge bases to the space | Yes | Yes | Yes | Yes | No | No |
| Move knowledge bases to another space | Yes | Yes | Yes | Yes | No | No |
| Open a knowledge base | Yes | Yes | Yes | Yes | Yes | No |
| Delete a knowledge base | Yes | Yes | Yes | Yes | No | No |
| Edit a knowledge base | Yes | Yes | Yes | Yes | No | No |
| Index sources | Yes | Yes | Yes | Yes | No | No |
| Set up an index schedule | Yes | Yes | Yes | Yes | No | No |
| Get answers from knowledge bases using an assistant | Yes | Yes | Yes | Yes | Yes | No |
| View sources from knowledge base | Yes | Yes | Yes | Yes | Yes | No |

Tenant and analytics administrator Qlik Answers assistant actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Chat with an assistant | Yes |
| Create new assistants | No |
| Move assistants to the space | No |
| Move assistants to another space | No |
| Open an assistant | Yes |
| Delete an assistant | Yes |
| Edit an assistant | No |
| Add and remove knowledge bases | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes |

Tenant and analytics administrator Qlik Answers knowledge base actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create knowledge bases | No |
| Move knowledge bases to the space | No |
| Move knowledge bases to another space | No |
| Open a knowledge base | Yes |
| Delete a knowledge base | Yes |
| Edit a knowledge base | No |
| Index sources | No |
| Set up an index schedule | No |
| Get answers from knowledge bases using an assistant | Yes |

### Managed space roles and legacy Qlik Answers experience permissions

Qlik Answers assistant actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chat with an assistant  Can contribute, Can view, and Has restrictive view also require Can consume data to chat with assistants. | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Create new assistants | Yes | Yes | No | Yes | No | No | No | No |
| Move assistants to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move assistants to another space | Yes | Yes | No | Yes | No | No | No | No |
| Open an assistant | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Delete an assistant | Yes | Yes | No | Yes | No | No | No | No |
| Edit an assistant | Yes | Yes | No | Yes | No | No | No | No |
| View assistant knowledge bases | Yes | Yes | No | Yes | Yes | No | No | No |
| Add and remove knowledge bases | Yes | Yes | No | Yes | No | No | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | No | Yes | Yes | No | No | No |

Qlik Answers knowledge base actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create knowledge bases | Yes | Yes | No | Yes | No | No | No | No |
| Move knowledge bases to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move knowledge bases to another space | Yes | No | No | Yes | No | No | No | No |
| Open a knowledge base | Yes | Yes | No | Yes | Yes | No | No | No |
| Delete a knowledge base | Yes | Yes | No | Yes | No | No | No | No |
| Edit a knowledge base | Yes | Yes | No | Yes | No | No | No | No |
| Index sources  Can contribute requires Can consume data in the space with the data. | Yes | Yes | No | Yes | No | No | No | Yes |
| Set up an index schedule | Yes | Yes | No | Yes | No | No | No | Yes |
| Get answers from knowledge bases using an assistant | Yes | Yes | No | Yes | Yes | Yes | Yes | No |
| View sources from knowledge base | Yes | Yes | No | Yes | Yes | Yes | Yes | No |

Qlik Answers assistant actions by space role in a managed space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chat with an assistant | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Create new assistants | Yes | Yes | No | Yes | No | No | No | No |
| Move assistants to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move assistants to another space | Yes | Yes | No | Yes | No | No | No | No |
| Open an assistant | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Delete an assistant | Yes | Yes | No | Yes | No | No | No | No |
| Edit an assistant | Yes | Yes | No | Yes | No | No | No | No |
| Add and remove knowledge bases | Yes | Yes | No | Yes | No | No | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | No | Yes | Yes | No | No | No |

Qlik Answers knowledge base actions by space role in a managed space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create knowledge bases | Yes | Yes | No | Yes | No | No | No | No |
| Move knowledge bases to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move knowledge bases to another space | Yes | No | No | Yes | No | No | No | No |
| Open a knowledge base | Yes | Yes | No | Yes | Yes | No | No | No |
| Delete a knowledge base | Yes | Yes | No | Yes | No | No | No | No |
| Edit a knowledge base | Yes | Yes | No | Yes | No | No | No | No |
| Index sources  Can contribute requires Can consume data in the space with the data. | Yes | Yes | No | Yes | No | No | No | Yes |
| Set up an index schedule | Yes | Yes | No | Yes | No | No | No | Yes |
| Get answers from knowledge bases using an assistant | Yes | Yes | No | Yes | Yes | Yes | Yes | No |
| View sources from knowledge base | Yes | Yes | No | Yes | Yes | Yes | Yes | No |

Tenant and analytics administrator assistant actions in a managed space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Chat with an assistant | Yes |
| Create new assistants | No |
| Move assistants to the space | Yes |
| Move assistants to another space | Yes |
| Open an assistant | Yes |
| Delete an assistant | Yes |
| Edit an assistant | No |
| Add and remove knowledge bases | No |
| Review answers and feedback  Information noteThis requires the Audit Admin user role. | Yes |

Tenant and analytics administrator knowledge base actions in a managed space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create knowledge bases | No |
| Move knowledge bases to the space | Yes |
| Move knowledge bases to another space | Yes |
| Open a knowledge base | Yes |
| Delete a knowledge base | Yes |
| Edit a knowledge base | No |
| Index sources | No |
| Set up an index schedule | No |
| Get answers from knowledge bases using an assistant | Yes |
