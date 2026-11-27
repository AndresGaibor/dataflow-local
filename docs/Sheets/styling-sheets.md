---
title: "Styling sheets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/styling-sheets.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with sheets"]
---

# Styling sheets

You can customize the style of your [sheet](#glossary-0 "Glossary term") changing the title and description, adding conditions for when the sheet displays in the application and adding sheet thumbnails.

## Changing the title and description of a sheet

You can change the title and description of your sheets. You can either use a fixed sheet title, or a dynamic sheet title based on an expression.

Do the following:

1. In the application overview, click ![App objects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sheet2.svg) to view the sheets.
2. Do one of the following:
   - If you are in grid view, ![Grid View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid.svg), click the sheet title followed by clicking ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit.svg).
   - If you are in list view, ![List view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list.svg), click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit.svg).
3. Edit Title and Description.
4. Click outside the text area.

The changes you made are saved.

Tip noteYou can also change a sheet’s title and description in the Sheet properties panel.

### Using a dynamic sheet title

You can set a dynamic sheet title based on an expression in the Title expression property of the sheet properties panel. You can use any valid chart expression. For more information, see [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm).

If you set a dynamic sheet title, the fixed title (Title) is not used.

[Creating dynamic sheet titles using expressions](https://share.vidyard.com/watch/5uRpbAWBn8RRWqoo4G4ndh)

## Hiding toolbar, sheet header, and application navigation bar options

You can hide the toolbar and sheet header in your application. This means that these areas will not display on any sheet, for any user, regardless of permissions. Any user with Can edit rights in the application can toggle these elements on or off. You can also hide individual elements in your application navigation bar, toolbar, and sheet header.

### Toolbar

The toolbar is the area above the sheet that contains the following buttons:

- Assets
- Sheets
- Bookmarks
- Insight Advisor
- Smart search (![Smart search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_search.svg))
- Selection buttons:

  - Step back selection (![Step back](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_back.svg))
  - Step forward selection (![Step forward](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_forward.svg))
  - Clear all selections (![Clear all selections](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_clear_selections2.svg))
- Selections tool (![Selections tool](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_tool.svg))
- Edit sheet

You can optionally hide Assets, Sheets, and Bookmarks buttons to the toolbar. If you remove Assets, Sheets and Bookmarks will display without the assets panel.

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
2. In the menu, switch to the UI settings tab.
3. Do one of the following:

   - To hide the toolbar, turn off Toolbar.
   - To hide Assets, under Toolbar, select Assets.
   - To hide Sheets, under Toolbar, select Sheets.
   - To hide Bookmarks, under Toolbar, select Bookmarks.
4. Click Done.

### Sheet header

The sheet header is the area on the sheet that contains the sheet title, title image, and the sheet navigation arrows.

If you hide the sheet header, the navigation arrows move to the toolbar.

You can optionally hide the sheet title.

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
2. In the menu, switch to the UI settings tab.
3. Do one of the following:

   - To hide the sheet header, turn off Sheet header.
   - To hide the sheet title, under Sheet header, select Sheet title.
4. Click Done.

### Application navigation bar

You can optionally hide the following options in the application navigation bar for your application:

- Logo
- Navigation
- Ask Insight Advisor
- Resource center
- Notifications
- Profile

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
2. In the menu, switch to the UI settings tab.
3. Under App navigation bar, select the options you want to hide in the application navigation bar.
4. Click Done.

### When to hide application interface elements

#### Advantages

Hiding the toolbar and sheet headers creates more space for charts, filter panes, and other objects.

Turning off sheet headers means that this area will not appear when you download or share sheets, send subscriptions, or generate Qlik Automate reports. This is helpful if you are using your sheets to create PowerPoint presentations or dashboards.

Removing the toolbar means application developers have more control over which features other users can access easily. For example, hiding the Edit sheet button might discourage other application developers from editing the application.

#### Disadvantages

Hiding the toolbar does not completely remove capabilities such as bookmarks, notes, Insight Advisor, or sheet editing. For example, bookmarks can still be found in the application overview. However, application consumers may think that these features are no longer available.

If you hide the toolbar and sheet header, the only way to navigate between sheets is by using keyboard shortcuts or button objects. For more information, see [*Keyboard navigation and shortcuts in apps*](../UserInterface/keyboard-navigation-and-shortcuts.htm) and [*Creating buttons*](../Visualizations/Button/create-buttons.htm).

If the selections area is hidden, users may not realize that selections have been applied to the application. You may need to add filter panes to your sheets or filters to individual charts. For more information, see [*Creating filter panes*](../Visualizations/FilterPane/create-filter-panes.htm) and [*Applying filters to visualizations*](visualization-filters.htm).

### Examples

A sheet displaying the toolbar and sheet header. The toolbar shows Notes, Insight Advisor, current selections, and more. The sheet header contains the title image, sheet title, and navigation arrows.

![A Qlik Sense sheet where the toolbar and sheet header are visible at the top.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DashboardSheet_HeaderandToolbar_shown-dev-rev.png "Click to view full size")

The same sheet as above, but the toolbar is visible and the sheet header is hidden. Users can no longer see the title image, sheet title, or navigation arrows.

![A Qlik Sense sheet where sheet header is hidden.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DashboardSheet_Toolbar_shown-rev2.png "Click to view full size")

The same sheet as above, but the sheet header is visible and the toolbar is hidden. Users cannot see which selections have been applied.

![A Qlik Sense sheet where sheet header is hidden. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DashboardSheet_Header_shown-rev2.png "Click to view full size")

The same sheet as above, but the header and toolbar have both been hidden.

![A Qlik Sense sheet where both the toolbar and sheet header are hidden. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DashboardSheet_HeaderandToolbar_allhidden-rev2.png "Click to view full size")

## Adding custom logos

You can add custom logos to application navigation bars. These replace logos set in the navigation bar of tenants.

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg)Settings.
2. In the menu, switch to the UI settings tab.
3. Under App navigation bar, click ![Palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette_outline.svg).
4. Under Logo, click ![Palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg).
5. Select an existing image or upload a new image.
6. Click Insert.

