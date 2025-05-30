#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # sorted in non-decreasing order

        # return index1 and index2 added by one as an array of length 2

        # may not use the same element twice

        """
        Approach:
        Init two pointers, one left and other in the end right. We then need to look whether targets are giving result that we need. If we overshoot
        we need to decrease right, if we udnershoot we need to increase left. Keep this until pointers will not match

        Time Complexity: O(n) - traverse each element once
        Space Complexity: O(1) - we are not using extra space
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            answer = numbers[left] + numbers[right]

            if target == answer:
                return [left + 1, right + 1]
            elif answer > target:
                right -= 1
                answer = 0
            else:
                left += 1
                answer = 0