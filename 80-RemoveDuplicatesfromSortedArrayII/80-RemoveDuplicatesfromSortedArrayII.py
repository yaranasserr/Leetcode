# Last updated: 7/8/2025, 5:03:21 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}
        write = 0 
        for n in nums :
            freq[n] = 1 + freq.get(n,0)
            if freq[n] <=2 :
                nums[write] = n 
                write +=1 

        return write 





        