# https://leetcode.com/problems/word-break/
# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# # Solution 1
# def word_break(s, word_dict):
#     """
#     :type s: str
#     :type word_dict: List[str]
#     :rtype: bool
#     """
#     words = {len(item): set() for item in word_dict}
#     for i in range(len(word_dict)):
#         words[len(word_dict[i])].add(word_dict[i])
#
#     result = 0
#     current_string = ""
#     # First find out if any word from word_dict is in s
#     for i in range(len(s)):
#         current_string += s[i]
#         # there are keys with remaining length in words
#         if len(s) - i in words:
#             # if any of the words with the length len(s) - i is equal to current string
#             if s[:len(s) - i - 1] in words[len(s) - i] or s[i:len(s) + 1] in words[len(s) - i]:
#                 print("yes")
#                 current_string = ""
#                 result += 1
#
#     # print(result)
#     print(current_string)
#     if result > 0 and len(current_string) == 0:
#         return True
#     return False
#     # Second find out if the words are next to each other - there must be no other chars in-between them

# Solution 1 - dynamic programming - LeetCode solution
# O(n^3) time complexity, O(n^2) space complexity
def word_break(s, word_dict):
    """
    :type s: str
    :type word_dict: List[str]
    :rtype: bool
    """
    word_set = set(word_dict)
    words = [False] * (len(s) + 1)
    words[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if words[j] and s[j:i] in word_set:
                print(s[j:i])
                words[i] = True
                break
    print(words)
    return words[len(s)]


print(word_break("leetcode", ["leet", "code"]))
print(word_break("applepenapple", ["apple", "pen"]))
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(word_break("a", ["a"]))
print(word_break("aaaaaaa", ["aaaa", "aaa"]))
