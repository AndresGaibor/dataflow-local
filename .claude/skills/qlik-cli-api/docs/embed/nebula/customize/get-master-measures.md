---
source: https://qlik.dev/embed/nebula/customize/get-master-measures/
last_updated: 2025-07-08T16:09:30Z
---

# Evaluate master measure data

> **Note:** Where possible, use [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

> **Third-party cookies:** This tutorial leverages cookies for auth, which are blocked by some browser vendors.
> Please use an OAuth solution where possible, which doesn't leverage cookies.

## Overview

In this tutorial, you are going to learn how to get and monitor a list of master
measure values for use within your mashup. There are some scenarios where
just having a number of KPIs in your mashup is all that you need. For example,
you could have a portal page where you want to display a few master measure
values while using third-party visualizations or even vanilla HTML. This
tutorial uses [enigma.js](https://qlik.dev/toolkits/enigma-js) to connect to an app,
pull in the desired master measures, and then evaluate and monitor them.

## Prerequisites

To use the example page in this tutorial, ensure that you have the following:

- The ID of an existing Qlik Sense application to embed that contains one or
  more master measures.
- A [web integration](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm)
  configured that contains the location of the web page that will be embedding the
  Qlik Cloud application.
- A [content security policy](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)
  entry with the `frame-ancestors` directive added for the location of the webpage
  that will be embedding the Qlik Sense application.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables that appear in the sample code.

| Variable                 | Description                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------- |
| `<TENANT>`               | The domain for the tenant you are accessing. Equivalent to `tenant.region.qlikcloud.com`.               |
| `<WEB_INTEGRATION_ID>`   | The unique identifier of the web integration.                                                           |
| `<APP_ID>`               | The unique identifier of the Qlik Sense application.                                                    |
| `<MASTER_MEASURE_NAMES>` | A list of master measure names. These are the measures that will be fetched and evaluated from the app. |

## Pseudocode

The code example in this tutorial provides a basic, fully functional web page
(note however that all data is only displayed within the browser's console --
the web page itself will be blank) that executes the following sequence:

1. Logs into the Qlik Cloud tenant.
2. Fetches the CSRF token so that a WebSocket connection can be made to the
   Engine.
3. Connects to the application using enigma.js.
4. Establishes listeners on the WebSocket session `closed` and `suspended`
   events.
5. Gets a list of all master measure definitions from the app and logs
   them to the console.
6. Filters the list of all master measures down to only those that have
   matching names found with the `MASTER_MEASURE_NAMES` variable and
   logs them to the console.
7. Builds a HyperCube of the desired master measures (no dimensions) and
   logs it to the console.
8. Creates a dictionary of the measure names and values from step 7 for
   ease of use and logs it to the console.
9. Establishes a listener for change events on that HyperCube so that if
   selections are made, the app is reloaded, etc -- the HyperCube will
   be updated and logged to the console again.

The intent here is that you take the dictionary object that contains the
master measures and associated values and display that information on
your page however you'd like. You would want to make sure that you
update your display on the page each time the HyperCube fires a change
event.

## Sample code

The sample code showcases a few capabilities in one example, providing a
boilerplate you can modify. Here are some of the features:

- Catches session events, such as displaying a custom modal dialog or redirecting
  to another web page.

- Handles browser support for third-party cookies. For more information, see
  [Third-party cookie handling with embedded content](https://qlik.dev/embed/iframe/authenticate/third-party-cookie-handling-with-embedded-content).

`embed:./snippets/dims-and-measures/measures/get-master-measures.html`
