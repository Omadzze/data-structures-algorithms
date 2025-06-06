#https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.\
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # return node at which the two lists interstected
        # else return null

        node_a_seen = set()

        while headA is not None:
            node_a_seen.add(headA)
            headA = headA.next

        while headB is not None:
            if headB in node_a_seen:
                return headB

            headB = headB.next

        return None