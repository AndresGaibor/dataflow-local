---
source: https://qlik.dev/embed/iframe/quickstart/app-integration-getting-started/
last_updated: 2025-07-08T16:09:30Z
---

# Set default options for embedded applications from the URL

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> To do something similar with qlik-embed, refer
> to [qlik-embed UIs and parameters](https://qlik.dev/embed/qlik-embed/parameters/),
> in particular the `classic/app` UI.

## Introduction

The App Integration API is a URL based embedding method that accepts parameters
in the URL path for default selections, bookmarks, and more. Here are some
different ways you can use the App Integration API to control the behavior of
an embedded Qlik Cloud Analytics application.

## Requirements

- A Qlik Cloud tenant
- A web application hosted on an external domain
- A content security policy entry for embedding an iframe in your
  web application. For more information, see [Content security policy for embedding iframes](https://qlik.dev/embed/iframe/authenticate/csp-iframe-config).
- A web integration ID entry to allow your web application domain
  to access Qlik Cloud. For more information, see [Managing web integrations](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm)
  on Qlik Help.

## App integration examples

These examples use the App Integration API.

### Integrating app

This example integrates the Qlik Sense demo app "Sales Discovery" (`appid=4d541aea-a8b1-4cef-a4c2-6bda620321a9`).

Example: iframe integration

```html
<iframe src="https://<TENANT_URL>/sense/app/4d541aea-a8b1-4cef-a4c2-6bda620321a9"/>
```

### Integrating sheet

This example integrates the Qlik Sense demo app "Sales Discovery" with sheet
"Performance Dashboard" (sheetid=XuWLHFK).

Example: iframe integration

```html
<iframe src="https://<TENANT_URL>/sense/app/4d541aea-a8b1-4cef-a4c2-6bda620321a9/sheet/XuWLHFK/state/analysis"/>
```

### Integrating app with bookmark

This example integrates the Qlik Sense demo app "Sales Discovery" with bookmark
"Sales Rep Name" (bookmarkid=UCVp).

Example: iframe integration

```html
<iframe src="https://<TENANT_URL>/sense/app/4d541aea-a8b1-4cef-a4c2-6bda620321a9/sheet/XuWLHFK/state/analysis/bookmark/UCVp"/>
```

### Integrating app with single selection

This example integrates the Qlik Sense demo app "Sales Discovery" selecting the
Region Name "International" on the "Transactions" sheet (sheetid=zBAFH).

Example: iframe integration

```html
<iframe src="https://<TENANT_URL>/sense/app/4d541aea-a8b1-4cef-a4c2-6bda620321a9/
sheet/zBAFH/state/analysis/select/Region Name/International"/>
```

### Integrating app with numeric value selections

> **Note:** For selections containing numeric values and search terms, the text representation should be added within square
> brackets, as in \[value1].

This example integrates the Qlik Sense demo app "Sales Discovery" selecting the
Month "Feb" which has a numeric value "2" on the "Transactions" sheet (sheetid=zBAFH).

Example: iframe integration text representation

```html
<iframe src="https://<TENANT_URL>/sense/app/4d541aea-a8b1-4cef-a4c2-6bda620321a9/sheet/zBAFH/state/analysis/select/Month/[Feb]/"/>
```

You can also define the numeric value instead of the text representation value,
and the result will be the same.

Example: iframe integration numeric value

```html
<iframe src="https://<TENANT_URL>/sense/app/4d541aea-a8b1-4cef-a4c2-6bda620321a9/sheet/zBAFH/state/analysis/options/clearselections/select/Month/2"/>
```

### Clearing previous selections in an app

You may want to clear all selections in the app before applying your own
selections. To do so, add option parameter clearselections.

Example: iframe integration

```html
<iframe src="https://<TENANT_URL>/sense/app/4d541aea-a8b1-4cef-a4c2-6bda620321a9/
sheet/zBAFH/state/analysis/options/clearselections/select/Region Name/International"/>
```

### Integrating app with multiple selections

This example integrates the Qlik Sense demo app "Sales Discovery" with the
following selections made on the "Top Customers" sheet (sheetid=JTxTF).

Year: 2014
Region Name: Canada and International
The option parameter `clearselections` is also included to clear all previous
selections in the app before applying the selections.

Example: iframe integration

```html
<iframe src="https://<TENANT_URL>/sense/app/4d541aea-a8b1-4cef-a4c2-6bda620321a9/sheet/XuWLHFK/state/
analysis/options/clearselections/select/Year/2014/select/Region Name/International;Canada"/>
```
