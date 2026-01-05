# Last updated: 1/5/2026, 12:33:44 PM
1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        total_sum = 0
4        negative_count = 0
5        min_abs_value = float('inf')
6        
7        for row in matrix:
8            for value in row:
9                total_sum += abs(value)
10                if value < 0:
11                    negative_count += 1
12                min_abs_value = min(min_abs_value, abs(value))
13        
14        if negative_count % 2 == 1:
15            total_sum -= 2 * min_abs_value
16        
17        return total_sum