---
title: "Exploring applications with conversational analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/insights-chat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data"]
---

# Exploring applications with conversational analytics

Insight Advisor Chat is a chat-based interface for conversational analytics. Insight Advisor Chat lets you search for insights in any application you can access.

Insight Advisor Chat

![Insight Advisor Chat, showing a conversation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insight-chat-rev.png "Click to view full size")

Information note

Insight Advisor Chat is not available when a tenant is use the Qlik Answers agentic experience. Users can use Qlik Answers to explore applications with natural language.

## Opening Insight Advisor Chat

Do the following:

- Click ![Sparkle](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sparkle.svg) Ask Insight Advisor in the navigation bar.

The chat window opens as an overlay so you can continue your content navigation experience while maintaining the conversation with Insight Advisor Chat.

Click ![pin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pin_outline.svg) to pin the Insight Advisor Chat window. Pinning the window resizes the entire page so that your navigation experience is optimized. Clicking ![unpin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pin.svg) unpins the window.

Insight Advisor Chat window pinned as a sidebar while navigating content

![Insight Advisor Chat window pinned as a sidebar while navigating content](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insight-chat-experience-pinned.png "Click to view full size")

## Using Insight Advisor Chat

You can enter your question or you can click the microphone ![Microphone](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_microphone.svg) icon if your browser's voice-to-text capability is supported in Insight Advisor Chat.
You can select your chat language from the list of supported languages. Insight Advisor Chat questions that you enter are encrypted before they are persisted. Insight Advisor Chat returns applications that contain relevant results. When you select an application, Insight Advisor Chat provides a text response or [visualization](#glossary-1 "Glossary term"). Insight Advisor Chat may suggest further analyses for your question that create different visualizations. You can also ask follow up questions, such as in Germany or for 2019, and Insight Advisor Chat provides new results.

What you can search for and view from applications depends on the application and your [permissions](#glossary-2 "Glossary term") in that application's space.
For more specific information, see [*Application content availability in Insight Advisor Chat*](insight-advisor-available-chat.htm#App).

Information noteIf you need assistance, enter help.

To view and select from available options, click Apps, Dimensions, or Measures or enter Show apps, Show Dimensions, or Show measures. Dimensions and Measures display corresponding master dimensions and measures from an application. If an application has none, dimension and measure fields are displayed instead.

You can click Questions to view up to five random example questions from the applications to which you have access. You can click Questions again to refresh the list of questions. Clicking an example question enters the question into the chat where you can edit it before sending it.

You cannot make [selections](#glossary-3 "Glossary term") in visualizations as you can in an application. You can view tooltips for the visualizations and, depending on the data in the application, scroll through large [charts](#glossary-4 "Glossary term"). You can click Explore this further to view a visualization in Insight Advisor in the source application.

Applications must be enabled for insights if you want them to appear in Insight Advisor Chat. For more information, see [*Making applications available in Insight Advisor Chat*](insight-advisor-available-chat.htm#Enabling).

## Using natural language questions

Natural language questions and searches need to reference [field](#glossary-5 "Glossary term") names or synonyms for field names from the data model of applications.
You can view available applications by entering Show apps. You can view available dimensions and measures by typingshow dimensions and show measures. Clicking a dimension shows the first 10 values for that dimension. Clicking a measure applies that measure.

Natural language questions support three kinds of filters:

- Time: A unit of time or date. For example, Show me 2019 Sales.
- Category: A value from one of the dimensions. For example, Show me Sales by Product for Sweden.
- Measure: A value or values from a measure. For example, Show me Sales for Sweden by Product under 1K.

You can phrase your questions for facts, comparisons, and rankings.
Facts are statements such as What are my sales or Show expenses over time for 2019. You can ask for a comparison by adding vs or compare to your question. For example, Compare sales to expenses over time. You can ask for rankings by adding top  to your question. For example, Show me top 10 product by sales for 2020.

If an application defines time periods in the [load script](#glossary-6 "Glossary term"), [logical model](#glossary-7 "Glossary term"), or autocalendar, you can ask Insight Advisor for time period comparisons. You can ask for months, quarters, and years in comparisons. To ask for a comparison, use vs, over, against, or compare to in your question. For example:

- Sales for 2021 vs 2022
- Sales for 2021 over 2022
- Sales for 2021 against 2022
- Compare sales for 2021 to 2022
- Sales for 2021 compare to 2022

## Providing feedback

You can leave feedback on visualizations generated by Insight Advisor and Insight Advisor Chat. Feedback can be used by audit administrators to improve the user experience, through changes to the application's [business logic](#glossary-8 "Glossary term") or the data itself.

Click ![Thumbs up](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_like_outlined.svg) or ![Thumbs down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dislike_outlined.svg) on a chart generated by Insight Advisor Chat to provide feedback on the visualization. You can indicate a positive or negative response, and write a comment.

Dialog for providing feedback on Insight Advisor Chat analyses

![Feedback dialog for chart recommended by Insight Advisor Chat.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_iac-feedback-dialog.png "Click to view full size")

For more information, see [*Using feedback and usage metrics to improve application usability*](insight-advisor-usage-metrics.htm).

## Using Insight Advisor Chat through external collaboration platforms

For Qlik Cloud tenants, you can use Insight Advisor Chat to access conversational analytics in external collaboration platforms, such as Microsoft Teams. For more information, see [*Accessing Insight Advisor Chat through external collaboration platforms*](insight-advisor-chat-external.htm).

## Supported languages

The following languages are supported for natural language questions in Insight Advisor Chat:

- German
- English
- Spanish
- French
- Italian
- Dutch
- Polish
- Portuguese
- Swedish

For a list of supported example questions by language, see [*Supported questions by language*](insight-advisor-create-visualizations.htm#Supporte2).

### Language notes

The following limitations apply to language support in Insight Advisor Chat:

- In Spanish, field names and values containing letters with accents (á, é, í, ó, ú, ü, ñ,) or inverted punctuation marks (¿, ¡) are not treated as being the same as the same values without accents. For example:

  - México would not return results for Mexico, nor would Mexico return results for México.
  - Categorias would not return results for Categorías, nor would Categorías return results for Categorias.

  If you want terms recognized as equivalents, add them as synonyms in the application. For more information, see [*Adding synonyms to Insight Advisor*](../BusinessLogic/business-logic-vocabulary-synonyms.htm).
- Natural language responses in supported languages only provide a general statement when the question includes more than two filters or more than two data value filters on a dimension. The filters used are included in the response, however.
- Composite words containing field names are not supported for natural language questions in German, Dutch, and Swedish.

## Voice-to-text data transfer considerations

In many internet browsers, Insight Advisor voice-to-text search functionality uses the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) for external processing of voice-to-text data. This is used by both Insight Advisor Search and Insight Advisor Chat. The user’s internet browser may send the audio recorded by the browser API to an external source for transcription. Voice processing will be handled by the web service chosen by the user’s web browser. As a result, the captured information could be sent to a third-party server. The data is therefore not guaranteed to stay within the user’s Qlik region. Qlik is not responsible for the data processing by this third-party.

If users want to restrict this information flow to their relevant third-party browser (turn off the voice-to-text feature), this might be achieved through specific controls, including settings within their browser of choice and other security configurations.

## Permissions

Whether you are using Insight Advisor Chat from an activity center or through an external collaboration platform, your access is affected by administrator-assigned privileges (in the form of security roles and permissions) and space roles.

If your Qlik Cloud tenant is licensed for Qlik Answers and has turned on cross-region inference, Insight Advisor Chat will not be available. Use Qlik Answers with your application instead to explore your data and create sheets and visualizations.

### Administrator-assigned

Consider the following:

- To access Insight Advisor Chat within Qlik Cloud, a tenant administrator must assign you specific permissions. See:

  - [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm) (capacity-based subscriptions)
  - [*Default permissions and custom roles*](../Admin/permissions-scopes.htm) (user-based subscriptions)
  - [*Default permissions and custom roles*](../Admin/permissions-scopes-anonymous.htm) (Qlik Anonymous Access subscriptions)
- If you are accessing Insight Advisor Chat through an external collaboration platform, a tenant administrator needs to assign specific permissions to you. For more information, see [*Administration activity center requirements for Qlik Cloud administrators*](insight-advisor-chat-microsoft-teams.htm#MCAdmin).
- Administrator-assigned permissions—in particular, permissions for content download—can affect your access to Insight Advisor Chat. See:

  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes-capacity-model.htm#InApp) (capacity-based subscriptions)
  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes.htm#InApp) (user-based subscriptions)
  - [*'In-application content download' permission: Additional details*](../Admin/permissions-scopes-anonymous.htm#InApp) (Qlik Anonymous Access subscriptions)

### Space roles

For applications in collaborative spaces, space roles further govern your access to Insight Advisor Chat. For more information, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)

## Limitations

Insight Advisor Chat has the following limitations:

- The following charts do not support scroll bars and tool tips in Insight Advisor Chat:
  - Combo chart
  - Scatter plot
  - Waterfall chart
- Natural language responses are not available for questions with multiple dimensions or three or more measures.
- When using voice-to-text for natural language questions, your Insight Advisor language should match the language used in your data.
- Applications using Section Access require additional configuration for service users to make the applications available in Insight Advisor Chat. For more information, see [*Using Section Access and Insight Advisor Chat*](../Scripting/Security/manage-security-with-section-access.htm#Section). Applications using Section Access have the following limitations:

  - Application suggestions for your question include applications using Section Access from the spaces to which you have access. If you do not have access to those applications, selecting the applications will do nothing.
- Insight Advisor Chat displays applications enabled for chat in the hub from spaces that you can access.
  You must have permission in these spaces to view the applications. If you have Can manage permission in a [managed space](#glossary-9 "Glossary term"), but do not have Can view or Can contribute, you will see applications from that managed space in Insight Advisor Chat, but will not be able to see visualizations from them.
- New master dimensions, master measures, and business logic vocabulary added to applications are not available in Insight Advisor Chat until after the application reloads.
- If a field name contains only numerical values, that field will be used when generating results from a natural language search instead of a superlative (such as top or bottom with the same numerical value.

  For example, if you searched for top 3 service providers and one of your fields was named 3, 3 will be used in the results instead of the top 3 results for service providers.
- Time period comparisons have the following limitations:
  - An application must define time periods in the load script, logical model, or autocalendar to support time period comparisons.
  - For natural language questions or searches, such as year over year or month over month, the whole statement must be written out. Abbreviations such as YOY or MOM are not supported.
  - Time period comparisons only support up to one measure and one dimension in the natural language question.
- For information about supported analysis types for natural language insights, see [*Limitations*](insight-advisor-create-visualizations.htm#Limitati).
- English questions using the trend keyword with one measure and a time filter are not supported.

Related learning:

- [How do I make applications accessible to Insight Advisor in Qlik Cloud?](/lnk/How_make_apps_access_Insight_Advisor)
- [How do I use the Ask Insight Advisor applications button to get started?](/lnk/How_Ask_Insight_Advisor_button)
- [Using Insights to Create Visualizations](/lnk/Use-Insights-Create-Visualizations_QS)
