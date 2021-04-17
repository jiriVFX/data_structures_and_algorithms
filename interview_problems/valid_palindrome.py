# https://leetcode.com/problems/valid-palindrome/
# Given a string s, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
import re, string


# O(n) time complexity, O(1) space complexity
def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # Clean the string of all unwanted characters
    # One working solution, but not the fastest

    # valid_characters = string.ascii_letters + string.digits
    # clean_string = "".join(char for char in s if char in valid_characters)
    # clean_string.lower()
    # print(clean_string)

    # Fastest way in python - using RegEx, based on this Stack Overflow post
    # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
    # [\W] equals [^a-zA-Z0-9_], [\W_] equals [^a-zA-Z0-9]

    # Compile regular expression
    # \W_ Returns a match where the string DOES NOT contain any word characters and underscores
    # This is the same as below, but in one line - re.sub('[\W_]+', '', s)
    # Compiling RegEx though can be faster when having lot of regular expressions
    invalid_chars_regex = re.compile("[\W_]+")
    # Replace all non-alphanumerical characters by empty string ""
    clean_string = invalid_chars_regex.sub("", s)
    # Convert all characters to lower case
    clean_string = clean_string.lower()

    # Check whether the string is palindrome
    # if len(clean_string) is even, we check every character,
    # if len(clean_string) is odd, we don't have to check the middle character

    for i in range(len(clean_string) // 2):
        if clean_string[i] != clean_string[-(1 + i)]:
            return False

    return True


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
