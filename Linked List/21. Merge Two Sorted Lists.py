#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
        First let's create dummy listnode where we will store values,
        we then would have "tail" that will point always to the last node in a linked list.

        we need to check values and if one smaller we need link it to the tail and go to next value

        if reached limit for one of the linked list we need to link all values to the tail

        finally we are returning linked list values that we build

        Time compleixty: O(n + m) - traversing each list, n list and m list
        Space Complexity: O(1)
        """

        final_list = ListNode()
        tail = final_list # point to the last node in a linked list

        while list1 and list2:
            if list1.val > list2.val:
                # append list 2 value
                tail.next = list2
                # go to next value
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next

            tail = tail.next

        # if we reached limit for one of the list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return final_list.next