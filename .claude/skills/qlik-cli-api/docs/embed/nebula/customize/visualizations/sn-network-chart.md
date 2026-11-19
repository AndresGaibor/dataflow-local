---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-network-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating Network charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The network chart lets you draw a network of
connected nodes and edges from a specific
type of data set. A network chart shows how
information flows, how components interact,
and where components exist in the network.
The network chart is included in the Visualization bundle.

Learn more about the [network chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [network chart API specification](https://qlik.dev/apis/javascript/sn-network-chart/).

![network chart example](https://qlik.dev/_astro/sn-network-chart.0acHn_A5.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "qlik-network-chart",
      load: () => Promise.resolve(window["sn-network-chart"]),
    },
  ],
});

// Rendering a Sankey chart on the fly
nuked.render({
  type: "qlik-network-chart",
  element: document.querySelector(".network"),
  fields: [
    "ID",
    "Name"
    "LinkTo",
    "Group",
    "=Sum(Volume)"
  ],
});
```

## Formatting your data

A network chart requires data that is structured
consistently according to a network data model
where each record can have multiple parents and
children. Each record needs to contain at least:

- A field that identifies the node,
  the node identifier.
  Node identifier values must be integer values,
  starting from 0 and in sequential order.
- A field with the name of the node.
- A field that defines the parent node. This value
  needs to be the node identifier of another
  node. If this field is empty, and no
  other record refers to this node, a disconnected node is created.

Here is some example data that you
can save in a text editor and load
in a new app. You need to load both
example files. The example shows
passenger flows between different airports.

- ID is the identifier of an airport node.
- Name is the name of an airport node.
  This is used as label of the node.
- LinkTo contains the node identifier
  of the parent node.
- Group states the group of a node.
  This can be used to color the nodes according to group.
- Volume is the passenger flow volume
  between ID and LinkTo. This can be
  used as a measure in edge size.
- NodeVolume is the total passenger
  flow volume for a node. This is loaded
  in a separate table as the chart
  cannot aggregate the volumes automatically.

### Example 1: Airports1.csv

```text
ID;Name;LinkTo;Group;Volume
0;Frankfurt;;0;
1;London;0;1;5
2;Madrid;0;1;4
2;Madrid;1;1;8
3;Warsaw;0;1;7
4;Arlanda;0;1;1
3;Warsaw;1;1;5
4;Arlanda;1;1;6
5;Tunis;0;2;8
5;Tunis;2;2;4
6;Berlin;0;1;6
6;Berlin;4;1;4
7;Rome;0;1;6
7;Rome;6;1;3
8;San Francisco;0;3;2
9;New York;0;3;9
```

### Example 2: Airports2.csv

```text
ID,NodeVolume
0,48
1,24
2,16
3,12
4,11
5,12
6,13
7,9
8,2
9,9
```

## Installing

If you use npm: `npm install @nebula.js/sn-network-chart`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-network-chart).
