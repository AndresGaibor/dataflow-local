---
source: https://qlik.dev/extend/create-custom-themes/
last_updated: 2026-10-16T14:01:15Z
---

# Custom theme overview

Qlik Sense comes with six themes: Sense Classic, Sense Focus, Sense Breeze, Sense Horizon, Foundation,
and New Horizon.
In addition to these, you can create custom themes based on your company standards.

## Creating custom themes

You do not need previous experience developing custom themes,
but you should have at least a basic understanding of JSON and JavaScript.

With custom themes you can precisely style an app by changing the colors, adding
images and backgrounds as well as specifying the font sizes and font colors on
a global or granular basis throughout your app. You can also define color
palettes to be used and customize the specifications for margins, padding, and spacing.

A custom theme is a collection of files stored in a folder. It must contain a
definition (QEXT) file, a main JSON file, and optionally any other assets you
might need to support the custom theme, such as CSS files, custom font files
and images.

> **Warning:** Document Object Model (DOM) selectors in custom CSS are not a supported pattern. While they can be
> helpful for customizing the look and feel of applications, the DOM is subject
> to change at any time. To provide your feedback, raise tickets on the [Qlik Ideation portal](https://community.qlik.com/t5/Ideation/ct-p/qlik-product-insight)
> when you need custom CSS customization. This helps prioritize supported
> customization options to add to the platform.
>
> For more information, see
> [CSS best practices for Sense themes](https://qlik.dev/extend/create-custom-themes/custom-themes-css-best-practices).

The custom styles are defined in the following way:

- In the JSON file you define the style for the individual visualization types,
  for example bar charts and line charts.

When you have created a custom theme, zip the JSON file with any additional resources
and upload it to Qlik Cloud as an extension.

> **Note:** Fonts from a custom theme are not supported when embedding Qlik objects cross-domain unless you use
> `<qlik-embed iframe="true">`. Using the `iframe="true"` mode may impact performance.

## Download Qlik theme definitions

Each section contains a preview of the theme's colors and JSON definition.
You can view the definition below, download the individual `theme.json` file,
or download a ZIP package containing `theme.json` and a generated QEXT file. The ZIP
packages are ready to upload and use in Qlik Cloud or Qlik Sense Enterprise on Windows.

To install a ZIP package, see
[Uploading and managing themes](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-themes.htm)
for Qlik Cloud, or
[Installing custom themes](https://help.qlik.com/en-US/sense-developer/Subsystems/Extensions/Content/Sense_Extensions/CustomThemes/custom-themes-installing.htm)
for Qlik Sense Enterprise on Windows and Qlik Sense Desktop.

### Foundation

Download Foundation theme.json · Download Foundation ZIP package

<details>
  <summary>View Foundation theme.json</summary>

  <pre>
    <code>
      {JSON.stringify(foundationTheme, null, 2)}
    </code>
  </pre>
</details>

### New Horizon

Download New Horizon theme.json · Download New Horizon ZIP package

<details>
  <summary>View New Horizon theme.json</summary>

  <pre>
    <code>
      {JSON.stringify(newHorizonTheme, null, 2)}
    </code>
  </pre>
</details>

### Sense Classic

Download Sense Classic theme.json · Download Sense Classic ZIP package

<details>
  <summary>View Sense Classic theme.json</summary>

  <pre>
    <code>
      {JSON.stringify(senseTheme, null, 2)}
    </code>
  </pre>
</details>

### Sense Focus

Sense Focus uses the Sense Classic `12 Colors` palette.

Download Sense Focus theme.json · Download Sense Focus ZIP package

<details>
  <summary>View Sense Focus theme.json</summary>

  <pre>
    <code>
      {JSON.stringify(cardTheme, null, 2)}
    </code>
  </pre>
</details>

### Sense Breeze

Download Sense Breeze theme.json · Download Sense Breeze ZIP package

<details>
  <summary>View Sense Breeze theme.json</summary>

  <pre>
    <code>
      {JSON.stringify(breezeTheme, null, 2)}
    </code>
  </pre>
</details>

### Sense Horizon

Download Sense Horizon theme.json · Download Sense Horizon ZIP package

<details>
  <summary>View Sense Horizon theme.json</summary>

  <pre>
    <code>
      {JSON.stringify(horizonTheme, null, 2)}
    </code>
  </pre>
</details>
