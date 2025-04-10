#https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def recursion(root):
            if root is None:
                return 0
            else:
                left_root = recursion(root.left)
                right_root = recursion(root.right)

            return max(left_root, right_root) + 1

        return recursion(root)