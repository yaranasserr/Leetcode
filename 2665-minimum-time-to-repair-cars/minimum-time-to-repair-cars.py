class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
   
 
        res = 0 
        l = 1
        r = max(ranks) * (cars)**2

        def canRepairInTime(mid):
            count = 0 
            for r in ranks :
                #n ≤ sqrt(mid / r)
                count += int(sqrt(mid/r))
            if count >= cars :
                return True 
            return  count >= cars 



        # search range [l,r]
        while l <= r:
            m=(l+r)//2
            if canRepairInTime(m) :
                # minimize the minutes 
                res = m 
                r = m - 1
                
            else :
                l = m +1

        return  res



        