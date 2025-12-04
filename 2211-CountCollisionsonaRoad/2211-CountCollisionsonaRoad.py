# Last updated: 12/4/2025, 9:43:36 PM
1class Solution:
2    def countCollisions(self, directions: str) -> int:
3        res = 0
4        flag = -1
5
6        for c in directions:
7            if c == "L":
8                if flag >= 0:
9                    res += flag + 1
10                    flag = 0
11            elif c == "S":
12                if flag > 0:
13                    res += flag
14                flag = 0
15            else:
16                if flag >= 0:
17                    flag += 1
18                else:
19                    flag = 1
20        return res