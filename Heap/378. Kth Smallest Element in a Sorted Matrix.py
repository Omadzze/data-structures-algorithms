#https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        """
        Finding Kth smallest element from the matrix.

        Approach:
        Flatten everything in the matrix and create heap
        pop elements and decremenent k everytime and then return root element

        Time Complexity: O(n^2 log(n)) - due to flattening and then poping and removing elements
        Space Compelixty: O(n^2) - since we are storing everythiing in the list after flattening
        """

        heap = []

        for i in range(len(matrix)):
            for j in matrix[i]:
                heapq.heappush(heap, j)

        while k > 1:
            heapq.heappop(heap)
            k -= 1

        return heap[0]