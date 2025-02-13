class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap key - num , val (list of indices)
        # hashmap={}
        # for i,num in enumerate(nums):
        #     if num not in hashmap:
        #         hashmap[num]=[]
        #     hashmap[num].append(i)
        
        # for indices in hashmap.values():
        #     for j in range(len(indices) - 1):  # Check all consecutive indices
        #         if abs(indices[j] - indices[j + 1]) <= k:
        #             return True
        # return False
        


        hashmap = {}  # key: num, value: last index where it appeared
        
        for i, num in enumerate(nums):
            if num in hashmap and abs(i - hashmap[num]) <= k:
                return True
            hashmap[num] = i  # Update the last seen index of num
        
        return False

            

        
     
       
        

        