# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
# so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# - It is the empty string, contains only lowercase characters, or
# - It can be written as AB (A concatenated with B), where A and B are valid strings, or
# - It can be written as (A), where A is a valid string.

# Solution 1
# O(n) time complexity, O(n) space complexity - using stack
def min_remove_to_make_valid(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    i = 0

    while i < len(s):
        if s[i] == "(":
            # save position of the bracket instead of the bracket itself
            stack.append(i)
            # increment i
            i += 1
        elif s[i] == ")":
            # if it is a closing bracket
            if len(stack) > 0:
                # if there is at least one opening bracket in the stack
                # remove opening bracket from a stack
                stack.pop()
                # increment i
                i += 1
            else:
                # if there are no opening brackets in the stack, remove the closing bracket
                # we don't increment i as length of the string is now -1
                if i < len(s) - 1:
                    s = s[:i] + s[i + 1:]
                else:
                    s = s[:i]
        else:
            # if it's not a bracket
            i += 1

    # check whether there are any opening brackets left in the stack
    # that would mean we have to remove the opening brackets left in the stack at the positions we saved
    if len(stack) > 0:
        for i in range(len(stack)):
            # every iteration one bracket is removed from a string
            # => every position is moving 1 to the left
            position = stack[i]
            if position - i >= 0:
                position -= i

            if position < len(s) - 1:
                s = s[:position] + s[position + 1:]
            else:
                s = s[:position]

    return s


# print(min_remove_to_make_valid("lee(t(c)o)de)"))
# print(min_remove_to_make_valid("a)b(c)d"))
# print(min_remove_to_make_valid("))(("))
# print(min_remove_to_make_valid("(a(b(c)d)"))

# Solution 1.1 - optimized solution 1 - turning s into a list
# O(n) time complexity, O(n) space complexity - using stack
def min_remove_to_make_valid2(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    s = list(s)

    for i in range(len(s)):
        if s[i] == "(":
            # save position of the bracket instead of the bracket itself
            stack.append(i)
        elif s[i] == ")":
            # if it is a closing bracket
            if len(stack) > 0:
                # if there is at least one opening bracket in the stack
                # remove opening bracket from a stack
                stack.pop()
            else:
                # if there are no opening brackets in the stack,
                # replace the closing bracket with an empty string
                s[i] = ""

    # check whether there are any opening brackets left in the stack
    # that would mean we have to remove the opening brackets left in the stack at the positions we saved
    if len(stack) > 0:
        for position in stack:
            # every iteration one bracket is replaced with an empty string
            s[position] = ""

    # convert list back to string
    s = "".join(s)

    return s


print(min_remove_to_make_valid2("lee(t(c)o)de)"))
print(min_remove_to_make_valid2("a)b(c)d"))
print(min_remove_to_make_valid2("))(("))
print(min_remove_to_make_valid2("(a(b(c)d)"))
