# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.


# Stack solution - O(n) time complexity, O(n) space complexity
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
        # Check whether stack is empty
        elif len(stack) > 0:
            # If it's a closing bracket, check whether it matches the last opening bracket in stack
            last_in_stack = stack[len(stack) - 1]
            if bracket == brackets[last_in_stack]:
                # If it does, remove the last bracket from stack
                stack.pop()
            else:
                # Otherwise, the input string is not valid
                return False
        else:
            # If the bracket is a closing bracket and stack is empty
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
print(is_valid("([])]]]"))

