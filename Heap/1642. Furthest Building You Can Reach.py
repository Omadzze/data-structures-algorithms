#https://leetcode.com/problems/furthest-building-you-can-reach/
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        """
        We need first traverse everything and then understand which points the  most highest and put there ladders, to the points which are less higher we can
        use bricks.
        """

        # heap for ladders
        ladder_allocations = []

        # traverse heights
        for i in range(len(heights) - 1):
            # calculate next height
            climb = heights[i + 1] - heights[i]

            # if it's jump down skip it
            if climb <= 0:
                continue

            # otherwise allocate a ladder for this climb
            heapq.heappush(ladder_allocations, climb)

            # if we used all the ladders
            if len(ladder_allocations) <= ladders:
                continue

            # we need to remove bricks and pop ladders
            # free up ladders
            bricks -= heapq.heappop(ladder_allocations)

            if bricks < 0:
                return i

        return len(heights) - 1