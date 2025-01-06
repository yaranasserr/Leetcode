from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates and maintain order
        
        def dfs(start, cur, total):
            if total == target:
                res.append(cur.copy())  # Found a valid combination
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Stop further exploration if the number exceeds the target
                if total + candidates[i] > target:
                    break
                # Include the current candidate and move to the next
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])  # Move to the next index
                cur.pop()  # Backtrack
        
        dfs(0, [], 0)
        return res
