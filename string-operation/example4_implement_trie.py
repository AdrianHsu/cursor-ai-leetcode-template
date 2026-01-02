"""
LeetCode 208: Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(m)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        Time Complexity: O(m) where m is the length of the word
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        Time Complexity: O(m) where m is the length of the prefix
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Test cases
def test_trie():
    trie = Trie()
    
    # Test case 1
    trie.insert("apple")
    result1 = trie.search("apple")
    assert result1 == True, f"Test case 1 failed: got {result1}, expected True"
    print("Test case 1 passed: insert('apple'), search('apple') -> True")
    
    # Test case 2
    result2 = trie.search("app")
    assert result2 == False, f"Test case 2 failed: got {result2}, expected False"
    print("Test case 2 passed: search('app') -> False")
    
    # Test case 3
    result3 = trie.startsWith("app")
    assert result3 == True, f"Test case 3 failed: got {result3}, expected True"
    print("Test case 3 passed: startsWith('app') -> True")
    
    # Test case 4
    trie.insert("app")
    result4 = trie.search("app")
    assert result4 == True, f"Test case 4 failed: got {result4}, expected True"
    print("Test case 4 passed: insert('app'), search('app') -> True")
    
    # Test case 5
    result5 = trie.startsWith("xyz")
    assert result5 == False, f"Test case 5 failed: got {result5}, expected False"
    print("Test case 5 passed: startsWith('xyz') -> False")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_trie()

