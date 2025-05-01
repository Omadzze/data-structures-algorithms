#https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """

        We would need to traverse the tree and return elements level by level. Note that they should be in [[level1], [level2], [level3]]

        Time Complexity: O(n) - since we are traversing each node once
        Space Complexity: O(m) - m depending on the depth of tree and number of nodes in it.  As we store elements in answer and temp_array.

        """

        queue = deque()

        if root:
            queue.append(root)
        else:
            return []

        answer = []

        while len(queue) > 0:
            # temp values
            temp_array = []

            for _ in range(len(queue)):

                current = queue.popleft()

                temp_array.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            answer.append(temp_array)

        return answer