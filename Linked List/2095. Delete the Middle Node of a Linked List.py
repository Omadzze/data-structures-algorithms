#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        Two pointers approach:
        Using slow and fast pointers

        We can create two pointers fast pointer will always be n + 2 times ahead of slow pointer,
        thus when fast pointer will get to the ending we will stop pointer and slow pointer will be
        in position where it will be near the target that should be removed.

        Slow pointer: n
        Fast pointer: n+2

        By removing we simple need to ignore the target and not connect other values then target
        Input: previous -> target(don't append) -> next
        Output: previous -> next

        Time Complexity: O(n) - since iteration stops when fast reached the end and slow connect to values
        together so it's constant time

        Space complexity O(1)
        """

        # if we have only one node
        if head.next == None:
            return None

        # slow (n), fast (n+2)
        slow, fast = head, head.next.next

        # iterate two pointers till fast is not none
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # once fast is none, connect previous -> target (not connect it) -> next
        slow.next = slow.next.next

        # return the list
        return head