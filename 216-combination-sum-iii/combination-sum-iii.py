class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates=list(range(1,10))
        res = []
        def dfs(i,cur,k,total):
            # base case 1 : total is reached
            if total == n and len(cur)==k :
                res.append(cur.copy())
                return 
            # base case 2 : total cant be reached 
            if total > n or i >= len(candidates):
                return 

            cur.append(candidates[i])

            dfs(i+1,cur,k,total+candidates[i])

            cur.pop()
            dfs(i+1,cur,k,total)

        dfs(0,[],k,0)
        return res





        