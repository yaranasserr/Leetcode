from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}  
        write_index = 0 

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] <= 2: 
                nums[write_index] = num
                write_index += 1

        return write_index  

