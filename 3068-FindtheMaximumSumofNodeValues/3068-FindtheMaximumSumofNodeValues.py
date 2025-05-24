# Last updated: 5/24/2025, 2:02:06 PM
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # find delta array which = xor array - original array 
        xor = [n^k for n in nums]
        delta = [x-n for x,n in zip(xor,nums)]
        delta.sort(reverse=True)
        original = sum(nums)

        for i in range(0,len(delta)-1,2):
            gain = delta[i]+delta[i+1]
            if gain > 0 :
                original += gain 
            else:
                break
           
          
        return original
        