#https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        To solve this problem we need to create two heads, one for even and one for odd

        The odd head should start from first element
        While even head should start from second element

        Once odd will be fully traversed we would need to connect odd to even head.

        Time Complexity: O(n) - n total number of nodes
        Space Complexity: O(1)
        """

        # edge case if we have one value in a linked list

        if head == None:
            return None

        # Odd (n), Even (n + 1)
        odd, even = head, head.next

        even_head = even

        while even and even.next:
            # point odd to the next odd node
            odd.next = even.next
            odd = odd.next
            # point even to the next even node
            even.next = odd.next
            even = even.next

        # connect odd with even head to make full sequence
        odd.next = even_head
        return head