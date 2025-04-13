#https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # We need to put flowers in a way that there will be spaces one after another
        # the thing is that we need to check left_value middle_value and right_value.
        # If we have in the middle 1 then we can not new flower from left and right sides.
        # we can use if, else statements and check values

        # increase counter if we have 0

        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # chcke left side
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                # chheck right side
                empty_right_plot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if empty_left_plot and empty_right_plot:
                    # count total of flowerbed that we have
                    flowerbed[i] = 1
                    count += 1

        return count >= n