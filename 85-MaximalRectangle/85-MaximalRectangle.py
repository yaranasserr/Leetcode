# Last updated: 1/11/2026, 12:49:41 PM
1from typing import List
2
3class Solution:
4    def maximalRectangle(self, matrix: List[List[str]]) -> int:
5        if not matrix or not matrix[0]:
6            return 0
7        
8        rows, cols = len(matrix), len(matrix[0])
9        height = [0] * cols       # consecutive 1's vertically
10        left = [0] * cols         # left boundary for rectangle
11        right = [cols] * cols     # right boundary (exclusive)
12        max_area = 0
13        
14        for i in range(rows):
15            cur_left, cur_right = 0, cols
16            
17            # update height
18            for j in range(cols):
19                if matrix[i][j] == '1':
20                    height[j] += 1
21                else:
22                    height[j] = 0
23            
24            # update left
25            for j in range(cols):
26                if matrix[i][j] == '1':
27                    left[j] = max(left[j], cur_left)
28                else:
29                    left[j] = 0
30                    cur_left = j + 1
31            
32            # update right
33            for j in range(cols-1, -1, -1):
34                if matrix[i][j] == '1':
35                    right[j] = min(right[j], cur_right)
36                else:
37                    right[j] = cols
38                    cur_right = j
39            
40            # compute area
41            for j in range(cols):
42                max_area = max(max_area, height[j] * (right[j] - left[j]))
43        
44        return max_area
45
46