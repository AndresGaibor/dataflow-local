---
source: https://qlik.dev/changelog/20-api-updates-nebula-engine/
last_updated: 2026-10-26T15:10:16Z
---

# SaaS API Updates 24-Feb-2022

### Engine RPC

Two new methods are added to the Engine RPC.

- `GetFieldsResourceIds` that returns a list of resource ids (QRI) for fields
  that belongs to the data model. Key fields (that belongs to multiple tables),
  returns one resource identifier per table. Read more [here](https://qlik.dev/apis/json-rpc/qix/doc/#getfieldsresourceids)
- `GetFieldsFromExpression` that retrieves any fields from an expression.
  Learn more about this [here](https://qlik.dev/apis/json-rpc/qix/doc/#getfieldsfromexpression)

### nebula.js updates

The nebula stardust package now comes with TypeScript definitions. It
references the Qlik's Engine definitions published at @types/qlik-engineapi.
This will enable developers to take advantage of code autocompletion, verifying
correct types, etc. within modern IDE's.

![a screenshot of autocompletion in VS code](https://qlik.dev/_astro/auto.Ckf8FlQ5.png)

![a screenshot showing types in VS code](https://qlik.dev/_astro/types.D_fc2568.png)
