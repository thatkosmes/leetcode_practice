# 3512. Minimum Operations to Make Array Sum Divisible by K

**Difficulty:** Easy  
**Topic:** Algorithms / Python  
**Platform:** LeetCode

## Problem Description

You are given an integer array `nums` and an integer `k`. You can perform the following operation any number of times:

- Select an index `i` and replace `nums[i]` with `nums[i] - 1`.

Return the **minimum number of operations** required to make the sum of the array divisible by `k`.

### Examples

**Example 1:**

```
Input: nums = [3, 9, 7], k = 5
Output: 4
Explanation:
Perform 4 operations on nums[1] = 9. Now, nums = [3, 5, 7].
The sum is 15, which is divisible by 5.
```

**Example 2:**

```
Input: nums = [4, 1, 3], k = 4
Output: 0
Explanation:
The sum is 8, which is already divisible by 4. No operations are needed.
```

**Example 3:**

```
Input: nums = [3, 2], k = 6
Output: 5
Explanation:
Perform 3 operations on nums[0] = 3 and 2 operations on nums[1] = 2.
Now, nums = [0, 0], sum is 0, divisible by 6.
```

## Solution Approach

The problem can be solved using a **simple modular arithmetic approach**:

1. **Compute the sum of the array**.
2. **Check the remainder modulo `k`**:
   - If the remainder is 0, **no operations are needed**.
   - Otherwise, the remainder itself is the **minimum number of decrement operations** needed.
3. **Implementation**:
   - Implemented as a **Python function**.
   - Added **local tests** to verify correctness for standard, edge, and interesting cases.

This approach is straightforward, efficient, and easy to understand.

## Solution Logic

- Each decrement reduces the total sum by 1.  
- To make the sum divisible by `k`, we need to remove exactly the remainder (`sum % k`).  
- This ensures the sum becomes divisible in **the minimum number of operations**.  
- No need to decrement multiple elements separately if the sum is considered globally.

## Time and Space Complexity

- **Time Complexity:** `O(n)` — computing the sum of `n` elements.  
- **Space Complexity:** `O(1)` — only a few extra variables are used.