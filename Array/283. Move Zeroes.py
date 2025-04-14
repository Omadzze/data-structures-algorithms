#https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Problem requires put 0 behind while all other values in the beginning

        Approach: 
        We can initialize two pointers, one pointer will be at 0 in the beginning while
        other will be iterating. With the right pointer we would check whether
        values is not 0. If yes we would then check values in-place and update 
        left pointer

        Time Complexity:
        O(n) - since we are going through values once per iteration, n - number of elements in a list
        """


        left = 0

        for right in range(len(nums)):
            # right should not equal to 0
            if nums[right] != 0:
                # update value
                nums[left], nums[right] = nums[right], nums[left]
                # update pointer
                left += 1