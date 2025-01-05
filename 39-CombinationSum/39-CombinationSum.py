class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
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
            dfs(i,cur,total+candidates[i])
            # do not incude 
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return res
            

            




        