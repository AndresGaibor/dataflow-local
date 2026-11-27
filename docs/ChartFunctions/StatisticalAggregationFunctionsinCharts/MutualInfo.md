---
title: "MutualInfo - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/MutualInfo.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# MutualInfo - chart function

MutualInfo calculates the mutual information (MI) between two fields or between aggregated values in Aggr().

MutualInfo returns the aggregated mutual information for two datasets. This allows key driver analysis between a [field](#glossary-0 "Glossary term") and a potential driver. Mutual information measures the relationship between the datasets and is aggregated for (x,y) pair values iterated over the [chart](#glossary-1 "Glossary term") [dimensions](#glossary-2 "Glossary term"). Mutual information is measured between 0 and 1 and can be formatted as a percentile value. MutualInfo is defined by either [selections](#glossary-3 "Glossary term") or by a set expression.

MutualInfo allows different kinds of MI analysis:

- Pair-wise MI: Calculate the MI between a driver field and a target field.
- Driver breakdown by value: The MI is calculated between individual field values in the driver and target fields.
- Feature selection: Use MutualInfo in a grid chart to create a matrix where all fields are compared to each other based on MI.

MutualInfo does not necessarily indicate causality between fields sharing mutual information. Two fields may share mutual information, but may not be equal drivers for each other. For example, when comparing ice cream sales and outdoor temperature, MutualInfo will show mutual information between the two. It will not indicate if it is outdoor temperature driving ice cream sales, which is likely, or if it is ice cream sales that drives outdoor temperature, which is unlikely.

When calculating mutual information, associations affect the correspondence between and the frequency of values from fields that are from different tables.

Returned values for the same fields or selections may vary slightly. This is due to each MutualInfo call operating on a randomly selected sample and the inherent randomness of the MutualInfo algorithm.

MutualInfo can be applied to the Aggr() function.

Syntax:

MutualInfo({SetExpression}] [DISTINCT] [TOTAL] field1, field2 , datatype [, breakdownbyvalue [, samplesize ]])

Return data type: numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field1, field2 | The expressions or fields containing the two sample sets for which the mutual information to be measured. |
| datatype | The data types contained in the target and driver,  1 or 'dd' for discrete:discrete  2 or 'cc' for continuous:continuous  3 or 'cd' for continuous:discrete  4 or 'dc' for discrete:continuous  Data types are not case sensitive. |
| breakdownbyvalue | A static value corresponding to a value in the driver. If supplied, the calculation will calculate the MI contribution for that value. You can use ValueList() or ValueLoop(). If Null() is added, the calculation will calculate the overall MI for all values in the driver.  Breaking down by value requires the driver contain discrete data. |
| samplesize | The number of values to sample from the target and driver. Sampling is random. MutualInfo requires a minimum sample size of 80. By default, MutualInfo only samples up to 10,000 data-pairs as MutualInfo can be resource intensive. You can specify greater numbers of data-pairs in the sample size. If MutualInfo times out, reduce the sample size. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Limitations:

Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Function examples

