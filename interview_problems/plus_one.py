# https://leetcode.com/problems/plus-one/
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# E.g. [1, 2, 3] represents 123
# We return [1, 2, 4] which represents 124

# Solution 1: Naive brute force approach, first that came in mind
# O(2n) time complexity, O(2n) space complexity
def plus_one(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    number = ""
    numbers = []
    # Convert digits in the list to string
    for digit in digits:
        number += str(digit)
    # Convert string back to integer and plus 1
    number = int(number) + 1
    # Convert back to string
    number = str(number)
    # Convert back to int list
    for char in number:
        numbers.append(int(char))

    return numbers


print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([0]))
print(plus_one([9, 9, 9, 9]))


# Solution 2: Bit better approach after a bit of thinking
# O(2n) time complexity (in the worst case with [9,9,9,9,9], otherwise better)
# O(n) space complexity
def plus_one2(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digit = digits.pop()
    zeroes = []

    if digit == 9:
        # Keep removing last number until you find number that is not 9
        while digit == 9 and len(digits) > 0:
            digit = digits.pop()
            zeroes.append(0)
        # Raise the value of the first number that is not 9 by 1
        if digit != 9:
            digit += 1
        else:
            # In case the last digit was 9 too
            digits.append(1)
            digit = 0
        digits.append(digit)
        # Append all the zeroes
        digits.extend(zeroes)
    else:
        # If the last digit is not 9, we can just plus 1 and append back to the list
        digits.append(digit + 1)

    return digits


print(plus_one2([1, 2, 3]))
print(plus_one2([4, 3, 2, 1]))
print(plus_one2([0]))
print(plus_one2([9, 9, 9, 9]))


# Solution 3: The best approach after bit more thinking
# O(n) time complexity (in the worst case with [9,9,9,9,9], otherwise O(1))
# O(1) space complexity
def plus_one3(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if digits[-1] == 9:
        i = len(digits) - 1
        # Continue replacing 9s with 0s until the current digit is not 9 or i is 0 (end of the list)
        while digits[i] == 9 and i > 0:
            digits[i] = 0
            i -= 1
        if digits[i] != 9:
            digits[i] += 1
        else:
            # If the last digit is 9 too
            digits[i] = 1
            digits.append(0)
    else:
        digits[-1] += 1

    return digits


print(plus_one3([1, 2, 3]))
print(plus_one3([4, 3, 2, 1]))
print(plus_one3([0]))
print(plus_one3([9, 9, 9, 9]))
