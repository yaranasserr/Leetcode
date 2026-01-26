# Last updated: 1/26/2026, 12:44:47 PM
1class Solution:
2    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
3        A.sort()
4        n = len(A)
5        minDiff = 2e6 + 1
6        res = []
7
8        for i in range(1, n):
9            diff = A[i] - A[i - 1]
10            if diff < minDiff:
11                minDiff = diff
12                res = [[A[i - 1], A[i]]]
13            elif diff == minDiff:
14                res.append([A[i - 1], A[i]])
15
16        return res
17