#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # concat together all the words in s
        # lowercase them
        # after that we can put one pointer in the beginning and other pointer in the ending
        # we then can check values and decrease and increase pointers if the same return true else false

        # note that we don't care about other chars then strings

        # Time Complexity: O(n) - since we are traversing each value once and it depends on number of chars that we have in s
        # Space Complexity: O(1)

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


