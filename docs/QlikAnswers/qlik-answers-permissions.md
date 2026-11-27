---
title: "Qlik Answers access and permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/qlik-answers-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Deploying and administering Qlik Answers"]
---

# Qlik Answers access and permissions

Access to Qlik Answers is controlled by your user role and space role permissions.

Qlik Answers has several points of access control. Access to Qlik Answers assistants and knowledge bases is controlled by user role permissions set in the Administration activity center. Access to individual assistants, knowledge bases, and the data sources used by the knowledge bases is controlled by space role permissions.

## User role permissions

User role permissions are set by administrators in the Administration activity center. Available user role permissions vary depending on whether or not the agentic Qlik Answers experience is enabled. For more information, see [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm).

### Agentic Qlik Answers permissions

Under Content types, there are the following permissions for Qlik Answers:

- Enable Qlik Answers for applications: Control whether users can activate Qlik Answers for applications and view AI readiness details and scores. The following permissions are available:

  - Allowed: Users can activate Qlik Answers for applications and view AI readiness details and scores.
  - Not allowed: Users cannot activate Qlik Answers for applications or view AI readiness details and scores.

  Information note

  Although Enable Qlik Answers for applications is allowed by default, we recommend that you set it to Not allowed in the default permissions and create a custom role with it set to Allowed. Assign the custom role to the specific users who should be able to activate Qlik Answers for applications and optimize applications for AI.
- Manage assistants: Control what level of access users have with assistants. The following permissions are available:

  - Allowed: Users can create and manage assistants.
  - Not allowed: Users cannot access assistants.
- Manage knowledge bases: Control what level of access and interaction users have with knowledge bases. The following permissions are available:

  - Allowed: Users can create, manage, index, and search knowledge bases.
  - Not allowed: Users cannot access knowledge bases in Qlik Cloud.
- Index knowledge bases: Control indexing rights with knowledge bases. The following permissions are available:

  - Allowed: Users can index knowledge bases and create a reindexing schedule.
  - Not allowed: Users cannot index knowledge bases.
- Search knowledge bases: Control search access to knowledge bases. Search allows users access to knowledge base contents when asking Qlik Answers questions. The following permissions are available:

  - Allowed: Users can search knowledge bases when asking questions of Qlik Answers assistants.
  - Not allowed: Users cannot search knowledge bases.
- Manage skills: Control what level of access users have with skills. The following permissions are available:

  - Allowed: Users can upload and manage skills.
  - Not allowed: Users cannot upload or manage skills.

Information note

To run actions added to Qlik Answers assistants, users also require Automations > Shared Automations set to Allowed.

Information note

