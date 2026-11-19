---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/navigationmenu/
last_updated: 2024-11-08T11:37:41+01:00
---

# Navigation menu

## Overview

The navigation menu offers an alternative method of navigating between sheets and sheet groups in an app.
By default, it displays all public sheets and groups in an app if the app is hosted on Qlik Cloud
or Qlik Sense Enterprise client-managed.
If the app is running on Qlik Sense Desktop, or is a private app on Qlik Sense Enterprise
client-managed, the menu shows all private sheets and groups instead.

![Vertical layout of the navigation menu](https://qlik.dev/_astro/sn-nav-menu-vertical.DZ_B7Ypf.png)

You can customize the menu layout and the text formatting and colors in the menu.
There are also options for background image sizing and positioning.

![Horizontal layout of the navigation menu with customized colors for menu items](https://qlik.dev/_astro/sn-nav-menu-horizontal-style-1.BhJFh2SJ.png)

## Default settings for the navigation menu

- By default, no title, subtitle, or footnotes are displayed.
- The navigation menu appears as a standard menu but can be configured as a [drawer menu](#drawer-mode) for compact
  access to navigation.
- No dividers are displayed between menu items.
- Sheets and sheet groups are sorted according to their order in the assets panel of the app.

## Drawer mode

You can choose to enable the drawer mode for the navigation menu.
This mode displays the navigation menu as a button that opens a drawer menu over the app, listing sheets and sheet
groups.

This mode offers compact access to navigation for apps that need to maximize screen space for content.

![Navigation menu in drawer mode with a button that opens a drawer menu](https://qlik.dev/_astro/sn-nav-menu-drawer.hainolS6.png)

To enable the drawer mode, add the following to your configuration:

```json
  "layoutOptions": {
    "drawerMode": true
  }
```
