#https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        """
        Approach:
        1. Left pointer start and right pointer end with incremenet and decrement
        2. check if value == k then increment result and update pointers
        if overshoot we need to decrement right side.
        else undershoot we need to increment left side.

        Note that array should be sorted

        Time Complexity O(nlog n) - because we are using sorting, while pointer opeation cost O(n)
        """
        nums = sorted(nums)

        left = 0
        right = len(nums) - 1

        counter = 0
        total = 0

        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                counter += 1
                left += 1
                right -= 1
            elif total > k:
                right -= 1
            else:
                left += 1

        return counter