---
source: https://qlik.dev/changelog/228-qlik-embed-insights-feed-cards/
last_updated: 2026-06-18T19:53:37+01:00
---

# New insights/feed-cards UI for qlik-embed

You can now embed insight feed cards in your web application using the
`insights/feed-cards` UI in qlik-embed. Powered by the
[Discovery Agent](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/discovery-agent.htm),
this new UI renders a scrollable list of insight feed cards for the signed-in user, with
optional app filtering and app navigation handling.

Configure visibility of the "View source" action with `show-source`, or intercept app navigation
events with `intercept-app-navigation` to handle custom navigation logic in your host application.
The "View source" action automatically opens the app in the correct tenant based on your
authentication context, supporting both OEM and multi-tenant scenarios.

For more information, refer to [UIs and
parameters](https://qlik.dev/embed/qlik-embed/parameters/#insightsfeed-cards) or [Analyzing Discovery Agent
feeds](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/feeds.htm)
in Qlik Help.
