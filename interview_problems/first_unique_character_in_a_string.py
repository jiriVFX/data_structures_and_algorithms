# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string s, return the first non-repeating character in it and return its index.
# If it does not exist, return -1.

# The accepted solution is the last one
# I included all the solutions I tried just for the record

# Brute force naive approach
# O(n^2) time complexity - very inefficient! (Time exceeded on LeetCode)


def first_uniqchar(s):
    """
    :type s: str
    :rtype: int
    """
    unique = True

    for i in range(len(s)):
        for j in range(len(s)):
            # When the same character is found, but on a different position
            if s[i] == s[j] and i != j:
                unique = False
                # We don't need to check the rest of the characters
                break
        # If the character is unique, return its index i
        if unique:
            return i
        # Reset unique before checking another character
        unique = True
    return -1


print(first_uniqchar("leetcode"))
print(first_uniqchar("loveleetcode"))
print(first_uniqchar("aabb"))


# O(2n) time complexity - much better, O(26) -> O(1) space complexity (alphabet has fixed number of characters)
# Ouputs correct results on the local machine,
# but different results on LeetCode
# LeetCode Python seems to use unordered dictionaries (Like before Python 3.7), which is causing the problem
def first_uniqchar2(s):
    """
    :type s: str
    :rtype: int
    """
    unique_dict = {}

    for i in range(len(s)):
        if s[i] in unique_dict:
            unique_dict[s[i]] = -1
        else:
            unique_dict[s[i]] = i

    for index in unique_dict.values():
        if index > -1:
            return index
    return -1


print(first_uniqchar2("leetcode"))
print(first_uniqchar2("loveleetcode"))
print(first_uniqchar2("aabb"))


# O(n) time complexity, O(1) space complexity
# Similar to the previous solution, but using OrderedDict to be accepted by LeetCode
# OrderedDict should be supported across Python versions
# It ensures the inserted items are inserted in order and maintain it (like Python 3.7+ dictionaries)

from collections import OrderedDict


def first_uniqchar3(s):
    """
    :type s: str
    :rtype: int
    """
    unique_dict = OrderedDict()

    for i in range(len(s)):
        if s[i] in unique_dict:
            unique_dict[s[i]] = -1
        else:
            unique_dict[s[i]] = i

    for index in unique_dict.values():
        if index > -1:
            return index
    return -1


print(first_uniqchar3("leetcode"))
print(first_uniqchar3("loveleetcode"))
print(first_uniqchar3("aabb"))



# EXPLANATION OF THE LEETCODE WRONG OUPUT PROBLEM

# If you tried the solution with dictionary, you might have run into a problem, when you get correct output on your local machine, but wrong one on LeetCode.
#
# **So this code:**
# ```
#     unique_dict = {}
#
#     for i in range(len(s)):
#         if s[i] in unique_dict:
#             unique_dict[s[i]] = -1
#         else:
#             unique_dict[s[i]] = i
#
#     for index in unique_dict.values():
#         if index > -1:
#             return index
#     return -1
# ```
#
# **Tested with following inputs:**
# ```
# "leetcode"
# "loveleetcode"
# "aabb"
# ```
#
# **Local machine output:**
# ```
# 0
# 2
# -1
# ```
#
# **LeetCode output:**
# ```
# 4
# 8
# -1
# ```
#
# After few hours of searching for the cause of the problem, I figured out that LeetCode dictionaries are unordered for some reason (like before Python 3.7).
#
# **Tested with "leetcode" input, the dictionary is ordered, when printed on the local machine:**
# ```
# {'l': 0, 'e': -1, 't': 3, 'c': 4, 'o': 5, 'd': 6}
# ```
# **But LeetCode prints unordered dictionary**
# ```
# {u'c': 4, u'e': -1, u'd': 6, u'l': 0, u'o': 5, u't': 3}
# ```
#
#
# # Solution
#
# To ensure the dictionary is ordered across different Python versions, we have to use collections.OrderedDict - [StackOverflow](https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6)
#
# ```
# from collections import OrderedDict
#
#
# def first_uniqchar3(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     unique_dict = OrderedDict()
#
#     for i in range(len(s)):
#         if s[i] in unique_dict:
#             unique_dict[s[i]] = -1
#         else:
#             unique_dict[s[i]] = i
#
#     for index in unique_dict.values():
#         if index > -1:
#             return index
#     return -1
# ```
#
# **This modified code now returns correct ouput on LeetCode too.**

