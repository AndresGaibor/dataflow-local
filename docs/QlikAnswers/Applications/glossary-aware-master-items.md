---
title: "Combining master item descriptions and business glossary terms"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Applications/glossary-aware-master-items.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Best practices for preparing applications for Qlik Answers"]
---

# Combining master item descriptions and business glossary terms

Descriptions and business glossary terms can both provide context for a master item. This topic explains how Qlik Answers combines these inputs when one or both are available.

Before Qlik Answers can answer a question about a master item, it needs to understand what that master item means. It does not rely on the master item name alone. It reads the context you have added to your data model:

- The description on the master item
- The business glossary term definition and synonyms, if the master item is linked to a glossary term

Information noteMaster items and their linked business glossary terms are evaluated at indexing time. If a glossary term's definition changes after the application has been indexed, Qlik Answers does not pick up that update automatically. Reindex the app for the change to take effect.

## What Qlik Answers reads to understand a master item

For a master item (a measure or dimension defined in the application), Qlik Answers looks at up to three sources of meaning:

- Master item description: The free-text description entered directly on the measure or dimension. This is application-specific and is usually written by the application modeler or data developer.
- Linked glossary term definition: If the master item is linked to a term in your business glossary, Qlik Answers reads that term definition. This is governed, cross-application content usually written by a data steward or governance owner.
- Glossary term synonyms: Alternate names listed on the linked glossary term (for example, Revenue and Net Sales).

  Synonyms are always additive. Qlik Answers uses them to recognize alternate phrasing in a question, and they are never dropped or overridden.

Information note

The Related terms field on a glossary term is not used to build a master item meaning. Related terms point to nearby concepts (for example, linking Revenue to Cost and Margin), but the relationship is not defined tightly enough to include in master item interpretation.

## How Qlik Answers combines descriptions and terms

When a master item has both a description and a linked glossary term, Qlik Answers applies the following rules:

Qlik Answers situation for combining descriptions and terms

| Situation | What Qlik Answers does |
| --- | --- |
| Only a description is entered on the master item, and no glossary term is linked. | Uses the description as the master item meaning. |
| No description is entered on the master item, but a glossary term is linked. | Uses the glossary term definition as the master item meaning and adds synonyms as alternate names. |
| Both a description and a linked glossary term exist, and they agree. | Uses the description as the primary master item meaning and adds glossary definition and synonyms as additional context. |
| Both exist, but they describe the master item differently. | Uses the description only and ignores the glossary definition. The mismatch is flagged for review in AI optimization. Synonyms are still added. |

The guiding principle is that the master item description is the primary source of truth, because it is written specifically for that master item in that application. The glossary adds shared business context only when doing so does not create a contradictory meaning.

Information noteOnly glossary terms in Verified state are considered.

## When a description and glossary term disagree

Consider a measure called Luxury Car Count. Its master item description explains that the luxury threshold follows a definition approved by a pricing committee and describes what is included in that count. The same master item is linked to a glossary term called Luxury Car Count, where the definition states that second-hand luxury cars are excluded.

If these statements do not agree on whether second-hand cars are in scope, Qlik Answers does not merge them into a blended definition. Instead, it uses the master item description as the master item meaning.

## Best practices for writing descriptions and glossary terms

Use the following best practices when working with both master item descriptions and business glossary terms with Qlik Answers.

### Master item descriptions

Use the following best practices when writing master item descriptions:

- Write as if you are explaining the master item to a new colleague. Use plain business language, not a description of the formula.
- Call out edge cases explicitly. If the measure includes or excludes something users might assume differently, say so clearly. For example, canceled orders, tax, returns, or specific date ranges.
- If the master item does not need a glossary term, a clear description on its own is sufficient. A glossary link is not required for Qlik Answers to understand a master item.

### Glossary term definitions

Use the following best practices when creating glossary terms:

- Keep the definition focused on the governed business meaning of the term, not on how one application uses it.
- Use the Abbreviation field on a term for its short form. For example, 'BT' for 'Business Technology'. This is separate from synonyms in applications. Each synonym term can have its own abbreviation.
- When a glossary definition changes, review linked master items. If an application description matched the old definition, it can become out of sync.

### Keeping the two in sync

- Treat the description and linked glossary definition as a working pair, not independent fields. If they describe different scopes, Qlik Answers prefers the description and flags the mismatch.
