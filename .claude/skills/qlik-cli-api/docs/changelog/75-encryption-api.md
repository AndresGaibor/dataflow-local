---
source: https://qlik.dev/changelog/75-encryption-api/
last_updated: 2025-07-08T16:09:30Z
---

# The Encryption API is changing to support only multi-region keys for Customer Managed Keys (CMK)

Qlik offers customers the ability to encrypt their tenants with their own
key. The [Encryption API](https://qlik.dev/apis/rest/encryption)
provides you with the ability to deploy, manage, and cycle encryption keys on
one or more Qlik Cloud tenants via supported providers.

In the [initial release of the Encryption API](https://qlik.dev/changelog/62-encryption-api/),
the API supported both single and multi-region Key Management Service (KMS) keys.

Multi-region keys support Disaster Recovery Processes. Tenants configured with a
single-region key will not operate if Qlik Cloud is cut over to a DR region, therefore
Qlik is removing support for single-region keys for new CMK providers. If
you are currently using a single-region key, Qlik recommends that you create a multi-region
key to seamlessly use your tenant in a back-up region in
case of an outage in your primary region.

In no sooner than 30 days from the date of this post, new CMK provider configurations will
require a multi-region key. Existing single-region CMK configurations will not be impacted.
