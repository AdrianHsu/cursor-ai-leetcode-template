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

