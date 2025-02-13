class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index= {} # n: key , value : index
        for i , n in enumerate(nums):
            diff = target - n
            if diff in num_index:
                return[num_index[diff],i]
            num_index[n] = i # add n as key and i as value 

       
         
