#https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        """
        We need to find kth largest element from the heap

        Approach:
        For that we can iterate through the heap and create a min-heap, we then will store only k elements
        and thus we could simply took first element from the heap and it will be our result
        """
        #k = 4
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)

        return heap[0]
