#https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        """
        We need to find pivot index. The pivot index found only if left and right parts are equal to each other.
        Otherwise we would need to return -1

        Approach:
        1. For that we would need to calculate total sum of right most value, we then need to subract each time right value
        2. and add up to the left value and check whether it's equal or not.
        """

        left_sum = 0
        # total sum
        right_sum = sum(nums)

        for num in range(len(nums)):
            right_sum -= nums[num]

            # check if left and right similar
            if right_sum == left_sum:
                return num

            left_sum += nums[num]

        # if we have rightmost we need to return -1
        return -1