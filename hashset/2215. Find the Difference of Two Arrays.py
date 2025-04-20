#https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        """
        With the set we can check whether elements are in a list1 or list2.

        Time Complexity O(n + m) - because we need to iterate through 2 lists
        """

        first_set = set(nums1)
        second_set = set(nums2)

        answer = [[], []]
        for num1 in first_set:
            if num1 not in second_set:
                answer[0].append(num1)

        for num2 in second_set:
            if num2 not in first_set:
                answer[1].append(num2)

        return answer