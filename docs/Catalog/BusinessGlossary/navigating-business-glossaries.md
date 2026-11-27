---
title: "Navigating business glossaries"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/BusinessGlossary/navigating-business-glossaries.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with business glossaries"]
---

# Navigating business glossaries

Business glossaries have the following areas of interaction:

- Terms: View and create the terms and categories of the glossary.
- Glossary overview: View and create an overview for the glossary.
- Glossary details: View additional details about the glossary, edit templates, and export the glossary.

## Terms

Terms contains the terms and categories in the glossary. Terms are the building blocks that make up the collection of business concepts, words, or phrases in a business glossary. Anyone with access to edit in a space can contribute to terms in a business glossary. The Steward assigned to the glossary must approve edits made by other users for the changes to be saved as Verified. Glossary terms that are related to one another can be linked together with specific term relationships. Term relationships such as: is a, synonym of, or defined by specify how glossary terms are related. Fine-tuning these relational mappings can add meaning and context to your business glossary.

Terms are organized into logical classifications called categories. Categories are folder directories arranged logically to reflect how a user may search for information in a business glossary. Categories are the key to organizing and classifying your content in valuable ways. If categories make sense to users searching for a term, this will encourage use and collaboration across various areas of your organization. A term can be part of one or more categories.

The Terms tab provides three views: ![Select tile icon for tile view](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_profile_tile.svg)Tile view, ![Select list icon for list view](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_profile_list.svg)List view, and ![Select list icon for hierarchy view](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/drill_down.svg)Hierarchy view.

Tile and list views detail Terms in the business glossary. The mapping and organization of your business glossary is designed in the Hierarchy view. For more information on developing business glossaries, see [*Creating terms and categories*](Configuring-categories-terms.htm).

Terms in tile view

![Glossary showing terms in the tile view](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_businessGlossaryTermsTile-rev.png "Click to view full size")

Hierarchy view of Terms

![Category view of Terms](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_glossary_categoryview-rev.png "Click to view full size")

All views provide filters by which to narrow search on term names and content including descriptions and abbreviations. Content search can also be limited by entering search text with the following filters: Categories, Status, Stewards (glossary), Tags, or All filters.

### Viewing terms

If you click on a term, you can view the term in full.

Full term

![Glossary showing the full entry for a single term.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_glossary-entry-rev.png "Click to view full size")

Terms have the following fields of information:

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

### Linked data products

When viewing a business glossary, the Linked data products tab displays all data products that have been linked to this term. This allows you to quickly see which data products are associated with the business concept represented by the term.

Data products in this tab are displayed with their Qlik Trust Score™, which indicates the overall quality and reliability of the data product. The trust score is calculated as the average of the trust scores of all datasets within that data product. For more information on Qlik Trust Score™, see [*Qlik Trust Score™*](../../DataIntegration/DataProducts/Qlik-Trust-score.htm).

#### Accessing linked data products

You can click any data product in the list to navigate to the data product details page for more information, such as the datasets it contains and its overall documentation.

### Viewing categories

Categories enforce a strict hierarchy. A category with a different parent can have the same name; allowing for example, a different Customer category to exist in IT and Sales. Categories with the same parent cannot have the same name. For example, the category IT can only have one Customer sub-category.

Categories have the following fields available:

- Name: Category name
- Description: Summary of the category.

  The description can cover how the collection of terms within this category is logical. For example, if the category is Customer, the description can indicate how the terms in this category support roles servicing customer through contracts, protocols, processes, etc.
- Category Stewards: List of individuals responsible for this category.

  This field is informational only; individuals selected and saved to this field and are not given any permissions or additional privileges. For more information on roles and permissions for business glossaries, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../../Spaces/managing-managed-spaces.htm).
- Parent category: Category that will be the parent of this nested category. These relations between categories help to build the mapping and structure of the business glossary.

## Glossary overview

Glossary overview provides an area to provide information about the glossary, such as the objectives of the glossary, key ways of working for developing the glossary, and contacts who can help contributors with their work on the glossary, such as the users given the Steward role.

The glossary overview tab is a rich text editor that allows for hyperlinks and ample space to provide relevant content that facilitates use and engagement of your business glossary. Add any sections that make sense for the business glossary you are creating. Common sections used in the overview include:

- An overview that describes the objectives of the glossary. This section can describe the use cases or issues the glossary is intended to solve. For example: The key purpose of this glossary is to provide a common framework for employees across the sales, marketing, IT , and technical support departments. The terms within this glossary are organized into categories that are related to one another so that various roles across functional departments can better understand the context and meaning of the terms as understood and used in the fulfillment and support of sales orders.
- Ways of working. Describe the roles of contributing individuals and teams responsible for content. You can provide links to supporting organizational resources like contract templates, SLAs, warranties, corporate policies, instructional courses, mission statements, org charts, etc.
- Primary contact(s) that users can email or message for help, questions, and suggestions. At minimum this section should include the glossary Steward contact. Contact information for individuals responsible for specific categories and terms can be helpful.

Glossary overview

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_glossary-overview-rev.png "Click to view full size")

## Glossary details

Glossary details provides:

- Details: Key information about the glossary in Qlik Cloud, such as space and tags.
- Term template: An editable template for new terms being added to the glossary.
- Import & export: Import and export glossary files.

Glossary details

![The Details section of Glossary details](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_glossary-details-rev2.png "Click to view full size")

### Details

When setting up a business glossary whether the glossary has been imported or created, configuration of the business glossary Details is a key foundational component. Details has the following fields:

- Name: The name of your business glossary.
- Description: High-level value statement and summary of what content the business glossary will contain. This description should provide readers with an idea about what information they can expect to find in your glossary.
- Space: Select a space to move and save the glossary to if you would like to move it out of the default personal space.

  Information noteOnce a glossary is moved to a new space it will no longer be available in the current space. Only members of the new space will have access to the glossary.
- Tags: Apply any tags with words, phrases, or acronyms that will assist users to find your business glossary. For example, if the glossary is about contracts, tags such as terms, agreement, warranty, ACV, Annual Contract Value will help with organization and search.

### Term template

The term template is a rich text editor that provides the option to customize properties as suggested guidelines for new terms. These properties appear in the Related information field of the term editor window. The properties should elicit specific details that will enforce common structures across lines of business. For example, if your business glossary is about reports, you may ask users defining terms to provide information about sources, required software, scheduled updates, security concerns or required permissions.

The term template is also an opportunity to provide guidelines for README text fields.

An example term template:

##Term title, report name

##Required information and software

##Example commands

##Notes

##README
Report ID:
Report objective:
Owner(s):
Approval process URL:

### Import & export

Import & export allows you to both import glossary terms into your glossary and download the business glossary's JSON file.

You can import categories and terms into your glossary from glossary files. You can also reimport glossary files to update terms with any changes made to the glossary files. For more information, see [*Setting up business glossaries*](Setting-up-business-glossaries.htm#Importin).

You can view the logs for imports under Import log files.

Import & export

![Import & export section of Business Glossary.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_glossary-import-export-rev.png "Click to view full size")

You can exported your glossary in the Qlik Cloud glossary format. The glossary file is then available for import into a different environment. For more information, see [*Importing and exporting glossaries*](exporting-glossaries.htm).
