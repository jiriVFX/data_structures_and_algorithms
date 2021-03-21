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


# Version with variable number of stairs we can climb each time
def climb_stairs_x(n, x=[1, 2]):
    """
    :type n: int
    :type x: list
    :rtype: int
    """
    # O(n^2) time complexity
    fibonacci = [0, 1]
    if n > 1:
        for i in range(2, n + 2):
            current = 0
            for j in x:
                if i - j >= 0:
                    current += fibonacci[i - j]
            fibonacci.append(current)
        print(fibonacci)
        return fibonacci[n + 1]
    else:
        if n >= 0:
            return fibonacci[n]


print(climb_stairs(5))
print(climb_stairs_x(5, [1, 2, 3]))
