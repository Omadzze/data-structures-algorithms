#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def recursion(left, right):

            # if not elements to create binary tree
            if left > right:
                return None

            middle = (left + right) // 2

            # preorder traversal (steps: node, left, right)
            root = TreeNode(nums[middle])
            root.left = recursion(left, middle - 1)
            root.right = recursion(middle + 1, right)
            return root

        rec = recursion(0, len(nums) - 1)
        return rec
