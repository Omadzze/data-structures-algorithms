#https://leetcode.com/problems/keys-and-rooms/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        """
        We need to find whether we can open all the rooms with the set of keys.
        For that we can use BFS, go thourgh the all keys that we have and and store them
        as visited.

        Approach:
        1.  Init first starting room
        2. pop elemetn and check whether it was visited if not append elemenets
        3. check an answer
        """

        # init starting room
        visited = set([0])
        queue = deque([0])

        while queue:
            current_room = queue.popleft() # popup each time key

            # iterate through key
            for key in rooms[current_room]:
                # if key was not appended
                if key not in visited:
                    # append it
                    visited.add(key)
                    queue.append(key)

        # check whether we have same number keys as rooms
        return len(visited) == len(rooms)