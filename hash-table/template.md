# Hash Table Template

## Basic Structure
```python
# Dictionary/Hash Map
from collections import defaultdict

hash_map = {}
# or hash_map = defaultdict(list)

hash_map[key] = value
value = hash_map.get(key, default_value)

# Set
hash_set = set()
hash_set.add(value)
if value in hash_set:
    # Process
```

## Common Patterns

### 1. Frequency Counting
```python
def count_frequency(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq
```

### 2. Two Sum Pattern
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### 3. Grouping
```python
def group_by_key(items):
    groups = {}
    for item in items:
        key = get_key(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups
```

### 4. Sliding Window with Hash
```python
def sliding_window(s):
    char_count = {}
    left = 0
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        # Shrink window if needed
        while condition:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
```


## Key Techniques
- Use defaultdict for cleaner code
- Counter from collections for frequency
- Set for O(1) lookup
- Hash map for O(1) key-value access

