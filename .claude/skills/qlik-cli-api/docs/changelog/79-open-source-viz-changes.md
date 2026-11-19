---
source: https://qlik.dev/changelog/79-open-source-viz-changes/
last_updated: 2024-02-20T10:32:09Z
---

# Nebula visualization libraries are returning to closed source

> **Note:** This changelog was updated on February 20, 2024 to clarify the customer impact of
> this change.

Qlik regularly reviews the resources offered to platform developers to help them
build better solutions with Qlik Products, and has identified low usage of the
open source nebula.js and mobile visualization libraries.

These libraries were originally published to foster collaboration
and engagement with developers as they customized or developed visualizations, but
due to customer feedback and usage data, these will be moved back to closed source.
Moving these projects back to closed source will support
better integration with internal build and test tooling, and free up resources
for investment in these and other visualizations.

No sooner than 30 days from the date of this notice, Qlik will stop updates to
the following repositories, and set them as archived:

- [carbon-core](https://github.com/qlik-oss/carbon-core/)
- [dist-flow](https://github.com/qlik-oss/dist-flow/)
- [react-native-carbon](https://github.com/qlik-oss/react-native-carbon)
- [react-native-helium](https://github.com/qlik-oss/react-native-helium)
- [react-native-simple-grid](https://github.com/qlik-oss/react-native-simple-grid)
- [sn-action-button](https://github.com/qlik-oss/sn-action-button)
- [sn-container](https://github.com/qlik-oss/sn-container)
- [sn-list-objects](https://github.com/qlik-oss/sn-list-objects)
- [sn-map](https://github.com/qlik-oss/sn-map)
- [sn-mekko-chart](https://github.com/qlik-oss/sn-mekko-chart)
- [sn-network-chart](https://github.com/qlik-oss/sn-network-chart)
- [sn-org-chart](https://github.com/qlik-oss/sn-org-chart)
- [sn-scatter-plot](https://github.com/qlik-oss/sn-scatter-plot)
- [sn-treemap](https://github.com/qlik-oss/sn-treemap)
- [sn-word-cloud](https://github.com/qlik-oss/sn-word-cloud)

The following repositories were previously archived:

- [sn-pivot-table](https://github.com/qlik-oss/sn-pivot-table)
- [sn-table](https://github.com/qlik-oss/sn-table)

Although Qlik will no longer accept community contributions to these repositories,
the consumption of these libraries and components remains unchanged. Customers
should continue to leverage the NPM packages for each component for use in their
web apps. Existing integrations using these NPM packages will not be impacted by
this change.

Any issues found while using the NPM packages should be raised
via [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).
