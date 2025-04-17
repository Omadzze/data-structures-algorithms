#https://leetcode.com/problems/container-with-most-water/submissions/1609573542/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        """
        Task:
        We have a rectangle and we need to calculate it's area, to calculate area we need to go trough the bars
        by using two pointers, left beginning right end. We then will multiply the height and width together
        to get maximum area from the recntagle.

        Time Complexity O(n) - since we are going through the list one time
        Space compexity O(1)
        """

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left

            # find max area
            max_area = max(max_area, min(height[left], height[right]) * width)

            # check values
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area