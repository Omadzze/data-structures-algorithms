#https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursion:
        1. Traverse left-tree most
        2. Traverse right-tree most
        3. Take middle/root value

        Compelixty:
        Time: O(n)
        Spae: O(n)
        """
        def recursion(root, result):
            if root is not None:
                recursion(root.left, result)
                recursion(root.right, result)
                result.append(root.val)

        result = []
        recursion(root, result)
        return result