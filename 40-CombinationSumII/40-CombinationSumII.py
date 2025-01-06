class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        # cur is the list of holding numbers 

        def dfs(i,cur,total):
            if total == target :
                res.append(cur.copy())
                return 
                # it is imposibble to reach the number 
            if i >= len(candidates) or total > target :
                return 
            # include the candidate
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            # do not incude 
            cur.pop()
            # skipping ia nd its duplicates 
            while i+1 < len(candidates) and candidates[i]== candidates[i+1]:
                i+=1

            dfs(i+1,cur,total)

        dfs(0,[],0)
        return res
        