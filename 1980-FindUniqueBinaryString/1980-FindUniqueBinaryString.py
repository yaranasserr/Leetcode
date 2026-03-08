# Last updated: 3/8/2026, 2:57:58 PM
1# class Solution:
2#     def findDifferentBinaryString(self, nums: List[str]) -> str:
3#         n= len(nums[0])
4#         string = "".join(map(str, [1]*(n))) 
5#         deca = int(string, 2)
6#         res = []
7#         for i in range(deca+1):
8#             res.append(i)
9
10#         binary_list = [format(num, f'0{n}b') for num in res]
11#         notin=[]
12#         for b in binary_list:
13#             if b not in nums:
14#                 notin.append(b)
15        
16#         return notin[0]
17class Solution:
18    def findDifferentBinaryString(self, nums: List[str]) -> str:
19        return "".join("0" if nums[i][i] == "1" else "1" for i in range(len(nums)))