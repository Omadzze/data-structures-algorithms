#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        """
        Approach:
        1. Sliding window approach, we need to create window that will keep track of vowels
        2. Other window should go through characters and add up or remove counter

        Time Complexity O(n)
        """

        vowels = {'a', 'e', 'i', 'o', 'u'}
        answer = 0
        count = 0

        # build the window of size k, count number of vowels in container
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count

        # slide window to the right and add chars or remove them if they are not longer in the window range.
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)

        return answer