#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        """
        We need to find max value by adding together values in one level. We then would need to return level
        index of max value.

        Approach BFS:
        1. Increment level every time with the default sum
        2. Once it incremented check whether it's higher and if it's higher update all values
        """

        queue = deque()

        if root:
            queue.append(root)

        level, answer, max_sum = 0, 0, float("-inf")

        while len(queue) > 0:
            level += 1 # increment level
            sum_current_level = 0 # we need to put to default value after each level update

            for i in range(len(queue)):

                current = queue.popleft()

                sum_current_level += current.val # keep track of current sum value

                if current.right:
                    queue.append(current.right)

                if current.left:
                    queue.append(current.left)

            # check whether sum is higher than max sum and update all values
            if sum_current_level > max_sum:
                max_sum = sum_current_level
                answer = level

        return answer