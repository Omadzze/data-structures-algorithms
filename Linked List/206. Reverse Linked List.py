#https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        Approach (Two pointers):
        Given a linked list which we need to reverse. We could use two pointers both will make connection between each other
        and reverse the sequence. Once connection was estbalished we need to update pointers to the next values.

        Time Complexity O(n)
        Space Complexity O(1)
        """

        if head == None:
            return None

        previous, current = None, head

        while current:
            # keep next value from a list
            next_value = current.next
            # assign next value to previous  2 -> 1
            current.next = previous
            # keep link
            previous = current
            # update to next value e.g. 3
            current = next_value

        return previous