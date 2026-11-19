---
source: https://qlik.dev/changelog/72-qlik-embed-release/
last_updated: 2024-08-01T13:17:48+01:00
---

# Use qlik-embed to integrate Qlik into your web applications

qlik-embed is Qlik’s new library for embedding data and analytics UI with
confidence and ease. Browsers like Chrome and Safari are making it more complex
to embed content from one software application to another, and you are encouraged to
use qlik-embed to keep pace with evolving privacy and security standards.

With a simple script defining how you want to connect to Qlik, you can embed
content from Qlik applications using web-components as easily as this:

```html
<qlik-embed
  id="visualization"
  ui="analytics/chart"
  app-id="<Qlik Sense Application ID>"
  object-id="<Chart object ID>"
></qlik-embed>
```

You can also take advantage of a framework like React:

```javascript
import { QlikEmbed } from "@qlik/embed-react";
<QlikEmbed ui="analytics/chart" appId={appId} objectId={objectId} />
```

Learn more about embedded analytics for the modern
web here, or
explore the reorganised embed section, which
makes it easier to find content for your framework of choice.

If you'd like to jump into a real example, check out
this quickstart.
