---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-table/
last_updated: 2026-11-06T17:13:57+01:00
---

# Creating tables

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The table shows several fields simultaneously, where the content
of each row is logically connected, and may consist of multiple dimensions and measures.
Selections can only be made within the dimension columns, each of which provides a
search feature in the header.

Learn more about the [table chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [table chart API specification](https://qlik.dev/apis/javascript/sn-table/).

## Table virtualization

Virtualization enabled by default is a convenient way of displaying a substantial amount of data on the client-side
without the need for pagination.

![table virtualization example](https://qlik.dev/_astro/sn-virtualized-table.nvXfEYP6.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: {
    theme: "light", // default is light
    language: "en-US", //default is en-US
    keyboardNavigation: false, // tell Nebula to handle navigation, default is false
    constraints: {
      active: false, // allow interactions, default is false
    },
  },
  types: [
    {
      name: "table",
      load: () => Promise.resolve(window["sn-table"]),
    },
  ],
});
// Rendering a table which enables virtualization
nuked.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity", "=Sum([Sales Price])"],
});
```

## Table pagination

Pagination allows for quick navigation in large datasets by splitting up the data into pages with a certain amount of
rows. It also enhances accessibility and readability.

To activate pagination in a table, the usePagination property needs to be set to true.

![table pagination example](https://qlik.dev/_astro/sn-table-pagination.BbWeSb5-.png)

```js
// Rendering a table which pagination
nuked.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity", "=Sum([Sales Price])"],
  properties: {
    usePagination: true,
  },
});
```

## More examples

The table's appearance can be customized to a great extent. Below are some basic examples:

### Styling

Both the header and the body of the table can be styled with colors and font sizes.
Additionally, the hover effect on rows can also be styled.

![table example with styling](https://qlik.dev/_astro/sn-table-styling.xnOjFJwY.png)

```js
nuked.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity", "=Sum([Sales Price])"],
  properties: {
    components: [
      {
        key: "theme",
        content: {
          fontSize: 20,
          fontColor: {
            index: -1,
            color: "#276e27",
          },
          hoverEffect: true,
          hoverColor: {
            index: -1,
            color: "#7db8da",
          },
          hoverFontColor: {
            index: -1,
            color: "#4477aa",
          },
        },
        header: {
          fontSize: 16,
          fontColor: {
            index: -1,
            color: "#f8981d",
          },
        },
      },
    ],
  },
});
```

### Column styling

A specific column can be styled with background and font colors.
This is achieved through expressions, allowing the color to vary based on the cell's value.

To change properties on a measure,
the measure itself needs to be defined under `properties` on `qDef.qDef`,
followed by the column colors under qAttributeExpressions.

![table example with column styling](https://qlik.dev/_astro/sn-table-column-styling.Cy8t2cSM.png)

```js
nuked.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity"],
  properties: {
    qHyperCubeDef: {
      qMeasures: [
        {
          qDef: {
            qDef: "Revenue",
          },
          qAttributeExpressions: [
            {
              qExpression: `=if(Revenue < 400, '#ff0000', '#00ff00')`,
              qAttribute: true,
              id: "cellBackgroundColor",
            },
            {
              qExpression: `=if(Revenue < 400, '#ffffff', '#000000')`,
              qAttribute: true,
              id: "cellForegroundColor",
            },
          ],
        },
      ],
    },
  },
});
```

### Text alignment

Each column's text alignment can be set to left, center, or right.
The default setting is left for text values and right for number values, including those related to dates.

This example has a left-aligned number values.

![table example with adjusted text alignment](https://qlik.dev/_astro/sn-table-align.De2pM8eR.png)

```js
nuked.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity"],
  properties: {
    qHyperCubeDef: {
      qMeasures: [
        {
          qDef: {
            qDef: "Revenue",
            textAlign: {
              auto: false,
              align: "left",
            },
          },
        },
      ],
    },
  },
});
```

## Totals settings

Numeric values' totals are displayed below the respective measure names.
You can modify the label name, whether to display the totals and their placement, either at the top or bottom.

![table example with totals](https://qlik.dev/_astro/sn-table-totals.tF7hvRan.png)

```js
nuked.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity", "=Sum([Sales Price])"],
  properties: {
    totals: {
      label: "Totals",
      position: "bottom",
      show: true,
    },
  },
});
```

## Column width and order

The column width can be defined in different ways:

- `auto` calculates the column width so that the total table width equals the chart width.
- `fitToContent` calculates a width based on the cells' content.
- `pixels` uses a specified pixel value.
- `percentage` sets the column width to specified percentage of the chart width.

![table example with adjusted column width](https://qlik.dev/_astro/sn-table-column-width.CtAmDE9k.png)

```js
nuked.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity"],
  properties: {
    qHyperCubeDef: {
      qMeasures: [
        {
          qDef: {
            qDef: "Revenue",
            columnWidth: {
              type: "pixels",
              pixels: 350,
            },
          },
        },
      ],
    },
  },
});
```

A custom table order can be set using the `qHyperCubeDef.qColumnOrder` property.

![table example with adjusted column order](https://qlik.dev/_astro/sn-table-column-order.DwTrueIF.png)

```js
nuked.render({
  element: document.querySelector(".object"),
  type: "table",
  fields: ["Sales Quantity", "Customer", "=Sum([Sales Price])"],
  properties: {
    qHyperCubeDef: {
      qColumnOrder: [0, 2, 1],
    },
  },
});
```

## Keyboard navigation

You can use a keyboard to navigate both paginated and virtualized tables.

When mounting the table, there are two modes to
choose from by setting the property `keyboardNavigation`
to either true or false (default).

Setting keyboardNavigation to true tells nebula to handle focusing in and out of the table,
while setting it to false makes the first cell of the table focusable in
sequential keyboard navigation. For more information about the stardust
`useKeyboard` hook, see the [reference documentation](https://qlik.dev/apis/javascript/nebula-js/#entries-usekeyboard).

![Demonstration of keyboard navigation with keyboardNavigation set to true](https://qlik.dev/_astro/sn-table-keyboard-true.Dx6wVL4w.gif)

This is an example of navigating the table with `keyboardNavigation: true`. The entire table can be focused,
then **space/enter can be pressed to focus inside the table**.

```js
const n = embed(enigmaApp, {
  context: {
    keyboardNavigation: true,
  },
  // ...
});

