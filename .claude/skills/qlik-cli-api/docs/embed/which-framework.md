---
source: https://qlik.dev/embed/which-framework/
last_updated: 2026-03-18T16:49:43Z
---

# Which framework

## Introduction

A number of different web technologies exist for embedding Qlik Cloud content
into a web app. It's recommended to use qlik-embed, although there may be requirements
relating to your use case, available frameworks, and your level of familiarity with
the technology that make another framework more suitable.

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) for your solution, as it provides most of the capabilities of
> iFrame, capability API, and nebula/enigma embedding in a single package, while handling for modern authentication,
> more modern web frameworks, and more.

This guide explores the different integration options and highlights why some
may be a better fit for your deployment.

| Framework                                                 | Purpose                                                                                                                                  | Flexibility |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [qlik-embed](https://qlik.dev/embed/qlik-embed/)          | Embed whole analytics sheets, objects, non-analytics experiences, and also interact with base APIs in a simple wrapper                   | High        |
| [iFrame](https://qlik.dev/embed/iframe/)                  | Embed whole analytics sheets or whole objects                                                                                            | Low         |
| [Capability APIs](https://qlik.dev/embed/capability-api/) | Embed and interact with Qlik Sense app models                                                                                            | Medium      |
| [Nebula / Enigma](https://qlik.dev/embed/nebula/)         | Pro-code method for embedding and interacting with Qlik Sense apps                                                                       | High        |
| [REST APIs](https://qlik.dev/apis/)                       | Adding experiences which aren't present in a framework, such as reports, data alerts, generated AI insights, and more via base REST APIs | High        |

## qlik-embed

**Level of complexity**: Simple to Advanced, use case dependent

Qlik's primary embedding framework, [qlik-embed](https://qlik.dev/embed/qlik-embed/),
simplifies embedding of
Qlik technologies, while also increasing the potential breadth and depth of
your integrations.

qlik-embed works with applications written in plain HTML through to frameworks
like React and Svelte. No matter which qlik-embed library you choose, the
configuration options will be the same, the methods and
properties will be the same. The only differences will be those inherent in the
framework you use to implement qlik-embed into your application.

> **Note:** Fonts from a custom theme are not supported when embedding Qlik objects cross-domain unless you use
> `<qlik-embed iframe="true">`. Using the `iframe="true"` mode may impact performance.

### Use cases best suited for qlik-embed

- Majority of use cases, since qlik-embed wraps nebula, as well as providing
  a native iframe experience via certain UI modes.
- Want to solve for third party cookies and browser controls out of the box.
- Low code sheet embed through to single object and calls into the app model,
  within a single framework.

## iFrame

**Level of complexity**: Simple

iFrame embedding allows sheets or objects to be integrated into web apps and portals, often without
the need for any JavaScript or other code. You only need an `iframe` tag, which can be generated on
any Qlik Sense page using the [App Integration API](https://qlik.dev/apis/javascript/app-integration/)
(for whole sheets), or [Single Integration API](https://qlik.dev/apis/javascript/single-integration/) (for
single objects).

The App Integration API provides parameters that can be used to create a URL that returns a complete
HTML page containing the embedded app. For more information, see the
[Set default options for embedded applications from the URL guide](https://qlik.dev/embed/iframe/quickstart/app-integration-getting-started).

With the Single Integration API, you can integrate single Qlik Sense visualizations, sheets, or snapshots
into an iFrame. For more information, see the
[Embed single objects using iframes and the Single Integration API guide](https://qlik.dev/embed/iframe/quickstart/single-integration-getting-started/).

While iFrames are often considered the simplest solution, they are flexible, and can even be used with
anonymous use cases when deployed in conjunction with other services or APIs. They can also be used with
other Qlik integration tools such as enigma.js to do things like setting themes within an iFrame.

### Use cases best suited for iFrames

- Where solution won't be affected by third-party cookie blocking.
- Want more native Qlik capability (sheets, data alerts, etc.).
- For non-technical users, requires low code.
- Quick embedding into a web page where security controls for content are lax.
- Framework isolation is required (for example, the parent page is using Angular \< v2).

## Capability APIs

**Level of complexity**: Intermediate

The [Capability APIs](https://qlik.dev/apis/javascript/capability) are a collection
of JavaScript APIs
that allow you to embed Qlik Sense content into a web app or portal. With just a few lines of code, it
is possible to create a visualization that leverages the Qlik Sense visualization library. You can even
interact with the engine to return data and metadata from an application.
See [Capability APIs](https://qlik.dev/embed/capability-api/)
for an overview and examples.

### Use cases best suited for Capability APIs

- When you want to customize the Qlik experience to match your user interface.
- When you want to customize the layout of Qlik objects without the overhead of multiple iFrames.
- When you want to interact with Qlik directly, that is, without going through visualizations.
- When you want to access the Qlik Sense client without using the Qlik Sense UI, that is,
  the selection model.

## nebula.js

**Level of complexity**: Intermediate/Advanced

nebula.js is a collection of JavaScript libraries, visualizations, and CLI
that helps developers build and integrate visualizations on top of Qlik's
Associative Engine. It can be used for integrating existing visualizations with
web apps as well as for building custom visualizations.

### Use cases best suited for nebula.js

- When you want to embed a specific visualization with low overhead.
- When you want to build customized visualizations.
- When you are already building web apps or sites using modern frameworks and want to use Qlik data and
  visualizations.

## enigma.js

**Level of complexity**: Advanced

The [enigma.js](https://qlik.dev/toolkits/enigma-js) JavaScript library helps you communicate
with the Qlik Associative Engine in JavaScript environments using engine API abstraction.

enigma-go is a go library with the same capabilities.

Examples of use include building your own browser-based analytics tools, back-end services, or command-line
scripts.

### Use cases best suited for enigma.js

- When you want to interact at a "low level" with the engine APIs, but not at the lowest level.
