---
title: "Background layers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/background-layer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Background layers

Background layers enable you to display a custom base map for your map visualization.

A background layer could, for example, be a map of an airport that then has a point layer with WIFI hotspot locations overlaid on it. If the custom base map format supports transparency, you can overlay it on top of another map. Qlik Sense supports the following custom maps formats as background layers:

- Slippy or tile map services (TMS)
- Web Map Service (WMS)
- Image URL (Image)

  Information noteURLs that contain resource requests to external resources must have its origins allowlisted in the Content Security Policy, else the resource will not be loaded.
  WMS resources must have both img-src and connect-src directives allowlisted.

  See also: [Managing Content Security Policy](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)

Maps services must be located on their own server. Unlike other layers, the background layer uses no dimensions or measures and only displays an external base map.

If your WMS contains areas with no data, you can set the areas with no data to be transparent. This enables the WMS background layer to be overlaid on another base map or background layer. You can also choose which WMS layers to include in the background layer.

You can insert an image as a background layer. This can be used as a custom base map. You could add an image of a floor plan and use it as a custom base map. An image background layer can also be overlaid on top of another background layer. For example, you could insert an image of a detailed local map as a background layer over top another map. Background layers support the following image types:

- .png
- .jpg
- .jpeg
- .gif

Map with background layer displaying a TMS OpenStreetMap map.

![Map with background layer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_backgroundlayer.png "Click to view full size")

## Adding a background layer

Background layer configuration varies depending on the type of background map.

### Adding a TMS background layer

Do the following:

1. From Layers in the properties panel, click Add layer.
2. Select Background layer.
3. After Format, select TMS.
4. After URL, enter the URL to a tile or slippy map server.

   For example, http://a.tile.opencyclemap.org/cycle/${z}/${x}/${y}.png.
5. After Attribution, enter the attribution string for the map.

   For example, &copy; <a href='http://www.opencyclemap.org/' target='\_blank'>OpenCycleMap</a>. Map data &copy; <a href='http://www.openstreetmap.org/copyright' target='\_blank'>OpenStreetMap</a> contributors.

Once the layer is added, you can adjust settings for the layer in the properties panel.

### Adding a WMS background layer

You can optionally use HTTP header authentication when adding a WMS background layer, including the username and password in the URL passed to the WMS server. You can enter the username and password manually or use expressions to define them.

Warning noteIf you use basic authentication, any user with access to the application can potentially extract the credentials used.

Do the following:

1. From Layers in the properties panel, click Add layer.
2. Select Background layer.
3. Under Format, select WMS.
4. Click WMS setup.
5. Under WMS server URL, enter the URL.
6. If you are using basic authentication, select Use basic authentication.

   1. After User, enter the username.

      To use an expression, click ![Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
   2. After Password, enter the password.

      To use an expression, click ![Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
7. Under Version, select the WMS version.
8. Click Load WMS.
9. After CRS, enter the coordinate reference system used by the WMS map.
10. Select Transparent to generate map images that are transparent where there is not data.

    Information note

    This is not supported by all WMS.
11. Under Image format, select the WMS image format.
12. Under Layers, select the map layers that your WMS server supports.
13. Click Save.
14. After Attribution, enter the attribution string for the map.

    For example, &copy; <a href='http://www.opencyclemap.org/' target='\_blank'>OpenCycleMap</a>. Map data &copy; <a href='http://www.openstreetmap.org/copyright' target='\_blank'>OpenStreetMap</a> contributors.

Once the layer is added, you can adjust settings for the layer in the properties panel.

### Adding an image background layer

Images can be used as a custom base map, such as for floor plans. When using an image background layer as a custom base map, set Base map in Map settings to None. Select Undefined meters or Undefined degrees as the projection. The location data for your other layers must use same coordinate system as this background layer.

Tip note

When you add an image background layer for a smaller geographic area as a custom base map, add a layer containing data, such as a point layer, at the same time. This lets the map automatically zoom in to the position of your image background layer.

Tip note

The lowest unit in the scale bar is 10 meters. If this measurement is too large for your image, you can disable the scale bar in Presentation and then proportionally adjust up your image in the background layer to the scale you want. Scale the location data you want to use in other layers as well.

Do the following:

1. From Layers in the properties panel, click Add layer.
2. Select Background layer.
3. Under Format, select Image.
4. After URL, enter the URL of the image.
5. Position your image by entering the coordinates for the top left and bottom right corners of the image.

   Coordinates must be in the same coordinate type as was selected in Projection.

   Tip note

   If you are unsure of the coordinates in your image background layer, enable Show debug info. This will display the coordinates for the current center of your map.
6. After Attribution, enter the attribution string for the image.

   For example, &copy; <a href='http://www.opencyclemap.org/' target='\_blank'>OpenCycleMap</a>. Map data &copy; <a href='http://www.openstreetmap.org/copyright' target='\_blank'>OpenStreetMap</a> contributors.

Once the layer is added, you can adjust settings for the layer in the properties panel. For image background layers being used as custom base maps, it is recommended that you change the Limit zoom levels and Limit pan navigation settings to set the focus on your custom map.
