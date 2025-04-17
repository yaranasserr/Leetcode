class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        #0 <= i < j < n
        # nums[i] == nums[j]
        # i * k % k == 0
        n = len(nums)
        res = []
        pairs = 0 
        for i in range(n):
            for j in range(i,n):
                if nums[i] == nums[j] and ((i*j)%k) == 0 and i <j :
                    
                    pairs +=1

        return pairs 



        