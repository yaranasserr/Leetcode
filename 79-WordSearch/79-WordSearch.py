class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        #i : current char in target word

        def dfs(r,c,i): 
            if i == len(word):
                return True
                # out of bounce , wrong character ,character visited twice 
            if r < 0 or c < 0 or r >= rows or c>=cols  or word[i] != board[r][c] or (r,c) in path:
                return False 

            path.add((r,c)) # CHAR IS FOUND
            res = (dfs(r+1,c,i+1)
            or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))

            path.remove((r,c))
            return res 
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True 

        return False 
            

        