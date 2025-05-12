#https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        max_heap = []

        # add all elements to max heap
        for i in range(len(stones)):
            heapq.heappush(max_heap, -1 * stones[i])

        # check whether we have elements in max-heap
        while len(max_heap) > 1:
            # access elements
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if x != y:
                new_value = y - x
                heapq.heappush(max_heap, -1 * new_value)

        # return root element if we have values else 0
        if len(max_heap):
            return -max_heap[0]
        else:
            return 0