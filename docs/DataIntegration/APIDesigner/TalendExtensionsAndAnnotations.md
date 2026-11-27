---
title: "Talend extensions and annotations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/TalendExtensionsAndAnnotations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with OpenAPI Specification and RAML definitions"]
---

# Talend extensions and annotations

Export your API with Talend extensions or annotations to keep the expressivity provided by API Contracts.

When exporting an API, you can choose to include Talend extensions for OpenAPI Specification, or
Talend annotations for RAML. These allow you to keep
the structure of your API as defined in API Contracts.

For example, in the Contacts API, resources and operations are sorted
into sections, and text blocks are used to add information.

![Screenshot of the Contacts API.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/designer_talend_extensions.png)

If you export this definition without Talend extensions or annotations, sections and
text blocks are not exported. However, with the extensions or annotations, they are included
in the code.

The section information is added to any element contained in a section:

```
    x-talend:
      section: "Companies"
```

Text blocks are added at the end of the file:

```
  texts:
    3a36b8ba-2969-46f0-a36e-9d715eeece36:
      title: "Authentication"
      content: "This API is secured using Basic Authentication.\n\nAll **read operations are open** and don't require authentication. However, all **write operations require authentication**. "
      section: "General"
    612e4b7f-0530-4835-8a47-f580869c67df:
      title: "Error handling"
      content: "This API uses standard HTTP status codes to indicate the status of a response.\n\nThere are two main categories of error responses. Each have a different response payload structure.\n\n* Simple errors\n* Detailed errors\n\n\n# Simple errors\n\n| Name | Code | Description |\n| -------- | -------- | -------- |\n| Bad request     | 400     | The request was unacceptable     |\n| Unauthorized     | 401     | The request has not been applied because it lacks valid authentication credentials for the target resource.     |\n| Forbidden     | 403     | The server understood the request, but is refusing to fulfill it     |\n| Not Found     | 404     | The server has not found anything matching the request URI     |\n| Not acceptable     | 406     | The server is unable to return a response in the format that was requested by the client     |\n| Unsupported Media Type     | 415     | The server is refusing to service the request because the entity of the request is in a format not supported by the requested resource for the requested method     |\n| Too many requests     | 429     | Too many requests hit the API too quickly     |\n| Server error     | 500     | A technical error occured  |\n\n\n\n\n\n\n# Detailed errors\n| Name | Code | Description |\n| -------- | -------- | -------- |\n| Unprocessable entity     | 422     | The server understands the content type of the request entity, and the syntax of the request entity is correct, but was unable to process the contained instructions.     |\n\n\n\n\n"
| Server error     | 500     | A technical error occurred  |\n\n\n\n\n\n\n# Detailed errors\n| Name | Code | Description |\n| -------- | -------- | -------- |\n| Unprocessable entity     | 422     | The server understands the content type of the request entity, and the syntax of the request entity is correct, but was unable to process the contained instructions.     |\n\n\n\n\n"
      section: "General"
```
