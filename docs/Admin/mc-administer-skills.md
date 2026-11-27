---
title: "Managing skills for tenant and analytics administrators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-skills.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Managing skills for tenant and analytics administrators

If you are a tenant admin or analytics admin, you can change the owner of skills, move skills to another space, and delete skills.

Skills contain instructions that shape how Qlik Answers responds in applications and assistants. For more information, see [*Working with skills*](../QlikAnswers/Skills/working-with-skills.htm).

## Administrator access levels for managing skills

Tenant and analytics administrators have different levels of access to skills:

- Tenant administrators: Can manage all skills in [managed spaces](#glossary-0 "Glossary term"), shared spaces, and personal spaces.
- Analytics administrators: Can manage skills in managed and shared spaces. Cannot manage skills in other users' personal spaces.

Information noteSkill owners and users with the required space permissions can also manage skills from the catalog. For more information, see [*Managing skills*](../QlikAnswers/Skills/managing-skills.htm).

## Skills overview

To manage skills, go to the Content page in the Administration activity center and open the Skills tab. The tab displays a table with information about the owner of each skill and the space where it is located.

As a tenant admin or analytics admin, you can perform the following actions on skills:

- Change the owner of the skill
- Move the skill to another space
- Delete the skill

## Changing owner of skills

As a tenant or analytics admin, you can change the owner of a skill.

Do the following:

1. In the Administration activity center, go to Content > Skills.
2. Select one or more skills and click Change owner.
3. In the Change owner dialog, select the user you want as the new owner, and then click Apply.

## Changing space of skills

As a tenant or analytics admin, you can move a skill to another space.

Do the following:

1. In the Administration activity center, go to Content > Skills.
2. Select one or more skills and click Move.
3. In the Move dialog, select the space where you want to move the skills, and then click Confirm.

   Information note

   When changing the space of a skill, you might need higher permissions. If required, select the Get elevated privileges checkbox before confirming.

   Elevated privileges are required if you are not the owner of the skill, or do not have Can manage permission for either the current or new space. These privileges are temporary and are reverted after the space change is complete.

## Deleting skills

As a tenant or analytics admin, you can delete skills.

Do the following:

1. In the Administration activity center, go to Content > Skills.
2. Select one or more skills and click Delete.
3. In the Delete skills dialog, select the checkbox to confirm the deletion, and then click Delete.
