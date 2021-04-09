# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.


# O(n) time complexity, O(n) space complexity
# Causes Runtime Error on LeetCode, the cause is unknown
def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    brackets = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    for bracket in s:
        # If it is an opening bracket, add it to the stack
        if bracket in brackets:
            stack.append(bracket)
        else:
            # If it's a closing bracket, check whether it matches the last opening bracket in stack
            last_in_stack = stack[len(stack) - 1]
            if bracket == brackets[last_in_stack]:
                # If it does, remove the last bracket from stack
                stack.pop()
            else:
                # Otherwise, the input string is not valid
                return False

    # Check whether the stack is empty
    if len(stack) == 0:
        return True
    else:
        return False


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))
print(is_valid("([])"))

# print("-----------------------------------------------")
# # O(n^2) time complexity, O(1) space complexity
# # To make the previous code work on older versions of python (pre 3.7), we have to use OrderedDict
# from collections import OrderedDict
#
#
# def is_valid2(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     open_brackets = OrderedDict()
#     open_brackets["("] = 0
#     open_brackets["{"] = 0
#     open_brackets["["] = 0
#
#     closed_brackets = OrderedDict()
#     closed_brackets[")"] = 0
#     closed_brackets["}"] = 0
#     closed_brackets["]"] = 0
#
#     for bracket in s:
#         if bracket in open_brackets:
#             open_brackets[bracket] += 1
#         else:
#             closed_brackets[bracket] += 1
#
#     for (open_bracket, num1), (closed_bracket, num2) in zip(open_brackets.items(), closed_brackets.items()):
#         # print(f"{num1} == {num2}")
#         if num1 != num2:
#             return False
#     return True
#
#
# print(is_valid2("()"))
# print(is_valid2("()[]{}"))
# print(is_valid2("(]"))
# print(is_valid2("([)]"))
# print(is_valid2("{[]}"))
# print(is_valid2("([])"))
