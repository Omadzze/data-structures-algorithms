#https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        """
        1. Sliding window approach
        2. Primary goal will be remove 0 if it exist and then calculate window size till the next 0 and then calculate it once again
        3. For that we would need to use left and right pointers and put into sliding window
        """

        left = 0 # left pointer
        k = 1 # number of removals
        counter = 0 # number of 0
        for right in range(len(nums)):
            if nums[right] == 0:
                counter += 1

            if counter > k:
                if nums[left] == 0:
                    counter -= 1
                left += 1

        return right - left