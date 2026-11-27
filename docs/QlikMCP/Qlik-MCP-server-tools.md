---
title: "Qlik MCP tools"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server-tools.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik MCP server"]
---

# Qlik MCP tools

The Qlik MCP server includes tools that let your LLM perform actions for you in your Qlik Cloud tenant. You can customize your experience by selecting which Qlik MCP tools you want available.

## Access permissions and Qlik MCP tools

Access to MCP tools is controlled by your permissions. You require the Qlik MCP: Allowed permission in a custom role to access Qlik MCP tools from your MCP client.

Additionally, as the Qlik MCP tool is authorized as the connecting user, it uses your existing user role and space permissions. You also need to have permission in Qlik Cloud to use the capabilities or content type used by the tools. For example, if you do not have permission to access lineage in Qlik Cloud, you cannot use the Qlik MCP tool Qlik get lineage. Depending on your permissions, some tools may respond with no access if you cannot use the capability or feature in Qlik Cloud.

Tool availability can also be limited by your tenant's licensing.

## Selecting Qlik MCP tools

The Qlik MCP tools are a catalog of purpose-built actions that an LLM can call to perform actions in your Qlik Cloud tenant. These actions include:

- Finding applications and datasets
- Inspecting fields and chart metadata
- Applying and clearing filters
- Creating and editing sheets, charts, and containers
- Managing governed assets like glossary terms and data products.

Each tool represents a specific capability with well-defined inputs and outputs.

### Available Qlik MCP Tools

The table below shows an overview of current Qlik MCP tools categories and tool names.

Information note

New tools are not available in your client until after you re-authenticate with the Qlik MCP server. If you want to refresh your available tools, sign out and then back in again to the Qlik MCP server in your MCP client.

MCP clients often cache tool definitions. If new tools are missing or updated tools behave as before, restart your MCP client or reconnect to the Qlik MCP server.

