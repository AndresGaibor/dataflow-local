---
source: https://qlik.dev/embed/iframe/authenticate/csp-iframe-config/
last_updated: 2026-03-18T16:49:43Z
---

# Content security policy for embedding iframes

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> Content security policies are not required when using [qlik-embed with OAuth](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/).

## Overview

Embedding visualizations and Qlik Sense experiences in custom web applications
requires a content security policy (CSP) definition in your tenant. The CSP
configuration instructs your tenant to allow cross-site requests for selected
web-content and protocol types from an external domain.

Content Security Policy (CSP) is a browser mechanism for mitigating and
preventing cross-site scripting (XSS) attacks. Setting a CSP header in the
management console enables Qlik components embedded in external web applications
to render in your web application and work as expected.

If your solution includes embedding Qlik Sense visualizations using iframes, the
tenant hosting the analytic content must have a CSP entry. Here's how to perform
the configuration.

## Configuring Qlik Cloud to allow iframe embedding in your web application

1. Open a web browser and navigate to your Qlik Cloud tenant. Once authenticated
   to your tenant, click the waffle icon and select Management Console.

   ![a screenshot of the management console menu of Qlik Cloud.](https://qlik.dev/_astro/6.E-7psjhr.png)

2. Select Content Security Policy in the Integration section of the side menu.
   Click the Add button on the right side of the screen.

   ![a screenshot of the add configuration button of Qlik Cloud.](https://qlik.dev/_astro/7.DYTda7Rx.png)

3. In the Add origin window, give the entry a name and provide the
   origin for the web application, for example `myembeddedsite.com`). Under the origin,
   select the `frame-ancestors` directive.

   ![a screenshot of the csp configuration screen of Qlik Cloud.](https://qlik.dev/_astro/8.DBv1UoLD.png)

By selecting the `frame-ancestors` directive, the web application with the
iframe tag containing a reference to Qlik Cloud renders the requested content.

## Conclusion

In this tutorial, you learned how to configure content security policy to allow
an iframe referencing content from Qlik Cloud to render in your web
application.

For more information on content security policy in Qlik Cloud, see
[Managing Content Security Policy (CSP)](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)
on Qlik Help.

For more information on content security policy in general, see the
[Content Security Policy (CSP) Quick Reference Guide](https://content-security-policy.com/).
