# https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# O(n^2) time complexity, O(n^2) space complexity
def generate(num_rows):
    """
    :type num_rows: int
    :rtype: List[List[int]]
    """
    pascal_triangle = [[1]]

    for level in range(1, num_rows):
        current_lvl = []
        # Each new level can be defined as +1 length of the previous one: len(pascal_triangle[level - 1]) + 1
        # or simply as current level + 1
        for j in range(level + 1):
            # The first and the last items are always 1
            if j == 0 or j == level:
                current_lvl.append(1)
            else:
                # Every other item is [j - 1] + [j] of the previous level
                current_lvl.append(pascal_triangle[level - 1][j - 1] + pascal_triangle[level - 1][j])
        # Append current level to the triangle
        pascal_triangle.append(current_lvl)

    return pascal_triangle


print(generate(5))
print(generate(1))
