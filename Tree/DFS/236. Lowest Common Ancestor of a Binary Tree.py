# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        1 .We are give p value and q value, both of these values can represent overlap combined with the root
        2. Once we combined values and found overlap we then have few things to do
        3. We need find value that has this descendants or it can be the same value of "p" descendant

        Approach:
        To find an overlap we can traverse the tree and look when our tree will reach p and q, if it reached both of these then we can return True
        and answer
        """

        def dfs(root):

            nonlocal answer

            # if we reached the end of branch
            if not root:
                return False

            # tree traversing
            left = dfs(root.left)
            right = dfs(root.right)

            # check whether we reached p or q
            if root == p:
                mid = True
            elif root == q:
                mid = True
            else:
                mid = False

            if mid + left + right >= 2:
                answer = root

            return mid or left or right


        answer = None
        dfs(root)
        return answer