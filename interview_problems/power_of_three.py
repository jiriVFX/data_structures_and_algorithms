# https://leetcode.com/problems/power-of-three/
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.

# Naive solution
# O(log3 n) time complexity (much less than O(n) in reality)
def is_power_of_three(n):
    """
    :type n: int
    :rtype: bool
    """
    x = 0
    power_three = 3 ** x
    while n > power_three:
        x += 1
        power_three = 3 ** x

    if power_three == n:
        return True
    return False


print(is_power_of_three(27))
print(is_power_of_three(0))
print(is_power_of_three(9))
print(is_power_of_three(45))
print(is_power_of_three(1))


# # Similar naive solution
# # O(log3 n) time complexity solution
# # This same code outputs different results on LeetCode compared to the local machine,
# # Reason uknown, but it is not unusual as LeetCode seems to run an older version of Python
# def is_power_of_three2(n):
#     """
#     :type n: int
#     :rtype: bool
#     """
#     while n > 1:
#         n = n / 3
#     if n == 1:
#         return True
#     return False
#
#
# print(is_power_of_three2(27))
# print(is_power_of_three2(0))
# print(is_power_of_three2(9))
# print(is_power_of_three2(45))
# print(is_power_of_three2(1))
