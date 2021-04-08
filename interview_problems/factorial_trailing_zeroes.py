# https://leetcode.com/problems/factorial-trailing-zeroes/
# Given an integer n, return the number of trailing zeroes in n!.
# Follow up: Could you write a solution that works in logarithmic time complexity?

# O(n^2) time complexity, O(1) space complexity
def trailing_zeroes(n):
    """
    :type n: int
    :rtype: int
    """
    factorial = 1
    zeroes = 0
    for i in range(n, 1, -1):
        factorial *= i

    factorial = str(factorial)
    for i in range(len(factorial) - 1, 0, -1):
        if factorial[i] != "0":
            break
        zeroes += 1

    return zeroes


print(trailing_zeroes(3))
print(trailing_zeroes(5))
print(trailing_zeroes(0))


# O(n^2) time complexity - but worse than the previous solution - Time Limit Exceeded on LeetCode
# O(1) space complexity
# def trailing_zeroes2(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     factorial = 1
#     zeroes = 0
#     for i in range(n, 1, -1):
#         factorial *= i
#
#     print(factorial)
#     i = 10
#     # We find number of trailing zeroes by modulo 10, 100, 1000...
#     while factorial % i == 0:
#         zeroes += 1
#         i *= 10
#
#     return zeroes
#
#
# print(trailing_zeroes2(3))
# print(trailing_zeroes2(5))
# print(trailing_zeroes2(0))
# print(trailing_zeroes2(10))

# O(log5 n) time complexity, O(1) space complexity
def trailing_zeroes3(n):
    """
    :type n: int
    :rtype: int
    """
    # We can get trailing zeroes by floor dividing n by 5 (finding out how many 5s are in n)
    zeroes = 0

    while n > 0:
        n //= 5
        zeroes += n

    return zeroes


print(trailing_zeroes3(3))
print(trailing_zeroes3(5))
print(trailing_zeroes3(0))
