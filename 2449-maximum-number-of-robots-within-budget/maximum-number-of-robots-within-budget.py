from typing import List
from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        cur = 0  # Sum of running costs
        i = 0  # Left pointer of the window
        n = len(chargeTimes)
        d = deque()  # Monotonic decreasing deque to track max chargeTimes
        max_robots = 0  # Maximum number of robots that can be run within budget

        for j in range(n):
            cur += runningCosts[j]  # Add the running cost of the current robot

            # Maintain the deque to store indices of chargeTimes in decreasing order
            while d and chargeTimes[d[-1]] <= chargeTimes[j]:
                d.pop()
            d.append(j)

            # If cost exceeds budget, shrink the window
            while d and chargeTimes[d[0]] + (j - i + 1) * cur > budget:
                if d[0] == i:  # If the max chargeTime is at i, remove it
                    d.popleft()
                cur -= runningCosts[i]  # Remove the running cost of robot i
                i += 1  # Move the left boundary of the window

            max_robots = max(max_robots, j - i + 1)  # Update the max robots count

        return max_robots

        # l = 0 
        # r = len(chargeTimes) 
        # res = 0 

        # def canaddrobot(mid):
        #     # take up to m robots caclulate if they are within budget
        #     res = max(chargeTimes[:mid+1]) + mid*sum(runningCosts[:mid+1])
        #     if res <= budget :
        #         return True 
        #     else :
        #         return False 
    
        # while l <= r :
        #     m = (l+r)//2
        #     if canaddrobot(m):
        #         # increase the range 
        #         res = m
        #         l = m+1 
        #     else:
        #         r = m-1 

        # return res

        




        