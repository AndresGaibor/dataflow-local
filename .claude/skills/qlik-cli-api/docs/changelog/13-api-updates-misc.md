---
source: https://qlik.dev/changelog/13-api-updates-misc/
last_updated: 2026-10-26T15:10:16Z
---

# SaaS API Updates 17-sept-2021

### Evaluations API

The Evaluations API now includes a new endpoint `/evaluations/{id}/download`
that allows you to download a detailed XML log for your evaluation. Learn more
about this [here](https://qlik.dev/apis/rest/evaluations#%23%2Fentries%2Fevaluations%2F-id%2Fdownload-get)

### Items API

When fetching items using the Items API, you now have the ability to filter
by three new subtype resources - `automation`, `dataset`, and `dataasset`.
Additionally, if you want to speed up response time, you can now omit the
actions array from the response by setting the `noActionParam` to true.
This ensures that the actions for each item is not evaluated.

### New Natural Language API

The new Natural language API (`/questions/actions/ask`) enables you to ask
questions and context aware partial questions against applications enabled
for conversational analytics or a specific app to receive Insight Advisor
generated responses and suggestions.
Learn more about creating customized conversational analytics interfaces [here](https://qlik.dev/embed/gen-ai/create-chatbot-nl-api).

### Users API

In the User [definition](https://qlik.dev/apis/rest/users#%23%2Fdefinitions%2FUser)
`created`, `lastUpdated` and `roles` fields have been deprecated.

### JSON engine RPC

A new experimental method `Doc.SearchValues` has been added to the Qlik
Associative Engine. For more details read [here](https://qlik.dev/apis/json-rpc/qix/doc/#searchvalues)
