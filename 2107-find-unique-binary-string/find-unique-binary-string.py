# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         n= len(nums[0])
#         string = "".join(map(str, [1]*(n))) 
#         deca = int(string, 2)
#         res = []
#         for i in range(deca+1):
#             res.append(i)

#         binary_list = [format(num, f'0{n}b') for num in res]
#         notin=[]
#         for b in binary_list:
#             if b not in nums:
#                 notin.append(b)
        
#         return notin[0]
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join("0" if nums[i][i] == "1" else "1" for i in range(len(nums)))