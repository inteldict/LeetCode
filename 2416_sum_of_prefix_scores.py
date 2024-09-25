"""
# 2416. Sum of Prefix Scores of Strings

You are given an array words of size n consisting of non-empty strings.

We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].

    For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".

Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.

Example 1:

Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
Explanation: The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.

Example 2:

Input: words = ["abcd"]
Output: [4]
Explanation:
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 1000
    words[i] consists of lowercase English letters.
"""
import unittest
from typing import List


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        words = ["abc", "ab", "bc", "b"]
        out = [5, 4, 3, 2]
        self.assertEqual(out, self.solution.sumPrefixScores(words))

    def test_2(self):
        words = ["abcd"]
        out = [4]
        self.assertEqual(out, self.solution.sumPrefixScores(words))


# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.score = 0
#
#     def add_child(self, c):
#         child = self.children.setdefault(c, TrieNode())
#         child.score += 1
#         return child
#
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word) -> None:
#         node = self.root
#         for c in word:
#             node = node.add_child(c)
#
#     def getPrefixScore(self, word: str) -> int:
#         node = self.root
#         total_score = 0
#         for c in word:
#             node = node.children[c]
#             total_score += node.score
#         return total_score
#
#
# class Solution:
#     def sumPrefixScores(self, words: List[str]) -> List[int]:
#         trie = Trie()
#         for word in words:
#             trie.insert(word)
#         return [trie.getPrefixScore(word) for word in words]

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}  # Initialize a hash map for trie
        for w in words:
            cur = trie  # At the beginning of each word, the pointer should point to the beginning of the trie
            for c in w:
                cur = cur.setdefault(c, {})
                # Instead of store the end of the word in the regular trie,
                # we are storing the number of occurrences of the prefix at each letter
                if '#' not in cur:
                    cur['#'] = 0
                cur['#'] += 1
        res = []
        # Calculate result
        for w in words:
            cur = trie
            count = 0  # Count occurrences of each character in this word
            for c in w:
                cur = cur[c]
                count += cur['#']
            res.append(count)
        return res

# def custom_main():
#     input_data = sys.stdin.read().strip()
#     lines = input_data.splitlines()
#
#     num_test_cases = len(lines)
#     results = []
#
#     for i in range(num_test_cases):
#         words = json.loads(lines[i])
#
#         result = Solution().sumPrefixScores(words)
#
#         results.append(json.dumps(result, separators=(',', ':')))
#
#     with open('user.out', 'w') as f:
#         for result in results:
#             f.write(f"{result}\n")
#
#
# if __name__ == "__main__":
#     custom_main()
#     exit(0)
