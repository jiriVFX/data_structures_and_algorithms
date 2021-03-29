# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree
# in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.root = None

    # Just for printing our tree, so we can see what we are doing
    def traverse_preorder(self, current_node, print_list):
        print_list.append(current_node.val)
        if current_node.left is not None:
            self.traverse_preorder(current_node.left, print_list)
        if current_node.right is not None:
            self.traverse_preorder(current_node.right, print_list)
        return print_list

    def sorted_array_to_bst(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 0:
            middle = len(nums) // 2
            root = TreeNode(nums[middle])

            left = nums[:middle]
            right = nums[middle + 1:]

            root.left = self.sorted_array_to_bst(left)
            root.right = self.sorted_array_to_bst(right)

            return root
        else:
            return None


solution = Solution()
tree_root = solution.sorted_array_to_bst([-10, -3, 0, 5, 9])
print(solution.traverse_preorder(tree_root, []))

solution = Solution()
tree_root = solution.sorted_array_to_bst([1, 3])
print(solution.traverse_preorder(tree_root, []))

solution = Solution()
tree_root = solution.sorted_array_to_bst([0, 1, 2, 3, 4, 5])
print(solution.traverse_preorder(tree_root, []))
