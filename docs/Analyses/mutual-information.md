---
title: "Mutual information analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/mutual-information.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Mutual information analysis

Detect and show key driver analysis between the a field and potential driver fields.

Mutual information shows the statistical measurement of the dependency between a target (the first selected dimension) and up to 10 other fields.

Mutual information analyses creates a measure of certainty between pairs of values using a machine learning algorithm that applies random data distributions.

Mutual information selects one field (measure or dimension) as the target and then selects 1 to 10 dimensions or measures as drivers. Results for this analysis type for the same fields or selections might vary due to the random data selection.

The dependency indicator ranges between 0 percent (no dependency) and 100 percent(strong dependency).

Mutual information analysis

![Mutual information analysis, showing the mutual dependency between City and Cost of Sale as 75.34%](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-mutual-information.png "Click to view full size")

Mutual information does not necessarily indicate causality between fields sharing mutual information. Two fields may share mutual information, but may not be equal drivers for one another. For example, when comparing ice cream sales and outdoor temperature, a mutual information analysis will show mutual information between the two. It will not indicate if it is outdoor temperature driving ice cream sales, which is likely, or if it is ice cream sales that drives outdoor temperature, which is unlikely.

## Creating mutual information analyses

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Mutual information into the sheet.
3. Click Add dimension and select a target field for mutual information analysis.
4. Click Add dimension and a select a second field as the driver for mutual information analysis.
5. Optionally, add additional drivers. In the properties panel, under Data, click Add and select another dimension.

   You may have a total of 10 drivers.
6. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
