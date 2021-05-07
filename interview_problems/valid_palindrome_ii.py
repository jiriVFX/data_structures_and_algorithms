# https://leetcode.com/problems/valid-palindrome-ii/
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# Solution 1 - two pointers
# O(N) time complexity, O(1) space complexity
def valid_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 1:
        return True

    # check for non-matching pair
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - (1 + i)]:
            # if chars don't match
            # try to skip one char from left and one from right
            # to see whether either of them creates a valid palindrome
            return is_palindrome(s, i + 1, len(s) - (1 + i)) or is_palindrome(s, i, len(s) - (2 + i))
    # if all char pairs match, it is already a palindrome from the start
    return True


# find out if string is a palindrome
def is_palindrome(string, left, right):
    # if any pair of chars don't match, it's not palindrome
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(valid_palindrome("aba"))
print(valid_palindrome("abca"))
print(valid_palindrome("abc"))
print(valid_palindrome("cbbcc"))