n.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity", "=Sum([Sales Price])"],
  properties: {
    usePagination: true,
  },
});
```

![Demonstration of keyboard navigation with keyboardNavigation set to false](https://qlik.dev/_astro/sn-table-keyboard-false.KY7IBjMg.gif)

This is an example of navigating the table with `keyboardNavigation: false`.
The first cell of the table can be focused, allowing tabbing straight
into the table. When pagination is enabled, you can also tab to the pagination controls.

```js
const n = embed(enigmaApp, {
  context: {
    keyboardNavigation: false,
  },
  // ...
});

n.render({
  type: "table",
  element: document.querySelector(".table"),
  fields: ["Customer", "Sales Quantity", "=Sum([Sales Price])"],
  properties: {
    usePagination: true,
  },
});
```

### Keyboard shortcuts

Both paginated and virtualized tables support keyboard shortcuts for navigation
and selections. Shortcuts for navigating between pages and using pagination
controls are only available when pagination is enabled.

Available shortcuts depend on your location in the chart and the active mode.

| Keyboard shortcut                        | On table header                        | On table body                                               | In selections mode on body                                                              | On pagination controls                           |
| ---------------------------------------- | -------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Arrow keys**                           | Move focus                             | Move focus                                                  | Move focus                                                                              | -                                                |
| **Space**                                | Open column header menu                | Select cell and enter selection mode (on a selectable cell) | Select/deselect cell                                                                    | Activate control                                 |
| **Enter**                                | Open column header menu                | -                                                           | Confirm selections                                                                      | Activate control                                 |
| **Tab**                                  | Go to pagination controls when enabled | Go to pagination controls when enabled                      | Go to pagination controls when enabled, or to the selection toolbar in virtualized mode | Go to next control                               |
| **Shift + Tab**                          | Navigate out of the table              | Navigate out of the table                                   | Go to selection toolbar                                                                 | Go to previous control or back to the table body |
| **Shift + Up/Down arrows**               | -                                      | Select multiple values (on a selectable cell)               | Selects multiple values (on a selectable cell)                                          | -                                                |
| **Ctrl/Cmd + Shift + Left/Right arrows** | Go to previous/next page               | Go to previous/next page                                    | Go to previous/next page                                                                | Go to previous/next page                         |
| **Esc**                                  | Blur and focus the wrapping element\*  | Blur and focus the wrapping element\*                       | Cancel selections                                                                       | -                                                |
| **Home / End**                           | Move focus to the first/last column    | Move focus to the first/last column                         | Move focus to the first/last row in the current column                                  | -                                                |
| **Page Up / Page Down**                  | Move focus down 10 rows (Page Down)    | Move focus up/down 10 rows                                  | Move focus up/down 10 rows                                                              | -                                                |

\*Only works when `keyboardNavigation: true` is set in context.

> **Note:** In selection mode, the last row is the last row on the current page in paginated tables,
> and the last row of the dataset in virtualized tables.
>
> After confirming selections with `Enter`, focus returns to the first header cell.
> Pressing `Esc` cancels unconfirmed selections and restores focus to the current cell.
>
> The `Ctrl/Cmd + Shift + Left/Right` shortcuts for changing pages apply to paginated tables only.

The column header menu provides options for sorting, searching, making selections, and adjusting column width.
To adjust the column width, use the `Left` or `Right` arrow key.
Press `Space` or `Enter` to confirm the change, or `Esc` to cancel it.

Press `Esc` to close the header menu.

![table example showing keyboard shortcuts](https://qlik.dev/_astro/sn-table-keyboard-shortcuts.DhSEQ0ut.gif)
