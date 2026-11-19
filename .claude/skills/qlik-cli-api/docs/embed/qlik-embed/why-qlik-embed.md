---
source: https://qlik.dev/embed/qlik-embed/why-qlik-embed/
last_updated: 2026-01-16T09:28:04Z
---

# Why qlik-embed

## Introduction

In this post, you are going to learn about qlik-embed, Qlik's library for
embedding data and analytics user interfaces into your own web applications.

As browser makers introduce new privacy and security features into their
browsers, embedding content from one software application to another has become
more complex. You must consider third-party cookies, cross-site request
forgery, content security policy, and other concerns before
the visualization you want to place inside your application will render
successfully.

With qlik-embed, the intent is to resolve these concerns in advance so that you
can embed analytics into your web applications with confidence and ease.

Use Qlik Cloud, or Qlik Sense Enterprise client-managed May 2024 release or later
with qlik-embed.

The guiding principles for qlik-embed are:

- A first-class component of a unified front-end core architecture ensuring
  embedded solutions do not break when core product features change.
- Make it easy to embed any Qlik UI in a world wide web without iframes.
- Mitigate authentication complexity by providing ways to embed content without
  introducing third-party cookie issues.

## Why qlik-embed

Qlik-embed is designed to work with applications written in plain HTML to more
robust frameworks like React and Svelte. In fact, no matter which qlik-embed
library you choose the configuration options will be the same, the methods and
properties will be same. The only differences will be those inherent in the
framework you use to implement qlik-embed into your application.

Using qlik-embed web components is an improvement over iframes in several key
ways:

1. qlik-embed allows you to configure the properties of the content you're
   embedding. Iframes don't offer configuration options unless they are driven by
   parameters in the source URL.
2. qlik-embed supports modern auth strategies like OAuth2, mitigating
   third-party cookie and cross-site scripting issues between web applications.
   Iframes rely on cookies to render content, a method browser makers are actively
   making harder to do.
3. qlik-embed provides access to the API of the embedded content so you can work
   with the code underneath to enrich the parent web page. Iframes do not support
   this capability without hacks and workarounds.

## Why qlik-embed over Capability API or nebula.js

If you're already embedding Qlik into your web applications and enterprise
solutions, here are more reasons why you're going to want to switch to qlik-embed.

1. qlik-embed is entity-based, so no matter in which framework qlik-embed
   becomes available, it will work with the same properties, methods, and
   capabilities without tweaks, workarounds, or hoops to jump through. qlik-embed
   is available as a web-component (@qlik/embed-web-components), React library
   (@qlik/embed-react), and Svelte library (@qlik/embed-svelte), with Vue and
   Angular support planned.

2. You don't have to deal with RequireJS anymore if you move from Capability API.

3. If you use nebula.js to embed visualizations, qlik-embed removes all the
   chart and component loading, reduces the number of lines of code needed to embed
   an object, and does it using less memory. With qlik-embed handling embedding
   duties, nebula.js can focus on being the library for creating and extending
   visualizations for Qlik Analytics.

4. qlik-embed replaces Nebula by using it under the covers
   to render content, so you don't have to learn multiple embedding libraries or
   make trade-offs in which library to implement because of restrictions or
   limitations.
