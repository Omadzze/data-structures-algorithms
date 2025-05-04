#https://leetcode.com/problems/find-if-path-exists-in-graph/?envType=problem-list-v2&envId=breadth-first-search

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        ## DFS

        # store all edges in a 'graph' since they are now in a list
        graph = collections.defaultdict(list)

        # since we have doulbe list we need to take elements and sotre in a graph [[0, 1]] [[a, b]]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(curr_node):
            if curr_node == destination:
                return True
            seen[curr_node] = True

            # for all the neigbors of the current node, that we didn't vsited before
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    if dfs(next_node):
                        return True
            return False

        return dfs(source)


        """
        ## BFS

        # store all edges in a 'graph' since they are now in a list
        graph = collections.defaultdict(list)

        # since we have doulbe list we need to take elements and sotre in a graph [[0, 1]] [[a, b]]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
  
        # store nodes to be visited in a queue
        seen = [False] * n
        seen[source] = True
        queue = collections.deque([source])

        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True

            # for all the neigbors of the current node, that we didn't vsited before
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)

        return False
        """