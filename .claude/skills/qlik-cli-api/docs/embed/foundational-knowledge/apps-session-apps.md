---
source: https://qlik.dev/embed/foundational-knowledge/apps-session-apps/
last_updated: 2026-03-18T16:49:43Z
---

# Qlik Sense - Apps and session apps

A Qlik Sense app is a container which stores both your application metadata (business
logic, navigation, expressions, etc), and the data upon which the analytics are
performed.

With respect to building embedded solutions, there are two types of Qlik Sense app
you might use:

- Qlik Sense app: This is any Qlik Sense app that is persisted for use by one or
  many users.
- Qlik Sense **session** app: This a temporary Qlik Sense app which is generated for,
  and tied to an individual user's session, and is discarded at the end of that session.

In most cases, standard Qlik Sense apps are the most performant way of serving analytics,
since the generation of a new session app requires a data reload which will cause a
delay in serving those analytics to the user.

## What is a Qlik Sense app?

When exported, a Qlik Sense app is a binary file of type `.QVF`, which contains
both application metadata and your loaded data.

The app will contain content such as:

- Analytics components: sheets, sheet objects such as chart objects, stories,
  bookmarks, snapshots, master items, and other app properties and configuration metadata.
- Data model & business model: data load script, data model view layout, logical model,
  and vocabulary.
- Data: data loaded into the app, which is used to generate the hypercubes for
  analytics, variables, and custom objects.

This data is all portable with this `.QVF` file. Qlik Cloud Analytics builds on this
as the base component, with other services referencing the Qlik Sense app when
generating and returning AI insights, reports, data alerts, and more.

## When might you use a session app?

You might consider using session apps when:

- You need the latest data: as a good practice, you only load data for the current
  user, with fewer than 100,000 rows of data. This helps minimize
  reload duration and delay to the end user.
- You do not wish to persist data for privacy or security reasons.
- You wish to run tests or validation to test specific capabilities.
- You want to draft models or analysis before committing to a persistent app.
- Your users wish to pull custom data sets into apps for ad hoc analysis that won't
  be needed later.

If you have requirements relating to larger data sets, consider exploring capabilities
such as [on demand apps](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/using-OnDemand-apps.htm),
[dynamic views in apps](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DynamicViews/dynamic-views.htm),
or [direct query apps](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/direct-query-apps.htm).

Read about how to implement [session apps](https://qlik.dev/apis/json-rpc/qix#session-apps).
