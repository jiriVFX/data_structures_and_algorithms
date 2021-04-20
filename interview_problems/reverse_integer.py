# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Solution 1  - string reversion - proved slightly faster than the division
# O(log10 x) time complexity (number of digits), O(1) space complexity
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    negative = False
    # remember whether x is positive or negative
    if x < 0:
        negative = True
        # make x positive
        x *= - 1
    # convert x to string
    x = str(x)
    # reverse x
    x = x[::-1]
    # convert back to int
    x = int(x)
    # if x was originally negative
    if negative:
        # make x negative again
        x *= - 1

    # if number goes over the specified limits (-2^31 to 2^31)
    if x > 2147483648 or x < -2147483648:
        return 0
    return x


# print(reverse(123))
# print(reverse(-123))
# print(reverse(120))
# print(reverse(0))
# print(reverse(1534236469))


# Solution 2 - division
# O(log10 x) time complexity (number of digits), O(n) space complexity (number of digits)
def reverse_2(x):
    """
    :type x: int
    :rtype: int
    """
    reversed_int = 0
    negative = False
    # remember whether x is positive or negative
    if x < 0:
        negative = True
        # make x positive
        x *= - 1

    # create reversed int
    while x != 0:
        digit = x % 10
        # remove one zero from x
        x = int(x / 10)
        reversed_int = reversed_int * 10 + digit

    # if x was originally negative
    if negative:
        # make x negative again
        reversed_int *= - 1
    # if number goes over the specified limits (-2^31 to 2^31)
    if reversed_int > 2147483648 or reversed_int < -2147483648:
        return 0

    return reversed_int


print(reverse_2(123))
print(reverse_2(-123))
print(reverse_2(120))
print(reverse_2(0))
print(reverse_2(1534236469))
