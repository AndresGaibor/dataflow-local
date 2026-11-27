---
title: "Creating a map focused on a region"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/Map-HowIBuiltThis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Creating a map focused on a region

Expand/Collapse all

# Creating a map focused on a region

You can configure your map charts to stay focused on a region of interest, such as a country. You can also set the minimum and maximum zoom levels of your map. This controls how far the Qlik Sense zooms into the map when you make [selections](#glossary-0 "Glossary term").

The following example explains how to make a map with the focus locked on a single region and with a custom maximum zoom level.

The map chart with panning limited to just the region of interest

![Map chart with panning limited to region of interest.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-map-example-zoom-out.png "Click to view full size")

This map has set a pan limit so users cannot pan the focus of the map [visualization](#glossary-1 "Glossary term") away from the region of interest. Users can drill down between separate map layers, but they cannot scroll outside of the initial view.

This map visualization uses a point layer and an area layer with two drill-down [dimensions](#glossary-2 "Glossary term"). One drill-down dimension enables the area layer to display counties after states are selected. The other drill-down dimension enables the point layer to display cities as a points after a state is selected in the area layer.

A zoom limit is applied to the map chart. When a state is selected in the area layer, the map drills down to display the counties in the area layer and the cities in a separate point layer. The map remains zoomed a level appropriate for a general regional overview.

A map chart with a state selection applied

![A map chart with a state selection applied](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-map-example-zoom-in.png "Click to view full size")

## Dataset

This example uses two sets of data. You must import this data into Qlik Sense. You can add the data to a spreadsheet and import it into Qlik Sense. You can also import the table from this help page as a web file.

City data

Sample city data

| City | City Code | County | State | Latitude | Longitude |
| --- | --- | --- | --- | --- | --- |
| New York | 1 | New York County | US | 40.730599 | -73.986581 |
| Los Angeles | 2 | Los Angeles County | CA | 34.053678 | -118.242702 |
| Chicago | 3 | Cook County | IL | 41.875555 | -87.624421 |
| Philadelphia | 5 | Philadelphia County | PA | 39.952335 | -75.163789 |
| Phoenix | 6 | Maricopa County | AZ | 33.446768 | -112.075672 |
| San Antonio | 7 | Bexar County | TX | 29.4246 | -98.49514 |
| San Diego | 8 | San Diego County | CA | 32.717421 | -117.162771 |
| Dallas | 9 | Dallas County | TX | 32.776196 | -96.796899 |
| San Jose | 10 | Santa Clara County | CA | 37.34385 | -121.883135 |
| Austin | 11 | Travis County | TX | 30.271129 | -97.7437 |
| Indianapolis | 12 | Marion County | IN | 39.76838 | -86.158045 |
| Jacksonville | 13 | Duval County | FL | 30.332184 | -81.655651 |
| Columbus | 15 | Franklin County | OH | 39.96226 | -83.000706 |
| Charlotte | 16 | Mecklenburg County | NC | 35.227087 | -80.843127 |
| Detroit | 17 | Wayne County | MI | 42.348664 | -83.056738 |
| Memphis | 18 | Shelby County | TN | 35.149022 | -90.051628 |
| Seattle | 19 | King County | WA | 47.603832 | -122.330062 |
| Denver | 20 | Denver County | CO | 39.739154 | -104.984703 |
| Boston | 22 | Suffolk County | MA | 42.360482 | -71.059568 |
| Nashville | 23 | Davidson County | TN | 36.162226 | -86.774342 |
| Baltimore | 24 | Baltimore City County | MD | 39.290861 | -76.610807 |
| Portland | 25 | Multnomah County | OR | 45.520247 | -122.674195 |
| Las Vegas | 26 | Clark County | NV | 36.166286 | -115.149225 |
| Milwaukee | 27 | Milwaukee County | WI | 43.034993 | -87.922497 |
| Albuquerque | 28 | Bernalillo County | NM | 35.084103 | -106.650985 |
| Tucson | 29 | Pima County | AZ | 32.221742 | -110.926476 |
| Fresno | 30 | Fresno County | CA | 36.73082 | -119.699202 |
| Sacramento | 31 | Sacramento County | CA | 38.581572 | -121.4944 |
| Kansas City | 32 | Jackson County | MO | 39.084469 | -94.56303 |
| Colorado Springs | 33 | El Paso County | CO | 38.833958 | -104.825348 |
| Atlanta | 34 | Fulton County | GA | 33.749099 | -84.390185 |
| Omaha | 35 | Douglas County | NE | 41.258732 | -95.937873 |
| Raleigh | 36 | Wake County | NC | 35.780402 | -78.639078 |
| Miami | 37 | Miami-Dade County | FL | 25.774266 | -80.193659 |
| Minneapolis | 38 | Hennepin County | MN | 44.9773 | -93.265469 |
| Tulsa | 39 | Tulsa County | OK | 36.152436 | -95.990409 |
| Cleveland | 40 | Cuyahoga County | OH | 41.505161 | -81.693445 |
| New Orleans | 41 | Orleans Parish | LA | 29.949932 | -90.070116 |

Customer

Sample customer data

| Customer | Customer Number | City Code |
| --- | --- | --- |
| A Superior System | 10000453 | 1 |
| Beech Aircraft Corporation | 10003882 | 1 |
| Deere and Company | 10009863 | 1 |
| Gailey Enterprises | 10012851 | 1 |
| J.A. Bauer Pottery Company | 10017852 | 1 |
| Old Towne Creations | 10020715 | 1 |
| Real World | 10022755 | 1 |
| ValueClick | 10025878 | 1 |
| A&G | 10000457 | 2 |
| Bell Canada Enterprises | 10004207 | 2 |
| Échange CAC Exchange | 10010832 | 2 |
| Gainunion | 10012885 | 2 |
| J.M. Haggar | 10018129 | 2 |
| OnDeck Systems | 10020849 | 2 |
| Reflex Presentations | 10022962 | 2 |
| Wasabi | 10026294 | 2 |
| Aadast | 10000471 | 3 |
| Bendix Corporation | 10004255 | 3 |
| ECI com | 10010855 | 3 |
| Galaxy Marketing Associates | 10012907 | 3 |
| Johnson and Higgins | 10018352 | 3 |
| One Planet Solutions | 10020864 | 3 |
| Relcom | 10022978 | 3 |
| Wayne'sWorld | 10026334 | 3 |
| ABI TruTrac | 10000488 | 5 |
| Best Way! Imaging | 10004602 | 5 |
| Ed Stefanov | 10010881 | 5 |
| Gamacles | 10013011 | 5 |
| Joy Line | 10018371 | 5 |
| Onebox | 10020907 | 5 |
| SageGroup | 10023511 | 5 |
| VEI | 10026023 | 5 |
| AboveNet | 10000496 | 6 |
| Bezeq | 10005043 | 6 |
| EDA Today | 10010882 | 6 |
| Gamma One Conversions | 10013039 | 6 |
| K | 10018518 | 6 |
| Keystroke Quality | 10019420 | 6 |
| Outsource Documents | 10020982 | 6 |
| PAGE | 10021240 | 6 |
| Sarcom | 10023703 | 6 |
| Systems of Missouri | 10024915 | 6 |
| Velos Medical Informatics | 10026038 | 6 |
| Abplus | 10000497 | 7 |
| BF Datacom | 10005099 | 7 |
| Edmark | 10010923 | 7 |
| GammaGraphX (GGX) | 10013052 | 7 |
| K&K Enterprises | 10018603 | 7 |
| Overdreams | 10021006 | 7 |
| SAS Institute | 10023757 | 7 |
| Ventana s Group | 10026081 | 7 |
| ABSolute | 10000499 | 8 |
| BH Feldman Consulting | 10005236 | 8 |
| Elbit Oy | 10010990 | 8 |
| Gammel Group | 10013061 | 8 |
| Karickal Exports | 10018868 | 8 |
| Owl's Eye Productions | 10021015 | 8 |
| SAT-SAGEM (usa) | 10023780 | 8 |
| White Oak Interactive | 10026365 | 8 |
| Absolute Magic | 10000501 | 9 |
| Bibb Manufacturing Company | 10005376 | 9 |
| Eloi Companies | 10011018 | 9 |
| Gandalf Systems | 10013079 | 9 |
| KAT Micro Distributing | 10018877 | 9 |
| P.C'S | 10021111 | 9 |
| Science Applications International (SAIC) | 10023964 | 9 |
| Xcert | 10026521 | 9 |
| Abstract | 10000502 | 10 |
| BidCast | 10005620 | 10 |
| Elucidex | 10011052 | 10 |
| Ganymede | 10013080 | 10 |
| Kendrick Jansen | 10018950 | 10 |
| P.C.G. Associates | 10021107 | 10 |
| Screen Digest | 10024016 | 10 |
| Xyratex | 10026868 | 10 |
| AC Exchange | 10001103 | 11 |
| Bien Logic | 10005688 | 11 |
| Embedded Support Tools (EST) | 10011089 | 11 |
| Garbee and Garbee | 10013127 | 11 |
| Kennecott Copper Corporation | 10018957 | 11 |
| Pacific Bell | 10021160 | 11 |
| Smith Manufacturing Company | 10024477 | 11 |
| Yurie Systems | 10027119 | 11 |
| AC&E | 10001263 | 12 |
| Acara | 10001786 | 12 |
| Big | 10005810 | 12 |
| Big Picture Technologies | 10005919 | 12 |
| EMC | 10011093 | 12 |
| Garlin Imports | 10013137 | 12 |
| KENROB and Associates | 10019066 | 12 |
| Packet Design | 10021232 | 12 |
| Sterling Armament Company | 10024704 | 12 |
| Zero G | 10027370 | 12 |
| Acacia | 10001784 | 13 |
| Big Mountain Multi | 10005861 | 13 |
| Emergency | 10011286 | 13 |
| Gate9th | 10013312 | 13 |
| Kerite Company | 10019194 | 13 |
| PADL | 10021239 | 13 |
| Sun Microsystems | 10024880 | 13 |
| Acc Tonec | 10001818 | 15 |
| Big Planet | 10005922 | 15 |
| Enterprises | 10011355 | 15 |
| Gatierf Publications | 10013341 | 15 |
| kGS | 10019469 | 15 |
| Page Marketing | 10021242 | 15 |
| T & S | 10024916 | 15 |
| Accel Partners | 10002114 | 16 |
| Biz-comm | 10006836 | 16 |
| Equitable Life Assurance Society | 10011360 | 16 |
| GCC Technologies | 10013376 | 16 |
| KillerGraffix | 10019502 | 16 |
| Page Research | 10021270 | 16 |
| T.F.C. | 10024918 | 16 |
| Accent Interactive | 10002115 | 17 |
| Boott Cotton Mills Corporation | 10006916 | 17 |
| Farmland Industries | 10011499 | 17 |
| GDC | 10013426 | 17 |
| Kim Tom Co | 10019512 | 17 |
| PageBoy | 10021283 | 17 |
| T.J.T. International | 10024919 | 17 |
| Accent Systems | 10002117 | 18 |
| Borden Company | 10006917 | 18 |
| Farrell Lines Company | 10011546 | 18 |
| GEAR | 10013538 | 18 |
| Kimball (W.W.) Company | 10019514 | 18 |
| PagePoint | 10021286 | 18 |
| T.M. Denton Consultants | 10024924 | 18 |
| Access Point | 10002128 | 19 |
| Accidental | 10002137 | 19 |
| Boston and Albany Railroad Company | 10006919 | 19 |
| Bre-X | 10007117 | 19 |
| FCS | 10011600 | 19 |
| Federated Co-Operatives Limited | 10011732 | 19 |
| GearSource | 10013572 | 19 |
| Gehlken Enterprises | 10013670 | 19 |
| Levi Strauss and Company | 10019783 | 19 |
| Lobster Productions | 10019952 | 19 |
| PageSites | 10021297 | 19 |
| PageWeavers | 10021302 | 19 |
| T3West | 10024930 | 19 |
| Tag Systems | 10024942 | 19 |
| AccessWare | 10002136 | 20 |
| Brazilian Traction, Light and Power Company | 10006977 | 20 |
| Federal Express Corporation | 10011623 | 20 |
| Gebbie Press | 10013574 | 20 |
| Lewis Grocer Company | 10019812 | 20 |
| PageWave | 10021300 | 20 |
| Tadpole | 10024940 | 20 |
| ACCPAC International | 10002138 | 22 |
| Brentano's | 10006983 | 22 |
| FenP Innovators | 10011821 | 22 |
| Greymac Trust Company | 10013870 | 22 |
| Lucky | 10020080 | 22 |
| Pallister Management | 10021305 | 22 |
| Take 3 | 10025022 | 22 |
| Accrue | 10002139 | 23 |
| C&C | 10007134 | 23 |
| Fentek Industries | 10011842 | 23 |
| Grove Farm Co., Inc. | 10013871 | 23 |
| Market | 10020181 | 23 |
| Palo Alto | 10021331 | 23 |
| Talarian | 10025024 | 23 |
| Accton | 10002140 | 24 |
| C. Hoelzle Associates | 10007163 | 24 |
| Fenwick & West | 10011870 | 24 |
| Grumman Corporation | 10013899 | 24 |
| Maui Island(MIC) | 10020193 | 24 |
| Panasonic | 10021350 | 24 |
| Target | 10025052 | 24 |
| AccuCom | 10002142 | 25 |
| C.O.F. | 10007183 | 25 |
| Ferrari | 10011918 | 25 |
| Guarantee Mutual Life Company | 10014043 | 25 |
| MaxBan | 10020227 | 25 |
| Pangaea Systems | 10021380 | 25 |
| Taroch | 10025063 | 25 |
| ACCUCOMP | 10002144 | 26 |
| C3 Development | 10007253 | 26 |
| FiberPlex | 10011979 | 26 |
| GURUs | 10014059 | 26 |
| MaXpeed | 10020239 | 26 |
| Panix | 10021411 | 26 |
| Tartanchase | 10025086 | 26 |
| AccuLAN | 10002149 | 27 |
| C3I | 10007258 | 27 |
| FICOM | 10012023 | 27 |
| H.H. Robertson Company | 10014064 | 27 |
| MAXSTRAT | 10020247 | 27 |
| Paraclipse | 10021494 | 27 |
| Taskers of Andover, Ltd. | 10025158 | 27 |
| Accumedic Systems | 10002150 | 28 |
| Cabco West | 10007268 | 28 |
| Fifth Generation | 10012128 | 28 |
| HarborGroup | 10014238 | 28 |
| Maxtor | 10020256 | 28 |
| Parian Development Group | 10021575 | 28 |
| Tatters | 10025213 | 28 |
| Ace Equipment | 10002153 | 29 |
| Cadtex | 10007309 | 29 |
| Fifth Moon | 10012157 | 29 |
| HarveyOpolis | 10014540 | 29 |
| Maxwell Laboratories | 10020266 | 29 |
| Password Busters | 10021641 | 29 |
| Teamaker | 10025239 | 29 |
| Acer | 10002154 | 30 |
| Cajun | 10007448 | 30 |
| Filene’s | 10012158 | 30 |
| HBS | 10014802 | 30 |
| Mb digital marketing | 10020281 | 30 |
| Patrick Townsend & Associates | 10021677 | 30 |
| Teammax | 10025241 | 30 |
| ACES Research | 10002155 | 31 |
| CalComp | 10007457 | 31 |
| Filetron | 10012161 | 31 |
| Hederman Brothers | 10015011 | 31 |
| McGraw-Hill Publishing Company | 10020306 | 31 |
| Patton Enterprises | 10021736 | 31 |
| Teamsolve | 10025242 | 31 |
| ACI | 10002159 | 32 |
| Caleidoscopio S.r.l. | 10007468 | 32 |
| Emergent | 10011345 | 32 |
| FIND/SVP | 10012305 | 32 |
| GateMaster | 10013332 | 32 |
| Hekimian Laboratories | 10015253 | 32 |
| Mead Corporation | 10020323 | 32 |
| Paul Budde | 10021750 | 32 |
| Todd Shipyards Corporation | 10025267 | 32 |
| ACME Laboratories | 10002161 | 33 |
| Calypso | 10007536 | 33 |
| Finder | 10012328 | 33 |
| Helfand Enterprises | 10015267 | 33 |
| Medics | 10020332 | 33 |
| PayMaxx | 10021794 | 33 |
| Transylvania Company | 10025288 | 33 |
| Acsior | 10002412 | 34 |
| Camelot IT | 10007591 | 34 |
| Finest Host | 10012369 | 34 |
| Helius | 10015325 | 34 |
| Melville Shoe Corporation | 10020340 | 34 |
| Payton Group International | 10021800 | 34 |
| UBF | 10025304 | 34 |
| Action Systems | 10002501 | 35 |
| Camros | 10007866 | 35 |
| Finisar | 10012399 | 35 |
| Hercules Incorporated | 10015686 | 35 |
| Mersey Docks | 10020364 | 35 |
| Pick Professionals | 10021802 | 35 |
| UK Total.net | 10025353 | 35 |
| ActivCard | 10002520 | 36 |
| Champion International | 10009606 | 36 |
| Firehole | 10012514 | 36 |
| hesketh.com | 10015789 | 36 |
| Nancy Leffingwell Enterprises | 10020449 | 36 |
| Picka | 10021804 | 36 |
| UKnames.net | 10025359 | 36 |
| Active | 10002526 | 37 |
| Dan River Mills, Inc. | 10009633 | 37 |
| FireTrans | 10012600 | 37 |
| Hewlett Packard | 10015886 | 37 |
| Nbase | 10020491 | 37 |
| PLAINFIELD ROOFING AND SHEET METAL | 10026438 | 37 |
| Ultimate Group | 10025392 | 37 |
| Aberdeen | 10000486 | 38 |
| Ad-vantage | 10003687 | 38 |
| Besicorp | 10004516 | 38 |
| Data General Corporation | 10009639 | 38 |
| ECS Associates | 10010865 | 38 |
| Galaxy Systems | 10012927 | 38 |
| G-Com International | 10013397 | 38 |
| Hidden Oak | 10015956 | 38 |
| Jones and Laughlin Steel Corporation | 10018363 | 38 |
| NBTel | 10020492 | 38 |
| One World | 10020868 | 38 |
| QualityLogic | 10022166 | 38 |
| Safe | 10023495 | 38 |
| Ultra-Image | 10025418 | 38 |
| Vectrix | 10026009 | 38 |
| Ad Agency | 10003554 | 39 |
| Day and Zimmermann, Inc. | 10009645 | 39 |
| G.R. Barron | 10012761 | 39 |
| Hill and Knowlton, Inc. | 10016113 | 39 |
| NBX | 10020515 | 39 |
| Quallaby | 10022167 | 39 |
| Underwriters Laboratories | 10025467 | 39 |
| Associates | 10003749 | 40 |
| Dayton Rubber Company | 10009650 | 40 |
| Gadzoox Microsystems | 10012792 | 40 |
| iBEAM | 10016780 | 40 |
| Nematron | 10020662 | 40 |
| Quantum | 10022201 | 40 |
| Universal Access | 10025608 | 40 |
| Beckman Instruments, Inc. | 10003857 | 41 |
| De Postel | 10009669 | 41 |
| Gaecom | 10012799 | 41 |
| Id | 10017290 | 41 |
| Oki | 10020672 | 41 |
| Rdlabs | 10022746 | 41 |
| Userland | 10025737 | 41 |

## How I built this

Do the following:

1. Import the data into Data manager.
2. Make the recommended associations between the two tables in Data manager.
3. Create two drill-down dimensions, one of State and County and one of State and City.
4. Add a map and in Presentation, set a Custom zoom level with a maximum zoom of 7x zoom.
5. Add a point layer with State -City as the dimension. Set the following properties:
   - In Location, set the scope to Custom and enter 'USA' in Country.
   - In Size & Shape, set Size by to Count(Distinct(Customer)).
   - In Colors, color by measure using Count(Distinct(Customer)).
   - In Options>Layer display, set Visible drill-down levels to Custom and select City.
6. Add an area layer with State-County as the dimension. Set the following properties:
   - In Location, set the scope to Custom, enter 'USA' in Country, and State in Administrative area (Level 1).
   - In Colors, color by measure using Count(Distinct(Customer)) and set the Opacity slider to 40%.
7. Center the region in the map and then set Limit pan navigation to Custom and click Set pan limit.
