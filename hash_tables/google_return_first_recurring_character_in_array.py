# Return first recurring character in an array
# If an array has only unique items, return undefined/None

# + Usually O(1) (to insert, get, delete), worst case O(n) (more records at the same address)
# time complexity solution using a set (hash table)
# - Memory consumption is higher - O(n) now
dict_seen_this_set = set()
def return_first_recurring(array):
    for item in array:
        if item in dict_seen_this_set:
            return item
        else:
            dict_seen_this_set.add(item)
    return None


print(return_first_recurring([1, 5, 1, 2, 3, 5, 1, 2, 4]))