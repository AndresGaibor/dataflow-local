---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-nav-menu/
last_updated: 2025-03-04T16:54:00+01:00
---

# Creating navigation menu objects

> **Notes:**
>
> - Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
>   and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.
> - Qlik Sense Mobile SaaS doesn't support the `sn-nav-menu` visualization because
>   it doesn't support the nebula.js API for sheet navigation and rendering.

The navigation menu object offers an alternative method of navigating between
sheets and sheet groups in an app. By default, the navigation menu displays
all public sheets and groups in an app if the app is hosted on Qlik Cloud or Qlik Sense Enterprise client-managed.
If the app is running on Qlik Sense Desktop, or is a private app on Qlik Sense Enterprise
client-managed, the menu shows all private sheets and groups instead.

You can customize the text formatting and colors in the menu, and the
background image has sizing and positioning options.

![navigation menu object example](https://qlik.dev/_astro/sn-nav-menu-vertical.DZ_B7Ypf.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "sn-nav-menu",
      load: () => Promise.resolve(window["sn-nav-menu"]),
    },
  ],
  flags: {AOSHARE: true, AOSHARE_FROM_SPACE: false},
});

// Rendering a navigation menu object
nuked.render({
  type: "sn-nav-menu",
  element: document.querySelector(".menu"),
});
```

## More examples

The navigation menu's appearance can be customized to a great extent. Below are some basic examples:

### Orientation and layout

You can configure the menu to have a horizontal layout.

![navigation menu object in horizontal mode example](https://qlik.dev/_astro/sn-nav-menu-horizontal.cUXu_g4c.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "sn-nav-menu",
      load: () => Promise.resolve(window["sn-nav-menu"]),
    },
  ],
  flags: {AOSHARE: true, AOSHARE_FROM_SPACE: false},
});

// Rendering a navigation menu object
nuked.render({
  type: "sn-nav-menu",
  element: document.querySelector(".menu"),
  properties: {
    "layoutOptions": {
      "orientation": "horizontal",
      "alignment": "top-center",
    },
  },
});
```

### Styling

You can style the navigation menu with colors, font sizes, hovering effects, rounded corners, and more.

![navigation menu object styling example](https://qlik.dev/_astro/sn-nav-menu-horizontal-style-1.BhJFh2SJ.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "sn-nav-menu",
      load: () => Promise.resolve(window["sn-nav-menu"]),
    },
  ],
  flags: {AOSHARE: true, AOSHARE_FROM_SPACE: false},
});

// Rendering a navigation menu object
nuked.render({
  type: "sn-nav-menu",
  element: document.querySelector(".menu"),
  properties: {
    "layoutOptions": {
      "drawerMode": false,
      "hideDrawerIcon": false,
      "orientation": "horizontal",
      "layout": "fill",
      "alignment": "top-center",
      "separateItems": false,
      "dividerColor": {
        "color": "rgba(0,0,0,0.12)",
        "index": -1
      },
      "largeItems": false,
      "showItemIcons": false
    },
    "components": [
      {
        "key": "general"
      },
      {
        "key": "theme",
        "content": {
          "fontSize": "18px",
          "fontStyle": {
            "bold": true,
            "italic": false,
            "underline": false,
            "normal": true
          },
          "defaultColor": {
            "index": 15,
            "color": "#000000",
            "alpha": 1
          },
          "defaultFontColor": {
            "color": "#ffffff",
            "alpha": 1
          },
          "highlightColor": {
            "index": -1,
            "color": "#3ba63b",
            "alpha": 1
          },
          "highlightFontColor": {
            "color": "#ffffff",
            "alpha": 1
          },
          "hoverColor": {
            "index": -1,
            "color": "#ffa82e",
            "alpha": 1
          },
          "borderRadius": "20px"
        }
      }
    ]
  },
});
```

### Sheet navigation control

The navigation menu can be used to navigate between sheets in an app by
connecting the app's sheet navigation API to the navigation menu object.

![sheet control example](https://qlik.dev/_astro/sn-nav-menu-sheet-control.Be1gAHQ7.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "sn-nav-menu",
      load: () => Promise.resolve(window["sn-nav-menu"]),
    },
  ],
  flags: {AOSHARE: true, AOSHARE_FROM_SPACE: false},
});

// Sheet object where sheet is controlled by a navigation api. The navigation api is exposed from sheet
const sheetObject = await nuked.render({
  id: 'EMFeb',
  element: document.querySelector(".sheet"),
});

// Rendering a navigation menu object
nuked.render({
  type: "sn-nav-menu",
  element: document.querySelector(".menu"),
  properties: {
    "layoutOptions": {
      "drawerMode": false,
      "hideDrawerIcon": false,
      "orientation": "horizontal",
      "layout": "fill",
      "alignment": "top-center",
      "separateItems": false,
      "dividerColor": {
        "color": "rgba(0,0,0,0.12)",
        "index": -1
      },
      "largeItems": false,
      "showItemIcons": false
    },
    "components": [
      {
        "key": "general"
      },
      {
        "key": "theme",
        "content": {
          "fontSize": "18px",
          "fontStyle": {
            "bold": true,
            "italic": false,
            "underline": false,
            "normal": true
          },
          "defaultColor": {
            "index": 15,
            "color": "#000000",
            "alpha": 1
          },
          "defaultFontColor": {
            "color": "#ffffff",
            "alpha": 1
          },
          "highlightColor": {
            "index": -1,
            "color": "#3ba63b",
            "alpha": 1
          },
          "highlightFontColor": {
            "color": "#ffffff",
            "alpha": 1
          },
          "hoverColor": {
            "index": -1,
            "color": "#ffa82e",
            "alpha": 1
          },
          "borderRadius": "20px"
        }
      }
    ]
  },
  navigation: sheetObject.navigation,
});
```

## Requirements

Requires `@nebula.js/stardust` version `5.4.2` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-nav-menu`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-nav-menu).
