#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # all the triplets return


        # first != second

        # first != third

        # second != third

        # triple value should give == 0
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            # when all nums i positive then there is no sense to check values anymore since it never be equal to 0
            if nums[i] > 0:
                break
            # check whether previous value not the same as curr val
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)

        return res

    def twoSum(self, nums, i, res):

        lower = i + 1
        higher = len(nums) - 1

        while lower < higher:
            answer = nums[i] + nums[lower] + nums[higher]

            if answer < 0:
                lower += 1
            elif answer > 0:
                higher -= 1
            else:
                # if it equals
                res.append([nums[i], nums[lower], nums[higher]])
                lower += 1
                higher -= 1
                while lower < higher and nums[lower] == nums[lower - 1]:
                    lower += 1