| Example | Result |
| --- | --- |
| mutualinfo(Age, Salary, 1) | For a table including the dimension `Employee name` and the [measure](#glossary-4 "Glossary term") mutualinfo(Age, Salary, 1), the result is 0.99820986. The result is only displayed for the totals cell. |
| mutualinfo(TOTAL Age, Salary, 1, null(), 81) | If you create a filter pane with the dimension Gender, and make selections from it, you see the result 0.99805677 when Female is selected and 0.99847373 if Male is selected. This is because the selection excludes all results that do not belong to the other value of Gender. |
| mutualinfo(TOTAL Age, Gender, 1, ValueLoop(25,35)) | 0.68196996. Selecting any value from Gender will change this to 0. |
| mutualinfo({1} TOTAL Age, Salary, 1, null()) | 0.99820986. This is independent of selections. The set expression {1} disregards all selections and dimensions. |

Data used in examples:

Salary:

LOAD \* inline [

"Employee name"|Age|Gender|Salary

Aiden Charles|20|Male|25000

Ann Lindquist|69|Female|58000

Anna Johansen|37|Female|36000

Anna Karlsson|42|Female|23000

Antonio Garcia|20|Male|61000

Benjamin Smith|42|Male|27000

Bill Yang|49|Male|50000

Binh Protzmann|69|Male|21000

Bob Park|51|Male|54000

Brenda Davies|25|Male|32000

Celine Gagnon|48|Female|38000

Cezar Sandu|50|Male|46000

Charles Ingvar Jönsson|27|Male|58000

Charlotte Edberg|45|Female|56000

Cindy Lynn|69|Female|28000

Clark Wayne|63|Male|31000

Daroush Ferrara|31|Male|29000

David Cooper|37|Male|64000

David Leg|58|Male|57000

Eunice Goldblum|31|Female|32000

Freddy Halvorsen|25|Male|26000

Gauri Indu|36|Female|46000

George van Zaant|59|Male|47000

Glenn Brown|58|Male|40000

Harry Jones|38|Male|40000

Helen Brolin|52|Female|66000

Hiroshi Ito|24|Male|42000

Ian Underwood|40|Male|45000

Ingrid Hendrix|63|Female|27000

Ira Baumel|39|Female|39000

Jackie Kingsley|23|Female|28000

Jennica Williams|36|Female|48000

Jerry Tessel|31|Male|57000

Jim Bond|50|Male|58000

Joan Callins|60|Female|65000

Joan Cleaves|25|Female|61000

Joe Cheng|61|Male|41000

John Doe|36|Male|59000

John Lemon|43|Male|21000

Karen Helmkey|54|Female|25000

Karl Berger|38|Male|68000

Karl Straubaum|30|Male|40000

Kaya Alpan|32|Female|60000

Kenneth Finley|21|Male|25000

Leif Shine|63|Male|70000

Lennart Skoglund|63|Male|24000

Leona Korhonen|46|Female|50000

Lina André|50|Female|65000

Louis Presley|29|Male|36000

Luke Langston|50|Male|63000

Marcus Salvatori|31|Male|46000

Marie Simon|57|Female|23000

Mario Rossi|39|Male|62000

Markus Danzig|26|Male|48000

Michael Carlen|21|Male|45000

Michelle Tyson|44|Female|69000

Mike Ashkenaz|45|Male|68000

Miro Ito|40|Male|39000

Nina Mihn|62|Female|57000

Olivia Nguyen|35|Female|51000

Olivier Simenon|44|Male|31000

Östen Ärlig|68|Male|57000

Pamala Garcia|69|Female|29000

Paolo Romano|34|Male|45000

Pat Taylor|67|Female|69000

Paul Dupont|34|Male|38000

Peter Smith|56|Male|53000

Pierre Clouseau|21|Male|37000

Preben Jørgensen|35|Male|38000

Rey Jones|65|Female|20000

Ricardo Gucci|55|Male|65000

Richard Ranieri|30|Male|64000

Rob Carsson|46|Male|54000

Rolf Wesenlund|25|Male|51000

Ronaldo Costa|64|Male|39000

Sabrina Richards|57|Female|40000

Sato Hiromu|35|Male|21000

Sehoon Daw|57|Male|24000

Stefan Lind|67|Male|35000

Steve Cioazzi|58|Male|23000

Sunil Gupta|45|Male|40000

Sven Svensson|45|Male|55000

Tom Lindwall|46|Male|24000

Tomas Nilsson|27|Male|22000

Trinity Rizzo|52|Female|48000

Vanessa Lambert|54|Female|27000

] (delimiter is '|');

Related learning:

- [How do I evaluate relationships using Mutual information?](/lnk/How_evaluate_relationships_using_Mutual_information)
