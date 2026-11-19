---
source: https://qlik.dev/changelog/87-qlik-api-introduction/
last_updated: 2025-07-08T16:09:30Z
---

# qlik/api 1.0.0 release

`@qlik/api` is a collection of javascript modules which each exposes an api
built to make the integration process for javascript solutions as easy as
possible. The library is built for both browser and NodeJS usage and will
seamlessly integrate with qlik-embed libraries.

`@qlik/api` provides Qlik Cloud REST endpoints and access to the Qlik Analytics
Engine (QIX).

## REST

`@qlik/api` REST interfaces are generated from open-api specifications released
from those Qlik Cloud services that exposes a restful API. The code generation
tool runs using the specs, building typescript for all api calls documented in
the specification. One module per api is generated.

You can learn more about the available modules in
the [REST](https://qlik.dev/toolkits/qlik-api/rest/) section
of the typescript types repository on
[Qlik Open Source](https://github.com/qlik-oss/qlik-api-ts).

## QIX

Qlik's Analytics Engine Service (QIX) is the runtime service for Qlik Sense
applications and several analytics services in Qlik Cloud. `@qlik/api` offers a
fully typed api for connecting to and consuming Qlik Sense Applications
including "Qlik Sense mixins" which previously only was used internally by
in-house Qlik developers.

More info about QIX can be found in
the [qix](https://qlik.dev/toolkits/qlik-api/qix/) section.

Learn more about `@qlik/api` in the [toolkits](https://qlik.dev/toolkits/qlik-api/) section.
