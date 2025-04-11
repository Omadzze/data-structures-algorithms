#https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        """
        1. We have a root node which considers as "good" after that we need to compare values whether we have smth higher than root node value
        2. If we have we would need to update our max_value and increase counter++ since we have good value
        3. Else we are doing nothing

        Possible solutions:
        1. Use recursion: Go through nodes and compare them with the root node if path contains higher value, update value max_value, counter++

        Constraints:
        Each node's value is between [-10^4, 10^4]

        Complexity:
        Time: O(n) - visit one node at a time
        Space: O(n)
        """

        def dfs(node, current_max):
            # init count instance
            nonlocal count

            if node.val >= current_max:
                count += 1

            # update max value
            new_max = max(current_max, node.val)

            # recursion from left and right side
            if node.right:
                dfs(node.right, new_max)

            if node.left:
                dfs(node.left, new_max)


        count = 0
        # since we have negative values we need to init negative inf. current max
        dfs(root, float("-inf"))
        return count