| Category | Summary | Tool name |
| --- | --- | --- |
| App Discovery & Metadata | Find applications, explore structure, understand what data is available. | - qlik\_search - qlik\_describe\_app - qlik\_get\_fields - qlik\_list\_sheets - qlik\_get\_sheet\_details |
| Application Script Lifecycle | Create apps, manage scripts, run reloads, and inspect load outcomes. | - qlik\_create\_app - qlik\_get\_dataset\_script - qlik\_get\_script - qlik\_update\_script - qlik\_start\_app\_reload - qlik\_get\_reload\_status - qlik\_get\_reload\_log - qlik\_cancel\_app\_reload - qlik\_get\_data\_model |
| Automations | Discover, create, update, and delete automations, and manage automation connections and connectors to perform actions like sending notifications or executing workflows. | - qlik\_fetch\_automation\_run - qlik\_get\_automation\_by\_id - qlik\_get\_automation\_inputs - qlik\_get\_automation\_run\_display - qlik\_list\_all\_automation\_runs - qlik\_list\_automation\_runs - qlik\_list\_automation\_connections - qlik\_list\_automation\_connectors - qlik\_get\_automation\_connector - qlik\_get\_automation\_connector\_webhook\_configuration - qlik\_create\_automation - qlik\_update\_automation - qlik\_delete\_automation - qlik\_start\_automation\_run - qlik\_start\_automation\_run\_interactive - qlik\_update\_automation\_run\_input - qlik\_get\_automation\_run |
| Bookmarks | View, create, update, and delete bookmarks in applications. | - qlik\_list\_bookmarks - qlik\_create\_bookmark - qlik\_select\_bookmark - qlik\_delete\_bookmark |
| Business Glossary | Manage business terms, definitions, categories, and linkages to data assets. | - qlik\_create\_glossary - qlik\_get\_full\_glossary\_export - qlik\_get\_glossary\_categories - qlik\_create\_glossary\_category - qlik\_search\_glossary\_terms - qlik\_get\_glossary\_term - qlik\_create\_glossary\_term - qlik\_update\_glossary\_term - qlik\_delete\_glossary\_term - qlik\_update\_term\_status - qlik\_get\_glossary\_term\_links - qlik\_create\_glossary\_term\_links |
| Data pipeline projects | Gets the connection’s tables and views, and the project’s binding values. | - qlik\_search\_connection\_objects - qlik\_get\_pipeline\_project\_details |
| Datasets & Data Quality | Inspect datasets, schemas, profiles, trust scores, and quality metrics. | - qlik\_get\_dataset - qlik\_get\_dataset\_schema - qlik\_get\_dataset\_profile - qlik\_get\_dataset\_sample - qlik\_get\_dataset\_freshness - qlik\_get\_dataset\_trust\_score - qlik\_get\_dataset\_memberships - qlik\_update\_dataset\_metadata - qlik\_update\_dataset\_quality - qlik\_get\_dataset\_quality\_computation\_status |
| Data Exploration & Analysis | Query data, build calculations, explore field values. | - qlik\_create\_data\_object - qlik\_get\_field\_values - qlik\_search\_field\_values - qlik\_get\_chart\_data - qlik\_get\_chart\_info |
| Data Products | Create, manage, activate, and distribute curated data products. | - qlik\_create\_data\_product - qlik\_get\_data\_product - qlik\_get\_data\_product\_documentation - qlik\_update\_data\_product - qlik\_update\_data\_product\_space - qlik\_update\_activate\_data\_product - qlik\_update\_deactivate\_data\_product - qlik\_delete\_data\_product |
| Knowledge bases | Search knowledge bases and use their contents to get answers. | - qlik\_search\_knowledgebase\_chunks |
| Lineage | Trace data origins and transformations. | - qlik\_get\_lineage |
| Machine Learning — Full Qlik Predict | Use Qlik Predict to train, deploy, manage, and predict with machine learning models. | - qlik\_start\_training\_experiment\_automl - qlik\_get\_training\_experiment\_automl - qlik\_create\_training\_report\_automl - qlik\_start\_deployment\_automl - qlik\_get\_deployment\_automl - qlik\_start\_realtime\_prediction\_automl - qlik\_start\_batch\_prediction\_automl - qlik\_get\_batch\_prediction\_automl - qlik\_get\_model\_automl - qlik\_get\_dataset\_profile\_automl - qlik\_delete\_resource\_automl |
| Master Items (Dimensions & Measures) | Manage reusable governed dimensions and measures. | - qlik\_list\_dimensions - qlik\_create\_dimension - qlik\_update\_dimension - qlik\_delete\_dimension - qlik\_list\_measures - qlik\_create\_measure - qlik\_update\_measure - qlik\_delete\_measure |
| Semantic Models (Data Products) | Discover and author the governed semantic model (tables, relationships, measures, and dimensions) of a data product. | - qlik\_get\_data\_product\_semantic\_model - qlik\_create\_data\_product\_semantic\_model - qlik\_create\_data\_product\_semantic\_model\_measures\_dimensions - qlik\_update\_data\_product\_semantic\_model - qlik\_update\_data\_product\_semantic\_model\_measures\_dimensions - qlik\_delete\_data\_product\_semantic\_model\_objects |
| Selections & Filtering | Apply and manage filters that affect all visualizations. | - qlik\_select\_values - qlik\_clear\_selections - qlik\_get\_current\_selections |
| Visualization & Sheets | Create, edit, organize, and remove dashboards, charts, filters, and containers. | - qlik\_create\_sheet - qlik\_add\_chart - qlik\_add\_filter - qlik\_update\_sheet - qlik\_duplicate\_sheet - qlik\_delete\_sheet - qlik\_update\_chart - qlik\_update\_filter - qlik\_add\_container - qlik\_update\_container - qlik\_delete\_object - qlik\_get\_chart\_properties\_schema |

## What the tools can each accomplish

### App Discovery and Metadata

Use these tools to find the right Qlik analytics application and quickly understand what’s inside it before you build charts or apply filters. This category supports an end-to-end discovery flow: search across Qlik resources to locate relevant applications.

The following tools are available:

- qlik\_search: Search for Qlik resources (applications, datasets, data products, glossaries, knowledge bases, pipeline projects, pipeline connections) by name or content.
- qlik\_describe\_apps: Get comprehensive metadata for an application including fields, owner, publishing status.
- qlik\_get\_fields: List all data fields available in an application for use as dimensions.
- qlik\_list\_sheets: List all sheets in an app.
- qlik\_get\_sheet\_details: Get details about a specific sheet including all charts and their types.
- qlik\_search\_spaces: Search for spaces based on a query string.

#### Prompt example:

"I need to analyze customer churn." This simple prompt allows to:

