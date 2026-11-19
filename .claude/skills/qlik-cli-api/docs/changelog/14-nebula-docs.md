---
source: https://qlik.dev/changelog/14-nebula-docs/
last_updated: 2026-06-02T18:15:45+01:00
---

# nebula.js updates

### Nebula Documentation

Nebula CLI is the main entry point to start making a nebula
visualization, enabling a local development server, and building extensions and
mashups.

The Nebula CLI now has updated and detailed documentation updates specifically
on the following

## Nebula serve

Allows to run a nebula visualization with a local web development server.

`nebula serve`

For more details read [here](https://qlik.dev/extend/extensions/nebula-js/set-up-nebula-environment/nebula-serve)

## Nebula build

Used to build a nebula visualization bundle.

`nebula build`

Read more [here](https://qlik.dev/extend/extensions/nebula-js/deploy-extension/nebula-build)

## Nebula sense

Used to generate Qlik Sense specific files to use a nebula visualization as
an extension.

`nebula sense`

Learn more about this [here](https://qlik.dev/extend/extensions/nebula-js/deploy-extension/nebula-sense)

### Nebula Charts

While nebula.js provides capabilities & APIs to build mashups and custom
visualizations, it's primary purpose is often to display Qlik developed charts.
These charts are available through npm under the @nebula.js scope. Learn more
about it \[here].

## Core packages

The new core build allows to significantly reduce the size of bundle, thus
bringing down the overhead of downloading large amount of codes to be run.
Refer to an example [here](https://github.com/qlik-oss/nebula.js-examples/tree/main/examples/simple-setup)

### Nebula API

nebula.js API has the following new updates:

## new useEmbed hook

The useEmbed hook allows access to the Nebula instance inside a chart, for
adding charts into charts. Read the API specs.

## new useKeyboard hook

The useKeyboard hook enables mashups to do sense-client style keyboard
navigation across chart objects. Read the API specs.

## new option for Field-listbox

You can now alter property definition for Field-listbox.
