#https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        """
        If both asteroids go to similar direction then we are doing nothing
        Else they are going to relative to each other we need to take highest value and remove lowest value.
        We then appending this to the final value as well asteroids that didn't collide.

        We will to the stack asteroids that are positive. Once asteroid is negative we will pop last
        element from the stack to compare them
        """

        stack = []
        answer = []

        for aster in asteroids:
            # append positive asteroids
            if aster > 0:
                stack.append(aster)

            else:
                # check whether stack list not 0 and previous element is negative
                while len(stack) > 0 and stack[-1] < abs(aster):
                    stack.pop()

                # if in stack no values we need to append it
                if len(stack) == 0:
                    answer.append(aster)
                else:
                    # both asteroids collided
                    if stack[-1] == abs(aster):
                        stack.pop()

        answer += stack
        return answer