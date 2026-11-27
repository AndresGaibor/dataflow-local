---
title: "Visualizing positive and negative contributions to the result with a waterfall chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WaterfallChart/waterfall-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating waterfall charts"]
---

# Visualizing positive and negative contributions to the result with a waterfall chart

This example shows how to make a waterfall [chart](#glossary-0 "Glossary term") to visualize how positive and negative values contribute to the final result.

We want to see the positive contributions to CO2 in the atmosphere, such as oil or gas, in relation to negative factors, such as land sink.

![Waterfall chart showing positive and negative contributions to CO2](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_waterfall_CO2.png)

## Dataset

In this example, we will use a simple [dataset](#glossary-1 "Glossary term") that you can copy to a text file to use as data source. It contains the atmosphere CO2 level in ppm from 1870, as well as the positive and negative contributors to CO2 in the atmosphere in the time between 1870 and 2017.

```
Atmosphere 1870,Coal,Oil,Gas,Cement,Land,Imbalance,Land sink,Ocean sink,Atmosphere 2017
288,94,72,31,5,88,-12,-89,-72,405
```

(Source: CDIAC/GCP/NOAA-ESRL/UNFCCC/BP/USGS)

Add the text file as data source in an empty application and load the data. Make sure that you use comma as field delimiter.

## Visualization

We add a waterfall chart to the [sheet](#glossary-3 "Glossary term") and add the fields as [measures](#glossary-4 "Glossary term") in the following order. Edit the label for each measure to remove the Sum() part.

- Sum(Atmosphere1870)
- Sum(Coal)
- Sum(Oil)
- Sum(Gas)
- Sum(Cement)
- Sum(Land)
- Sum(Imbalance)
- Sum(Land\_sink)
- Sum(Ocean\_sink)

To add a bar that shows the calculated result, the CO2 level for 2017, open the final measure and select Subtotals in the [properties](#glossary-5 "Glossary term") panel.
You can set Subtotal label to Atmosphere 2017.

![Waterfall chart showing positive and negative contributions to CO2](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_waterfall_CO2.png)

## Discovery

As you can see in the chart, the CO2 level in the atmosphere is higher in 2017 than in 1870. Coal is the main contributor of CO2. Some of the increase is offset by carbon sinks that absorb CO2, for example, the ocean. As we can see, this is unfortunately not enough to stop the increase of CO2 in the atmosphere
