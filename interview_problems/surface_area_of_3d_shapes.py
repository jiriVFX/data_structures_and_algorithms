# https://leetcode.com/problems/surface-area-of-3d-shapes/
# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
# After placing these cubes, you have decided to glue any directly adjacent cubes to each other,
# forming several irregular 3D shapes.
# Return the total surface area of the resulting shapes.
# Note: The bottom face of each shape counts toward its surface area.

# Solution 1
# O(n^2) time complexity, O(1) space complexity
def surface_area(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # calculate surface area of each position - num of cubes * 4 + bottom + top
    # minus number of touching sides with cubes on left, right, top and bottom
    # 2 * because we have to subtract both current cube wall and previous cube wall touching on the same side
    final_area = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if the current field is not empty
            if grid[i][j] > 0:
                area = grid[i][j] * 4 + 2

                # if there are cubes on the left
                if j > 0 and grid[i][j - 1] > 0:
                    # subract the smaller of two fields (the actual number of touching sides)
                    sides_to_subtract = min(grid[i][j], grid[i][j - 1])
                    # subtract touching sides on the left
                    area = area - sides_to_subtract

                # if there are cubes on the right
                if j < len(grid[i]) - 1 and grid[i][j + 1] > 0:
                    # subract the smaller of two fields (the actual number of touching sides)
                    sides_to_subtract = min(grid[i][j], grid[i][j + 1])
                    # subtract touching sides on the left
                    area = area - sides_to_subtract

                # if there are cubes in the previous row
                if i > 0 and grid[i - 1][j] > 0:
                    # subract the smaller of two fields (the actual number of touching sides)
                    sides_to_subtract = min(grid[i][j], grid[i - 1][j])
                    # subtract touching sides on the left
                    area = area - sides_to_subtract

                # if there are cubes in the next row
                if i < len(grid[i]) - 1 and grid[i + 1][j] > 0:
                    # subract the smaller of two fields (the actual number of touching sides)
                    sides_to_subtract = min(grid[i][j], grid[i + 1][j])
                    # subtract touching sides on the left
                    area = area - sides_to_subtract

                    # if the current field is empty
            else:
                area = 0

            # add result to complete surface area
            final_area += area

    return final_area


print(surface_area([[2]]))
print(surface_area([[1, 2], [3, 4]]))
print(surface_area([[1, 0], [0, 2]]))
print(surface_area([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(surface_area([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
