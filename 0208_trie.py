"""
# 208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.



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



Constraints:

    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.

"""
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_1(self):
        trie = self.trie
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app");
        self.assertTrue(trie.search("app"))


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


#
# class Trie:
#
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word: str) -> None:
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_word = True
#
#     def search(self, word: str) -> bool:
#         node = self.root
#         for c in word:
#             if c not in node.children:
#                 return False
#             node = node.children[c]
#         return node.is_word
#
#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for c in prefix:
#             if c not in node.children:
#                 return False
#             node = node.children[c]
#         return True

# def buildTrie(self, dictionary):
#     root = TrieNode()
#     for word in dictionary:
#         node = root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_word = True
#     return root

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
