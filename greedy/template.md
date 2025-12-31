# Greedy Template

## Basic Strategy
```python
def greedy_solution(problem):
    # Sort or prioritize
    items = sort_by_priority(problem)
    
    result = []
    for item in items:
        if is_valid_choice(item, result):
            result.append(item)
    
    return result
```

## Common Patterns

### 1. Activity Selection
```python
def activity_selection(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    result = [activities[0]]
    last_end = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end:
            result.append((start, end))
            last_end = end
    
    return result
```

### 2. Fractional Knapsack
```python
def fractional_knapsack(items, capacity):
    # Sort by value/weight ratio
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    total_value = 0
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break
    
    return total_value
```

### 3. Minimum Coins
```python
def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    
    for coin in coins:
        if amount >= coin:
            count += amount // coin
            amount %= coin
    
    return count if amount == 0 else -1
```

### 4. Jump Game
```python
def can_jump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
        if max_reach >= len(nums) - 1:
            return True
    return True
```

## Key Techniques
- Make locally optimal choice at each step
- Often requires sorting first
- Prove greedy choice is safe
- Greedy doesn't always work - verify correctness

