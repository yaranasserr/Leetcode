# Last updated: 3/26/2025, 1:18:37 PM
# class Solution:
#     def minOperations(self, grid: List[List[int]], x: int) -> int:
#         m= len(grid)
#         n = len(grid[0])
#         if len(grid) ==1 :
#             return 0
#         rem=[]
#         count = 0
#         for r in range(m):
#             for c in range(n):
#                 rem.append(grid[r][c]%x)

#         if not  all( x==0  for x in rem):
#             return -1
#         else:

#             nums = [num for row in grid for num in row] #flatten to 1D
#             nums.sort()
#             median = nums[len(nums) // 2]

#             return sum(abs(num - median) // x for num in nums)


from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a 1D list
        nums = [num for row in grid for num in row]

        # Check feasibility: The difference between any two numbers must be a multiple of x
        base = nums[0]
        if any((num - base) % x != 0 for num in nums):
            return -1

        # Sort the numbers
        nums.sort()
        
        # Find the median
        median = nums[len(nums) // 2]
        
        # Compute the total number of operations
        return sum(abs(num - median) // x for num in nums)



        



        