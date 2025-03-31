# Last updated: 3/31/2025, 6:16:29 PM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=range(1,10)
        res = []

        def backtrack(i,cur,total):
            if total==n and len(cur)==k:
                res.append(cur.copy())
                return 
            if i>= len(nums) or total> n :
                return 

            cur.append(nums[i])
            backtrack(i+1,cur,nums[i]+total) # number dont repeat
            # dont include this number 
            cur.pop()
            backtrack(i+1,cur,total)


        backtrack(0,[],0)
        return res 


        
        

  




        