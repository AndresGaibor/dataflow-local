---
title: "Managing public collections"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/public-collections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Managing public collections

By default, [collections](#glossary-0 "Glossary term") are private. Tenant admins, analytics admins, and other designated users can make collections public to share them with all other members of the tenant. Public collections are managed in the Insights and Analytics activity centers.

## Making collections public and private

Public collections do not change members' access to content in spaces. Members will only be able to see content in public collections to which they already have access.

Do the following:

1. Ensure you have the [*Required permissions*](#Required).
2. Go to the Insights or Analytics activity center.
3. To make a collection public, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the collection, select Make public, and click Make public.
4. To make a public collection private again, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), select Make private, and click Make private.

Information noteAn empty collection cannot be made public.

Tip noteYou can also set the visibility of a collection when creating it. Use the Visibility drop down menu and select Private or Public.

## Required permissions

To make collections public and private, you need to be one of the following:

- Tenant administrator
- Analytics administrator
- User or administrator with the Public collections admin permission set to Allowed. See [*The Public collections permission*](#Public).

### The Public collections permission

Tenant administrators configure the Public collections permission to control whether users can manage public collections.

For the Public collections permission, the following options are available:

- Allowed: Can set any collection in the tenant to public or private.

  With Allowed, users can update (rename) and delete public collections, and can add and remove content in public collections.
- Not allowed: Cannot set any collection in the tenant to public or private.

  With Not allowed, users cannot update (rename) or delete public collections, and cannot add or remove content in public collections.

By default, tenant and analytics administrators have the Public collections admin permission set to Allowed. This cannot be changed.

This permission is configured via a custom security role. To learn more about configuring custom security roles, see:

- [*Roles and permissions for users and administrators*](permissions-admins-users-capacity-model.htm) (capacity-based subscriptions)
- [*Roles and permissions for users and administrators*](permissions-admins-users.htm) (user-based subscriptions)
- [*Roles and permissions for users and administrators*](permissions-admins-users-anonymous.htm) (Qlik Anonymous Access subscriptions)

For information about the permissions available through default permissions and custom roles, see:

- [*Default permissions and custom roles*](permissions-scopes-capacity-model.htm) (Capacity-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes.htm) (User-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes-anonymous.htm) (Qlik Anonymous Access subscriptions)
