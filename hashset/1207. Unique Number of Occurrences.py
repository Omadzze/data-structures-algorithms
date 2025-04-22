#https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        """
        To find number of occurences we would neeed to create dict that will have key::occurneces pairs.
        We then would traverse values in this dic and look whether number of unique values are matching with the length of dict

        Time Complexity O(n) - since we are traversing through the array once
        """

        # by default val will be 0
        occurences_dict = defaultdict(int)

        for i in range(len(arr)):
            # append key::ocurrences
            occurences_dict[arr[i]] += 1
        # values compare to unique values
        return len(occurences_dict) == len(set(occurences_dict.values()))