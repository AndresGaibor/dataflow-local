---
title: "Expression functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Expression-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets", "Building expressions"]
---

# Expression functions

Use functions to transform row values, handle missing data, or retrieve related values when building expressions. For details, see [*Building expressions*](Building-expressions.htm).

The functions below describe movement-task expressions in SaaS-managed landing, lake landing, and replication tasks. Use the function signature displayed in your editor. Square brackets in signatures indicate optional arguments; do not enter the brackets.

For CDC Storage and Streaming Transform functions, see [*Transformation functions*](../Lakehouse/transformation-functions.htm). For storage, transform, and data mart expressions executed on a cloud data platform, use that platform's function syntax.

## String functions

Prefix and suffix functions act on the beginning or end of a string. Character replacement acts on individual characters instead of matching a whole prefix or suffix.

String function arguments, behavior, and examples

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$CONCAT(X, Y)` | Joins the two strings `X` and `Y`, in that order. Returns NULL if either argument is NULL. Nest calls to join more than two strings. | `$CONCAT('My', 'Picture')` returns `'MyPicture'`. `$CONCAT('My', NULL)` returns NULL. |
| `$INSTR(string, substring)` | Returns the one-based position of the first occurrence of `substring` in `string`. Returns 0 if the substring is not found. | `$INSTR('mystring', 'ing')` returns `6`. `$INSTR('mystring', 'xyz')` returns `0`. |
| `$LENGTH(string)` | Returns the number of characters in `string`, not its size in bytes. | `$LENGTH('mystring')` returns `8`. |
| `$LOWER(string)` | Returns a copy of `string` with ASCII letters converted to lowercase. | `$LOWER('ABC')` returns `'abc'`. |
| `$LTRIM(string[, characters])` | Removes characters from the beginning of `string`. The optional `characters` argument is a set of characters to remove, not a prefix. If omitted, removes spaces. | `$LTRIM(' orders')` returns `'orders'`. `$LTRIM('@@orders', '@')` returns `'orders'`. |
| `$REMOVE_PREFIX(string, prefix)` | Returns a copy of `string` with the specified beginning `prefix` removed. | `$REMOVE_PREFIX('mystring', 'my')` returns `'string'`. |
| `$REMOVE_SUFFIX(string, suffix)` | Returns a copy of `string` with the specified ending `suffix` removed. | `$REMOVE_SUFFIX('mystring', 'ing')` returns `'mystr'`. |
| `$REPLACE(string, pattern, replacement)` | Replaces every occurrence of `pattern` in `string` with `replacement`. All three arguments are required. Use an empty replacement string to remove matching text. | `$REPLACE('a-b-c', '-', '_')` returns `'a_b_c'`. `$REPLACE('a-b', '-', '')` returns `'ab'`. |
| `$REPLACE_CHARS(string, chars, replacement)` | Replaces each character listed in `chars` with the character at the same position in `replacement`. Unlisted characters remain unchanged. If a replacement position is missing, the first replacement character is used. | `$REPLACE_CHARS('mystring', 's', 'z')` returns `'myztring'`. `$REPLACE_CHARS('abcde', 'abcd', '123')` returns `'1231e'`. |
| `$REPLACE_PREFIX(string, prefix, replacement)` | Replaces the beginning `prefix` in `string` with `replacement`. | `$REPLACE_PREFIX('mystring', 'my', 'new')` returns `'newstring'`. |
| `$REPLACE_SUFFIX(string, suffix, replacement)` | Replaces the ending `suffix` in `string` with `replacement`, rather than replacing every occurrence. | `$REPLACE_SUFFIX('mystring', 'ing', 'new')` returns `'mystrnew'`. |
| `$RTRIM(string[, characters])` | Removes characters from the end of `string`. The optional `characters` argument is a set of characters to remove, not a suffix. If omitted, removes spaces. | `$RTRIM('orders ')` returns `'orders'`. `$RTRIM('orders@@', '@')` returns `'orders'`. |
| `$SUBSTR(string, start[, length])` | Extracts text from `string`, starting at the one-based position `start`. `length` specifies the number of characters. If omitted, returns the remaining characters. | `$SUBSTR('abcdef', 2, 3)` returns `'bcd'`. |
| `$TRIM(string[, characters])` | Removes characters from both ends of `string`. The optional `characters` argument is a set of characters to remove, not a substring. If omitted, removes spaces. | `$TRIM(' orders ')` returns `'orders'`. `$TRIM('@#orders#@', '@#')` returns `'orders'`. |
| `$UNICODE(string)` | Returns the numeric Unicode code point of the first character in `string`. The argument must be a string. | `$UNICODE('ABC')` returns `65`. |
| `$UPPER(string)` | Returns a copy of `string` with ASCII letters converted to uppercase. | `$UPPER('abc')` returns `'ABC'`. |

## Numeric functions

Use these functions to calculate numeric values for the current row. `$MAX` and `$MIN` compare arguments within the row, not values across rows.

Numeric function arguments, behavior, and examples

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$ABS(X)` | Returns the absolute value of the numeric argument `X`. | `$ABS(-20)` returns `20`. |
| `$MAX(arg1, arg2, ...)` | Returns the largest value among the supplied numeric arguments. Supply at least two arguments. | `$MAX(10, 4, 20, 9)` returns `20`. |
| `$MIN(arg1, arg2, ...)` | Returns the smallest value among the supplied numeric arguments. Supply at least two arguments. | `$MIN(10, 4, 20, 9)` returns `4`. |
| `$RANDOM()` | Returns a pseudorandom signed integer. Takes no arguments. | `$RANDOM()` returns an integer that can be negative, zero, or positive. Its value varies between calls. |
| `$ROUND(value[, digits])` | Rounds `value` to `digits` decimal places and returns a floating-point value. If `digits` is omitted, rounds to zero decimal places. | `$ROUND(3.141592, 3)` returns `3.142`. |

