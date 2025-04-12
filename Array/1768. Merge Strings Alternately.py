#https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        """
        We need to return letters from a string in altering order, we would get two inputs word1 and word2.
        The idea is to return first value from word1 and the second value from word2.

        Solution:
        1. Use two pointers
        we need to check both strings to whether they are not exhausted. Once one of them will be exhausted we need to append
        values to the final output. We would need two step verification process one will be external and other will be internal. External will check whether one of elements still contains value and internal will check which element has a value.

        Time complexity:
        O(m + n) - since we have 2 inputs from which we need to iterate and push results to the list.
        """

        left = 0
        right = 0
        final_output = []
        # External check whether one of this still contains values
        while left < len(word1) or right < len(word2):
            # Internal check which of it contains value and which was exhausted
            if (left < len(word1)):
                final_output.append(word1[left])
                left += 1

            if (right < len(word2)):
                final_output.append(word2[right])
                right += 1

        return "".join(final_output)