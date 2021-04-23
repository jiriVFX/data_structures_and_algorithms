# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

# Solution 1 - moving window
# O(n) time complexity, O(n) space complexity
def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    current_count = 0
    highest_count = 0
    seen_chars = {}

    i = 0
    while i < len(s):
        # check the current char
        if s[i] in seen_chars:
            # if char is repeating, record the highest_count
            if current_count > highest_count:
                highest_count = current_count
            # reset values
            # move i to the last non-repeating position
            i = seen_chars[s[i]] + 1
            current_count = 0
            seen_chars = {}
        # store the position of the current char
        seen_chars[s[i]] = i
        current_count += 1
        # increment i
        i += 1

    # check in case of all unique characters in a string
    if current_count > highest_count:
        return current_count
    return highest_count


# print(length_of_longest_substring("abcabcbb"))
# print(length_of_longest_substring("bbbbb"))
# print(length_of_longest_substring("pwwkew"))
# print(length_of_longest_substring(""))
# print(length_of_longest_substring(" "))
# print(length_of_longest_substring("dvdf"))


# Solution 2 - optimized moving window - without moving back
# O(n) time complexity, O(n) space complexity
def length_of_longest_substring_2(s):
    """
    :type s: str
    :rtype: int
    """
    start = 0
    highest_count = 0
    seen_chars = {}

    i = 0
    while i < len(s):
        # check the current char
        # seen_chars[s[i]] must be >= start so we don't move backwards - "abba"
        if s[i] in seen_chars and seen_chars[s[i]] >= start:
            # if char is repeating, record the highest_count
            if i - start > highest_count:
                highest_count = i - start
            # start i to the last non-repeating position
            start = seen_chars[s[i]] + 1
        # store the position of the current char
        seen_chars[s[i]] = i
        # increment i
        i += 1

    # check in case of all unique characters in a string
    if i - start > highest_count:
        return i - start

    return highest_count


print(length_of_longest_substring_2("abcabcbb"))
print(length_of_longest_substring_2("bbbbb"))
print(length_of_longest_substring_2("pwwkew"))
print(length_of_longest_substring_2(""))
print(length_of_longest_substring_2(" "))
print(length_of_longest_substring_2("dvdf"))
print(length_of_longest_substring_2("abba"))
