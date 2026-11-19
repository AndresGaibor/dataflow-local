---
source: https://qlik.dev/embed/nebula/render/applying-themes/
last_updated: 2026-10-26T15:10:16Z
---

# Applying themes

Nebula supports using Qlik Sense themes to alter the
style of the embedded visualizations. Not all Sense
theme properties are supported, see section at the end.

## Registering themes

When configuring your Nebula instance you can pass in an
array of themes for usage in your mashup.

```js
import { embed } from '@nebula.js/stardust';
import theme from './myTheme';

const secondTheme = {
  type: "dark", // dark OR light Nebula UI theme
  /* Theme definition... */
}

const n = embed(enigmaApp, {
  context: {
    theme: 'myTheme',
  },
  themes: [
    {
      id: 'myTheme',
      load: () => Promise.resolve(myTheme),
    },
    {
      id: 'otherTheme',
      load: () => Promise.resolve(secondTheme),
    },
  ]
  types: [
    /* types */
  ],
});

n.render(/* chart 1*/);
n.render(/* chart 2*/);
```

Where the two theme variables are JavaScript objects
following the Qlik Sense theme properties. They are free
to include additional properties for custom charts.

## Consuming themes in charts

Utilizing themes in a chart is straightforward,
especially if you can inherit from an already existing chart.

```js
import { useEffect, useTheme, useElement } from '@nebula.js/stardust';
import ext from './properties';

export default function supernova(galaxy) {
  return {
    qae: {
      properties: {},
      data: {},
    },
    component() {
      const element = useElement();
      const Theme = useTheme();

      // Using the same styles as the bar chart
      const objectKey = 'object.barChart';

      useEffect(() => {
        const styles = {
          labelColor: Theme.getStyle(objectKey, 'label.name', 'color') || '#232323',
          fontSize: Theme.getStyle(objectKey, 'label.name', 'fontSize') || '12px',
          fontFamily: Theme.getStyle(objectKey, 'label.name', 'fontFamily') || 'Roboto',
          palette: Theme.getDataColorPickerPalettes()[0],
          primaryColor: Theme.getDataColorSpecials().primary,
        };
        render(element, styles); // Do some rendering
      }, [Theme.name(), element]);
    },
    ext: ext(galaxy),
  };
}
```

The `getStyle(...)` function takes three arguments, an object key,
a property key and an attribute. These combine to create
the search path for the value you are after. The preceding example has
`object.barChart.label.name.color` as one full path, which means it
starts to look there. If `color` is not specified at this path
it traverses the theme to find the best match.

To use the theme in property panel components it needs to be
accessed through the galaxy object, passed into the supernova.
In this example you pass the galaxy directly into the `ext` function
which returns the property panel definition. Inside Qlik Sense, the theme is available at
`galaxy.anything.sense.theme`. Outside Qlik Sense, `galaxy.anything.sense` is undefined, so guard the access.

```js
// properties.js
export default function ext(galaxy) {
  const theme = galaxy.anything.sense?.theme;
  return {
    definition: {
      type: 'items',
      component: 'accordion',
      items: {
        data: {
          uses: 'data',
        },
        sorting: {
          uses: 'sorting',
        },
        settings: {
          uses: 'settings',
          items: {
            color: {
              component: 'color-picker',
              translation: 'properties.color',
              ref: 'myColor',
              defaultValue: theme?.getDataColorSpecials().primary,
            },
          },
        },
      },
    },
  };
}
```

## Differences to themes in Sense

While Nebula charts supports Sense themes, they
are not applied to items outside of the charts.
An example of this is the chart title and background.
This is instead possible through CSS overrides.
These are defined in the Nebula API as follows,
each detailing a CSS class to target the specified element.

- [CellElement](https://qlik.dev/apis/javascript/nebula-js/#definitions-cellelement)
  - element containing the chart as well as titles.
- [CellTitle](https://qlik.dev/apis/javascript/nebula-js/#definitions-celltitle)
- [CellSubTitle](https://qlik.dev/apis/javascript/nebula-js/#definitions-cellsubtitle)
- [CellFooter](https://qlik.dev/apis/javascript/nebula-js/#definitions-cellfooter)
- [VizElement](https://qlik.dev/apis/javascript/nebula-js/#definitions-vizelement)
  - element containing only the chart.
- [ActionElement](https://qlik.dev/apis/javascript/nebula-js/#definitions-actionelement)
  - selection toolbar items
- [ActionToolbarElement](https://qlik.dev/apis/javascript/nebula-js/#definitions-actiontoolbarelement)
  - popover action toolbar. (Since 2.1.0)

When using these CSS selectors keep in mind that
you need higher specificity to override the default styles.

```css
div.njs-cell {
  /* background of cell */
  background: maroon;
}

p.njs-cell-footer,
h6.njs-cell-title,
p.njs-cell-sub-title {
  /* color of titles font */
  color: white;
}

button.njs-cell-action {
  /* color of toolbar buttons */
  color: white;
}

div.njs-action-toolbar-popover {
  /* background of popover toolbar */
  background: darkolivegreen;
}
```

### Differences in chart themes

The specification for chart themes in Nebula
is the same as in Sense, with a few exceptions.

For more information, see [Custom theme JSON properties](https://help.qlik.com/en-US/sense-developer/Subsystems/Extensions/Content/Sense_Extensions/CustomThemes/custom-themes-properties.htm)
on Qlik Help.

Unsupported properties:

- `_inherit` - used by Sense to inherit from the default theme.
  Nebula uses a different default theme, so this does not work the same way.
- `_cards` - used by the Sense sheet, not applicable in Nebula.
- `custom_styles` - used in the client to inject arbitrary CSS. In a Nebula mashup,
  you can do this manually instead.

## Example

You can find an example mashup in the
[nebula.js-examples GitHub repository](https://github.com/qlik-oss/nebula.js-examples/tree/main/examples/themes).
