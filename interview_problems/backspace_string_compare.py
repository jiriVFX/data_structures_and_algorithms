# https://leetcode.com/problems/backspace-string-compare/
# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Solution 1 - naive brute force
# O(n^2) time complexity, O(n) space complexity (string slicing creates copy of string)
def backspace_compare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    output_s = ""
    output_t = ""
    # iterate over s
    for i in range(len(s)):
        if s[i] == "#":
            if len(output_s) > 0:
                output_s = output_s[:len(output_s) - 1]
        else:
            output_s += s[i]
    # iterate over t
    for i in range(len(t)):
        if t[i] == "#":
            if len(output_t) > 0:
                output_t = output_t[:len(output_t) - 1]
        else:
            output_t += t[i]

    # compare the two strings
    if output_s == output_t:
        return True
    return False


print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("ab##", "c#d#"))
print(backspace_compare("a##c", "#a#c"))
print(backspace_compare("a#c", "b"))
