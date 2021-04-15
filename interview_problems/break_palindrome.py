# Hackerrank problem
# Complete the 'breakPalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING palindromeStr as parameter.
# Return "IMPOSSIBLE" if string can't be created


def break_palindrome(palindrome_str):
    if len(palindrome_str) == 1:
        return "IMPOSSIBLE"

    return_palindrome = ""
    for i in range(len(palindrome_str)):
        position = ord(palindrome_str[i])
        # 97 = "a" in unicode
        if position > 97:
            # In Explanation "abca" is one of possible outputs for "acca", but test fails and expects "aaca" output
            # for this reason char is always replaced by an "a" (97)
            # position -= 1
            # new_char = chr(position)
            new_char = chr(97)
            return_palindrome += new_char
            # add the rest of the string
            return_palindrome += palindrome_str[i + 1:]
            # when changed char is in the middle of the string
            if i == len(return_palindrome) // 2 and (
                    return_palindrome[i] == return_palindrome[i - 1] == return_palindrome[i + 1]):
                return "IMPOSSIBLE"
            else:
                return return_palindrome
        else:
            return_palindrome += palindrome_str[i]

    return "IMPOSSIBLE"


print(break_palindrome("bab"))
