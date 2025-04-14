#https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        """
        We need to find consequence of i < j < k and return true if it exist
        otherwise false

        Approach:
        One of the approach was to create two infinity variables
        that will store values. We then will update those values
        at each iteration if we found values smaller. Otherwise if value bigger was found we are returning True

        Complexity:
        Time: O(n) - n size of nums
        Space: O(1)

        """

        # store negative and positive values
        first_num = float("inf")
        second_num = float("inf")

        for num in nums:
            # reassign value at each iteration if smaller value found
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True

        return False