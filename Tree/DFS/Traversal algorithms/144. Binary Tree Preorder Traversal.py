#https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        """
        1. Start with root val
        2. Go left
        3. Then go right

        In our case we are using LIFO method with stacks, so order of execution will be first add val to the list then add right values first(this will be last)
        Then we are adding left value(this will be taken first) and iterate

        [1, 2, 4, none_found, 5, 6, none_found 7, none_found, 3, 8, 9, none_found]

        Complexity:
        Time: O(n) - because we are visiting one node once
        Splace: O(n)
        """

        # base case
        if root is None:
            return []

        # appending tree to the stack
        stack = [root]
        result = []

        while stack:
            # LIFO - Last In First Out
            root = stack.pop()
            if root is not None:
                # take first value "root"
                result.append(root.val)
                # because of LIFO and "preorder type"
                # this will be processed last
                if root.right is not None:
                    stack.append(root.right)
                # should be last one because of LIFO method and "preorder type"
                # we will process it first
                if root.left is not None:
                    stack.append(root.left)

        return result
