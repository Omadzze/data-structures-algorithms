#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        """
        We have a candies and extra candies parameter. Extra candies should be given to every child and then we should compare
        which child has greates candies return true and lowest candies return false. One of the way is to select childs
        one after another and compare them. Note that we need to use max value parameter to find child with max candies at iteration

        Time Complexity:
        O(n) - we are iterating over array of integer once. We also put final value to the result
        Space Complexity:
        O(1)
        """

        final_values = []

        max_value = max(candies)

        for i in range(len(candies)):
            final_candies = candies[i] + extraCandies
            if final_candies >= max_value:
                final_values.append(True)
            else:
                final_values.append(False)

        return final_values