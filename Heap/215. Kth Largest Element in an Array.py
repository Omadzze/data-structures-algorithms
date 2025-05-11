#https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        """
        The problem requires us to find Kth largest element in the array.

        What we can do is actually add up element to the array,
        then we would check with the largest element so far in our heap,
        if we found largest element then simply pop from heap and append with
        new largest element

        While array is empty in the beginning we just want to populate it.

        Time Complexity: O(n) - since we are traversing through the whole array
        """

        maxHeap = []

        for i in range(len(nums)):
            # check if the curr length of heap is not more than K
            if len(maxHeap) >= k:
                # check root val with curr number
                if nums[i] > maxHeap[0]:
                    # remove root value
                    heapq.heappop(maxHeap)
                    # append with new larger value
                    heapq.heappush(maxHeap, nums[i])
                else:
                    continue
            else:
                heapq.heappush(maxHeap, nums[i])

        # return largest value (root value)
        return maxHeap[0]

