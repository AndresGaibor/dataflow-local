---
source: https://qlik.dev/embed/nebula/
last_updated: 2026-06-02T18:15:45+01:00
---

# nebula & enigma

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) rather than this framework.

nebula and enigma are the names of two JavaScript frameworks commonly used together for
embedding Qlik Analytics. While enigma provides the connectivity with Qlik Sense and
returns the data, nebula renders this into visual form.

Although usually seen together, they also have value on their own.

You can use nebula for [creating your
own visualization extensions](https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/) or presenting
data from a third party tool.

You can use enigma for anything where you need to
interact with a Qlik Sense app, with visuals from nebula, your own visualization
framework, or any other frameworks.

## nebula.js

nebula.js is a collection of JavaScript libraries, visualizations, and CLI
that helps developers build and integrate visualizations on top of Qlik's
Associative Engine. It can be used for integrating existing visualizations with
web apps as well as for it's primary purpose of building custom visualizations.

### Use cases best suited for nebula.js

- When you want to embed a specific visualization with low overhead.
- When you want to build customized visualizations.
- When you are already building web apps or sites using modern frameworks and want to use Qlik data and
  visualizations.

### nebula.js examples

- [Hello world example](https://qlik.dev/extend/extensions/nebula-js/quickstart/first-extension)
- [Replacing
  existing AngularJS & capability API extensions](https://qlik.dev/extend/extensions/nebula-js/quickstart/migrate-vis-extension-nebula)

## enigma.js

The [enigma.js](https://qlik.dev/toolkits/enigma-js) JavaScript library helps you communicate
with the Qlik Associative Engine in JavaScript environments using engine API abstraction.

enigma-go is a go library with the same capabilities.

Examples of use include building your own browser-based analytics tools, back-end services, or command-line
scripts.

### Prerequisites for using enigma.js

- JavaScript-based framework (browsers and node.js)
- golang for enigma-go

### Use case best suited for enigma.js

- When you want to interact at a "low level" with the engine APIs, but not at the lowest level.

### enigma.js examples

- [Leverage nebula and enigma.js to add analytics to a single page application](https://qlik.dev/embed/nebula/quickstart/build-a-simple-single-page-app)
- [Create a simple web app which retrieves data from Qlik Sense using enigma.js](https://qlik.dev/embed/nebula/quickstart/build-a-simple-web-app)
- [Handle Sheets in iframes with enigma.js](https://qlik.dev/embed/iframe/customize/handle-sheets-in-iframes-with-enigma)
- [Set the theme for embedded iframe content with enigma.js](https://qlik.dev/embed/iframe/customize/set-content-theme-for-iframe-with-enigma)
