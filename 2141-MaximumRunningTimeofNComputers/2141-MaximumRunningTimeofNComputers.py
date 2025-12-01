# Last updated: 12/1/2025, 9:14:28 PM
1class Solution:
2    def maxRunTime(self, n: int, batteries: List[int]) -> int:
3        # Get the sum of all extra batteries.
4        batteries.sort()   
5        extra = sum(batteries[:-n])
6        
7        # live stands for the n largest batteries we chose for n computers.
8
9        live = batteries[-n:]
10        
11        # We increase the total running time using 'extra' by increasing 
12        # the running time of the computer with the smallest battery.
13        for i in range(n - 1):
14            # If the target running time is between live[i] and live[i + 1].
15            if extra // (i + 1) < live[i + 1] - live[i]:
16                return live[i] + extra // (i + 1)
17            
18            # Reduce 'extra' by the total power used.
19            extra -= (i + 1) * (live[i + 1] - live[i])
20        
21        # If there is power left, we can increase the running time 
22        # of all computers.
23        return live[-1] + extra // n