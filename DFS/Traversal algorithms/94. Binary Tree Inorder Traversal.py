#https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        """
        Few possible ways to solve this problem
        1. Recurisve appraoch: Iterate through the left, append value, iterate right
            1.1 Note that recursive approach works in a way that it will iterate in left-side most till it will not reach the base case (None)
            then it will append value of it and iterate again in right-side most till it will not reach the base (None) again and append value.
            Repeat process

        Complexity:
        Time O(n) - recursive function, iterating through the each nodes
        Space O(n) - number of nodes
        """
        def recursive(root, result):
            if root is not None:
                # left
                recursive(root.left, result)
                # value
                result.append(root.val)
                # right
                recursive(root.right, result)

        result = []
        recursive(root, result)
        return result
