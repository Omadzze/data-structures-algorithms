#https://leetcode.com/problems/search-in-a-binary-search-tree/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        """
        Since we are given binary tree and we need to find element what we can do is acutally
        travese the tree by looking whether value is higher or lower, since we know that BST
        values from left side lower and from right side higher

        Time Compleixty: O(H) - height of the tree, O(log N) - average case and O(N) - is the worst case
        Space Complexity O(H) - to keep recursive stack
        """


        # Recursive approach
        if root is None or root.val == val:
            return root

        # returns the node and children nodes of the tree
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)