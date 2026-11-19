---
source: https://qlik.dev/embed/foundational-knowledge/app-anatomy/analytics-data-model/
last_updated: 2025-07-08T16:09:30Z
---

# Hypercube

Hypercubes in Qlik Sense represent extractions of the data loaded for apps, and
are defined through the HyperCubeDef property. A typical example of such data
is the data needed to display a particular type of visualization object, for
instance a bar chart. Configuration of what the contents of a hypercube should
be mainly consists of defining a set of dimensions that should be observed by
the hypercube, and a set of measures that should be computed based on those
dimensions. The resulting hypercube is a table where the first set of columns
represents dimensions, and the second set of columns represents the measures.
Each row of the table will contain one unique combination of dimension values
along with measures computed as if those dimension values were selected.

> **Note:** Hypercubes are defined through the HyperCubeDef property.

## Using hypercubes for calculations

To use hypercubes for calculations you must first specify valid dimensions and
measures. The dimensions are represented by an array of `NxDimension`. Each
dimension can be set either with `qLibraryId` (string of the dimension ID) or by
setting the field name as a string in `qFieldsDef` in class `NxInlineDimensionsDef`
(`qDef` in `NxDimension`). Now your hypercube is ready to perform calculations.

## Example

```json
"qHyperCubeDef": {
  "qDimensions":[
    {
      "qDef": {
        "qFieldDefs": ["Dim2"]
      }
    }
  ],
  "qMeasures":[
    {
      "qDef": {
        "qDef": "Count(AsciiNum)",
        "qLabel": "Count(AsciiNum)"
      }
    }
  ],
  "qInterColumnSortOrder":[0,1],
  "qInitialDataFetch":[
    {
      "qHeight": 500,
      "qLeft": 0,
      "qTop": 0,
      "qWidth": 0
    }
  ]
}
```
