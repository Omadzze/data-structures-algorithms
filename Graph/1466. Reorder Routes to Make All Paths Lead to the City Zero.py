#https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:


        # Cretaing graph
        neighbors = defaultdict(list)

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # keep origianl conntections
        edges = {(a, b) for a, b in connections}

        visit = set()
        changes = 0 # count changes that we will made

        def dfs(city):
            nonlocal edges, neighbors, visit, changes

            # iterate through the nodes
            for neighbor in neighbors[city]:
                # if we already checked the node skipped it
                if neighbor in visit:
                    continue

                # check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1

                # append to the visit and call recursively dfs
                visit.add(neighbor)
                dfs(neighbor)

        # Start
        visit.add(0)
        dfs(0)
        return changes