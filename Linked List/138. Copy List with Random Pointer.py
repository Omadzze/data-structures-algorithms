# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldCopy = {None: None}  # hashset to store values and links

        current = head

        # copy all values
        while current:
            copy = Node(current.val)  # take value
            oldCopy[current] = copy  # put these to the hashset
            current = current.next  # go to next element in a list

        current = head

        # make links at linked list
        while current:
            copy = oldCopy[current]  # access element
            copy.next = oldCopy[current.next]  # make link
            copy.random = oldCopy[current.random]  # make link
            current = current.next

        return oldCopy[head]