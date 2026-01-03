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

# heap often pair with Counter() 
from collections import Counter
count = Counter(nums)
for num, freq in count.items():

# 
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

Note, heapq is "Heap Queue"
So heappop() will pop the [0] (head), which is the smallest one

### 2. Merge K Sorted Lists (IMPORTANT)
```python
import heapq
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy

        while heap:
            node_val, list_idx, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
            curr.next = node
            curr = curr.next
        
        return dummy.next
```
How do you know what to store in heapq?
1. it must need `node.val` to be the key, as it is a min-heap sorted by val
2. it must need `node` itself to build the new linked list
3. how about `idx`?

If we do `heapq.heappush(heap, (node.val, node))` it will face errors
```
TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
    heapq.heappush(heap, (node.val, node))
```
so we need to include `idx` so that "if val is the same, we compare idx during sorting for these nodes" .

Hence, we need `node.val`, `idx`, and `node`.


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
    return [num for (_, num) in heap]
```
basically integrate with Counter.

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

## References
- https://www.1point3acres.com/bbs/thread-1159711-1-1.html