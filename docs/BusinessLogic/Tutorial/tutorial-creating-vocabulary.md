---
title: "Creating vocabularies"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Tutorial/tutorial-creating-vocabulary.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Tutorial – Customizing how Insight Advisor interprets data"]
---

# Creating vocabularies

Vocabulary enables you to add terms for [Insight Advisor](#glossary-0 "Glossary term"). These can be used to server as synonyms for fields and values not present in the data, define custom analysis, and provide example questions for [Insight Advisor Search](#glossary-1 "Glossary term"). Vocabulary does not require you to have a custom [logical model](#glossary-2 "Glossary term").

With vocabularies, you can define synonyms, custom analysis, and example questions. With synonyms, you can add terms to define values or [selections](#glossary-3 "Glossary term") of values from your data model. With custom analyses, you can define the response from custom questions or partial questions and indicate the specific results returned by Insight Advisor. Example questions let you add default questions users can select in Insight Advisor Search to help guide analysis.

## Why create vocabularies?

Vocabulary is a key tool for preparing your app for natural language questions. Insight Advisor attempts to link all natural language questions to [field](#glossary-5 "Glossary term") names and values in your data. It cannot know all possible search terms that your app users might enter. Vocabulary lets you fill these terminology gaps, linking terms to fields and fields values.

For example, in the tutorial app, you have some products that are swimwear. These items are in the category Beachwear in the data. In Sheet, if you search for swimwear, you will not get any results. Similarly, you cannot search for footwear and get results for both men's and women's footwear.

Custom analyses are useful when you know what analyses you want your app consumers to receive based on their search terms. For example, you know that your app users have a preference to viewing regional data as maps. You can use a custom analysis to make sure that maps are offered when users include regional in their searches.

Example questions can be used to help encourage users in their analysis and help guide them to insights. Users may not know what is possible in your app. Example questions can help make their analyses and exploration an easier experience.

## Creating beachwear vocabulary

Do the following:

1. From the app navigation menu, click Vocabulary.
2. In Synonyms, click Create terms.
3. In Terms, enter the following terms:

   - swimwear
   - swimsuits
   - swimming suits
   - beach clothes
4. Under Applies to, select CategoryName.
5. Under Condition, select In.
6. Under In, select the following values:

   - Beachwear
7. Click Create.

## Creating footwear vocabulary

Do the following:

1. In Synonyms, click Create terms.
2. In Terms, enter footwear.
3. Under Applies to, select CategoryName.
4. Under Condition, select In.
5. Under In, select the following values:

   - men's footwear
   - women's footwear
6. Click Create.

## Creating regional custom analysis

For this custom analysis, you will not specify a [measure](#glossary-6 "Glossary term"). This will allow Insight Advisor to pick a measure based on how the someone uses regional in their question.

Do the following:

1. Click Custom analysis.
2. Click Create terms.
3. Under Terms, enter regional.
4. Under Analysis, select Breakdown (Geospatial).
5. In Data, under Geographicals, select Country.
6. Click Chart.
7. Under Chart type, select Map.
8. Click Create.

## Creating example questions

Do the following:

1. Click Example questions.
2. Click Add question.
3. Under Language, select your language.
4. Under Question, enter Who are the top customers for sales.
5. Click Add.

## Results

Navigate to Sheet and open Insight Advisor. Select the search box. Who are the top customers for sales is now available there. Search for what is the average freight for footwear. You now receive results for both men's and women's footwear.

Next, search for gross profit for swimwear in 2026. You now get results for beachwear while searching with swimwear.

Now, search for show me regional sales. You now get a map distribution of the sales by country.

## Thank you!

Now you have finished this tutorial, and hopefully you have gained some more knowledge about [business logic](#glossary-7 "Glossary term") and Insight Advisor in Qlik Sense.
