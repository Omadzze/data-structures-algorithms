# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:

        """
        1. To somehow match it we need to know position of elements
        For example we need to remember position of first and last one
        and then reverse it.

        2. We need also to have list and check whether s in list of vowel values

        3. finally we need to change reverse charcters. Noe that this is string and
        it's immutable
        """

        lower_case = ['a', 'e', 'i', 'o', 'u']
        upper_case = ['A', 'E', 'I', 'O', 'U']

        left = 0
        right = len(s) - 1

        # because string immutable we would need create list
        s = list(s)

        while left < right:
            # check whether element is vowel
            if s[left] in lower_case or s[left] in upper_case:
                if s[right] in lower_case or s[right] in upper_case:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                else:
                    # right
                    right -= 1
            else:
                # left
                left += 1

        return "".join(s)