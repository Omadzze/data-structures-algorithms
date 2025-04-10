#https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        """
        The problem can be solved recursively. The idea is to first check the middle values in a tree.
        Then go below and check child values whether they are mirroing each other.
        Child from left branch should not mirror child from right branch. Iterate and return True

        Complexity:
        Time Complexity: O(n) - because we are going through the tree once, 'n' total number ofnodes
        Space Complexity O(n) - because we are using recursion
        """

        def isMirror(left_check, right_check):

            # traversed through all values and return True when finished
            if left_check is None and right_check is None:
                return True

            # if one node still contains value return false
            if left_check is None  or right_check is None:
                return False

            return(
                # if left and right similar value
                    (left_check.val == right_check.val)
                    # note that Left side: right child
                    # Right side: left child
                    #vice versa
                    and isMirror(left_check.right, right_check.left)
                    and isMirror(left_check.left, right_check.right)
            )

        return isMirror(root, root)