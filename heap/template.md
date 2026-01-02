# Heap / Priority Queue Template

## Basic Structure

### Python heapq Module
```python
import heapq

# Min heap (default)
heap = []
heapq.heappush(heap, item)      # Push item
heapq.heappop(heap)              # Pop smallest
heapq.heapify(list)              # Convert list to heap
heap[0]                          # Peek smallest (without popping)

# Max heap (negate values)
heap = []
heapq.heappush(heap, -item)     # Push negated value
-heapq.heappop(heap)             # Pop and negate back
```

### Custom Comparator
```python
import heapq

# Using tuples for custom ordering
heap = []
heapq.heappush(heap, (priority, item))  # Sorted by priority first
heapq.heappush(heap, (-priority, item)) # For max heap
```

## Common Patterns

### 1. Kth Largest/Smallest Element
```python
import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

### 2. Merge K Sorted Lists
```python
import heapq

def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))
    return result
```

### 3. Top K Frequent Elements
```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for freq, num in heap]
```

### 4. Find Median from Data Stream
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negated)
        self.large = []  # Min heap
    
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
```

## Key Techniques
- Use min heap for kth largest (keep k smallest, pop excess)
- Use max heap for kth smallest (negate values)
- Maintain heap size k for O(n log k) complexity
- Use tuples for custom sorting: (priority, item)
- Two heaps for median finding (small max heap + large min heap)