To work with machine learning in Qlik Answers, users also need the corresponding Qlik Predict permissions. For more information, see [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

Under Features and actions, there are the following permissions for Qlik Answers under Agentic AI:

- Data analysis: Controls user access to Qlik Answers agentic chat from Answers. The following permissions are available:

  - Allowed: Users can use application analysis and Answers assistants within the Qlik Answers agentic chat from Answers.
  - Not allowed: Users cannot access application analysis or Answers assistants from the Qlik Answers agentic chat. If they have the permissions, they can use the experience with legacy assistants.
- Data governance: Controls user access to the data governance tools within Qlik Answers agentic chat from Answers. The following permissions are available:

  - Allowed: Users can interact with data governance in the Qlik Answers agentic chat.
  - Not allowed: Users cannot interact with data governance in the Qlik Answers agentic chat.
- Qlik product help: Controls user access to the Help agent in the Qlik Answers agentic chat.

  - Allowed: Users can access the Help agent.
  - Not allowed: Users cannot access the Help agent.
- Review agent and chat interactions: Allows user access to both Answers review portal and Feedback in agentic assistants to review Qlik Answers conversations. The following permissions are available:

  - Allowed: Users can access the review portal and Feedback in agentic assistants to view conversations from Qlik Answers agentic experiences.
  - Not allowed: Users cannot access the review portal or view Feedback in agentic assistants.

Information noteThe audit admin user role also allows users to review conversations and view feedback in both agentic and legacy assistants.

To use the Data quality context, users also need Agentic AI > Data analysis set to Allowed, and the tenant subscription must have data quality entitlement enabled.

## Spaces permissions and Qlik Answers

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

### Shared space roles and Qlik Answers permissions

Qlik Answers assistant actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| View assistants in Answers assistants | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Chat with an assistant | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Create new assistants | Yes | Yes | Yes | Yes | No | No | No |
| Move assistants to the space | Yes | Yes | Yes | Yes | No | No | No |
| Move assistants to another space | Yes | Yes | Yes | Yes | No | No | No |
| Open an assistant | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Delete an assistant | Yes | Yes | Yes | Yes | No | No | No |
| Edit an assistant | Yes | Yes | Yes | Yes | No | No | No |
| View assistant applications and knowledge bases | Yes | Yes | Yes | Yes | No | No | Yes |
| Add and remove applications and knowledge bases | Yes | Yes | Yes | Yes | No | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | Yes | Yes | Yes | No | Yes |

Qlik Answers knowledge base actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Create knowledge bases | Yes | Yes | Yes | Yes | No | No | No |
| Move knowledge bases to the space | Yes | Yes | Yes | Yes | No | No | No |
| Move knowledge bases to another space | Yes | Yes | Yes | Yes | No | No | No |
| Open a knowledge base | Yes | Yes | Yes | Yes | No | No | Yes |
| Delete a knowledge base | Yes | Yes | Yes | Yes | No | No | No |
| Edit a knowledge base | Yes | Yes | Yes | Yes | No | No | No |
| Index sources | Yes | Yes | Yes | Yes | No | No | No |
| Set up an index schedule | Yes | Yes | Yes | Yes | No | No | No |
| Get answers from knowledge bases using an assistant | Yes | Yes | Yes | Yes | No | No | Yes |
| View sources from knowledge base | Yes | Yes | Yes | Yes | No | No | Yes |

Qlik Answers skill actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Upload skill | Yes | Yes | Yes | Yes | No | No | No |
| Move skills to the space | Yes | Yes | Yes | Yes | No | No | No |
| Move skills to other spaces | Yes | Yes | Yes | Yes | No | No | No |
| Open skills | Yes | Yes | Yes | Yes | No | No | Yes |
| Delete skills | Yes | Yes | Yes | Yes | No | No | No |
| Edit skill details | Yes | Yes | Yes | Yes | No | No | No |

Qlik Answers application actions – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| View applications in Application analysis | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Open Answers in an open application | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Ask question about the application in Qlik Answers | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Make application available to Qlik Answers | Yes | Yes | Yes | Yes | No | No | No |

Qlik Answers assistant actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| View assistants in Answers assistants | Yes | Yes | Yes | Yes | Yes | No |
| Chat with an assistant  Can view also requires Can consume data to chat | Yes | Yes | Yes | Yes | Yes | No |
| Create new assistants | Yes | Yes | Yes | Yes | No | No |
| Move assistants to the space | Yes | Yes | Yes | Yes | No | No |
| Move assistants to another space | Yes | Yes | Yes | Yes | No | No |
| Open an assistant | Yes | Yes | Yes | Yes | Yes | No |
| Delete an assistant | Yes | Yes | Yes | Yes | No | No |
| Edit an assistant | Yes | Yes | Yes | Yes | No | No |
| View assistant applications and knowledge bases | Yes | Yes | Yes | Yes | No | No |
| Add and remove applications and knowledge bases | Yes | Yes | Yes | Yes | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | Yes | Yes | Yes | No |

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

Qlik Answers skill actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Upload skill | Yes | Yes | Yes | Yes | No | No |
| Move skills to the space | Yes | Yes | Yes | Yes | No | No |
| Move skills to other spaces | Yes | Yes | Yes | Yes | No | No |
| Open skills | Yes | Yes | Yes | Yes | Yes | No |
| Delete skills | Yes | Yes | Yes | Yes | No | No |
| Edit skill details | Yes | Yes | Yes | Yes | No | No |

Qlik Answers application actions – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| View applications in Application analysis | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Open Answers in an open application | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Ask question about the application in Qlik Answers | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Make application available to Qlik Answers | Yes | Yes | Yes | Yes | No | No | No |

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
| Add and remove applications and knowledge bases | No |
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

Tenant and analytics administrator Qlik Answers skill actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Upload skill | No |
| Move skills to the space | No |
| Move skills to other spaces | No |
| Open skills | Yes |
| Delete skills | Yes |
| Edit skill details | No |

### Managed space roles and Qlik Answers permissions

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

Qlik Answers skill actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Upload skill | Yes | Yes | No | Yes | No | No | No | No |
| Move skills to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move skills to other spaces | Yes | No | No | Yes | No | No | No | No |
| Open skills | Yes | Yes | No | Yes | Yes | No | No | No |
| Delete skills | Yes | Yes | No | Yes | No | No | No | No |
| Edit skill details | Yes | Yes | No | Yes | No | No | No | No |

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

Qlik Answers skill actions by space role in a managed space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Upload skill | Yes | Yes | No | Yes | No | No | No | No |
| Move skills to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move skills to other spaces | Yes | No | No | Yes | No | No | No | No |
| Open skills | Yes | Yes | No | Yes | Yes | No | No | No |
| Delete skills | Yes | Yes | No | Yes | No | No | No | No |
| Edit skill details | Yes | Yes | No | Yes | No | No | No | No |

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

Tenant and analytics administrator skill actions in a managed space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Upload skill | No |
| Move skills to the space | Yes |
| Move skills to other spaces | Yes |
| Open skills | Yes |
| Delete skills | Yes |
| Edit skill details | No |

## Tenant administrator access to applications with Qlik Answers

Tenant administrators can open any application in a tenant, including applications in user's personal spaces. If they lack other permissions, such as space or section access, they cannot view the application's contents.

When a tenant administrator opens an application and then asks a question in Qlik Answers, if they lack sufficient space or application-level permissions to view the data or content in the application, Qlik Answers will not return results.

Submitting questions does not automatically grant authorization to receive results. To generate responses, tenant administrators must be granted the required access the space (such as space permissions) or within the application (such as through Section Access).

If questions appear to run, but no answers are returned, review and update the application access permissions accordingly.
