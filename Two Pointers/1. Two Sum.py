#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Traversing through the list of two sum to find an answer and return indices.
        Note that this is brute forece approach

        # Space Complexity O(n^2) - since we need to traverse elements two times
        # Space complexity O(1) - we don't need to store elements
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                answer = nums[i] + nums[j]

                if target == answer:
                    return [i, j]