## Styling the application navigation bar

You can style the navigation bar in the application with custom colors.

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
2. In the menu, switch to the UI settings tab.
3. Under App navigation bar, click ![Palette](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette_outline.svg).
4. Under Options, set the Background color and Foreground color.
5. Click Done.

## Setting a show condition for a sheet

You can set a condition in Show condition to show or hide a sheet in an application depending on if an expression evaluates as true or false. The sheet is only shown if the expression evaluates as true. Hiding a sheet does not hide or exclude data in an application.

For example, you could create a sheet that is only available if certain values are present in your data. Typically, you should use an if function. For more information, see [*if Script and chart function*](../Scripting/ConditionalFunctions/if.htm).

[Setting a show condition for a sheet](https://share.vidyard.com/watch/MkupcjehFZn4j4w83eGgKU)

## Changing the sheet thumbnail

You can replace the default thumbnail, to make it easier to distinguish between sheets in the application overview and in the assets panel. You can generate an image of the sheet, use one of the default images, or use an image of your own.

Note the following:

- The following formats are supported: .png, .jpg, .jpeg, and .gif.
- The optimal aspect ratio of a thumbnail is 8:5 (width:height).
- You can only add or change the thumbnail of a private sheet.

Do the following:

1. In the application overview, click ![App objects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sheet2.svg) to view the sheets.
2. Do one of the following:
   - If you are in grid view, ![Grid View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid.svg), click the sheet title followed by clicking ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit.svg).
   - If you are in list view, ![List view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list.svg), click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit.svg).
