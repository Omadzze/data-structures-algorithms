#https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        """
        Problem required to go trough the tree and caclulate values in nodes and compare them with targetSum values,
        if we found value count++ else go next

        However, there are certain things to consider in this problem
        1. We would need to use hashmap to solve this problem.
        Since we would already go through elements we would need to append them to the hashmap.
        If we will not append elements then we would go through hasmap every time which will increase Time Complexity.

        1.1 With the hashmap we make sure that complexity stays the same since values will be added and removed from the hashmap and we don't need to calculate values every time
        """

        def dfs(root, curr_sum):

            nonlocal count
            if not root:
                return

                # append current value
            curr_sum += root.val

            # check wheher it's equal to our target that we are looking for
            if curr_sum == targetSum:
                count += 1

            # append occurence of the value in the root
            count += dic[curr_sum - targetSum]

            # append current sum to the hashmap
            dic[curr_sum] += 1

            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)

            # remove current sum from the hashmap
            dic[curr_sum] -= 1

        count = 0
        dic = defaultdict(int)
        dfs(root, 0)
        return count