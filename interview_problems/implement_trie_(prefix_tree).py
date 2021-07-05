# https://leetcode.com/problems/implement-trie-prefix-tree/
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store
# and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
# - Trie() Initializes the trie object
# - void insert(String word) Inserts the string word into the trie.
# - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
#   and false otherwise.
# - boolean startsWith(String prefix) Returns true if there is a previously inserted string word
#   that has the prefix prefix, and false otherwise.

# O(n) time complexity - length of the word
# O(n) space complexity - length of the word
class CharNode:
    def __init__(self):
        self.end = False
        self.connected = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = CharNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.head
        # check char by char if it is already in the trie
        for char in word:
            if char not in current.connected:
                # add char to current letter's connections
                current.connected[char] = CharNode()
            # set new char as current
            current = current.connected[char]
        # if it is the last character of the word, mark the end of the word
        current.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.head
        # check char by char if exact word is in trie
        for char in word:
            # if the current char is not in the connected dict
            # or there are other chars in the trie after the last char of the word
            if char not in current.connected:
                return False
            else:
                current = current.connected[char]

        return current.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.head
        # check char by char if exact word is in trie
        for char in prefix:
            if char not in current.connected:
                return False
            else:
                current = current.connected[char]

        return True


trie = Trie()
trie.insert("word")
print(trie.search("word"))

trie.insert("apple")
print(trie.search("app"))
print(trie.startsWith("app"))
