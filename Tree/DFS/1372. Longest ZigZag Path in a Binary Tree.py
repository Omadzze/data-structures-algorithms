# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        """
        Problem:
        We need to find zig-zag pattern. Note: zig-zag is only working when it follows pattern.
        left to right or right to left, it can't be right, right. This is depth-first-search problem

        Approaches:
        Use recursion. we need to make if, else statements and check which path it currently tracks
        if pathf follows zig zag patterns then we need to increment counter++, otherwise keep as 1

        Finally, we would need to return max length. Note: don't forget to check base case

        Time complexity:
        Space Complexity O(n)
        Time complexity O(n)
        """

        def dfs(root, go_left, steps):
            """
            root: our Treenode,
            go_left: checks whether it goes to the left side
            steps: current counter, increase in every correct zig-zag iteration
            """
            nonlocal max_length


            if root:
                # return max length when tree was traversed
                max_length = max(max_length, steps)


                if go_left:
                    # if left was side, increment step and make it false so it will go to the right side
                    dfs(root.left, False, steps + 1)
                    # if we were expecting right but there were no then break step to 1 and expect Right side
                    dfs(root.right, True, 1)

                else:
                    dfs(root.left, False, 1)
                    # we were expecting right side and we got it increment value
                    dfs(root.right, True, steps + 1)

            return max_length

        max_length = 0
        return dfs(root, True, max_length)


