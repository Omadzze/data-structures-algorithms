#https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def removeStars(self, s: str) -> str:

        """

        Removing chars when star charcater was found

        Approach:
        adding elements to the stack opeartion

        1. We are adding elements till we found * once it was found we need to remove .pop last element
        and then continue.

        Time Complexity: O(n) - since we are going through the chars once.
        Splace Complexity: O(n)
        """

        stack = []

        for char in range(len(s)):
            if s[char] != "*":
                stack.append(s[char])
            else:
                stack.pop()
                continue

        return "".join(stack)