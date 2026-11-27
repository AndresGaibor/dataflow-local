---
title: "Working with reusable components"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/WorkingWithReusableComponents.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts"]
---

# Working with reusable components

OAS 3.0 brings reusable components to API definitions.

Reusable components allow you to use an element in several parts of your API,
without having to define it multiple times.

If you need to reuse the same header in ten different operations, you can
create a component, and then refer to the component in all the operations where it is needed.
Then, if you need to edit the header, you do not need to do it in all ten operations. You can
simply modify the component, and the change is automatically propagated to all the elements
that use it.

The following components are supported:

- Path variables
- Query parameters
- Headers
- Responses

Components are visible in the Components tab in the left panel.
