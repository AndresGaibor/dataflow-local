---
title: "Creating a map with an image background layer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/map-backgroundimage-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Creating a map with an image background layer

Expand/Collapse all

# Creating a map with an image background layer

You can use images as custom base maps in map [visualizations](#glossary-0 "Glossary term"). You may want to display data over a floor plan.

This example map chart displays an office floor plan with a point layer. Each bubble is positioned over an employee's desk. The weekly average of customer issues handled per day by the employee determines the size and color of each bubble.

Map example with floor plan image background with a point layer showing employees sized by the number of customer issues they have resolved

![Map example with floor plan image background with a point layer showing employees sized by the number of customer issues they have resolved](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_map-image-background-example_point.png "Click to view full size")

This example hides the default scale. Images do not have a consistent size scale. Image size in a map background layer is also dependent on what coordinates the user sets for the corners of the image.

## Dataset

This example uses two tables and a background image.

CustomerIssues

CustomerIssues

| Date | EmployeeNumber | CustomerIssues |
| --- | --- | --- |
| 8/1/2019 | 1 | 24 |
| 8/1/2019 | 2 | 31 |
| 8/1/2019 | 3 | 21 |
| 8/1/2019 | 4 | 42 |
| 8/1/2019 | 5 | 24 |
| 8/1/2019 | 6 | 40 |
| 8/1/2019 | 7 | 40 |
| 8/1/2019 | 8 | 19 |
| 8/1/2019 | 9 | 23 |
| 8/1/2019 | 10 | 47 |
| 8/1/2019 | 11 | 38 |
| 8/1/2019 | 12 | 21 |
| 8/1/2019 | 13 | 22 |
| 8/1/2019 | 14 | 15 |
| 8/1/2019 | 15 | 30 |
| 8/1/2019 | 16 | 46 |
| 8/1/2019 | 17 | 41 |
| 8/1/2019 | 18 | 31 |
| 8/1/2019 | 19 | 50 |
| 8/1/2019 | 20 | 27 |
| 8/1/2019 | 21 | 35 |
| 8/1/2019 | 22 | 38 |
| 8/1/2019 | 23 | 37 |
| 8/1/2019 | 24 | 31 |
| 8/1/2019 | 25 | 13 |
| 8/1/2019 | 26 | 11 |
| 8/2/2019 | 1 | 35 |
| 8/2/2019 | 2 | 31 |
| 8/2/2019 | 3 | 33 |
| 8/2/2019 | 4 | 14 |
| 8/2/2019 | 5 | 24 |
| 8/2/2019 | 6 | 33 |
| 8/2/2019 | 7 | 40 |
| 8/2/2019 | 8 | 14 |
| 8/2/2019 | 9 | 44 |
| 8/2/2019 | 10 | 24 |
| 8/2/2019 | 11 | 37 |
| 8/2/2019 | 12 | 39 |
| 8/2/2019 | 13 | 49 |
| 8/2/2019 | 14 | 16 |
| 8/2/2019 | 15 | 42 |
| 8/2/2019 | 16 | 13 |
| 8/2/2019 | 17 | 45 |
| 8/2/2019 | 18 | 48 |
| 8/2/2019 | 19 | 46 |
| 8/2/2019 | 20 | 18 |
| 8/2/2019 | 21 | 18 |
| 8/2/2019 | 22 | 45 |
| 8/2/2019 | 23 | 47 |
| 8/2/2019 | 24 | 31 |
| 8/2/2019 | 25 | 10 |
| 8/2/2019 | 26 | 21 |
| 8/3/2019 | 1 | 16 |
| 8/3/2019 | 2 | 34 |
| 8/3/2019 | 3 | 15 |
| 8/3/2019 | 4 | 44 |
| 8/3/2019 | 5 | 49 |
| 8/3/2019 | 6 | 18 |
| 8/3/2019 | 7 | 16 |
| 8/3/2019 | 8 | 41 |
| 8/3/2019 | 9 | 27 |
| 8/3/2019 | 10 | 46 |
| 8/3/2019 | 11 | 21 |
| 8/3/2019 | 12 | 49 |
| 8/3/2019 | 13 | 38 |
| 8/3/2019 | 14 | 30 |
| 8/3/2019 | 15 | 48 |
| 8/3/2019 | 16 | 17 |
| 8/3/2019 | 17 | 42 |
| 8/3/2019 | 18 | 48 |
| 8/3/2019 | 19 | 44 |
| 8/3/2019 | 20 | 44 |
| 8/3/2019 | 21 | 12 |
| 8/3/2019 | 22 | 44 |
| 8/3/2019 | 23 | 17 |
| 8/3/2019 | 24 | 24 |
| 8/3/2019 | 25 | 25 |
| 8/3/2019 | 26 | 33 |
| 8/4/2019 | 1 | 20 |
| 8/4/2019 | 2 | 45 |
| 8/4/2019 | 3 | 32 |
| 8/4/2019 | 4 | 37 |
| 8/4/2019 | 5 | 32 |
| 8/4/2019 | 6 | 50 |
| 8/4/2019 | 7 | 41 |
| 8/4/2019 | 8 | 14 |
| 8/4/2019 | 9 | 37 |
| 8/4/2019 | 10 | 39 |
| 8/4/2019 | 11 | 28 |
| 8/4/2019 | 12 | 35 |
| 8/4/2019 | 13 | 24 |
| 8/4/2019 | 14 | 19 |
| 8/4/2019 | 15 | 25 |
| 8/4/2019 | 16 | 26 |
| 8/4/2019 | 17 | 23 |
| 8/4/2019 | 18 | 45 |
| 8/4/2019 | 19 | 48 |
| 8/4/2019 | 20 | 36 |
| 8/4/2019 | 21 | 40 |
| 8/4/2019 | 22 | 21 |
| 8/4/2019 | 23 | 10 |
| 8/4/2019 | 24 | 42 |
| 8/4/2019 | 25 | 35 |
| 8/4/2019 | 26 | 26 |
| 8/5/2019 | 1 | 24 |
| 8/5/2019 | 2 | 28 |
| 8/5/2019 | 3 | 44 |
| 8/5/2019 | 4 | 19 |
| 8/5/2019 | 5 | 34 |
| 8/5/2019 | 6 | 37 |
| 8/5/2019 | 7 | 14 |
| 8/5/2019 | 8 | 26 |
| 8/5/2019 | 9 | 38 |
| 8/5/2019 | 10 | 25 |
| 8/5/2019 | 11 | 41 |
| 8/5/2019 | 12 | 35 |
| 8/5/2019 | 13 | 48 |
| 8/5/2019 | 14 | 36 |
| 8/5/2019 | 15 | 36 |
| 8/5/2019 | 16 | 37 |
| 8/5/2019 | 17 | 31 |
| 8/5/2019 | 18 | 44 |
| 8/5/2019 | 19 | 21 |
| 8/5/2019 | 20 | 28 |
| 8/5/2019 | 21 | 13 |
| 8/5/2019 | 22 | 10 |
| 8/5/2019 | 23 | 50 |
| 8/5/2019 | 24 | 35 |
| 8/5/2019 | 25 | 11 |
| 8/5/2019 | 26 | 39 |
| 8/6/2019 | 1 | 26 |
| 8/6/2019 | 2 | 14 |
| 8/6/2019 | 3 | 45 |
| 8/6/2019 | 4 | 27 |
| 8/6/2019 | 5 | 33 |
| 8/6/2019 | 6 | 21 |
| 8/6/2019 | 7 | 14 |
| 8/6/2019 | 8 | 45 |
| 8/6/2019 | 9 | 41 |
| 8/6/2019 | 10 | 35 |
| 8/6/2019 | 11 | 35 |
| 8/6/2019 | 12 | 13 |
| 8/6/2019 | 13 | 35 |
| 8/6/2019 | 14 | 26 |
| 8/6/2019 | 15 | 40 |
| 8/6/2019 | 16 | 14 |
| 8/6/2019 | 17 | 20 |
| 8/6/2019 | 18 | 23 |
| 8/6/2019 | 19 | 11 |
| 8/6/2019 | 20 | 23 |
| 8/6/2019 | 21 | 31 |
| 8/6/2019 | 22 | 48 |
| 8/6/2019 | 23 | 39 |
| 8/6/2019 | 24 | 50 |
| 8/6/2019 | 25 | 47 |
| 8/6/2019 | 26 | 40 |
| 8/7/2019 | 1 | 49 |
| 8/7/2019 | 2 | 39 |
| 8/7/2019 | 3 | 16 |
| 8/7/2019 | 4 | 28 |
| 8/7/2019 | 5 | 46 |
| 8/7/2019 | 6 | 37 |
| 8/7/2019 | 7 | 36 |
| 8/7/2019 | 8 | 15 |
| 8/7/2019 | 9 | 18 |
| 8/7/2019 | 10 | 25 |
| 8/7/2019 | 11 | 12 |
| 8/7/2019 | 12 | 37 |
| 8/7/2019 | 13 | 40 |
| 8/7/2019 | 14 | 35 |
| 8/7/2019 | 15 | 11 |
| 8/7/2019 | 16 | 12 |
| 8/7/2019 | 17 | 22 |
| 8/7/2019 | 18 | 16 |
| 8/7/2019 | 19 | 46 |
| 8/7/2019 | 20 | 39 |
| 8/7/2019 | 21 | 41 |
| 8/7/2019 | 22 | 26 |
| 8/7/2019 | 23 | 25 |
| 8/7/2019 | 24 | 34 |
| 8/7/2019 | 25 | 50 |
| 8/7/2019 | 26 | 41 |

EmployeeData

EmployeeData

| Employee | EmployeeNumber | Latitude | Longitude |
| --- | --- | --- | --- |
| Nehru Pollard | 1 | 2.1 | -2.1 |
| Duncan Bell | 2 | 1.675 | -2.1 |
| Arthur Miller | 3 | 2.1 | -1.6 |
| Latifah Randall | 4 | 1.675 | -1.6 |
| Glenna Giles | 5 | 2.1 | -1.1 |
| Chaim Gates | 6 | 1.675 | -1.1 |
| Elijah Mcgowan | 7 | 2.1 | -0.585 |
| Serina Richards | 8 | 1.675 | -0.585 |
| Nora Odonnell | 9 | 2.1 | 0.595 |
| Fiona Craig | 10 | 1.675 | 0.595 |
| Kirestin Mcguire | 11 | 2.1 | 1.155 |
| Francesca Wilkerson | 12 | 1.675 | 1.155 |
| Virginia Sanford | 13 | 2.1 | 1.6 |
| Beau Weeks | 14 | 1.675 | 1.6 |
| Justin Cook | 15 | 2.1 | 2.2 |
| Lisandra Sloan | 16 | 1.675 | 2.2 |
| Brody Ball | 17 | 2.1 | 2.6 |
| Kirk Welch | 18 | 1.675 | 2.6 |
| Julian Mcgee | 19 | 0.7 | 3.25 |
| Geoffrey Wheeler | 20 | 0.7 | 3.7 |
| Carter Leonard | 21 | 0.14 | 3.25 |
| Noel Watson | 22 | 0.14 | 3.7 |
| Damian Everett | 23 | -0.3 | 3.25 |
| Justina Frazier | 24 | -0.3 | 3.7 |
| MacKenzie Garcia | 25 | -0.85 | 3.25 |
| Germane Carey | 26 | -0.85 | 3.7 |

Background image

Example background image

![Example background image](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_map-image-background-example.png "Click to view full size")

## How I built this

Information noteURLs that contain resource requests to external resources must have its origins allowlisted in the Content Security Policy, else the resource will not be loaded.
WMS resources must have both img-src and connect-src directives allowlisted.

See also: [Managing Content Security Policy](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)

### Before you start

The following origin must be added to the allowlist in your tenant’s Content Security Policy: https://help.qlik.com. Add the origin with the img-src directive. This is done in the Administration activity center by an administrator.

For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

### Building the map

Do the following:

1. Add the data sources to your application and associate the tables using the EmployeeNumber fields in each table.
2. In a sheet, add a map chart.
3. In Map settings, do the following:

   - Change Base map to None.
   - Change Projection to User defined (degrees).
4. In Appearance > Presentation, do the following:

   - Toggle the Scale bar to Off.
   - Set Limit zoom levels to Custom and set the zoom to 7x zoom - 8x zoom.
5. Add a background layer to the map chart and in Data, do the following:

   - In Format, select Image.
   - Set the URL to https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui\_map-image-background-example.png.
   - Set the Top left corner to 2.5 for Top (latitude) and -4.1 for Left (longitude).
   - Set the Bottom right corner to -2.5 for Bottom (latitude) and 4.1 for Right (longitude).

   Information note

   At this point in the example, the image does not appear yet. After you add a point layer with the next step, the map updates with the correct scale and image position.
6. Add a point layer to the map chart and do the following:

   - In Data, add Employee as the field.
   - In Location, select Latitude and longitude fields. Set Latitude as the Latitude field and Longitude as the Longitude field.
   - In Size & Shape, set Size by Avg(CustomerIssues).
   - In Colors, do the following:

     - Set Colors to Custom and color By measure.
     - Select Avg(CustomerIssues) as the measure.
     - Select Diverging classes as the color scheme.

To get the same look and feel as the image at the top of the page, set the application theme to Sense Classic.
