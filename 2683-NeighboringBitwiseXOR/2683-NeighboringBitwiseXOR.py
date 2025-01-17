class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res = 0 
        for i in derived:
            res ^= i

        return True if res == 0 else False 
        
        