- Use qlik\_search to find applications related to “churn” or “customer retention”.
- For the best match, run qlik\_describe\_app to confirm it’s the correct application and see its metadata (owner and publishing status).
- Use qlik\_get\_fields to list available fields and identify candidate dimensions and measures like Customer, ChurnFlag, SubscriptionType, Region, and ChurnDate.
- Use qlik\_list\_sheets to see what dashboards already exist.
- For any promising sheet for instance, “Churn Overview,” call qlik\_get\_sheet\_details and summarize what charts are already available and what gaps remain.

### Application Script Lifecycle

These tools support the application and script lifecycle end-to-end in your MCP client. You can create an application , inspect and update its script, run a reload, and verify results from status and logs. This supports both guided authoring and automated workflows.

The following tools are available:

- qlik\_create\_app: Create a new Qlik analytics application in a target space.
- qlik\_get\_dataset\_script: Generate or retrieve script content from a dataset context.
- qlik\_get\_script: Retrieve the current application load script.
- qlik\_update\_script: Replace the full application load script.
- qlik\_start\_app\_reload: Start an application reload.
- qlik\_get\_reload\_status: Check reload progress and final state.
- qlik\_get\_reload\_log: Retrieve reload logs for validation and troubleshooting.
- qlik\_cancel\_app\_reload: Cancel an in-progress reload.
- qlik\_get\_data\_model: Inspect the resulting application data model after reload.

#### Prompt example:

"Create a new app called Sales Lifecycle Demo in my personal space. Draft a load script of it from our Orders dataset, then show me the full script."

"Update the script to include Customers and Products from the Customer dataset and reload the script. If the reload fails, return the reload log and suggest a script fix. If the reload succeeds, show the resulting data model summary."

### Automations

These tools let you find, create, update, and delete Qlik Cloud automations, and manage automation connections and connectors directly from your MCP client. Automations are reusable workflows that can trigger external actions such as sending notifications, executing integrations, or running scheduled tasks. By using these tools, LLMs can integrate Qlik Automate capabilities into agentic workflows, enabling autonomous automation lifecycle management and multi-step analysis tasks.

