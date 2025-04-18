#https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        """
        Task:
        We need to take K elements every time and find maximum average value and return this value

        Approach:
        We can use sliding window appraoch and take everyt time k elements and calculate max. We then go through the all elements
        and return best value

        """

        # taking init sum of k elemenets
        best = now = sum(nums[:k])
        # taking K elements every time
        for i in range(k,len(nums)):
            # removing one element and adding second
            now += nums[i] - nums[i-k]

            if now > best:
                best = now

        return best/k