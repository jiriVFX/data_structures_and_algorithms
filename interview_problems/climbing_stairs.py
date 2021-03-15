# https://leetcode.com/problems/climbing-stairs/
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    # It is basically the fibonacci sequence
    # The difference is we always have to return n+1 item from the sequence
    # If there are two stairs, there are two possible combinations: 1 + 1 and 2
    # O(n) time complexity
    fibonacci = [0, 1]
    if n > 1:
        for i in range(2, n + 2):
            current = fibonacci[i - 2] + fibonacci[i - 1]
            fibonacci.append(current)
        print(fibonacci)
        return fibonacci[n + 1]
    else:
        if n >= 0:
            return fibonacci[n]


print(climb_stairs(5))
