---
title: "AI processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-ai.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# AI processor

Uses generative AI functions from your third-party target data platform to transform the data.

The AI processor uses native generative AI model capabilities in your third-party target data platform. You can for example translate, classify, or summarize data in your transformation.

## Availability

AI processor capability is available for projects using the following target data platforms.

- Snowflake
- Databricks

Information noteThe available processor functions depend on availability in the target data platform. This means that if you use the AI processor, it is not possible to export the project and then import it to another project using a different data platform.

### Snowflake

AI processor capability is available for projects with Snowflake as target data platform, using Snowflake Cortex AI APIs.

Information noteFor more information about compute cost considerations when using Snowflake Cortex functions, see [Large Language Model (LLM) Functions (Snowflake Cortex)](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#label-cortex-llm-cost-considerations) .

The following functions are available:

- Analyze sentiment
- Classify
- Summarize
- Translate

For more information about the functions, see Snowflake documentation: [Available functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#available-functions).

### Databricks

AI processor capability is available for projects with Databricks as target data platform, using Databricks Foundation Model APIs. This Databricks capability is in Public Preview and can contain limitations, for example it is not supported on Databricks SQL Classic. For information about function specific limitations, see the link to Databricks documentation for each respective function.

See also [Databricks Previews support & details](https://docs.databricks.com/en/release-notes/release-types.html).

The following functions are available. Select which AI function to use in Function name.

- Analyze sentiment
- Classify
- Fix grammar
- Mask
- Similarity
- Summarize
- Translate

For more information about the functions, see Databricks documentation: [Alphabetical list of built-in functions](https://docs.databricks.com/en/sql/language-manual/sql-ref-functions-builtin-alpha.html).

## Analyze sentiment

Perform sentiment analysis on input text.

Available in: Databricks, Snowflake

### Input

Configuration of Analyze sentiment

| Property name | Configuration |
| --- | --- |
| Content | Select the column you want to perform sentiment analysis on. You can only select columns of string type. |
| Output column name | Enter a name for the generated output column.  The expected format is the following:   - must begin with [A-Za-z\_] characters. - can only contain [A-Za-z0-9\_] characters.   Example: ASDasd123\_4564 |
| Limit for preview | Set the number of rows to load in data preview. The default value is 10. If you set this to 0 there is no limit. |

### Output

Output of Analyze sentiment

| Target data platform | Configuration |
| --- | --- |
| Databricks | The sentiment is returned as a text string with the value of positive, negative, neutral, or mixed. If the sentiment cannot be detected, null is returned. |
| Snowflake | The sentiment is returned as a score between -1 to 1 for the given English-language input text.  -1 corresponds to the most negative sentiment, and 1 to the most positive sentiment. Values around 0 correspond to a neutral sentiment. |

## Classify

Classify input text according to labels you provide.

Available in: Databricks, Snowflake

### Input

Configuration of Classify

| Property name | Configuration |
| --- | --- |
| Content | Select the column you want to classify text for. You can only select columns of string type. |
| Classification labels | Add labels to use when classifying the data. Use plus to add more labels. You can use from 2 to 20 labels. |
| Limit for preview | Set the number of rows to load in data preview. The default value is 10. If you set this to 0 there is no limit. |

### Output

Output of Classify

| Target data platform | Configuration |
| --- | --- |
| Databricks | A text string is returned with the classification label matching the input string in Content. |
| Snowflake | A text string is returned with the classification label matching the input string in Content. |

## Fix grammar

Correct grammatical errors in a text column.

Available in: Databricks

### Input

Configuration of Fix grammar

| Property name | Configuration |
| --- | --- |
| Content | Select the column you want to fix grammar in. You can only select columns of string type. |
| Output column name | If you select Create a new column, you can enter a name for the generated output column.  The expected format is the following:   - must begin with [A-Za-z\_] characters. - can only contain [A-Za-z0-9\_] characters.   Example: ASDasd123\_4564 |
| Limit for preview | Set the number of rows to load in data preview. The default value is 10. If you set this to 0 there is no limit. |

### Output

Output of Classify

| Target data platform | Configuration |
| --- | --- |
| Databricks | A text string is returned with the grammar corrected. |

## Mask

Mask specified entities in a text column. Masked entities are replaced with [MASKED].

Available in: Databricks

### Input

Configuration of Mask

| Property name | Configuration |
| --- | --- |
| Content | Select the column you want to mask text entities in. You can only select columns of string type. |
| Mask labels | Add a label for each text entity that you want to mask. Use plus to add more labels. |
| Output column name | If you select Create a new column, you can enter a name for the generated output column.  The expected format is the following:   - must begin with [A-Za-z\_] characters. - can only contain [A-Za-z0-9\_] characters.   Example: ASDasd123\_4564 |
| Limit for preview | Set the number of rows to load in data preview. The default value is 10. If you set this to 0 there is no limit. |

### Output

Output of Classify

| Target data platform | Configuration |
| --- | --- |
| Databricks | A text string is returned with the specified entities masked. |

## Similarity

Compare two strings and computes the semantic similarity score.

Available in: Databricks

### Input

Configuration of Similarity

| Property name | Configuration |
| --- | --- |
| Content | Select the column you want to compare. You can only select columns of string type. |
| With | You can compare the text in Content with text from another string column or a value that you specify.   - Column  Select a column to compare with. You can only select columns of string type. - Value  Type a text value to compare with. |
| Output column name | Enter a name for the generated output column.  The expected format is the following:   - must begin with [A-Za-z\_] characters. - can only contain [A-Za-z0-9\_] characters.   Example: ASDasd123\_4564 |
| Limit for preview | Set the number of rows to load in data preview. The default value is 10. If you set this to 0 there is no limit. |

### Output

Output of Classify

| Target data platform | Configuration |
| --- | --- |
| Databricks | The score is returned as a float value between 0 and 1.0, where 1.0 means that the strings are equal. |

## Summarize

Generate a summary of the text in a text column.

Available in: Databricks, Snowflake

### Input

Configuration of Summarize

| Property name | Configuration |
| --- | --- |
| Content | Select the column you want to summarize. You can only select columns of string type. |
| Max word count | Set the maximum word count of the text summary. You can only set integer values.  The default value is 50. If you leave it empty or set it to zero, the maximum word count is not applied.  Information noteThis option is only available in Databricks. |
| Output column name | Enter a name for the generated output column.  The expected format is the following:   - must begin with [A-Za-z\_] characters. - can only contain [A-Za-z0-9\_] characters.   Example: ASDasd123\_4564 |
| Limit for preview | Set the number of rows to load in data preview. The default value is 10. If you set this to 0 there is no limit. |

### Output

Output of Summarize

| Target data platform | Configuration |
| --- | --- |
| Databricks | A text string is returned with a summary of the input string in Content. |
| Snowflake | A text string is returned with a summary of the input string in Content. |

## Translate

Translates the text content of a column.

Available in: Databricks, Snowflake

For information about supported languages, see reference documentation for the data platform.

### Input

Configuration of Translate

| Property name | Configuration |
| --- | --- |
| Content | Select the column you want to summarize. You can only select columns of string type. |
| Translate from | Select the language to translate from. You can also select to have the language auto-detected.  Available in: Snowflake |
| Translate to | Select the language to translate to. |
| Output column name | Enter a name for the generated output column.  The expected format is the following:   - must begin with [A-Za-z\_] characters. - can only contain [A-Za-z0-9\_] characters.   Example: ASDasd123\_4564 |
| Limit for preview | Set the number of rows to load in data preview. The default value is 10. If you set this to 0 there is no limit. |

### Output

Output of Translate

| Target data platform | Configuration |
| --- | --- |
| Databricks | A text string is returned with a translation of the input string in Content. |
| Snowflake | A text string is returned with a translation of the input string in Content. |

## Editing the processor

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