An official automation skill for LLMs, qlik-automation, is available from [GitHub: Official Skills](https://github.com/qlik-oss/agentic-skills). The skill guides LLMs in the use and creation of automations based on a user's prompt, ensuring a logical flow when creating and modifying automations.

The following tools are available:

- qlik\_fetch\_automation\_run: Fetch the current state of an automation run without polling.
- qlik\_get\_automation\_by\_id: Retrieve detailed information about a specific automation using its unique identifier.
- qlik\_get\_automation\_inputs: Retrieve the input fields required to run an automation, so you can discover which inputs are needed before you run it.
- qlik\_get\_automation\_run\_display: Retrieve the display output produced by a specific automation run.
- qlik\_list\_all\_automation\_runs: List all automation runs that you have permission to see across the tenant, giving an overview of automation activity.
- qlik\_list\_automation\_runs: List the runs for a specific automation, including status, start time, and duration. Use this to view the execution history and status of an automation.
- qlik\_list\_automation\_connections: List Qlik automation connections. Use this to discover configured connections that can be referenced in automation workspaces.
- qlik\_list\_automation\_connectors: List available Qlik automation connectors. Use this to discover connectors that can be used when building automation workspaces.
- qlik\_get\_automation\_connector: Get full details of a specific automation connector. Use this to inspect connection parameters, available blocks, and snippet templates for a connector.
- qlik\_get\_automation\_connector\_webhook\_configuration: Get webhook configuration for a specific automation connector. Use this to discover the webhook events a connector supports and the parameters each event exposes.
- qlik\_create\_automation: Create a new Qlik automation.
- qlik\_update\_automation: Update a Qlik automation's name, description, workspace, schedules, or concurrency limit.
- qlik\_delete\_automation: Delete a Qlik automation.
- qlik\_start\_automation\_run: Run an automation. This creates and starts a new run for the specified automation.
- qlik\_start\_automation\_run\_interactive: Start an automation and return the initial run state, supporting interactive input while the run is in progress.
- qlik\_update\_automation\_run\_input: Stop a running automation run immediately.
- qlik\_get\_automation\_run: Submit user inputs to an automation run that is waiting for input.

Automations have the following limitations when being used with Qlik MCP tools:

- Supported input types are limited to:

  - Single line
  - Multiple line
  - Dropdown

    Information noteDropdown inputs are limited to 10 options.
  - Multi-select.

    Information noteMulti-select inputs are limited to 10 options.

#### Prompt example:

"I've completed analysis on this month's sales trends. Search for automations related to notifications or email. Once you find one that sends email, show me its details. I want to run it to send a summary of my findings to stakeholders with the subject line 'Monthly Sales Trends Analysis'."

"What automations connectors can send emails?"

"I would like to create a Qlik automation using the qlik-automation skill that reloads my inventory app and sends a slack message in my #inventory-updates channel if the app reload fails."

### Bookmarks

This set of tools lets a user view and apply bookmarked selections in applications. Users can also create their own bookmarks from their current selections, allowing them to quickly reapply selections from their MCP client. Bookmarks created using the Qlik MCP tools can also be deleted.

The following tools are available:

- Qlik\_list\_bookmarks: List all bookmarks in an application.
- Qlik\_create\_bookmark: Create a new bookmark using the current selections.
- Qlik\_select\_bookmark: Select a bookmark. That changes the filters applied to the data model and returns the resulting selection state.
- Qlik\_delete\_bookmark: Delete a bookmark.

  Information note

  You can only delete bookmarks created using Qlik MCP tools.

#### Prompt example:

"Save the current selections as EMEA Q1 2026."

### Business Glossary

This set of tools lets a user set up and maintain a governed business glossary end-to-end:

- Create a glossary
- Organize it with categories
- Add and curate terms (including editing, removing, and managing life-cycle status such as draft -verified-deprecated)
- Connect those terms to real analytics assets (applications, datasets, fields, master items).

The following tools are available:

- qlik\_create\_glossary: Create a new business glossary
- qlik\_get\_full\_glossary\_export: Get complete glossary with all terms, categories, links (costly operation)
- qlik\_get\_glossary\_categories: Retrieve all categories for a glossary
- qlik\_create\_glossary\_category: Create a new category within a glossary
- qlik\_search\_glossary\_terms: Search for terms within a glossary
- qlik\_get\_glossary\_term: Get a specific term from a glossary
- qlik\_create\_glossary\_term: Create a new glossary term with description, tags, relationships
- qlik\_update\_glossary\_term: Modify an existing glossary term
- qlik\_delete\_glossary\_term: Remove a glossary term
- qlik\_update\_term\_status: Update term status (draft, verified, deprecated). Only a steward can verify a term. Once the term is verified only a steward can modify the term

  Information note

  This operation has three statuses:

  - draft: The term is in draft state.
  - verified: The term has been verified by a steward.
  - deprecated: The term is deprecated and should not be used.

  The status names are case-sensitive and must be provided exactly as above.
- qlik\_get\_glossary\_term\_links: Get resources linked to a glossary term

  This function supports two modes:

  - Single link mode: Provide individual parameters for instance resource\_id or resource\_type.
  - Batch mode: Provide a list of link dictionaries via the 'links' parameter

  Information note

  When linking to a subresource, all three subresource fields (subResourceId, subResourceName, and subResourceType) must be provided together for each link.
- qlik\_create\_glossary\_term\_links: Link a term to apps, datasets, fields, master items

#### Prompt example:

"Help me build and govern a Business Glossary for our Sales domain. Create a glossary called ‘Sales Glossary’, add categories ‘Revenue’, ‘Customers’, and ‘Pipeline’. Then create terms for ‘Annual Recurring Revenue (ARR)’ and ‘Customer Churn’ with clear definitions and tags for instance finance, and sales-ops, set them to draft, and link each term to the relevant dataset fields and the KPI master items."

### Datasets and Data Quality

These tools help a user understand, validate, and govern datasets by inspecting what the dataset is (metadata and data product memberships), what it contains (schema), what the data looks like (profiling statistics-distributions and a quick row sample). The tools also support stewardship workflows: improving dataset documentation (name-description) and triggering and monitoring data quality computations to refresh quality metrics over time.

The following tools are available:

- qlik\_get\_dataset: Load metadata of a dataset including trust score
- qlik\_get\_dataset\_schema: Load the schema (column definitions) of a dataset
- qlik\_get\_dataset\_profile: Load profile data (statistics, distributions) of a dataset
- qlik\_get\_dataset\_sample: Load first 10 rows of a dataset for preview
- qlik\_get\_dataset\_freshness: Get last updated timestamp of a dataset
- qlik\_get\_dataset\_trust\_score: Get the trust score of a dataset
- qlik\_get\_dataset\_memberships: Get data product memberships for a dataset
- qlik\_update\_dataset\_metadata: Update name and description of a dataset
- qlik\_update\_dataset\_quality: Request a data quality computation for a dataset
- qlik\_get\_dataset\_quality\_computation\_status: Check status of a quality computation

#### Prompt example:

“Assess the readiness of our Customer Orders dataset for a new dashboard. Show me its metadata and current trust score, confirm the last refresh time, and list which data products it belongs to. Then load the schema and a 10-row sample to sanity-check key fields like order\_date, customer\_id, and net\_amount. Run a dataset profile to spot missing values and outliers, and if quality metrics look stale, trigger a data quality computation and keep checking the job status until it completes. Finally, update the dataset description to document known constraints and recommended use.”

### Data Exploration & Analysis

These tools support quick and ad-hoc investigation of data and existing analytics content without requiring the user to permanently build new visualizations. You can create temporary calculations, or query objects to answer “what-if” questions, inspect fields by listing distinct values or search for specific values.

The following tools are available:

- qlik\_create\_data\_object: Create temporary calculation objects for ad-hoc analytics queries

  Information note

  Use get\_field\_values() or search\_field\_values() before applying selections to verify values exist.

  Warning note

  Qlik performs ALL calculations, therefore:

  - Never aggregate, sum, average, or compute on returned data: values are final.
  - For different calculations, call tool again with new expressions.
  - Always apply appropriate filters-selections to limit data size and improve performance.
- qlik\_get\_field\_values: Get distinct values for a specific field (use before filtering)

  Information note

  For high cardinality fields, always use qlik\_search\_field\_values() instead

  Warning note

  Use this tool or qlik\_search\_field\_values() BEFORE creating selections-filters to verify that the values exist. This helps avoid errors when applying filters with non-existent values.
- qlik\_search\_field\_values: Search for specific values across fields (verify before set analysis)

  Warning note

  Before creating data objects with set analysis or selections: Use qlik\_search\_field\_values to verify values exist. This prevents errors from non-existent filter values, especially important for: years, dates, currency codes, product names.

  Best practice example workflow:

  1. qlik\_search\_field\_values(fieldName="payment\_year", searchTerms=["2022"])
  2. Verify "2022" exists in results
  3. Create data object using {payment\_year={2022}.
- qlik\_get\_chart\_data: Retrieve paginated data from an existing chart visualization
- qlik\_get\_chart\_info: Get metadata about a chart without retrieving its data

#### Prompt example:

“Help me investigate why North region revenue dropped last month. First, check the existing ‘Revenue by Region’ chart: show me its metadata (dimensions, measures, filters, row count) and then pull the chart data for the last two months. Before I apply any selections, list the distinct values for Region and search the field values to confirm whether ‘North’, ‘NORTH’, or ‘Northern’ is used. Then create a temporary calculation to compare month-over-month revenue and margin for North vs other regions, and highlight which product categories contributed most to the change.”

### Data Products

These tools manage the full lifecycle of a data product as a governed, shareable package of datasets:

1. Create it.
2. Inspect its metadata and documentation.
3. Maintain its definition (name, description and which datasets it contains)
4. Control where and whether it’s available by moving it between spaces and activating or deactivating it.

They also support end-of-life cleanup by deleting a data product when it’s no longer needed.

The following tools are available:

- qlik\_create\_data\_product: Create a new data product
- qlik\_get\_data\_product: Get metadata for a specific data product
- qlik\_get\_data\_product\_documentation: Get markdown documentation of a data product
- qlik\_update\_data\_product: Update properties (name, description, datasets) of a data product
- qlik\_update\_data\_product\_space: Move a data product to a different space
- qlik\_update\_activate\_data\_product: Activate a data product in a specific space
- qlik\_update\_deactivate\_data\_product: Deactivate a data product
- qlik\_delete\_data\_product: Delete a data product

#### Prompt example:

“Create a data product called ‘Sales Analytics – Curated’ with a clear description and include these datasets: Orders, Customers, and Products. Then show me the data product metadata and pull its markdown documentation so I can review what consumers will see. Update the description to add usage guidance and add the Returns dataset as well. Move the data product to our Shared ‘Analytics’ space, activate it there for broader access, and if we later replace it with a new version, deactivate the old one. Finally, if the product is fully retired and no longer referenced, delete it.”

### Semantic Models (Data Products)

These tools give your LLM governed, agent-ready access to a data product's semantic model, which is the certified, reusable business logic (tables, relationships, measures, and dimensions) that is defined once at the data product level and consumed consistently across applications. Use them to:

- Retrieve the full semantic model of a data product so an agent can use it as context before building a load script or a new analytics application.
- List the measures and dimensions of a semantic model, including their names, expressions, descriptions, and tags.
- Retrieve table relationships, including the involved tables, fields, name, description, and cardinality.
- Create and update measure and dimension definitions, and define new table relationships, directly from a coding agent workflow.

As with in-application master items, these tools help you standardize and reuse business logic, but at the data product level, so the definitions are governed and shared across every application that consumes the data product.

Information noteAll tools are subject to the same space-level and role/permission-based access controls as the rest of the Qlik MCP server.

The following tools are available:

- qlik\_get\_data\_product\_semantic\_model: Retrieve the full semantic model of a data product (tables, selected fields, relationships, measures, and dimensions) in a structured, agent-readable format
- qlik\_create\_data\_product\_semantic\_model: Create a semantic model for a data product
- qlik\_create\_data\_product\_semantic\_model\_measures\_dimensions: Create measures and dimensions in a data product semantic model
- qlik\_update\_data\_product\_semantic\_model: Update a data product semantic model
- qlik\_update\_data\_product\_semantic\_model\_measures\_dimensions: Update measures and dimensions in a data product semantic model
- qlik\_delete\_data\_product\_semantic\_model\_objects: Delete objects from a data product semantic model

#### Prompt example:

“Retrieve the semantic model for our Operations data product so I can see what measures, dimensions, and table relationships are already defined. List the measures and dimensions with their descriptions and tags, and show me the relationships between the Production and Plant tables, including the cardinality. Then create a new measure called ‘Scrap Rate’ using our standard definition, and add descriptions and tags so other teams can discover and trust it.”

### Data pipeline projects

These tools help configure and validate pipeline projects defined in code. When MCP server is deployed with declarative pipeline support, you can use these tools to search available data sources and inspect pipeline project metadata before deployment.

The following tools are available:

- qlik\_search\_connection\_objects: List all source entities (tables, views) available in a data connection. Use this to discover what data sources are available when configuring data pipeline tasks.
- qlik\_get\_pipeline\_project\_details: Returns the project’s binding values.

#### Prompt examples:

- "Show me all available tables in our Sales database connection so I can decide which tables to include in the data pipeline."
- "Return the binding values of the 'CustomerETL' data pipeline project."

### Knowledge bases

This tool allows you to find knowledge bases and search their contents to get answers. The tool allows you to search the contents of specific knowledge bases.

The following tools are available:

- Qlik\_search\_knowledgebase\_chunks: Search within the indexed contents of a knowledge bases and use receive answers using the knowledge base content.

#### Prompt example:

"I'm preparing for a meeting with a prospective client. Look at my customer information, product use case, and competitive analysis knowledge bases and see which use cases best align with my client's needs while showing how we out perform the competition."

### Lineage

This tool lets a user trace where data comes from and how it flows by retrieving upstream lineage for a dataset or app. Because each call returns only one step back, you typically repeat it recursively to build the full chain. This is useful for:

- Impact analysis.
- Troubleshooting unexpected numbers.
- Governance or auditing.
- Identifying the true sources feeding a report or dataset.

The following tools are available:

- qlik\_get\_lineage: Load lineage history of a dataset or app (call recursively for full chain)

#### Prompt example:

“Show me the full upstream lineage for the Customer Orders dataset. Start from the dataset and walk back recursively until you reach the original source systems. For each step, summarize what the immediate parent is and note any key transformations or intermediate datasets or apps involved. Then tell me which upstream source is most likely to affect the net\_amount field if it changes.”

### Machine Learning — Full Qlik Predict

Full Qlik Predict tools offer the full Qlik Predict experience, including model training, training report generation, model deployment and management, and batch predictions.

The following tools are available:

- qlik\_get\_dataset\_profile\_automl: Profiles a dataset for ML, displaying column types, data distributions, and potential feature and target columns.
- qlik\_start\_training\_experiment\_automl: Starts model training for a selected target and evaluates multiple algorithms for comparison.
- qlik\_get\_training\_experiment\_automl: Retrieves an experiment’s current status, setup, and results.
- qlik\_create\_training\_report\_automl: Creates a report that summarizes a model training run.
- qlik\_get\_model\_automl: Provides information about a trained model, including its performance measures and feature importance.
- qlik\_start\_deployment\_automl: Makes a model available to generate predictions by deploying it to an ML deployment.
- qlik\_get\_deployment\_automl: Retrieves an ML deployment’s configuration and current status.
- qlik\_start\_batch\_prediction\_automl: Uses a deployed model to generate predictions for every record in a dataset.
- qlik\_get\_batch\_prediction\_automl: Retrieves the results of a batch prediction job and reports its status.
- qlik\_start\_realtime\_prediction\_automl: Generates on-demand predictions for individual records using a deployed model.
- qlik\_delete\_resource\_automl: Deletes experiments, models, or deployments.

#### Prompt examples:

These prompts can help you get started with running machine learning workflows via the Qlik MCP server. Note that a single prompt may call multiple tools depending on phrasing and other factors. You may also wish to enter prompts as smaller individual instructions if you need more control and feedback as you progress through workflows.

- "Train an experiment based on the ML - Churn data - training dataset to predict the Churned column. Provide a list of models in order from highest to lowest quality, flagging any quality issues in the process."
- Deploy the best model from <experiment ID or name>. Run a batch prediction against the ML - Churn data - apply dataset and provide a summary of the predictions, along with an assessment of their quality and reliability. "

### Master Items (Dimensions & Measures)

These tools help users standardize and reuse key business logic in an app by working with master (library) dimensions and measures. You can inventory what’s already available (to avoid duplicates and encourage consistency), and you can create new reusable dimensions and measures so charts across multiple sheets use the same field definitions and calculation expressions, improving governance, maintainability, and metric alignment.

You can update your master items with new definitions, allowing quick refinements. You can also delete master items. For example, you can ask your MCP client to clean up any master item that is not in use in an application.

Information noteYou can only update and delete master items created using Qlik MCP tools.

The following tools are available:

- qlik\_list\_dimensionst: List all library dimensions available in the app
- qlik\_create\_dimension: Create a reusable library dimension
- qlik\_update\_dimension: Update an existing library dimension in a Qlik app
- qlik\_delete\_dimension: Delete a library dimension from a Qlik app
- qlik\_list\_measures: List all library measures available in the app
- qlik\_create\_measure: Create a reusable library measure with expression
- qlik\_update\_measure: Update an existing library measure in a Qlik app
- qlik\_delete\_measure: Delete a library measure from a Qlik app

#### Prompt example:

“Help me standardize metrics in our Sales Performance app. First, list the existing library dimensions and measures so we don’t duplicate anything. Then create a new library dimension ‘Customer Segment’ based on the appropriate segment field, and create a reusable measure ‘Gross Margin %’ using our standard definition (gross margin divided by revenue, formatted as a percentage). After creating them, tell me the exact master item names I should reference when building charts so all dashboards use the same logic.”

### Selections & Filtering

These tools control the interactive filter state of a Qlik app:

- Apply selections to one or more fields (using exact values or pattern-predicate-style matching).
- Inspect what filters are currently active.
- Clear selections either globally or for a specific field.

Together they support guided analysis flows, reproducible investigation steps.

The following tools are available:

- qlik\_select\_values: Apply selections (filters) to fields - supports exact values and pattern matching

  Information note

  When to use selections over set analysis:

  - When you want to filter the entire app or session for multiple subsequent operations, use select\_values().
  - When you need a one-time filter for a specific calculation, use set analysis in expressions

  Selections persist across all operations until cleared they affect ALL subsequent data retrievals. As best practice, for single analytical queries, prefer set analysis over selections to avoid state management overhead.

  Warning note
  - Use qlik\_get\_field\_values() or qlik\_search\_field\_values() first to verify that the values you want to select exist. Selecting non-existent values will fail silently.
  - The returned selections are the actual current applied selection are truth. Any fields where selection failed for instance: where values did not exist will not appear in the returned list.
- qlik\_clear\_selections: Clear selections - all or specific field

  Warning noteThe returned selections are the actual current applied selection and they are the truth. Any fields where selection failed for instance, values did not exist, will not appear in the returned list.
- qlik\_get\_current\_selections: Get currently active selections or filters in the app

#### Prompt example:

“Set up my analysis context for the Executive Sales app: select Year = 2025 and Region = EMEA, and apply a pattern-based selection on Product Category to include only categories starting with ‘Cloud’. Then show me the current selections so I can confirm what’s active. After I review the KPIs, clear only the Product Category selection (keep Year and Region), and finally clear all selections to reset the app back to an unfiltered state.”

### Visualization & Sheets

These tools let users build and maintain dashboards in a Qlik application:

- Create sheets, and rename existing sheets or reposition and resize the objects on them.
- Add and update visualizations (charts, tables, KPIs) configured with dimensions, measures, colors, sorting, and styling.
- Add and update filter panes so users can interactively slice the analysis.
- Organize objects in layout containers or tab containers.
- Duplicate sheets to get editable copies, including copies of published sheets.
- Delete sheets and objects that are no longer needed.

Together, they support building, refining, and cleaning up self-service dashboards.

The following tools are available:

- qlik\_create\_sheet: Create a new empty sheet (dashboard) in the app
- qlik\_add\_chart: Add a chart to a sheet, layout container, or tab container. You can set explicit colors (a single color, or color by dimension, measure, or expression), sorting, and top or bottom N limits. You can also set presentation properties such as axes, legends, data labels, reference lines, and styling.

  Information note
  - Plan your query structure before making tool calls.
  - Test date-value existence with qlik\_search\_field\_values or qlik\_get\_field\_values first
  - Use set analysis over app-level selections for one-off queries
- qlik\_add\_filter: Add a filter pane to a sheet, layout container, or tab container. You can configure listbox settings for each field, such as histogram, frequency, and check boxes, and style the filter pane.
- qlik\_update\_sheet: Rename a sheet, update its description, and reposition or resize the objects on it.
- qlik\_duplicate\_sheet: Duplicate a sheet, including its charts and filter panes. The tool places the copy in the AI Generated sheet group. Use this tool to get an editable copy of a published sheet.
- qlik\_delete\_sheet: Delete a sheet and all objects on it.
- qlik\_update\_chart: Update an existing chart. The tool changes only the settings you provide and keeps all other settings, including styling applied outside the tool.
- qlik\_update\_filter: Update an existing filter pane, its fields, and its listbox settings. The tool changes only the settings you provide.
- qlik\_add\_container: Add a container to a sheet. Add a layout container to position objects freely on a grid, or a tab container to show objects as tabs.
- qlik\_update\_container: Update the settings of a container. You can also update the position of child objects in a layout container, or the tab order in a tab container.
- qlik\_delete\_object: Delete a chart, filter pane, or container. Sheets and master items have their own delete tools.
- qlik\_get\_chart\_properties\_schema: Get the JSON schema for the chart properties of a chart type or filter pane. MCP clients use the schema to configure styling and other settings correctly.

Information note

Editing sheets and objects requires your normal permissions on the app and sheet. You cannot edit published sheets directly. To change a published sheet, use qlik\_duplicate\_sheet to create an editable copy. For more information about duplicating sheets and sheet permissions, see [*Reusing sheets and sheet content*](../Sheets/reusing-sheets-and-sheet-content.htm).

Warning note

qlik\_delete\_sheet and qlik\_delete\_object permanently delete content. You cannot undo these actions. We recommend that you configure your MCP client to ask for confirmation before it runs delete tools.

#### Prompt examples:

- “Create a new sheet called ‘Sales Overview’ in our analytics app. Add a KPI for Total Revenue and Total Orders, a line chart showing Revenue by Month, and a bar chart showing Revenue by Region (sorted descending). Then add a filter panel with Year, Region, and Product Category so users can adjust the view. Make sure the visuals are titled clearly and the sheet is ready for an executive audience.”
- “Duplicate the Sales overview sheet and add a tab container with revenue by region and revenue by product.”
- “Change the bar chart on the Margins sheet to show the top 10 customers sorted by margin, in our brand color.”
