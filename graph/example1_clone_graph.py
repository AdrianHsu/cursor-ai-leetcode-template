"""
LeetCode 133: Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        """
        BFS approach with hash map
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        if not node:
            return None
        
        from collections import deque
        clone_map = {}
        queue = deque([node])
        clone_map[node] = Node(node.val)
        
        while queue:
            original = queue.popleft()
            clone = clone_map[original]
            
            for neighbor in original.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone.neighbors.append(clone_map[neighbor])
        
        return clone_map[node]

# Helper function to create graph from adjacency list
def create_graph(adj_list):
    if not adj_list:
        return None
    
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    
    for i, neighbors in enumerate(adj_list):
        for neighbor_val in neighbors:
            nodes[i].neighbors.append(nodes[neighbor_val - 1])
    
    return nodes[0] if nodes else None

# Helper function to convert graph to adjacency list
def graph_to_adj_list(node):
    if not node:
        return []
    
    from collections import deque
    visited = set()
    queue = deque([node])
    visited.add(node)
    adj_map = {}
    
    while queue:
        n = queue.popleft()
        adj_map[n.val] = [neighbor.val for neighbor in n.neighbors]
        
        for neighbor in n.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # Convert to list format
    max_val = max(adj_map.keys())
    result = [[] for _ in range(max_val)]
    for val, neighbors in adj_map.items():
        result[val - 1] = neighbors
    
    return result

# Test cases
def test_clone_graph():
    solution = Solution()
    
    # Test case 1
    adj_list1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph1 = create_graph(adj_list1)
    cloned1 = solution.cloneGraph(graph1)
    result1 = graph_to_adj_list(cloned1)
    result1.sort()
    expected1 = sorted([[2, 4], [1, 3], [2, 4], [1, 3]])
    assert result1 == expected1, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: cloned graph structure matches")
    
    # Test case 2: Single node
    adj_list2 = [[]]
    graph2 = create_graph(adj_list2)
    cloned2 = solution.cloneGraph(graph2)
    result2 = graph_to_adj_list(cloned2)
    assert result2 == [[]], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: single node cloned")
    
    # Test case 3: Empty graph
    graph3 = None
    cloned3 = solution.cloneGraph(graph3)
    assert cloned3 is None, f"Test case 3 failed"
    print(f"Test case 3 passed: empty graph handled")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_clone_graph()

