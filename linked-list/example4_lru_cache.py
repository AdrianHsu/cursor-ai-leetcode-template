"""
LeetCode 146: LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        """
        Initialize the LRU cache with positive size capacity.
        Time Complexity: O(1) for all operations
        Space Complexity: O(capacity)
        """
        self.capacity = capacity
        self.cache = {}  # key -> node mapping
        
        # Dummy head and tail for easier operations
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove an existing node"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Move node to head (most recently used)"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Remove the last node (least recently used)"""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key):
        """
        Return the value of the key if the key exists, otherwise return -1.
        Time Complexity: O(1)
        """
        node = self.cache.get(key)
        if not node:
            return -1
        
        # Move to head (most recently used)
        self._move_to_head(node)
        return node.val
    
    def put(self, key, value):
        """
        Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity, evict the least recently used key.
        Time Complexity: O(1)
        """
        node = self.cache.get(key)
        
        if not node:
            # Create new node
            new_node = ListNode(key, value)
            
            # Add to cache
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Remove least recently used
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            # Update existing node
            node.val = value
            self._move_to_head(node)


# Test cases
def test_lru_cache():
    # Test case 1
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    result1 = lru.get(1)
    assert result1 == 1, f"Test case 1 failed: got {result1}, expected 1"
    print("Test case 1 passed: put(1,1), put(2,2), get(1) -> 1")
    
    lru.put(3, 3)
    result2 = lru.get(2)
    assert result2 == -1, f"Test case 2 failed: got {result2}, expected -1"
    print("Test case 2 passed: put(3,3), get(2) -> -1")
    
    lru.put(4, 4)
    result3 = lru.get(1)
    assert result3 == -1, f"Test case 3 failed: got {result3}, expected -1"
    print("Test case 3 passed: put(4,4), get(1) -> -1")
    
    result4 = lru.get(3)
    assert result4 == 3, f"Test case 4 failed: got {result4}, expected 3"
    print("Test case 4 passed: get(3) -> 3")
    
    result5 = lru.get(4)
    assert result5 == 4, f"Test case 5 failed: got {result5}, expected 4"
    print("Test case 5 passed: get(4) -> 4")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_lru_cache()

