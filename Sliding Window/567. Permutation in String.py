#https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """
        Approach:
        We first initializing len(s1) and it will be our sliding window, as it can not exceed this limit.
        We then going though the window and checking by charcater level whether it has characters from s1
        if it has characters we are returning True else False.
        """

        s1_counter = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            sb = s2[i : i + len(s1)]

            if s1_counter == Counter(sb):
                return True

        return False


