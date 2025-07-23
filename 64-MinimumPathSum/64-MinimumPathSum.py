# Last updated: 7/23/2025, 3:56:41 PM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, comb):
            if i > n:
                if len(comb) == k:
                    res.append(comb.copy())
                return
            
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()
            backtrack(i + 1, comb)
        
        backtrack(1, [])
        return res