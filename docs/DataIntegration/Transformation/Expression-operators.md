---
title: "Expression operators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Expression-operators.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets", "Building expressions"]
---

# Expression operators

Use operators to calculate values, compare inputs, and combine conditions when [*Building expressions*](Building-expressions.htm).

The following semantics apply to movement-task expressions. Expressions executed on a cloud data platform use that platform's semantics. Put spaces around operators and quote text and date constants, such as `$HIRE_DATE < '2026-10-08'`.

## Arithmetic operators

Arithmetic operations on numeric values

| Operator | Meaning | Example and result |
| --- | --- | --- |
| `+` | Adds the two operands. | `2 + 3` returns `5`. |
| `-` | Subtracts the right operand from the left. A leading minus negates a value. | `5 - 2` returns `3`. |
| `*` | Multiplies the operands. | `3 * 4` returns `12`. |
| `/` | Divides the left operand by the right. Integer division truncates toward zero. A real operand preserves a fractional result. Division by zero returns NULL. | `7 / 2` returns `3`; `7.0 / 2` returns `3.5`. |
| `%` | Converts both operands to integers and returns the division remainder. This is not a percentage calculation. | `7 % 3` returns `1`. |

## Comparison operators

Comparisons return 1 for true and 0 for false. Ordinary comparisons with NULL return NULL; use `IS` or `IS NOT` to test missing values.

Comparing two values

| Operator | Meaning | Example and result |
| --- | --- | --- |
| `=` | Tests equality. | `3 = 3` returns `1`. |
| `!=` | Tests inequality. | `3 != 4` returns `1`. |
| `<>` | Alternative inequality operator. | `3 <> 3` returns `0`. |
| `<` | Tests whether the left value is smaller. | `2 < 3` returns `1`. |
| `<=` | Tests less than or equal to. | `3 <= 3` returns `1`. |
| `>` | Tests whether the left value is larger. | `4 > 3` returns `1`. |
| `>=` | Tests greater than or equal to. | `3 >= 3` returns `1`. |
| `IS` | Tests equality without returning NULL. Two NULL values are equal; a NULL and a non-NULL value are not. | `NULL IS NULL` returns `1`. |
| `IS NOT` | Tests inequality without returning NULL. | `NULL IS NOT 3` returns `1`. |

## Logical and conditional operators

Combining conditions and selecting values

| Operator | Meaning | Example and result |
| --- | --- | --- |
| `AND` | True when both conditions are true. A false operand makes the result false even if the other operand is NULL. | `(3 > 2) AND (4 < 3)` returns `0`. |
| `OR` | True when either condition is true. A true operand makes the result true even if the other operand is NULL. | `(3 > 2) OR (4 < 3)` returns `1`. |
| `IN` | Tests membership in a parenthesized list. If no value matches and the list contains NULL, returns NULL. An empty list returns 0, including for a NULL left operand. | `2 IN (1, 2, 3)` returns `1`; `4 IN (1, NULL)` returns NULL. |
| `CASE` | Returns the first matching branch. With a base value, compares it to each WHEN value. Without one, tests each WHEN condition. Uses ELSE if no branch matches, or NULL if ELSE is absent. | `CASE WHEN 5 > 3 THEN 'High' ELSE 'Low' END` returns `'High'`. `CASE 2 WHEN 1 THEN 'One' WHEN 2 THEN 'Two' END` returns `'Two'`. |

## String and pattern operators

Joining text and matching patterns

| Operator | Meaning | Example and result |
| --- | --- | --- |
| `||` | Concatenates text values. A NULL operand produces NULL. | `'John' || ' ' || 'Smith'` returns `'John Smith'`. |
| `LIKE` | Compares the left string with the right pattern. `%` matches zero or more characters; `_` matches one. Ignores ASCII letter case by default, but not non-ASCII case differences. ESCAPE specifies a single character for literal wildcards. | `'Alice' LIKE 'A%'` returns `1`. `'10%' LIKE '10!%' ESCAPE '!'` returns `1`. |
| `GLOB` | Case-sensitive matching using Unix-style patterns. `*` matches zero or more characters, `?` matches one, and brackets define a character set. | `'file.csv' GLOB '*.csv'` returns `1`; `'File.CSV' GLOB '*.csv'` returns `0`. |
| `MATCH` | Delegates to the application-defined `match()` function. A usable implementation is required; the default SQLite implementation raises an error. | `'Quarterly sales' MATCH 'sales'` illustrates the syntax. The result depends on the application implementation. |
| `REGEXP` | Delegates to the application-defined `regexp()` function. SQLite does not provide this function by default. | `'ABC123' REGEXP '^[A-Z]+[0-9]+$'` illustrates the syntax. Without an implementation, evaluation fails. |

## Bitwise operators

These binary operators act on integer bits, not logical conditions. `|` means bitwise OR even if the editor also lists it in a logical category.

Integer bit operations

| Operator | Meaning | Example and result |
| --- | --- | --- |
| `<<` | Shifts the left integer left by the number of bits in the right operand. | `3 << 1` returns `6`. |
| `>>` | Shifts the left integer right by the number of bits in the right operand. | `8 >> 1` returns `4`. |
| `&` | Bitwise AND: sets a result bit only where both operands have that bit set. | `6 & 3` returns `2`. |
| `|` | Bitwise OR: sets a result bit where either operand has that bit set. | `6 | 3` returns `7`. |

## Evaluation order and missing values

For the binary operators above, precedence from highest to lowest is concatenation; multiplication, division, and remainder; addition and subtraction; bitwise operations; ordered comparisons; equality and pattern tests; AND; then OR. Operators at the same level evaluate left to right. Parentheses override this order: `(2 + 3) * 4` returns `20`, while `2 + 3 * 4` returns `14`.

Most operators return NULL when an operand is NULL. The exceptions described above include `IS`, `IS NOT`, and specific `AND`, `OR`, and `IN` cases. Use `$COALESCE` when a missing value should have a replacement. See [*Expression functions*](Expression-functions.htm).
