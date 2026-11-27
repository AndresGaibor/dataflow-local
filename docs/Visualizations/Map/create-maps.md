---
title: "Creating maps"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/create-maps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating maps

Maps enable you to view your data geographically.

Maps have many ways to present your data. You can add multiple layers to your map to display different types of information on the same map. You can set a custom scope for locations so that if two locations have the same name, you display the locations and their data correctly. You can use drill-down [dimensions](#glossary-0 "Glossary term") to create a hierarchy of geographic areas for selection. You can limit the pan of a map to a specific view and scope of the map, such as a region of interest, out of which users cannot pan or zoom out. You can add custom base maps to your map and use non-WGS-84 coordinates.

You can add a map to the [sheet](#glossary-1 "Glossary term") you are editing.

Tip noteYou can create several map [visualizations](#glossary-2 "Glossary term") based on different point data or area data, which use the same dimension data.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty map to the sheet.
3. From Map settings, select the Base map.
4. From Layers in the properties panel, add layers to your map.

   Layers are placed above layers of the same type. You can set the order of layers by dragging layers up and down in the list. The layer at the top of your list is also overlaid on top of the other layers on your map.

   For information on configuring layers, see:

   - [*Point layers*](point-layer.htm)
   - [*Area layers*](area-layer.htm)
   - [*Line layers*](line-layer.htm)
   - [*Density layers*](density-layer.htm)
   - [*Chart layers*](chart-layer.htm)
   - [*Background layers*](background-layer.htm)

Once the map is created, you can adjust its appearance and other settings for the map and its layers in the properties panel.

Information noteThe ![Info](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info.svg) icon appears in the top-left corner of your map if there is an issue with the added layer. Click the icon to see the error message.

## Styling the map

There are options available in the properties panel for styling the text in the map chart. You can style the text in the title area and the labels for several types of map layers.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text in the title area

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling under Appearance > Presentation to customize the styling of the chart's title area (title, subtitle, and footnote). You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

You can style the text of the title information for the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote

### Customizing the text in the map layer labels

The font, font size, and text color for the layers of individual layers can be customized. You can style the text for the following types of map layers:

- Area layers
- Point layers
- Line layers
- Chart layers

Do the following:

1. Under Layers in the properties panel, click the layer for which you want to style the text.
2. Under Options > General, toggle on the Show label setting.
3. Use the options under Label font family to change the font for the layer labels.
4. Use the options under Label font size to adjust the text size of the layer labels.
5. Select a color for the label text under Label font color.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Customizing the selection color

You can customize the color for selections made in your map.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, after Selection color, select a color.

## Limiting location scope in map layers

By default, Qlik Sense searches a broad scope of locations for the location [field](#glossary-3 "Glossary term") when names are used. In cases where there are multiple possible matches, you may need to limit the scope of locations searched to ensure Qlik Sense displays the desired location.

Do the following:

1. From Layers in the properties panel, click Location.
2. Set Scope for location to Custom.
3. After Location type, select the type of data contained in the field or expression selected as Location field.
4. Optionally, after Country, enter a field, expression, or text indicating the country the locations in the Location field are located.
5. Optionally, after Administrative area (Level 1), enter a field, expression, or text indicating the first-level administrative area the locations in the Location field are located.
6. Optionally, after Administrative area (Level 2), enter a field, expression, or text indicating the second-level administrative area the locations in the Location field are located.

## Limiting panning in your map

You can limit the panning settings in your map to keep the view in your map limited to a set area, such as a specific region of interest. When you limit the panning in a map, you lock the map to the current view. The map will not zoom out further than the current view. You cannot pan the map beyond the limits of the current view. If you zoom in, you can pan, but you are limited by the boundaries of the pan limit.

Do the following:

1. From the properties panel, click Appearance.
2. In Presentation, set Limit pan navigation to Custom.
3. Set your map to the view you want to which you want to limit the pan.
4. Click Set pan limit.

You can toggle the set pan limit on and off with Limit pan navigation. You can clear the saved pan limit by clicking Clear pan limit.

## Using non-WGS-84 coordinate systems

If you have data and a background map in a projection other than WGS-84, you should set the base map to None, add your background map as a background layer, and then set your projection to use undefined degrees or meters depending on the unit of length used in your base map.

When using non-WGS-84 coordinates, you must use geometries loaded into a field. Location names cannot be used.

Do the following:

1. From the properties panel, click Map settings.
2. In Base map, select Empty (undefined degrees) or Empty (undefined meters).
3. Select Background layer.
4. After URL, enter the URL to a slippy map server.

   For example, http://a.tile.opencyclemap.org/cycle/${z}/${x}/${y}.png
   .
5. After Attribution, enter the attribution string for the map.

   For example, &copy; <a href='http://www.opencyclemap.org/' target='\_blank'>OpenCycleMap</a>. Map data &copy; <a href='http://www.openstreetmap.org/copyright' target='\_blank'>OpenStreetMap</a> contributors.
6. From Layers, click Add layer.
7. Select your layer type.
8. In Dimensions, click Add and select a field containing data in your map's coordinate system.

## Setting the zoom and selection behavior for maps

You can set the zoom and selection behavior for maps. Maps offers these options:

- Auto zoom: The map automatically zooms in to selections. This is the default option.
- Auto select visible: Zooming and panning change the selection based on the displayed points on the map.

  To use this option, create a table with spatial indexing data for your point data field using the Spatial index operation. The point data field used with Spatial index can contain coordinates or named locations. For more information, see [*Spatial index*](../../../Global_Common/GeoOperationsFunctions/Operations/SpatialIndex.htm).

  You can then add a point layer using the same point data field to display the points on the map.

  Users can turn off Auto select visible for a map while using it by clicking ![Turn off select visible](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_select_possible_outline.svg) in the hover menu.
- None: The map will never automatically zoom in.

Do the following:

1. From the properties panel, click Map settings.
2. Under Zoom behavior, select one of the following options:
   - Auto zoom
   - Auto select visible
   - None
3. If you selected Auto select visible, under Spatial index, select the field with the spatial index information.

## Server connection requirements

In order for a Qlik Sense map chart to be able to perform location lookup and show a background map (base map and layers), your web browser needs to be able to establish a connection with both of the following servers on port 443 (HTTPS):

- maps.qlikcloud.com (required for location lookups and background map)
- ibasemaps-api.arcgis.com (required for Satellite base map)

For more information, refer to the Map service connection requirements on [Ports used by user web browser](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Deploy_QSEoW/Ports.htm#anchor-3).

## Learn more

- [*Map chart*](Map.htm)
- [*Loading your own map data*](load-map-data.htm)
- [*Creating a drill-down dimension*](../../Dimensions/create-drill-down-dimension.htm)
- [Interpreting Map Charts](/lnk/Interpreting_map_charts)

Related learning:

- [Interpreting Map Charts](/lnk/Interpreting_map_charts)
