#https://leetcode.com/problems/task-scheduler/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # CPU tasks from A to Z andn umber n

        # idle or completion of one task

        # can be comppleted in any order

        # however gap of at least n intevals between two tasks with the same label

        """
        Approach:

        We can solve it as an array,
        with idle to be a bool
        we need to traverse and take only unique values

        from each char

        Once we traversed we know that there is no unique values left and we need to idle
        we need to repat everything again so it means recursion stack
        """

        count = Counter(tasks)

        max_heap = []

        # count how much chars we have and return as max heap
        for cnt in count.values():
            max_heap.append(cnt * -1)

        # create a heap
        heapq.heapify(max_heap)

        time = 0
        queen = deque()

        while max_heap or queen:
            time += 1
            if max_heap:
                # removing one element
                cnt = 1 + heapq.heappop(max_heap)
                # if it not equals to 0
                if cnt:
                    queen.append([cnt, time + n])

            if queen and queen[0][1] == time:
                heapq.heappush(max_heap, queen.popleft()[0])

        return time


