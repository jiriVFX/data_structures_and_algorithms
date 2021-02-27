# O(n) complexity

# Adds target_sum - current number in array to a comp set
# Set items are unordered, unchangeable, and do not allow duplicate values.
# In Python sets and dictionaries are hash tables
# If current number is already in the set, there is a target_sum of two numbers in the arrray
# E.G. 5 - 2 = 3, with the next iteration we'll find 3 => returns True

def has_pair_with_sum(arr, target_sum):
    comp = set()

    for i in arr:
        if i in comp:
            return True
        comp.add(target_sum - i)
    return False

# print(has_pair_with_sum([1, 2, 3, 9], 5))

# ----------------------------------------------------------------------------------------------------------------------

# Less clever version

def has_pair_with_sum2(array, target_sum):
    comp = set()

    for i in range(len(array)):
        if array[i] not in comp:
            comp.add(target_sum - array[i])
        else:
            return True
    return False

print(has_pair_with_sum2([1, 2, 3, 9], 5))