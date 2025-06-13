# Last updated: 6/13/2025, 12:02:10 PM
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l , r = 0 , 10**9
        res = 10**9 

        def isValid(threshold):
            i,cnt = 0,0 
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1]) <= threshold:
                    cnt +=1 # valid pairs 
                    i+=2 # skip those two values 
                else:
                    i+=1

                if cnt == p :
                    return True 

            return False 

        if p == 0 : return 0 




        while l <= r :
            m = l +(r-l) //2 

            if isValid(m):
                res = m
                r = m-1
            else:
                l = m+1 # try bigger num


        return res 



        
        
      