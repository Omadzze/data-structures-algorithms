#https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        """
        1. Prefix sum approach:
        1.1 We would need to calculate highest altitude which by default starts with 0
        1.2 We then iterate through the range of values and assign to the max_value of altitude and update it's value every time

        Time Compelixty: O(n) - since we are going trough the array one time
        Space Complexity: O(1)
        """

        current_altitude = 0

        highest_point = current_altitude

        for num in range(len(gain)):
            current_altitude += gain[num]

            if highest_point < current_altitude:
                highest_point = current_altitude

        return highest_point