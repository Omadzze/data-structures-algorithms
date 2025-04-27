# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        """
        Approach:

        1. Going through the values and appending them to the list
        2. We then creating pointers in the beginning and ending and calcuating maximum value
        3. Incremeneting and decrementing pointers and returning maximum value

        Time Complexity: O(n) - adding elements to the list and iterating by pointers
        Space Compleixty: O(n) - n since we have list to which we push elements
        """

        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next

        i = 0
        j = len(values) - 1

        maximum_sum = 0

        while i < j:
            maximum_sum = max(maximum_sum, values[i] + values[j])
            i += 1
            j -= 1

        return maximum_sum