#https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        """
        1. Sliding window approach. We need to keep range of window and change values in it.
        2. If we have 0 we can flip to 1 and we have K iterations.
        3. Once the window was updated we need to remove values from the window
        4. We need to keep track of max_value.
        5. this could be done by using two pointers and keeping track of window

        Time Complexity: O(n) - since we are going trough the whole list one time
        """

        left = 0
        for right in range(len(nums)):

            if nums[right] == 0:
                k -= 1

            # flip the number
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        # range
        return right - left + 1