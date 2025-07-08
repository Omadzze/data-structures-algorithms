# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 1. Traversing linked list
        """
        current = head

        while current:
            print(current.val)
            # move to next value
            current = current.next
        """

        # 2. Saerching in linked list
        """
        current = head

        while current:

            if current.val == 6:
                return True

            current = current.next

        return False
        """

        # 3. Find length of linked list
        """
        current = head
        length = 0

        while current:

            length += 1
            current = current.next

        return length
        """

        # 4. Insertion at the beginning
        """
        # create new node
        new_node = ListNode(0)
        # link new node to the beginning of head
        new_node.next = head
        # new_node it's new beginning of our linked list
        head = new_node

        return head
        """

        # 5. Insertion at the end
        """
        new_node = ListNode(6)

        if head:
            return new_node

        last = head

        # traverse till the last node in linked list
        while last.next:
            last = last.next

        # link last node to the new node
        last.next = new_node

        return head
        """

        # 6. Insert at specific position
        new_node = ListNode(7)

        current = head

        while current:

            if current.val == 3:
                next_val = current.next  # keep next value
                current.next = new_node  # assign to the new node
                new_node.next = next_val  # new node connect with next value

            current = current.next

        return head



