#https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        Time Complexity: O(n) - since we are traversing each element once
        Space Compleixty O(n) - since we are stroing elements in the set
        """

        seen = set()
        current = head

        # iterate till it will be none
        while current is not None:
            # check whether we already saw the value
            if current not in seen:

                seen.add(current)
                # add value and go to the next value
                current = current.next
            else:
                return current

        return None