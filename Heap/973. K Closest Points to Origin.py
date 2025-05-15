#https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # [x, y] value
        # k - integer

        """
        Approach:
        We need to return the points that are closest to the origin.
        For that we can make min_heap and populate it with list of vaues [i, x, y]
        we then can call heapify and sort these values
        after that we simply need to return only K elements with while loop by poping first element
        and appending to the result
        """

        min_heap = []
        for x, y in points:
            answer = x**2 + y**2
            # append multiple values to the heap
            min_heap.append([answer, x, y])

        # sort them with heam O(n)
        heapq.heapify(min_heap)
        result = []

        # note that we need return K elements
        while k > 0:
            # take up first element smallest one
            answer, x, y = heapq.heappop(min_heap)
            result.append([x, y])
            k -= 1

        return result