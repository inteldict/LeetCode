"""
# 432. All O`one Data Structure
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

    AllOne() Initializes the object of the data structure.
    inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
    dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
    getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
    getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

Note that each function must run in O(1) average time complexity.



Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"



Constraints:

    1 <= key.length <= 10
    key consists of lowercase English letters.
    It is guaranteed that for each call to dec, key is existing in the data structure.
    At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.


"""
import unittest


class Test(unittest.TestCase):

    def execute(self, operations, inputs, expected_results):
        # Iterate over the operations and inputs
        cirq_deque = None
        for i in range(len(operations)):
            operation = operations[i]
            args = inputs[i]
            if operation == "AllOne":
                # Instantiate the MyCalendar class
                cirq_deque = AllOne(*args)
                result = None
            else:
                # Dynamically call the 'book' method using getattr
                result = getattr(cirq_deque, operation)(*args)

            # Check the result against the expected value, if not the constructor
            if expected_results[i] is not None:
                self.assertEqual(result, expected_results[i], f"Failed on operation {operation} with args {args}")

    def test_1(self):
        operations = ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
        inputs = [[], ["hello"], ["hello"], [], [], ["leet"], [], []]

        # Expected outcomes for each 'book' operation
        expected_results = [None, None, None, "hello", "hello", None, "hello", "leet"]
        self.execute(operations, inputs, expected_results)

    def test_2(self):
        operations = ["AllOne", "inc", "inc", "inc", "inc", "getMaxKey", "inc", "inc", "inc", "dec", "inc", "inc",
                      "inc", "getMaxKey"]
        inputs = [[], ["hello"], ["goodbye"], ["hello"], ["hello"], [], ["leet"], ["code"], ["leet"], ["hello"],
                  ["leet"], ["code"], ["code"], []]

        # Expected outcomes for each 'book' operation
        expected_results = [None, None, None, None, None, "hello", None, None, None, None, None, None, None, "leet"]
        self.execute(operations, inputs, expected_results)


class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail  # Link dummy head to dummy tail
        self.tail.prev = self.head  # Link dummy tail to dummy head
        self.map = {}  # Mapping from key to its node

    def inc(self, key: str) -> None:
        # Increment the frequency of the key
        if key in self.map:
            node = self.map[key]
            self.moveKeyToNode(key, node, node.next, node.freq + 1)
        else:
            # Key is not present, so place it in the node after head (freq 1)
            first_node = self.head.next
            if first_node == self.tail or first_node.freq != 1:
                first_node = self.addNodeAfter(self.head, 1)
            first_node.keys.add(key)
            self.map[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.map:
            return  # Key does not exist

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key entirely if frequency is 1
            del self.map[key]
        else:
            self.moveKeyToNode(key, node, node.prev, freq - 1)

        # Remove node if it's empty
        if not node.keys:
            self.removeNode(node)

    # Helper method to move the key to a node with a specific frequency
    def moveKeyToNode(self, key, old_node, target_node, new_freq):
        old_node.keys.remove(key)

        if target_node == self.tail or target_node.freq != new_freq:
            target_node = self.addNodeAfter(old_node, new_freq)
        target_node.keys.add(key)
        self.map[key] = target_node

        if not old_node.keys:
            self.removeNode(old_node)

    # Helper method to add a new node with the given frequency after a specified node
    @staticmethod
    def addNodeAfter(prev_node, freq):
        new_node = Node(freq)
        next_node = prev_node.next
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node
        return new_node

    def dec(self, key: str) -> None:
        if key not in self.map:
            return  # Key does not exist

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.map[key]
        else:
            prev_node = node.prev
            if prev_node == self.head or prev_node.freq != freq - 1:
                # Create a new node if the previous node does not exist or freq is not freq - 1
                new_node = Node(freq - 1)
                new_node.keys.add(key)
                new_node.prev = prev_node
                new_node.next = node
                prev_node.next = new_node
                node.prev = new_node
                self.map[key] = new_node
            else:
                # Decrement the existing previous node
                prev_node.keys.add(key)
                self.map[key] = prev_node

        # Remove the node if it has no keys left
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""  # No keys exist
        return next(
            iter(self.tail.prev.keys)
        )  # Return one of the keys from the tail's previous node

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""  # No keys exist
        return next(
            iter(self.head.next.keys)
        )  # Return one of the keys from the head's next node

    @staticmethod
    def removeNode(node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node  # Link previous node to next node
        next_node.prev = prev_node  # Link next node to previous node
