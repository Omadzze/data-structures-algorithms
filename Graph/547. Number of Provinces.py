#https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75

class Solution:

    def dfs(self, node, isConnected, visit):
        """
        Iterates inside the nodes elements, and makes all of them visited, one by one.
        """
        visit[node] = True

        for i in range(len(isConnected)):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i, isConnected, visit)



    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        """
        We are given a matrix from which we can build an adjancey matrix and represent our graph.
        After matrix was build we can iterae through BFS or DFS and find province

        Approach:
        This approach iterates through the DFS and check each element and makes it as visit.
        It the returns total number of elements that are exist.

        Time compleixty: O(n^2) - since we are looping two times outside and inside when it it's in a dfs
        Space complexity: O(n) - since we have recursive calls
        """

        size = len(isConnected)
        total = 0
        visit = [False] * size # bool to check whether node was visited or not

        for i in range(size):
            if not visit[i]: # if path was not yet checked
                total += 1
                self.dfs(i, isConnected, visit) # iterate nodes inside tree

        return total