#https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # Recursive call
        def dfs(node):
            # check node
            if node is None:
                return []

            # check whether it's children node
            if node.left is None and node.right is None:
                return [node.val]

            # add up left and right part of tree together
            return dfs(node.left) + dfs(node.right)

        # compare both trees
        return dfs(root1) == dfs(root2)