3. Do one of the following:
   - If you want to generate a thumbnail based on the sheet, click ![Generate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_camera2.svg).
   - If you want to select a thumbnail image, do the following:

     1. Click ![Image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the default thumbnail.
     2. The Media library opens.
     3. Select the image you want to use as a thumbnail for the sheet and click Insert.
     4. Click ![Checkmark](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg) to stop editing.

The image you selected is now used as a thumbnail for the sheet, and is visible in the assets panel and in the application overview.

Tip noteYou can also change a sheet’s thumbnail in the assets panel or in the Sheet properties panel.

Fore more information, see [Managing a Qlik Sense site: Uploading objects to content libraries](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Administer_QSEoW/Managing_QSEoW/upload-objects-to-content-libraries.htm).

Govnote-not-inNot supported in Qlik Cloud Government.

## Adding a background color or image

You can customize the background of a sheet. You can choose a specific background color, or color by expression. Any image in the media library can be set as a background. The image can be positioned and resized so it does not fill the entire background.

The following formats are supported: .png, .jpg, .jpeg, and .gif. If you use a .gif, it can be animated or static.

Qlik Cloud Government note

Qlik Cloud Government does not support background images or colors in sheets.

Do the following:

1. Open the sheet in Edit mode.
2. Under Sheet properties, click Styling.
3. Set Background to Custom. The default is Auto.
4. Background color:

   - Single color: Choose a color using the color picker.
   - By expression: Set a color using a user-defined expression. For more information, see [*Color by expression*](../Colors/color-by-expression.htm).
5. Background image: Select Image from media library. The default is None.
6. Click ![Image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) on the default thumbnail.

   The Media library opens.
7. Select the image you want to use and click Insert.

   If the image you want is not already in the media library, click New upload and add the image.
8. Use the drop down to change the size of your image:
   - Original size
   - Always fit
   - Fit to width
   - Fit to height
   - Stretch to fit
   - Always fill
9. Under Position, you can change the alignment of the image. For example, the image can be centered on the sheet, or in the top-right corner.

The image and background color you selected is now visible on the sheet.

Sheet in Edit mode, with a background image set on the left

![A sheet in Edit mode. A decorative background image has been set to fill the left side of the sheet.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_sheet-background-image.png "Click to view full size")

## Customizing sheet styling with CSS

You can customize the styling of individual sheets with CSS. This can help supplement custom themes by allowing you to customize elements not covered by themes. Customized sheet styling can also be used to override any styling from the themes applied in the application.

Warning note

It is recommended that the use of CSS sheet styling be minimized as much as possible. It is recommended to use the available styling properties and styling options wherever possible instead of custom CSS.

CSS styling is best used only when there are no other options available. The CSS structure of any sheet is not static, it is not an API, and may change at any time. Keep CSS styling to a minimum, ensure it is correct, and make sure that it is easy to modify if a change happens that breaks it.

Custom CSS styling applied to sheets is not included in reports.

For more about custom themes, see [*Custom themes*](../Apps/style-app.htm#Custom).

Do the following:

1. Open the sheet in Edit mode.
2. Under Sheet properties, click Styling.
3. Set Custom styles to Activated.
4. Enter your CSS styling in the input box.

### Limitations

Custom CSS styling for sheets has several limitations. Added CSS is parsed and sanitized to remove and ignore any elements that would hide or break application functionality. You will be notified if you enter unsupported CSS. The following outlines some of the limitations when using CSS to style sheets:

- font-size cannot be larger than 18 px.
- HTML tags are not supported.
- The following selectors are not allowed:

  - Pseudo-selectors
  - Root selectors
  - \* selectors
- The following @rules are not supported:

  - charset
  - color-profile
  - counter-style
  - font-face
  - font-feature-values
  - font-palette-values
  - import
  - keyframes
  - media
  - namespace
  - page
  - position-try
  - property
- Injection is not allowed.
- display:none is only supported for custom user-defined elements or classes.
- Comments are not applied.
- Custom CSS styling is not supported by applications in the Qlik Analytics mobile app.
- Custom CSS styling applied to sheets is not included in reports.
