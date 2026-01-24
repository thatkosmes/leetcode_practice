# 620. Not Boring Movies

**Difficulty:** Easy  
**Topic:** SQL  
**Platform:** LeetCode

## Problem Description

Given a table `Cinema` containing information about movies, including their ID, title, description, and rating, we need to retrieve a list of movies that satisfy the following conditions:

- The movie ID is **odd-numbered**
- The movie description is **not equal to `"boring"`**

The resulting list should be **sorted by rating in descending order**.

## Table Schema

**Cinema**

| Column Name  | Type    |
|-------------|---------|
| id          | int     |
| movie       | varchar |
| description | varchar |
| rating      | float   |

- `id` is the primary key  
- `rating` is a float value in the range `[0, 10]`  

## Solution Approach

The problem can be solved using simple filtering and sorting logic in SQL:

1. **Filter odd-numbered IDs** using `id % 2 = 1`.
2. **Exclude boring movies** using `description != 'boring'`.
3. **Sort results by rating** in descending order using `ORDER BY rating DESC`.

This makes the solution straightforward and efficient.