# Bubble sort O(n^2) - super inefficient, space complexity O(1)

def bubble_sort(num_list):
    for _ in num_list:
        for i in range(len(numbers) - 1):
            if num_list[i] > num_list[i + 1]:
                # Swap the two numbers
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp


numbers = [13, 33, 6, 187, 1, 5, 89, 56, 2, 11]

print(f"Unsorted input: {numbers}")
bubble_sort(numbers)
print(f"Sorted output:  {numbers}")
