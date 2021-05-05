# https://leetcode.com/problems/maximum-number-of-balloons/
# Given a string text,
# you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Solution 1 - two dictionaries - universal, should works for any string
# O(n) time complexity, O(n) space complexity
def max_number_of_balloons(text):
    """
    :type text: str
    :rtype: int
    """
    balloon = "balloon"
    char_dict = {}

    # create dictionary with char count of balloon (can be used for any other string)
    for i in range(len(balloon)):
        if balloon[i] in char_dict:
            char_dict[balloon[i]] += 1
        else:
            char_dict[balloon[i]] = 1

    # check text for amount of letters from char_dict in text
    char_dict_2 = {}
    for i in range(len(text)):
        if text[i] in char_dict:
            if text[i] in char_dict_2:
                char_dict_2[text[i]] += 1
            else:
                char_dict_2[text[i]] = 1

    # calculate how many instaces of balloon can we form from text
    # has to be min_instances = float("inf") - LeetCode runs older version of Python
    # in Python 3 we import math and use min_instances = math.inf
    min_instances = float("inf")
    for char in char_dict:
        if char in char_dict_2:
            current_instances = char_dict_2[char] // char_dict[char]
            min_instances = min(min_instances, current_instances)
        else:
            return 0

    return min_instances


print(max_number_of_balloons("nlaebolko"))
print(max_number_of_balloons("loonbalxballpoon"))
print(max_number_of_balloons("leetcode"))
