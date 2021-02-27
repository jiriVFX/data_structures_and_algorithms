# Merge sorted arrays O(a+b)

def merge_sorted_arrays(array1, array2):
    merged_array = []
    i = 0
    j = 0

    while i < len(array1) or j < len(array2):
        if i < len(array1) and j < len(array2):
            # Append the smaller item to the merge_array
            if array1[i] < array2[j]:
                merged_array.append(array1[i])
                i += 1
            else:
                merged_array.append(array2[j])
                j += 1
        else:
            # One of the arrays is at its end and i or j is out of range
            if j < len(array2):
                merged_array.append(array2[j])
                j += 1
            if i < len(array1):
                merged_array.append(array1[i])
                i += 1

    return merged_array


print(merge_sorted_arrays([0, 3, 4, 31, 33, 41], [4, 6, 32, 64]))


# ----------------------------------------------------------------------------------------------------------------------
# # Easy fast way
# def merge_sorted_arrays_easy(array1, array2):
#     return sorted(array1 + array2)
#
#
# print(merge_sorted_arrays_easy([0, 3, 4, 31, 33, 41], [4, 6, 32, 64]))
