---
title: "Managing Content Security Policy ( CSP )"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system"]
---

# Managing Content Security Policy (CSP)

Control and manage your Content Security Policy (CSP) in Qlik Cloud to reduce the risk of security threats such as cross-site scripting (XSS) and data injection attacks.

Qlik Cloud uses Content Security Policy (CSP) Level 2. CSP provides an additional layer of security by restricting which external resources can be loaded by applications, extensions, and themes. By limiting allowed origins and resource types, CSP helps prevent malicious code execution, data theft, site defacement, and malware distribution.

Administrators with the required permissions can use CSP to control which external resources extensions and themes are allowed to load. If an extension or theme requests resources from external origins, these origins must be explicitly added to the CSP allowlist.

For more information about CSP, see [MDN Web Docs: Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP).

## Required permissions

To manage Content Security Policy entries, you must have one of the following:

- The Tenant Admin role
- A custom role that includes the Admin CSP permission

## Directives

Directives define which sources are allowed for specific types of resources. The following directives are supported:

CSP directives

| Directive | Description |
| --- | --- |
| child-src | Defines valid sources for web workers and nested browsing contexts loaded using elements such as <frame> and <iframe>. Use frame-src and worker-src for more specific control. |
| connect-src | Restricts the URLs that can be loaded using script interfaces. |
| font-src | Specifies valid sources for fonts loaded using @font-face. |
| form-action | Restricts the URLs that can be used as the [target](#glossary-0 "Glossary term") of submissions from a given context. |
| frame-ancestors | Specifies valid sources for embedding the resource using <frame>, <iframe>, <object>, <embed>, and <applet> elements. |
| frame-src | Specifies valid sources for nested browsing contexts using elements such as <frame> and <iframe>. |
| img-src | Specifies valid sources of images and favicons. |
| media-src | Specifies valid sources for loading media using the <audio>, <video>, and <track> elements. |
| object-src | Specifies valid sources for the <object>, <embed>, and <applet> elements.  Elements controlled by object-src are considered legacy HTML elements and are not receiving new standardized features, such as the security attributes sandbox or allow for <iframe>. It is recommended to restrict this fetch-directive where possible, for example by setting object-src 'none'. |
| script-src | Specifies valid sources for JavaScript. |
| style-src | Specifies valid sources for stylesheets. |
| worker-src | Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts. |

## Qlik Cloud default CSP

Qlik Cloud includes a default Content Security Policy with a set of allowlisted domains. Resources from these domains can be used without adding CSP entries.

Examples include:

- \*.qlikcloud.com – core Qlik Cloud services and APIs
- cdn.pendo.io – notification content
- gravatar.com – user profile icons

For a complete list, see [*Allowlisting domains and IP addresses*](../Introduction/qlik-cloud-dns-ip.htm).

## CSP entries and header limits

The following limits are built in and cannot be changed. If you reach either limit, remove redundant or unused CSP entries.

- Maximum number of CSP entries: 256 entries per tenant
- Maximum CSP header length: 6,144 characters

## Creating a CSP entry

Do the following:

1. In the Administration activity center, go to Content Security Policy.
2. Click Add.
3. Provide a name.
4. Enter the origin in one of the following formats:

   - domain.com
   - \*.domain.com

   Information noteQlik Sense enforces HTTPS for CSP entries.
5. Select the applicable directives.
6. Click Add.

Users must refresh their browser for the changes to take effect.

## Editing a CSP entry

Do the following:

1. In the Administration activity center, go to Content Security Policy.
2. Find the CSP entry you want to edit, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and select Edit.
3. Change the CSP options as needed.
4. Click Save.

Users must refresh their browser for the changes to take effect.

## Deleting a CSP entry

Do the following:

1. In the Administration activity center, go to Content Security Policy.
2. Select the CSP entries you want to remove and click Delete.
3. Confirm the deletion.

## Viewing and copying the CSP header

Do the following:

1. In the Administration activity center, go to Content Security Policy.
2. Click View header.
3. In the dialog, click Copy to clipboard.
4. Click Done.
