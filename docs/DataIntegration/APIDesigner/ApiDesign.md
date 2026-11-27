---
title: "API design"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/ApiDesign.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts"]
---

# API design

Use the editor to design your API.

## Going from requirements to an API

Like most technologies, an API is a solution to a problem. In order to design the right
API, you need to make sure the problem you are addressing is clearly defined by answering
the following questions:

- Who are the target consumers of this API?
- What kind of information will consumers manipulate via the API?
- What actions will consumers perform on the API?

For example, if you are a food delivery company,
you might want to build an API for your partner network that will enable them to browse
and search through a database of restaurants for which you provide a delivery service.

In this example, your API is targeting partners of your company.
They'll need to manipulate data about restaurants, and perform search queries on the data,
with certain filtering and sorting capabilities.

Another example: if you are a calendar SaaS company,
you might want to build an API so that other front-end developers in the world can create new mobile
and web applications based on your calendar system.

Thinking about the consumers of your API is the first step towards providing them with a
good developer experience. This will help your API stand out and increase engagement
levels.

## The elements that make up an API

There are four key concepts used when designing an API:

- A Resource is an element your consumers will interact with
  through your API. Resources are uniquely identified by a path, which combined with the
  API's endpoint provides a unique address for a resource on the web. For example, Calendars
  is the name of a resource that corresponds to a list of calendars, and its path is
  /calendars.
- An Operation is the action that can be performed on your
  resources. The most common operations are GET (read), POST (create), PUT (update) and
  DELETE. For example, List all Calendars is the name of an operation that uses the GET
  method on the Calendars resource.
- A Data type is a description of the actual data that is exchanged
  over the network. For example, Calendar is the name of a data type which will describe all
  the properties of a Calendar, such as its name, owner, and a reference to the events that
  belong to it. The List all Calendars operation returns a list of Calendar data types.
- A Component is a an element which can be reused throughout the
  API definition. For example, if you need to use the same query parameter in several
  operations, you can create it as a component and refer to it in as many operations as
  needed.

There are other useful elements that make up an API:

- An Endpoint is the main entry point for your API on the web. An
  endpoint is composed of a scheme such as HTTPS, and a host such as
  www.calendar-api.com.
- A Text block can be used to freely enter any text (including
  markdown) which can be placed anywhere in your API design. Use text blocks to explain
  transversal topics like authentication and error handling.
- A Section is used to meaningfully group together resources and
  data types. Use these to make your API design clearer and more developer friendly. You can
  drag and drop elements into sections in the left panel, and you can also reorder sections
  among each other.

In API Contracts, you will be
able to create these elements from the Create new menu in the
top-right corner.

![Create new menu expanded.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_the_menu_to_create_definition_elements_and_components.png)

Server URLs are created in the general information screen. A server URL can be
Published or Not published. If it is
published, it appears in the Live Documentation.

![List of all server URLs.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/serverurl_list.png)
