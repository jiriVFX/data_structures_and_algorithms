# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# O(2n) time complexity, O(1) space complexity
def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # Check whether s and t are the same length
    if len(s) == len(t):
        char_dict = {}
        # Add count of all characters to dictionary
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        print(char_dict)
        # Check whether the same characters in t are in dictionary
        for char in t:
            if char in char_dict and char_dict[char] > 0:
                char_dict[char] -= 1
            else:
                return False
        return True
    # If s and t are different lengths, they are not anagrams
    return False


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("ab", "a"))
