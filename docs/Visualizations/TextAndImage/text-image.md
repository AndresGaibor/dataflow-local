---
title: "Text & image"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/TextAndImage/text-image.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Legacy"]
---

# Text & image

The text & image [visualization](#glossary-0 "Glossary term") complements other visualizations by offering options to add text, images, hyperlinks, and [measures](#glossary-1 "Glossary term").

You can format and color the text and align the paragraphs. The background image has sizing and positioning options. You can also set the responsive behavior for text and images.

## When to use the text & image visualization

The text & image visualization is intended for presentation purposes, and does not support [selections](#glossary-2 "Glossary term"). However, the measures in the text & image visualization are updated when selections are made. Some typical uses:

- Use it on the first sheet of an application for essential information.
- Display a company image, or use a background image together with formatted text and measure values to present figures in a compelling way.
- Link to sites with additional information.
- Use the responsive behavior to ensure that the visualization renders well on all devices.

### Advantages

The text & image visualization contrasts with the other visualizations. You have many options for making the text & image visualization stand out next to more regular [charts](#glossary-3 "Glossary term").

### Disadvantages

You are limited to a few measure values and rather short texts, otherwise the text & image visualization will be cluttered.

## Mobile limitations

In the Qlik Analytics mobile app, the text & image visualization is a natively rendered visualization. Natively rendered visualizations have better performance compared to visualizations rendered in WebView. If a natively rendered visualization is wrapped inside a Container object, it will be rendered in an embedded WebView.

While natively rendered visualizations have greater performance, they do not support the full breadth of object styling (general styling or theme-based styling) when viewed in the Qlik Analytics mobile app. If styling of objects is important for mobile analysis, the application developer can place the object inside a Tab container, Container, or Layout container. This forces the WebView presentation and preserves styling.

## Learn more

- [*Creating text & image objects*](create-text-image-objects.htm)
