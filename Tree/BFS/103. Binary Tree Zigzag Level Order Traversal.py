#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """

        We are given tree we need to return values in zigzag order so that they will be chnaging from left to right and then
        from right to left in the next level

        Approach BFS:
        1. For that we can traverse the tree but add bool that will be turned on when we need to change track of adding elements
        2. We then could return answer
        """

        queue = deque()

        if root:
            queue.append(root)
        else:
            return []

        array_answer = []
        level = 0

        left_to_right = True

        while len(queue) > 0:

            # temp result
            array_temp = []
            level = False

            # iterate through each node
            for _ in range(len(queue)):

                current = queue.popleft()

                array_temp.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            if not left_to_right:
                array_temp.reverse()

            array_answer.append(array_temp)
            left_to_right = not left_to_right

        return array_answer