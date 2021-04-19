# https://leetcode.com/problems/count-primes/
# Count the number of prime numbers less than a non-negative number, n.

# Solution 1 - brute force
# O(n^2) time complexity, O(1) space complexity - Time limit exceeded on LeetCode
def count_primes(n):
    """
    :type n: int
    :rtype: int
    """
    primes_num = 0
    is_prime = True

    # test all numbers from 2 up to n - 1
    for i in range(2, n):
        is_prime = True
        # Modulo i with all number from 2 to i - 1
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            # print(i)
            primes_num += 1

    return primes_num


# print(count_primes(10))
# print(count_primes(0))
# print(count_primes(1))


# Solution 2 - Sieve of Eratosthenes
# O(n) time complexity, O(n) space complexity - list will all nums up to n
# from math import sqrt


def count_primes_2(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return 0

    # create a list of all numbers up to n and mark every number with 1 (1 for prime 0 for non-prime)
    numbers = [1] * n
    # 0 and 1 are not counted as primes
    numbers[0] = 0
    numbers[1] = 0

    # test all numbers up to i square root of n, starting from 2
    # sqrt(n) can be replaced by int(n ** 0.5), which is slighly faster
    for i in range(2, int(n ** 0.5) + 1):
        # if number is still marked as prime (with 1)
        if numbers[i] == 1:
            # mark all multiples of i as non-primes (0)
            # start from i * i as that is the first multiple of i
            for j in range(i * i, n, i):
                numbers[j] = 0

    return sum(numbers)


print(count_primes_2(10))
print(count_primes_2(0))
print(count_primes_2(1))


# # Solution 3 - Sieve of Eratosthenes - using set - proved slower than using list
# # O(n) time complexity, O(n) space complexity
# def count_primes_3(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     if n <= 2:
#         return 0
#
#     # set to include all non-prime numbers
#     numbers = set()
#
#     # test all numbers up to i square root of n, starting from 2
#     # sqrt(n) can be replaced by int(n ** 0.5)
#     for i in range(2, int(n ** 0.5) + 1):
#         # if number is not in numbers set already
#         if i not in numbers:
#             # all multiples of i are non-primes and will be added to numbers set
#             # start from i * i as that is the first multiple of i
#             for j in range(i * i, n, i):
#                 numbers.add(j)
#
#     # resulting number of primes equals all numbers up to n - 1 minus amount of items in numbers set minus 1
#     # we have to remove 1, because we start counting from 2, which is the first prime
#     num_of_primes = (n - 1) - len(numbers) - 1
#
#     return num_of_primes
#
#
# print(count_primes_3(10))
# print(count_primes_3(0))
# print(count_primes_3(1))
