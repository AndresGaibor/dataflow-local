---
title: "Qlik Answers limitations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/qlik-answers-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Qlik Answers limitations

This page describes known limitations and constraints you should be aware of when preparing applications, configuring assistants, and deploying Qlik Answers to end users.

## Mobile browser limitations

The chat experience is supported for mobile browsers, but creating and managing knowledge bases and assistants are not optimized for standard mobile browser screen sizes.

## Structured data limitations

Structured data in applications has the following limitations with Qlik Answers.

### Avoid set identifiers in master measure expressions

When Qlik Answers applies a filter to a master measure, it wraps the measure in an outer set expression. For example, to filter a measure called SUV Revenue by brand, Answers generates:

{<Brand={'Brand 1'}>} [SUV Revenue]

This works correctly when the master measure's expression does not contain a set identifier. Set identifiers include:

- $: Current selection state
- 1: Full dataset
- StateName: An alternate state name

If the master measure's expression contains an inner set identifier, the Qlik engine's set analysis precedence rules apply and the inner set identifier overrides the outer set entirely. The filter that Answers generated is silently discarded, and the measure returns unfiltered results with no error or warning.

For example, take the following master measure expression:

Sum({$<Car\_Type={'SUV'}>}Price)

If Qlik Answers wraps this in an outer set filter for Brand='Qlik Cars', the $ identifier causes the engine to ignore the outer Brand filter. The result is all SUV revenue across all brands, not Qlik Cars SUV revenue.

Master measure expressions affected by this behavior include any that use:

- {$<...>}: Current selection state identifier
- {1<...>}: Full dataset identifier
- {StateName<...>}: An alternate state identifier

As a best practice, where possible, avoid embedding set identifiers directly in the expressions of master measures intended for use with Qlik Answers. Instead, express the measure's filtering logic through the data model or use field-level filtering without a set identifier, so that Qlik Answers can apply outer set filters correctly.

If a master measure must contain an inner set identifier for use elsewhere in the app, be aware that Qlik Answers may return incorrect results when that measure is used in filtered queries.

### Free-text fields in structured tables

Qlik Answers queries the structured Qlik data model, including numeric values, categories, and aggregations. It does not analyze the content of free-text columns loaded from structured sources such as CRM notes, commentary fields, survey responses, or incident descriptions.

For example, a field called ChurnReason containing values like "Customer said pricing was too high compared to competitors" cannot be queried semantically. Qlik Answers can return the raw field value, but cannot reason over the text content across rows.

If your use case requires semantic analysis of free-text data, add that content as a knowledge base source using the supported file formats (TXT, PDF, DOCX, etc.). Note that moving text content to a knowledge base removes it from the associative data model context.

### Semantic layer limitations

Qlik Answers has the following limitations for indexing the semantic layer of applications.

#### What Qlik Answers indexes

Qlik Answers indexes the following from an application:

- Application name and description
- Data model fields and structure
- Logical model fields and groups (Overview and Fields and master items)
- Master dimension and master measure names and descriptions
- Business logic synonyms from the Vocabulary section
- Business glossary definitions, categories, and term linkages.

#### What is not indexed

The following are not indexed and have no effect on how Qlik Answers interprets queries:

- Label expressions on master items. The label expression is a display and visualization property only. It has no effect on indexing, query matching, or the terms Qlik Answers recognizes. Use the Name and Description fields on the master item instead.
- Calculated descriptions or dynamically computed properties on master items
- Business logic content from Packages, Hierarchies, Behaviors, Calendar periods, Custom analysis, and Example questions. These features are removed when a tenant is enabled for the agentic Qlik Answers experience.

#### Custom semantic understanding and app copies

- Custom semantic understanding is kept when you publish an app from a shared space to a managed space. It is not kept when you duplicate an app, or export it as a QVF and import it. The new app shows Qlik Answers-generated descriptions only. Edit the descriptions again in the new app, then reindex it.

### Application behavior limitations

Applications have the following limitations and considerations when using Qlik Answers.

#### Selection state independence

Qlik Answers operates independently of the application's selection state. Active dashboard filters, bookmark-applied selections, or filter actions triggered on sheet load do not scope or influence the answers that Qlik Answers returns.

This means:

- A user with Year = 2026 selected on the dashboard will still receive full-data answers from Qlik Answers unless the data is restricted by Section Access.
- Qlik Answers does not read, apply, or respond to the current selection context.

This is by design and ensures answer consistency regardless of the visual state of the app.

#### Add to sheet availability

The Add to sheet option, which allows users to save AI-generated charts and tables directly into application sheets, is only available when using Qlik Answers within an application. It is not available when interacting with an application through an assistant or through the Application analysis context outside an open application.

If your deployment model is assistant-centric and users need to add generated visualizations to applications, direct them to use Qlik Answers within the application rather than through the assistant.

#### Session context and feedback persistence

Qlik Answers maintains conversation history within a session. A user can return to a previous conversation thread and continue asking questions. The underlying app data, however, may have changed since the original conversation and earlier answers may no longer reflect the current data state.

In-session corrections and thumbs-down feedback do not persist across sessions and do not alter how Qlik Answers interprets future questions. Feedback is captured for administrator review but does not dynamically retrain or adjust response behavior.

To make permanent corrections to how Qlik Answers interprets a term, metric, or concept, update the relevant master item description or add a business logic synonym.

#### Visualization data point rendering limitations

Visualizations within Qlik Answers are optimized to render up to 200 data points simultaneously. This limitation primarily affects scenarios such as large line charts or other high-density visualizations where a significant number of points must be displayed at once within the Qlik Answers experience.

When the number of rendered data points exceeds 200, visualization performance and rendering stability may degrade, which can result in incomplete or failed chart rendering.

This limitation applies only to visualizations rendered directly within Qlik Answers. When a visualization is added to a Qlik sheet, the full dataset and all underlying data points continue to render and function normally within the standard Qlik analytics experience.
