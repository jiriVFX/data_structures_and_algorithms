# https://leetcode.com/problems/sqrtx/
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated,
# and only the integer part of the result is returned.

# Solution 1 - naive brute force
# O(sqrt (x)) time complexity, O(1) space complexity - very inefficient with large numbers
def my_sqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x <= 1:
        return x
    square = 1
    while square * square <= x:
        square += 1

    return square - 1


# print(my_sqrt(4))
# print(my_sqrt(8))
# print(my_sqrt(2147395599))


# Solution 2 - binary search
# O(n/2) time complexity, O(1) space complexity
def my_sqrt2(x):
    """
    :type x: int
    :rtype: int
    """
    minimum = 0
    maximum = x
    middle = 0

    while minimum <= maximum:
        # always has to be floor division, otherwise fails in edge cases
        middle = (minimum + maximum) // 2

        if middle * middle > x:
            maximum = middle - 1
        elif middle * middle < x:
            minimum = middle + 1
        else:
            return middle
    # when exact int is not found, return maximum
    return maximum


print(my_sqrt2(1))
print(my_sqrt2(36))
print(my_sqrt2(3))
print(my_sqrt2(4))
print(my_sqrt2(5))
print(my_sqrt2(8))
print(my_sqrt2(2147395599))
