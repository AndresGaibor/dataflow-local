---
title: "Creating bookmarks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Bookmarks/create-bookmark.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Bookmarking selections"]
---

# Creating bookmarks

[Bookmarks](#glossary-0 "Glossary term") let you save specific selection states. This allows you to review them later, and share them with other users.

Depending on the type of bookmark, not all bookmarks are rendered when you open the list of bookmarks you have created. The bookmarks are still available, and you can find them by searching by bookmark name.

Your bookmark can save selections of static field values, dynamic selections generated using [selection search](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/SelectionsToolbar/search-selections.htm), or both.

## Creating a bookmark

Do the following:

1. Make the [selections](#glossary-1 "Glossary term") on the [sheet](#glossary-2 "Glossary term") that you want to save as a bookmark. These selections can be static values you have selected manually, or values that dynamically change based on selection searches. For information about creating dynamic bookmarks with selection searches, see [*Working with dynamic bookmarks*](#DynamicBookmark).
2. Click Bookmarks in the assets panel.
3. Click Create new bookmark.
4. Title: By default, the name of the sheet and a summary of the selections are used as the title of the bookmark. You can change this if needed.

   Information noteDo not use a name already used by an alternate state.
5. Description: You have the option to enter a description of the bookmark.
6. Save sheet location: Toggle this on if you want the bookmark to switch to the sheet that was open when it was created. Toggling it off means that the user will stay in their current sheet when the bookmark is applied.

   Information noteIf the target sheet that was saved with this setting is deleted or is a private sheet, applying the bookmark will not open that sheet. The selections associated with this bookmark will still be applied to the application.
7. Save layout: Toggle this on if you want to save chart layouts, sorting, or expansions. Save layout does not include scrolling or position of visualizations.
8. Save all variable states: Toggle this on to save the current values of [variables](#glossary-4 "Glossary term") in the bookmark.

   Instead of using this setting, it is recommended that variable states in bookmarks be controlled by application creators on a variable by variable basis. For more information, see [*Including variable states in bookmarks and reports*](../Variables/using-variables-with-bookmarks.htm).

   Information note

   Variable states can still be included if Include in bookmarks is set on the variable by the application creator. For more information, see [*Including variable states in bookmarks and reports*](../Variables/using-variables-with-bookmarks.htm).

   Information note
   Variables created in the load script cannot have their state saved in bookmarks using Save all variable states.
    For more information, see [*Including variable states in bookmarks and reports*](../Variables/using-variables-with-bookmarks.htm).
9. Click Create.

## Working with dynamic bookmarks

You can create bookmarks with dynamic selection states. For example, rather than selecting the Region values Europe and Asia as static values, your bookmark could select all Region values that have total sales greater than $1,000,000.00.

Dynamic bookmarks allow you to capture realistic data filtering. A common example is selecting the current time period—for example, the current quarter or year—without hard-coding specific values.

Dynamic bookmarks are created using selection searches. For more information, see [*Searching within selections or visualizations*](../Selections/SelectionsToolbar/search-selections.htm).

### Creating a dynamic bookmark

Use the selections tool to create a dynamic bookmark. For more information about the selections tool, see [*Using the selections tool*](../Selections/use-selection-tool.htm).

Do the following:

1. In sheet view in analysis mode, click ![Selections tool](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_tool.svg) in the toolbar. The selections tool opens.
2. In the App dimensions section, find a dimension for which you want to create a dynamic bookmark. You can use one of the master dimensions listed by default, or turn on Show fields to use any dimension in the data model.
3. In the listbox for the dimension, click ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg).
4. Type a selection search. The search needs to result in at least one selection when creating the dynamic bookmark.

   Examples:

   ```
   =YearMonth>=Quarterstart(Now(),-1)
   ```

   ```
   =Sum(Sales)>1000000
   ```

   ```
   =ShippedStatus<>'Shipped'
   ```

   Your selection search can use text, numeric, expression, or compound search. For more information, see [*Searching within selections or visualizations*](../Selections/SelectionsToolbar/search-selections.htm).
5. Press Enter on your keyboard. This applies the selection search, creating a dynamic selection state.
6. If desired, you can add additional selection searches—or static field selections— to the bookmark definition. Repeat the steps above to add more selection searches, or select static field values using any selection method.
7. Click Bookmarks in the assets panel.
8. Click Create new bookmark.
9. Configure the settings for the new bookmark. For details about specific settings, see [*Creating a bookmark*](#Creating).
10. Click Create.

### Other ways to create dynamic bookmarks

You can also create a dynamic bookmark using any other method of selection search. This includes:

- Using a table-based visualization — specifically, the Table, Straight table, Pivot table, or Pivot table (Visualization bundle).
- Using any visualization that supports the View data feature.

However, because visualizations are often already configured with a limited data set, searching in selections in this way might not always result in at least one selection. For this reason, the easiest way to create a dynamic bookmark is using the selections tool.

## States and set expressions

When creating or editing a bookmark, you will see the possible alternate states that have been bookmarked. If a state includes selections, then the set expression for the selections is also shown.

You can copy the set expression by clicking Copy.

Information noteIf the bookmark selection includes a calculated [dimension](#glossary-5 "Glossary term") the set expression will show MISSING VALUES and cannot be used.

## Bookmark options

In sheet view, if you right-click on a bookmark, you will see the following options:

- Apply bookmark: The selections saved in the bookmark are applied and the sheet which the bookmark originates from is displayed. Any previous selections are cleared.
- Apply selections only: The selections saved in the bookmark are applied. Any previous selections are cleared.
- Make public: Making a bookmark public means that anyone can use it. You will no longer be the owner of the bookmark.
- Make private: Making a bookmark private returns it to the original owner's private bookmarks.
- Details: Displays location, layout state, and set expressions.
- Copy link: Copies the bookmark location so it can be shared.
- Set as default bookmark: When the application is opened, the layout state and the selection state of the default bookmark are used, instead of the application overview page. See [*Setting a default bookmark to create an application landing page*](set-default-bookmark.htm).
- Delete: The bookmark is deleted.

## Searching for bookmarks

Do the following:

1. In a sheet, click Bookmarks in the asset panel.
2. Type your search criteria in the search field.

   The list is filtered as you type.

Tip noteWhen you search in bookmarks, Qlik Sense looks for matches in titles and descriptions.

## Changing the title and description of a bookmark

You can change the title and description of a bookmark.

Do the following:

1. In a sheet, click Bookmarks in the asset panel.
2. Under My own, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the bookmark you want to edit and select Details.
3. Click Edit details.
4. Make your changes to Title and Description.
5. Click Done.

The changes are automatically saved.

Tip noteYou can also edit bookmarks from the application overview using the same procedure.

## Updating selections in private bookmarks

You can change the selections in a private bookmark, if the application is in a personal or shared space.

Do the following:

1. Make new [selections](#glossary-6 "Glossary term") on the [sheet](#glossary-7 "Glossary term") that you want to save as a bookmark.

   These new selections will completely override the selections in the original bookmark.
2. In a sheet, click Bookmarks in the asset panel.
3. Under My own, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the bookmark you want to edit and select Details.
4. Click Update bookmarks.
5. Click Confirm.

Your bookmark has been updated.

## Changing who can see the bookmark

Who can see your bookmark depends on the type of space in which its associated application is located, as well as whether the bookmark is public or private. Bookmark content might only be partially accessible to other users if the bookmark has been associated with a private sheet using the Save sheet location setting.

For more information, see [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm).

Public bookmarks can be grouped, allowing you to organize your bookmarks. For more information, see [*Grouping bookmarks*](grouping-bookmarks.htm).

### Personal space

Bookmarks within applications in your [personal space](#glossary-8 "Glossary term") cannot be viewed or applied by other users.

### Shared spaces

In [shared spaces](#glossary-9 "Glossary term"), private bookmarks can be made visible to others by right-clicking the bookmark and selecting Make public.

You or another space member with sufficient [permissions](#glossary-10 "Glossary term") can make the bookmark private by right-clicking it and selecting Make private.

To make private sheets, sheet groups, bookmarks, and stories public, you need one of the following roles in the shared space:

- Owner
- Can manage
- Can edit

In user-based subscriptions, these permissions apply only to users with a Professional user entitlement.

For more information, see [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm).

Here are some additional considerations for public bookmarks in a [shared space](#glossary-11 "Glossary term"):

- If you apply the setting Save sheet location when you create the bookmark, and its target sheet is public, space members and users with application-only access are brought to that sheet when they open the bookmark, in addition to applying the bookmarked selections to the application. If this setting is turned off, applying the bookmark will still apply the selections associated with the bookmark.
- Bookmarks save selection states and, optionally, information about the sheet you use to create them. Therefore, you can create a public bookmark using a private sheet and other users will be able to apply the bookmark's selections. They will not, however, be able to see the private sheet.

### Managed spaces

In an application published to a [managed space](#glossary-12 "Glossary term"), you can publish your private bookmarks to the Community by right-clicking the bookmark and selecting Publish. In a managed space, you need one of the following space roles to publish your private bookmarks to the Community:

- Owner
- Can manage
- Can contribute

You, as well as other managed space members with either the Owner or Can manage space role, can make a Community bookmark private again by right-clicking it and selecting Unpublish.

In user-based subscriptions, these permissions apply only to users with a Professional user entitlement.

For more information, see [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm).

Here are some additional considerations for bookmarks in a managed space:

- When an application is published from a shared to a managed space, all sheets, bookmarks, and [stories](#glossary-13 "Glossary term") that are public in the source application will become public content in the published application. Bookmarks that are private at the time when the application is published are not accessible in the published application.
- Public bookmarks cannot be changed into Community bookmarks.
- If you apply the setting Save sheet location when you create a public or Community bookmark, and its target sheet is a public or Community sheet, space members and users with application-only access are brought to that sheet when they open the bookmark. Whether this setting is toggled on or off, applying the bookmark will always apply the selections associated with the bookmark.
- Bookmarks save selection states and, optionally, information about the sheet you use to create them. Therefore, you can create a Community bookmark using a private sheet and other users will be able to apply the bookmark's selections. They will not, however, be able to see the private sheet unless it is published to the Community.

## Limitations

- Depending on the type of bookmark, not all bookmarks are rendered when you open the list of bookmarks you have created. The bookmarks are still available, and you can find them by searching by bookmark name.
- Bookmarks in Direct Query applications work differently. For more information, see [*Bookmark limitations*](../DirectQuery/limitations-direct-query.htm#Bookmarks).

## Learn more

- [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm)
- [*Set analysis*](../ChartFunctions/SetAnalysis/set-analysis-expressions.htm)
- [*Using alternate states for comparative analysis*](../Visualizations/alternate-states-comparative-analysis.htm)
- [Create and apply bookmarks](/lnk/Create_Apply_Bookmarks_QS)

Related learning:

- [Create and apply bookmarks](/lnk/Create_Apply_Bookmarks_QS)