## LOB functions

These functions work with binary large objects (BLOBs). The size argument `N` specifies bytes, not characters.

Binary value functions

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$HEX(blob)` | Returns uppercase hexadecimal text representing the bytes of `blob`. Numeric input is first converted to text; the result is not the number's machine representation. | `$HEX(X'4142')` returns `'4142'`. |
| `$RANDOM_BLOB(N)` | Returns `N` pseudorandom bytes. If `N` is less than 1, returns one byte. Do not use this function as a guarantee of cryptographic randomness. | `$RANDOM_BLOB(4)` returns a four-byte BLOB. Its value varies between calls. |
| `$ZERO_BLOB(N)` | Returns a BLOB containing `N` zero bytes. | `$HEX($ZERO_BLOB(3))` returns `'000000'`. |

## Null check functions

Null check function arguments, behavior, and examples

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$COALESCE(X, Y, ...)` | Returns the first non-NULL argument, in argument order. Supply at least two arguments. If all arguments are NULL, the result is NULL. An empty string is not NULL. | `$COALESCE(NULL, 'Unknown')` returns `'Unknown'`. `$COALESCE('', 'Unknown')` returns an empty string. |
| `$IFNULL(X, Y)` | Returns `X` if it is not NULL; otherwise, returns `Y`. Returns NULL if both arguments are NULL. Supply exactly two arguments. | `$IFNULL(NULL, 'Unknown')` returns `'Unknown'`. `$IFNULL('Known', 'Unknown')` returns `'Known'`. |
| `$NULLIF(X, Y)` | Returns NULL if `X` and `Y` are equal; otherwise, returns `X`. Supply exactly two arguments. | `$NULLIF('Unknown', 'Unknown')` returns NULL. `$NULLIF('Known', 'Unknown')` returns `'Known'`. |

## Date and time functions

Supply a date, time, or datetime string such as `'2026-10-08'`, `'12:34:56'`, or `'2026-10-08 12:34:56'`. Keep date constants in quotes so that hyphens are not interpreted as subtraction.

