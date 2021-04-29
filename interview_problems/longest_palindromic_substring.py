# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.

# Solution 1
# O(n^2) time complexity, O(1) space complexity
def longest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 1:
        return s

    start = 0
    end = 0
    length_1 = 0
    length_2 = 0
    max_length = 0

    for i in range(len(s)):
        # check maximum palindrome length for odd number of chars
        length_1 = move_from_middle(s, i, i)
        # check maximum palindrome length for even number of chars
        length_2 = move_from_middle(s, i, i + 1)
        # get the larger of the two
        max_length = max(length_1, length_2)

        if max_length > end - start:
            # new start is the middle - 1
            start = i - ((max_length - 1) // 2)
            # new end is the middle
            end = i + (max_length // 2)

    return s[start:end + 1]


# move pointers from the middle
def move_from_middle(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("a"))
print(longest_palindrome("ac"))
print(longest_palindrome("bb"))
print(longest_palindrome("abb"))
