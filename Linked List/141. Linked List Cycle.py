#https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """
        Detecting cycle in a linked list, we need to understand whether we have cycle or not. For this we can use hashet and simply append
        all the nodes to the set and check them up.

        Time complexity O(n) - since we are traversing all values once
        Space Complexity O(n) - since we are storing values in a hashset
        """

        # 1. Approach Hashset - not space efficient

        # hash set
        nodes_seen = set()
        current = head

        while current is not None:
            # check whether we have already same nodes
            if current in nodes_seen:
                return True

            nodes_seen.add(current)
            current = current.next

        return False

        # SOLUTION 2: Slow and Fast pointers
        """
        we need to check whether fast pointer is None or there
        is no other values to stop loop.

        1. we need check whether fast pointer referering to the slow pointer
        2. If it's referering we can output results directly

        Time Complexity: O(n) - since we are traversing list once.
        Space Complexity: O(1) - since we are not saving anything. 
        """

        #slow, fast = head, head

        #while fast and fast.next is not None:

       #     slow = slow.next
       #     fast = fast.next.next

       #     if slow == fast:
       #         return True

       # return False