Date calculation and formatting

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$DATE(date_string)` | Returns the date from `date_string` as text in `YYYY-MM-DD` format. | `$DATE('2026-10-08')` returns `'2026-10-08'`. |
| `$DATETIME(datetime_string)` | Returns the date and time from `datetime_string` as text in `YYYY-MM-DD HH:MM:SS` format. | `$DATETIME('2026-10-08 12:34:56')` returns `'2026-10-08 12:34:56'`. |
| `$JULIANDAY(datetime_string)` | Returns fractional days since noon in Greenwich on November 24, 4714 BCE. Subtract two Julian day values to calculate an elapsed number of days. | `$JULIANDAY('2000-01-01 12:00:00')` returns `2451545.0`. `$JULIANDAY('2026-10-09') - $JULIANDAY('2026-10-08')` returns `1.0`. |
| `$STRFTIME(format, datetime_string)` | Returns text formatted using `format`. The format comes before the date or datetime input. | `$STRFTIME('%Y-%m', '2026-10-08')` returns `'2026-10'`. |
| `$TIME(time_string)` | Returns the time from `time_string` as text in `HH:MM:SS` format. | `$TIME('12:34:56')` returns `'12:34:56'`. |

### Format substitutions

Combine the following substitutions with literal separators in `$STRFTIME`. For example, `'%Y-%m-%d %H:%M:%S'` formats both the date and time. An unsupported substitution returns NULL.

Date and time format substitutions

| Substitution | Meaning |
| --- | --- |
| `%d` | Day of month, 01-31. |
| `%H` | Hour, 00-24. |
| `%f` | Seconds with fractional part, SS.SSS. |
| `%j` | Day of year, 001-366. |
| `%J` | Julian day number. |
| `%m` | Month, 01-12. |
| `%M` | Minute, 00-59. |
| `%s` | Seconds since January 1, 1970, 00:00:00 UTC. |
| `%S` | Seconds, 00-59. |
| `%w` | Day of week, 0-6; Sunday is 0. |
| `%W` | Week of year, 00-53; weeks start on Monday. |
| `%Y` | Year, 0000-9999. |
| `%%` | A literal percent sign. |

## Data enrichment functions

Use a lookup to add a related value, such as a department name, from a table in the source or target endpoint.

Data enrichment function arguments, behavior, and examples

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$SOURCE_LOOKUP(time_to_live, schema, table, expression, condition, condition_params)` | Retrieves the value of `expression` from the source endpoint's `table`, in `schema`, for the record that matches `condition`. The condition parameters supply values for its placeholders in order. | `$SOURCE_LOOKUP(60, 'HR', 'DEPARTMENTS', 'DEPARTMENT_NAME', 'DEPARTMENT_ID=:1', $DEPARTMENT_ID)` retrieves the matching department name from the source. |
| `$TARGET_LOOKUP(time_to_live, schema, table, expression, condition, condition_params)` | Retrieves the value of `expression` from the target endpoint's `table`, in `schema`, for the record that matches `condition`. The condition parameters supply values for its placeholders in order. | `$TARGET_LOOKUP(60, 'dbo', 'DEPARTMENTS', 'DEPARTMENT_NAME', 'DEPARTMENT_ID=?', $DEPARTMENT_ID)` retrieves the matching department name from the target. |

`condition_params` represents a comma-separated list of arguments, not a single array argument. Both functions use the following parameters:

Lookup parameters and their relationships

| Parameter | Meaning |
| --- | --- |
| `time_to_live` | Required cache lifetime, with no default. Supply the cache lifetime in seconds, `'NO_CACHING'` to disable caching, or `'NO_EXPIRATION'` to keep cached results without expiration.  Short lifetimes refresh frequently changing data. Longer lifetimes reduce endpoint queries but can return cached values after the lookup data changes. Use no expiration only for data that does not change. |
| `schema` | Schema containing the lookup table, supplied as text. |
| `table` | Table to query within that schema, supplied as text. |
| `expression` | SQL expression selecting one column value, such as `'DEPARTMENT_NAME'` or `'PRICE * 1.2'`. Use the SQL dialect of the endpoint being accessed, not the outer expression's function syntax. |
| `condition` | SQL condition identifying the lookup record. Use the accessed endpoint's dialect and placeholder syntax: for example, `:1` and `:2` for Oracle, or `?` for Microsoft SQL Server. |
| `condition_params` | Values bound to the condition placeholders, in order. Column parameters such as `$COMPANY_ID` and `$DEPARTMENT_ID` supply values from the current row. |

