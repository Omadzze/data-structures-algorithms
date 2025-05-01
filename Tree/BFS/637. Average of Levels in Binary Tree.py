#https://leetcode.com/problems/average-of-levels-in-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        """
        We need to find average of number of nodes in the levels and return it.

        The average will be total_sum/number_elements

        Time Complexity: O(n) - each node is traversed once
        Space Complexity: O(m) - queue, temp can grow upto maximum number of nodes at any level
        """

        queue = deque() # create queue

        # append value to queue
        if root:
            queue.append(root)

        answer = []
        total = 0

        while len(queue) > 0:

            # temp values for the levels
            current_sum = 0
            number_elements = 0

            for i in range(len(queue)):

                current = queue.popleft()

                # itearte through the level
                current_sum += current.val
                number_elements += 1

                if current.right:
                    queue.append(current.right)

                if current.left:
                    queue.append(current.left)

            # average of a level
            total = current_sum / number_elements
            answer.append(total)

        return answer