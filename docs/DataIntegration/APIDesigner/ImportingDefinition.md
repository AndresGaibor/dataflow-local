---
title: "Importing a definition"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/ImportingDefinition.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with OpenAPI Specification and RAML definitions"]
---

# Importing a definition

Import an existing API definition into API Contracts.

This action creates a new API definition in API Contracts. To
import content into an existing API version instead, see [Importing
version content](WorkingWithMultipleVersions.htm "Import content from an existing contract into an API version, replacing or merging its current content.").

1. At the homepage or folder level, click Import.

   ![Screenshot of the Import button.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/designer_import_definition.png)
2. Select a format and a source.
3. Select a file or enter a URL, then click Import.

   ![Import definition dialog box.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/import2.png)

   If the definition does not conform to the corresponding OAS, Swagger, or RAML
   specification, the entire file is rejected or the invalid parts of the API are
   ignored.

   Information noteNote: When importing an OpenAPI 3.0 definition, read-only and
   write-only properties defined at the operation level are ignored.

You can now manage your API definition in API Contracts.