Index the lookup fields to reduce query cost. Select a condition that identifies the intended record, and set the added column's data type to match the selected value.

Information noteTesting calls to `$SOURCE_LOOKUP` and `$TARGET_LOOKUP` is not supported. See [*Testing expressions*](Building-expressions.htm#Testing).

### Source lookup example

For an Oracle source, the following expression retrieves `DEPARTMENT_NAME` from `HR.DEPARTMENTS` and caches the result for 60 seconds:

```
$SOURCE_LOOKUP(60, 'HR', 'DEPARTMENTS', 'DEPARTMENT_NAME', 'DEPARTMENT_ID=:1', $DEPARTMENT_ID)
```

If the current row has `DEPARTMENT_ID` 10 and the matching lookup record contains `'Sales'`, the result is `'Sales'`.

For a Microsoft SQL Server source, use its condition placeholder syntax. This example binds company and department values in that order:

```
$SOURCE_LOOKUP(60, 'dbo', 'DEPARTMENTS', 'DEPARTMENT_NAME', 'COMPANY_ID=? AND DEPARTMENT_ID=?', $COMPANY_ID, $DEPARTMENT_ID)
```

### Target lookup example

For a Microsoft SQL Server target, query the target table using its SQL dialect:

```
$TARGET_LOOKUP(60, 'dbo', 'DEPARTMENTS', 'DEPARTMENT_NAME', 'DEPARTMENT_ID=?', $DEPARTMENT_ID)
```

If the target lookup record for department 10 contains `'Sales'`, the result for an input value of 10 is `'Sales'`.

## Operation functions

Operation function arguments, behavior, and examples

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$OPERATION_INDICATOR(value_on_delete, value_on_update, value_on_insert)` | Returns the flag you specify for each source operation. The argument order is delete, update, then insert. Use a dedicated column to store the flags, and supply flag values that match its data type. | `$OPERATION_INDICATOR('Deleted', 'Updated', 'Inserted')` returns `'Updated'` for an update. |

In Qlik Replicate, this function also changes deletion handling: it retains the corresponding target record and flags it with `value_on_delete`. This deletion-handling behavior requires confirmation for Qlik Talend Cloud Data Integration.

## Logical functions

Conditional value selection

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$IFF(boolean_expression, true_value, false_value)` | Returns `true_value` if `boolean_expression` evaluates to true; otherwise, returns `false_value`. Supply the condition first, followed by the two result values. | `$IFF(10 > 5, 'High', 'Low')` returns `'High'`. `$IFF(3 > 5, 'High', 'Low')` returns `'Low'`. |

## Other functions

Pattern matching and value types

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$LIKE(pattern, string[, escape_character])` | Returns 1 for a match or 0 for no match; NULL input produces NULL. `%` matches zero or more characters; `_` matches one. Matching ignores ASCII letter case by default. The optional escape is one character. The pattern comes first, unlike the `LIKE` operator. | `$LIKE('A%', 'Alice')` returns `1`. `$LIKE('10!%', '10%', '!')` returns `1`. |
| `$TYPEOF(expression)` | Returns the value's storage class: `'null'`, `'integer'`, `'real'`, `'text'`, or `'blob'`. This is not the configured output column type. | `$TYPEOF(12.5)` returns `'real'`. |

## Hash functions

Hash function arguments, behavior, and examples

| Function | Behavior and arguments | Example and result |
| --- | --- | --- |
| `$SHA256(string)` | Returns the hexadecimal SHA-256 hash of the input string. | `$SHA256('abc')` returns `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`. |

A hash is not encryption. Predictable input values can still be identified by comparing their hashes.
