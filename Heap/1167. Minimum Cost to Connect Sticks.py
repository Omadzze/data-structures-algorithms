#https://leetcode.com/problems/minimum-cost-to-connect-sticks/

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        """
        Approach:
        It' simple we need to cretae heap and push and pop answers

        Time Complexity: O(n)
        Space Compleixty: Depends on a arr_sum since it stores elements and heap which also stroes elements
        O(n + m)
        """

        min_cost = 0
        # cretaes heap of elements
        heapq.heapify(sticks)

        while len(sticks) > 1:
            # pop x and y elements
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            answer = x + y
            min_cost += answer
            heapq.heappush(sticks, answer)

        return min_cost
