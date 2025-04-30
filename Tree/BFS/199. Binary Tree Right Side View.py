#https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        """
        The problem description wants to take elements if we will look from right side to the tree.
        Thus we can create BFS and then divide it to the number of levels, at each level we will append numbers
        to the list however we will start traversing from right side first. We would then simply need to slice
        and return right elements

        Like:
        [1], Level_1
        [3, 2], Level_2

        tmp_result[0] will return [1, 3]

        Space Complexity: O(n)
        Time Complexity: O(n)
        """

        answer = [] # store final results
        queue = deque() # create queue for BFS

        if root:
            queue.append(root) # append all elements to the queue


        while len(queue) > 0: # iterates if we have elements in
            tmp_result = [] # store temp values

            for i in range(len(queue)):

                current = queue.popleft()

                tmp_result.append(current.val)

                # traverse right tree and then left
                if current.right:
                    queue.append(current.right)

                if current.left:
                    queue.append(current.left)

            # return rightmost results
            answer.append(tmp_result[0])

        return answer




