#https://leetcode.com/problems/smallest-number-in-infinite-set/?envType=study-plan-v2&envId=leetcode-75

class SmallestInfiniteSet:

    def __init__(self):
        self.is_present = set() # prevent duplicate values, since we need only unique
        self.current_value = 1
        self.heap = [] # current sequence


    def popSmallest(self) -> int:
        # if we have values in a heap we can remove them
        if len(self.heap):
            smallest_element = heapq.heappop(self.heap)
            self.is_present.remove(smallest_element) # remove one unique value since we popped element
        else:
            # otherwise we are increasing counter
            smallest_element = self.current_value
            self.current_value += 1

        return smallest_element


    def addBack(self, num: int) -> None:
        # avoid duplicate value, only next value should be used
        if self.current_value <= num or num in self.is_present:
            return

        heapq.heappush(self.heap, num)
        self.is_present.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)