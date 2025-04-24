#https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75

class RecentCounter:

    """
    The task requires creation of queue which will save recent requests that came at certain timeframe.
    Also, it requires to delete old requests so that we would always have range of [t - 3000, t]

    Time Compliexty: O(1) - in a best case we would need to pop out single element from our queue
    Space Complexity O(1)
    """

    def __init__(self):
        # init queue
        self.requests = deque()


    def ping(self, t: int) -> int:
        # append values to quueen
        self.requests.append(t)

        # remove old elements from the queen FIFO
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)