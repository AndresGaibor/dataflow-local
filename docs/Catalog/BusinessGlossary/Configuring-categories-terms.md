---
title: "Creating terms and categories"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/BusinessGlossary/Configuring-categories-terms.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with business glossaries"]
---

# Creating terms and categories

Terms are the building blocks that make up the collection of business concepts, words, or phrases in a business glossary. Categories organize the terms. Anyone with access to edit in a space can contribute to terms in a business glossary. The Steward assigned to the glossary must approve edits made by other users for the changes to be saved as Verified.

Terms are organized into logical classifications called Categories. A term can be part of one or more categories and terms can be linked to one another. Glossary terms that are related to one another can be linked together with specific term relationships. Term relationships such as: is a, synonym of, or defined by specify how glossary terms are related. Fine-tuning these relational mappings can add meaning and context to your business glossary.

## Configuring categories

Categories are folder directories arranged logically to reflect how a user may search for information in a business glossary. Categories are the key to organizing and classifying your content in valuable ways. If categories make sense to users searching for a term, this will encourage use and collaboration across various areas of your organization.

When building category hierarchies, a practical approach is to breakdown larger concepts into smaller ones. For example, an organization could be broken down into lines of business or departments. Those departments can contain parallel sub-categories. An organization may have categories for the departments: Sales, Accounts Receivable, and Marketing and all of those categories can have its own sub-category: Customer. By creating a link to a Related term: Customer in another sub-category you can create hierarchical associations. Related terms can have the same name and different content or they can have identical content.

Categories enforce a strict hierarchy—A category with a different parent can have the same name; allowing for example, a different Customer category to exist in IT and Sales. Categories with the same parent cannot have the same name; for example, the category IT can only have one Customer sub-category.

## Creating a category

Do the following:

1. In the Terms tab Hierarchy view, select Create>Category.
2. Create new category modal displays. Enter values for the following fields:

- Name: Category name
- Description: Summary of the category.

  The description can cover how the collection of terms within this category is logical. For example, if the category is Customer, the description can indicate how the terms in this category support roles servicing customer through contracts, protocols, processes, etc.
- Category Stewards: List of individuals responsible for this category.

  This field is informational only; individuals selected and saved to this field and are not given any permissions or additional privileges. For more information on roles and permissions for business glossaries, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../../Spaces/managing-managed-spaces.htm).
- Parent category: Category that will be the parent of this nested category. These relations between categories help to build the mapping and structure of the business glossary.

## Creating and configuring terms

Each glossary term has a name—the concept it describes, and a short description that explains the concept at a high level. The Description should distinguish it from other terms and the Definition should provide meaningful details that are understandable to business and technical groups.

Do the following:

1. In the Terms tab Hierarchy view, select Create>Term.
2. Create new term modal displays. Enter values for the following fields:

- Name: Term name. Name must be set before adding other fields.
- Abbreviation: Industry or organizational abbreviation that the term is also known by. Terms are searchable by their abbreviations in Content search.
- Status: Approval state of the term. The Glossary Steward is responsible for moving the Term from Draft to Verified and the term status can also be changed to Deprecated. A deprecated term will remain in the glossary where it can also be deleted.
- Definition: The definition field is intended to be a short, concise definition of the term in business language that users understand.
- Related information: This is a rich-text field that allows for more information related to the term. Everything that is not part of the definition goes here for example: links to external information, how this definition was created, help about usage of the term, etc. Attributes can serve as suggested guidelines and are created in the Term template tab. For more information, see [*Setting up business glossaries*](Setting-up-business-glossaries.htm#Term).
- Linked resources: Glossary terms can be linked to applications, datasets, and master items that are available to the user in the current Qlik Cloud environment. The term editor selects these resources to link the term to related supporting content.

  Information noteMaster items are linked to glossary terms from inside applications. For more information, see [*Linking terms to master items*](business-glossaries-master-items.htm).
- Related terms: Glossary terms that are related to one another can be linked together with term relationships. The nature of the relationship between terms is specified by setting how the term relates to the linked term. These include: See also, Synonym, Replaced by and Replaces, Is a and Has subtype, Preferred term and See instead, and Defined by and Defines.
- Term Stewards: List of individuals responsible for this term.

  This field is informational only; individuals selected and saved to this field and are not given any permissions or additional privileges. For more information on roles and permissions for business glossaries, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../../Spaces/managing-managed-spaces.htm).
- Categories: Select one or more categories under which this term will be included.
- Tags: Apply metatags to define and organize this term. Tags that have been applied display (example: tag1, tier3, upgrade, etc.) Terms can be found by and narrowed down by the Tags filter in Content search.

Related learning:

- [Managing a business glossary in Qlik Cloud](/lnk/Managing_business_glossary_Cloud)
