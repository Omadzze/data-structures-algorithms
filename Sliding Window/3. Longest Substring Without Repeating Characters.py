#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        Approach:
        We need to find longest substring without duplicated characters. For that we can use set or simple array to store unique elements on it.
        We would always need to understand whether we already have elements or not and only after that we can count elements. Each time when Left
        will be updated we need to discard set. We would also need to update longest string after iteration
        """

        # init dic with coutner
        chars = Counter()

        left = right = 0

        result = 0

        while right < len(s):

            # append each element to dic
            r = s[right]
            chars[r] += 1

            # if some elements has 2 elements, discard one of this
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            # calculate max value
            result = max(result, right - left + 1)

            # go to next element
            right += 1

        return result