# Last updated: 5/4/2025, 2:15:40 PM
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = {} # pair : count
        count = 0 
        for a,b in dominoes:
            key = tuple(sorted([a,b]))
            if key in seen :
                count += seen[key]
                seen[key] +=1
            else:
                seen[key]=1 
        return count
 
           
            
        