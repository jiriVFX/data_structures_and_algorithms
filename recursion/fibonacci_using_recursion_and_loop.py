# Return nth number in Fibonacci sequence, n is given index number


# O(2^n) exponential time complexity
def fibonacci_rec(n):
    """Fibonacci sequence with recursion. Returns nth element in the sequence."""
    if n > 1:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    return n


# O(n) linear time complexity
def fibonacci_loop(n):
    """Fibonacci sequence with a for loop. Returns nth element in the sequence."""
    fibonacci_list = [0, 1]
    if n > 1:
        for i in range(1, n):
            next_number = fibonacci_list[i - 1] + fibonacci_list[i]
            fibonacci_list.append(next_number)
    return fibonacci_list[n]


# O(n) - dynamic programming.
# Caching already computed part of the sequence
def fibonacci_cached(n, cache):
    """More efficient recursive Fibonacci sequence with caching. Returns nth element in the sequence."""
    if n > 1:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci_cached(n - 1, cache) + fibonacci_cached(n - 2, cache)
            return cache[n]
    return n


print(fibonacci_rec(8))
print(fibonacci_loop(8))
print(fibonacci_cached(8, cache={0: 0, 1: 1}))
