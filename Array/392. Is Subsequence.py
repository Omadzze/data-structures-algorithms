#https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        """
        Approach:
        1. Init two pointers one to s and other to t
        2. Check length of both pointers and iterate till one of this will be not exhausted
        3. If one of this will be exhausted we need to check chars and return result

        Time compexity:
        O(n + m) - since we are going through the both strings only once and comparing them
        """

        left, right = 0, 0

        # note that with and condition we would specifically check whether one of the pointer was exhasuted or not
        while left < len(s) and right < len(t):

            if right == len(t):
                return False

            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                right += 1

        if left == len(s):
            return True
        else:
            return False

