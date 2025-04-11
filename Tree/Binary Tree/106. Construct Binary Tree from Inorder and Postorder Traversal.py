#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def recursion(left, right):

            # if no elements in subtrees
            if left > right:
                return None

            # popping last element from postorder to create root element
            value = postorder.pop()
            # assign root element to tree
            root = TreeNode(value)

            # split left and right subtree in inorder list based on a postorder root element
            index = idx_map[value]

            # create left and right subtree
            root.right = recursion(index + 1, right)
            root.left = recursion(left, index - 1)

            return root


        idx_map = {}
        for index in range(len(inorder)):
            # get value from inorder list
            value = inorder[index]
            # map hashmap index to the value from inorder list
            idx_map[value] = index

        return recursion(0, len(inorder) - 1)