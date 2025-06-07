#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
        Approach:
        We need to remove last element from the list and then return it's head.
        The thing is that to remove last element we need to know the size of the list
        first, we then can decrement size and simply do head.next.next to remove element
        """

        # creating dummy node in linked list
        dummy =  ListNode(0)
        # assign dummy node to head as first
        dummy.next = head
        length = 0
        first = head

        # iterate till the end
        while first is not None:
            length += 1
            first = first.next

        length -= n
        first = dummy

        # iterate backwards
        while length > 0:
            length -= 1
            first = first.next

        first.next = first.next.next
        return dummy.next