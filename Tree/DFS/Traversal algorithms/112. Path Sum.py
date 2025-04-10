#https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        """

        Recursive solution, possible to subtract current value with targetSum every time.

        1. Check for the base case when root is null
        2. subtract from targetSum value
        3. check whether it's leaf node
        4. recursively call for the each left and right nodes

        Time complexity:
        Space: O(n)
        Time: O(n)
        """

        # Base case to check whether root is null
        if root is None:
            return False

        targetSum -= root.val

        # check for leaf nodes
        if not root.left and not root.right:
            if targetSum == 0:
                return True

        # every time we are rerunning with the same targetSum
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)