#https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        """
        We need to find whether both word1 and word2 are same or not. E.g. with both strings we can create same word

        Approach:
        1. Check length of both strings whether it's equal or not
        2. Check words whether they have same characters or not
        3. Check whether number of characters in word1 is the same as word2

        Time Complexity: O(n + m) - n is the word1 and m is the word2. Since we are traverse once it's linear time
        """

        # unique char occurences
        word1_set = set(word1)
        word2_set = set(word2)

        # calculate number of chars
        word1_dict = defaultdict(int)
        word2_dict = defaultdict(int)

        # whether length same
        if len(word1) == len(word2):

            # whether chars same
            if word1_set == word2_set:
                # number of chars
                for char in range(len(word1)):
                    word1_dict[word1[char]] += 1

                for char in range(len(word2)):
                    word2_dict[word2[char]] += 1

                # return sorted values, e.g. integer of char occurences
                return sorted(word1_dict.values()) == sorted(word2_dict.values())

        return False
