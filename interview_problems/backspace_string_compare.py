# https://leetcode.com/problems/backspace-string-compare/
# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Solution 1 - naive brute force
# O(len(s) + len(t)) time complexity, O(n) space complexity (string slicing creates copy of the string)
def backspace_compare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # iterate over s
    output_s = clean_string(s)
    # iterate over t
    output_t = clean_string(t)

    # compare the two strings
    if output_s == output_t:
        return True
    return False


def clean_string(str_to_clean):
    output = ""
    for i in range(len(str_to_clean)):
        if str_to_clean[i] == "#":
            if len(output) > 0:
                output = output[:len(output) - 1]
        else:
            output += str_to_clean[i]
    return output


print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("ab##", "c#d#"))
print(backspace_compare("a##c", "#a#c"))
print(backspace_compare("a#c", "b"))
