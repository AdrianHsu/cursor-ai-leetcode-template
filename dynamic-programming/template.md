# Dynamic Programming Template

## Basic Structure

### 1. Top-Down (Memoization)
```python
def dp_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if base_case(n):
        return base_value
    
    memo[n] = dp_top_down(n-1, memo) + dp_top_down(n-2, memo)
    return memo[n]
```

### 2. Bottom-Up (Tabulation)
```python
def dp_bottom_up(n):
    dp = [0] * (n + 1)
    dp[0] = base_value_0
    dp[1] = base_value_1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

### 1. Top-Down (Memoization)

Imagine you are solving a large puzzle by breaking it into smaller pieces. Top-Down starts at the **final goal** () and works its way backward to the **base cases**.

* **How it works:** It uses **Recursion**. You ask, "To solve , what do I need?" It tells you, "You need  and ." You keep diving deeper until you hit a value you already know (the base case).
* **The "Memo" (Memoization):** Without the `memo` dictionary, recursion is extremely slow because it recalculates the same values over and over. Memoization is like keeping a **notebook**. Before calculating anything, the function checks the notebook: "Have I solved this before?" If yes, it returns the answer immediately.
* **Pros:** Easier to write if you understand the recursive relationship; only calculates subproblems that are actually needed.
* **Cons:** Can run into "Stack Overflow" errors if the recursion depth is too high.

---

### 2. Bottom-Up (Tabulation)

Instead of starting at the goal, you start at the **very beginning** (the base cases) and build your way up to the final answer.

* **How it works:** It uses **Iteration** (a `for` loop). You fill out a table (usually a List or Array) step-by-step.
* **The Table (Tabulation):** You start by filling `dp[0]` and `dp[1]`. Then, the loop uses those two values to calculate `dp[2]`. Then it uses `dp[1]` and `dp[2]` to calculate `dp[3]`, and so on.
* **Pros:** Usually faster than recursion because there is no function call overhead; no risk of stack overflow. It is often easier to optimize for space (e.g., only keeping the last two values instead of a whole array).
* **Cons:** You must solve all subproblems in order, even if some aren't strictly necessary for the final result.

---

## Common Patterns

### 1. Fibonacci
```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```

### 2. Climbing Stairs
```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```

### 3. 0/1 Knapsack
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],
                    dp[i-1][w-weights[i-1]] + values[i-1]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

### 4. Longest Common Subsequence
```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

## Key Techniques
- Identify overlapping subproblems
- Define state and transition
- Base cases are crucial
- Space optimization possible for 1D/2D arrays

