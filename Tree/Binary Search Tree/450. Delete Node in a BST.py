#https://leetcode.com/problems/delete-node-in-a-bst/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minValue(self, node):

        while (node.left != None):
            node = node.left

        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        """
        1. We need to return value in a tree, once value will be deleted then can recreate the tree again.
        2. Because if the value is deleted then the tree is invalid anymore and thus recretation is needed.

        Approach:
        1. Found the node to remove,
        2. Once node was removed we need to compare child nodes which of them has higher value
        3. We then need to put higher value node above and lower below this child node
        """

        if not root:
            return None

        # check which side of tree to traverse
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # check whether side of tree has elements and if no fall back to other side
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_value = self.minValue(root.right)
                root.val = min_value.val
                root.right = self.deleteNode(root.right, min_value.val)

        return root