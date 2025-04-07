#https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # we need to return levels of sequence, particularly values of it that will be in a list level 1: [3], level  2: [9, 20].

        # in order to do that we can use recursion and increment level each time we are calling our recursion and going deep in our tree
        # we then need to append values to the list


        levels = []

        def recursion(root, level):
            if root is not None:

                # check current level, if increased append []
                if len(levels) == level:
                    levels.append([])

                # append values to the empty []
                levels[level].append(root.val)
                recursion(root.left, level + 1)
                recursion(root.right, level + 1)

        recursion(root, 0)
        return levels

