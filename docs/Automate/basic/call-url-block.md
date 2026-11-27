---
title: "Call URL block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/call-url-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Call URL block

The call URL block calls a URL, typically from an API.

![call URL block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/call-URL-block.png)

An call URL block is commonly used in following situations:

- When an automation needs data from a URL.
- When an automation sends data to a URL.

## Configuring a call URL block

Configure the call URL block to interact with a URL.

### Inputs

The call URL block requires a valid URL of an API, an HTTP method, and an optional timeout value.

#### The URL

The URL filed is required and must include the full path URL.

Information noteWhen an automation calls out to an external server where SSL verification is required, the server should provide the complete chain certificates. If the complete chain certificate is not provided the verification may fail.

Call URL block input menu

![Call url block input settings](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/call-url-block-url.png)

The supported HTTP methods are:

- `GET`
- `PUT`
- `POST`
- `PATCH`
- `DELETE`

#### Parameters and headers

You can add parameters and headers to your URL as needed.

Information note

When you use the GET method, these parameters are added to the query string. For all other methods, parameters are added to the POST body.

Call URL parameters options

![parameters for call url block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/call-url-block-param.png)

Tip note

To see the raw JSON, click the Raw input toggle.
