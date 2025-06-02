#https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        """
        Approach:
        The task is to find lognest substring that is possible by changing K charcaters on it. For that we can use sliding widnow approach.
        We need to use hashset and append values to count how much A or B we have, once we calculated we need to keep our values in the window.
        If they are in a window we need to maximize and retunr result of consequence characters

        Time Complexity: O(n) - however we have 26 characters but everything will be gone once
        Space Complexity: O(1) - since we are storing values only in a dic
        """
        counter = {}

        left = 0
        result = 0

        for right in range(len(s)):
            # count chars
            counter[s[right]] = 1 + counter.get(s[right], 0)

            # keep chars in the window
            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1

            # return maximum sequence of chars
            result = max(result, right - left + 1)

        return result
