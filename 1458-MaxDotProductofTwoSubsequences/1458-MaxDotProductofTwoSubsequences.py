# Last updated: 1/8/2026, 8:35:03 PM
1class Solution:
2    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
3        
4        memo = {}
5
6        # max dot product of two subsequences starting at i,j
7        def dp(i,j):
8
9            if i == len(nums1) or j == len(nums2):
10                return float("-inf") # if we are passed the boundary, dont pick anything from there.
11
12            if (i,j) in memo:
13                return memo[(i,j)]
14
15            take = nums1[i] * nums2[j]
16            res = max(
17            # take i,j. move forward
18                take + dp(i+1, j+1),
19
20            # take this subsequence and just end.
21                take,
22
23            # skip i: i+1,j
24                dp(i+1,j),
25
26            # skip j: i,j+1
27                dp(i,j+1),
28            )
29
30            memo[(i,j)] = res
31
32            return memo[(i,j)]
33
34        return dp(0,0)