# 595. Big Countries

**Difficulty:** Easy
**Topic:** SQL
**Platform:** LeetCode

## Problem Description

You are given a table `World` that contains information about countries, including their name, continent, area, population, and GDP.

A country is considered **big** if **at least one** of the following conditions is satisfied:

* The country has an **area of at least 3,000,000 km²**
* The country has a **population of at least 25,000,000**

The task is to return the **name**, **population**, and **area** of all big countries.

The result table can be returned in **any order**.

---

## Table Schema

**World**

| Column Name | Type    |
| ----------- | ------- |
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |

* `name` is the primary key
* Each row represents one country

---

## Example

**Input:**

```
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
```

**Output:**

```
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```

---

## Solution Approach

This problem can be solved using **simple filtering conditions** in SQL.

The key idea is to:

* Select only the required columns: `name`, `population`, and `area`
* Filter rows where **either** of the following conditions is true:

  * `area` is greater than or equal to `3,000,000`
  * `population` is greater than or equal to `25,000,000`

Since the problem explicitly states that satisfying **any one** of the conditions is enough, the logical **OR** operator is used.

This makes the solution both clear and efficient.

---

## Solution Logic

* Each row represents a single country.
* For each country, we check two independent conditions:

  * Is the country large by **area**?
  * Is the country large by **population**?
* If at least one condition is satisfied, the country is included in the result.

No aggregation, grouping, or sorting is required for this problem.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)` — each row of the table is evaluated once.
* **Space Complexity:** `O(1)` — no additional data structures are used beyond the result set.
