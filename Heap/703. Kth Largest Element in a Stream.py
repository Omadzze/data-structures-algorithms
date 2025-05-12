#https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    """
    We need to create min heap, at the add function we need to shrink it to the Kth elemenets
    after we shrink it we also need to check whether root val is less than value that are passed
    if less we need to update with new highest value
    if we have more elemenets then Kth we need to pop elements
    """

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # check if less than Kth elements in a list
        # root val less than provided val
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            # if more than k elemenets remove
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)