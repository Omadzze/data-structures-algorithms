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


        """
        # 2. approach fast and slow pointer - space efficient

        slow = head
        fast = head
        
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        
        return False
        """
