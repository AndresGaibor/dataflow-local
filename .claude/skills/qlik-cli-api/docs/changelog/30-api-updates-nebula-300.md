---
source: https://qlik.dev/changelog/30-api-updates-nebula-300/
last_updated: 2026-10-26T15:10:16Z
---

# Nebula Updated

## Nebula version 3.0

The 3.0 version of Nebula has been released. It contains bug fixes,
dependency updates and a few new features. Below are select updates since version 2.0

### v3.0

- Minor bugfixes and dependency updates.

- Updated to internally use material UI v5 and React 18.

  - Breaking change for users of stardust/core [source repository](https://github.com/qlik-oss/nebula.js/tree/master/apis/stardust/core)
    In npm package [npm package](https://www.unpkg.com/browse/@nebula.js/stardust@2.12.0/core/)

  - Still compatible with React 17.

- Enigma Mocker:

  - New experimental API that allows examples and tests to run without a Qlik Sense Engine
    You can see source and documentation [here](https://github.com/qlik-oss/nebula.js/tree/master/apis/enigma-mocker)

- Improved support for qListObject in Nebula serve dev environment.

  - Supernovas/Extensions using qListObject data works better with automated property panel.

- Updated visualizations.
  New charts have been added and feature updates made to others. For instance:
  - See [New Nebula Map](https://qlik.dev/embed/visualizations-to-embed/map/sn-map)
  - and [Pivot table](https://qlik.dev/embed/visualizations-to-embed/pivot-table/sn-pivot-table)
  - See more [here](https://qlik.dev/extend/extensions/extension-api/build-extension/visualization).

### More Options

- v2.5: DisableCellPadding: reduces padding around visualizations [see here](https://qlik.dev/apis/javascript/nebula-js/#definitions-context)

- Listbox: [see here](https://qlik.dev/apis/javascript/nebula-js/#definitions-fieldinstance)
  - v2.6: dense: reduces padding and text size
  - v2.7: frequencyMode: Shows frequency count of values
  - v2.9: checkboxes: Shows values as checkboxes.

### Typescript Support

- v2.4: Typescript support
  - Nebula now comes with defined types and the build command now supports visualizations
    that use typescript.

Read more [here](https://qlik.dev/extend/extensions/nebula-js/deploy-extension/nebula-build/)
