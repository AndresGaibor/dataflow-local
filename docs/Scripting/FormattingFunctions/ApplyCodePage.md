---
title: "ApplyCodepage Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/ApplyCodePage.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Formatting functions"]
---

# ApplyCodepage Script and chart function

ApplyCodepage() applies a different code page character set to the field
or text stated in the expression. The codepage argument must be in number format.

Information noteAlthough ApplyCodepage can be used in chart expressions, it is more commonly used as a script function in the [Data load editor](#glossary-0 "Glossary term"). For example, as you load files that might have been saved in different character sets out of your control, you can apply the code page that represents the character set you require.

Syntax:

ApplyCodepage(text, codepage)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | Field or text to which you want to apply a different code page, given by the argument codepage. |
| codepage | Number representing the code page to be applied to the [field](#glossary-1 "Glossary term") or expression given by text. |

Example: Load script

| Example | Result |
| --- | --- |
| LOAD  ApplyCodepage(ROWX,1253) as GreekProduct,  ApplyCodepage (ROWY, 1255) as HebrewProduct,  ApplyCodepage (ROWZ, 65001) as EnglishProduct;  SQL SELECT ROWX, ROWY, ROWZ From Products; | When loading from SQL the source might have a mixture of different character sets: Cyrillic, Hebrew, and so on, from the UTF-8 format. These would be required to be loaded row by row, applying a different code page for each row. The codepage value 1253 represents Windows Greek character set, the value 1255 represents Hebrew, and the value 65001 represents standard Latin UTF-8 characters. |

## Learn more

[*Character set*](../ScriptSpecifiers/character-set.htm)
