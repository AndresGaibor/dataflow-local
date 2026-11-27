---
title: "Updating the data product in the marketplace"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Marketplace/Updating-the-marketplace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products"]
---

# Updating the data product in the marketplace

When you edit a data product that is already activated to a managed space, the changes remain local to your main data product. To make your edits available to consumers in the marketplace, you must explicitly update the marketplace.

## Updating the marketplace

Changes to the main data product are not automatically published to the marketplace copy. You must explicitly update the marketplace to sync your changes.

Updating a data product in the marketplace can also be performed through the corresponding [Qlik Public API](https://qlik.dev/apis/rest/data-governance/data-products/#patch-api-data-governance-data-products-dataProductId).

The pending changes indicator appears on the data product overview when you have unpublished changes. It displays the number of changes (for example, "3 changes") that are staged locally but not yet in the marketplace.

The pending count resets to zero after you update the marketplace.

**Main data product vs. marketplace copy:** Your main data product is editable. The copy in the marketplace is read-only from the consumer perspective. When you update the marketplace, your changes sync to that marketplace copy.

Prerequisites:

- Your data product must be activated to a managed space.
- You must have edit permission on the main data product space.
- You must have publish permission on the managed space where the data product is activated.

1. In the data product Overview, click the pending changes indicator on the left. It shows "N changes" when you have unpublished changes.
2. Review the changes.
3. To apply the changes, you can either:

   - Click Update in marketplace in the changelog.
   - Or close the changelog and click Update in marketplace on the right.

   There is no confirmation dialog. The update applies immediately.

The marketplace copy is updated with your changes and consumers can access the updated data product details and new datasets or fields.

The applications using the data product can access the new fields and datasets on their next data reload.

When you receive a permission error, you may lack publish permission on the managed space. Contact your workspace administrator to verify you have the required permission, or ask an administrator to update the marketplace on your behalf.
