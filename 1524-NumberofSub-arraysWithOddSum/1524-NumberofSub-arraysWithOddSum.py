class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur = 0 
        even = 0 
        odd = 0
        res = 0 
        mod = 10**9 +7
        for i in arr :
            cur+=i 
            if cur%2 :
                # odd
                res = (res+even+1)% mod
                odd+=1
            else:
                res = (res+odd)% mod
                even+=1
        return res
                


            