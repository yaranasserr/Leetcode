class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        
        # child 1: (0,0) main diagonal
        child1_total = sum(fruits[i][i] for i in range(n))
        
        # mark cells that child 1 visited 
        blocked = set((i, i) for i in range(n))
    
        memo2 = {}
        def dfs2(i, j):
            if i == n-1 and j == n-1:
                return 0 
            
            if i >= n or j < 0 or j >= n:
                return float('-inf')
            
            if (i, j) in memo2:
                return memo2[(i, j)]
            
            current = 0 if (i, j) in blocked else fruits[i][j]
            
            
            max_next = max(
                dfs2(i+1, j-1),
                dfs2(i+1, j),
                dfs2(i+1, j+1)
            )
            
            memo2[(i, j)] = current + max_next
            return memo2[(i, j)]
        
        child2_total = dfs2(0, n-1)
        
        
        memo3 = {}
        def dfs3(i, j):
            if i == n-1 and j == n-1:
                return 0  
            
            if i < 0 or i >= n or j >= n:
                return float('-inf')
                
            if (i, j) in memo3:
                return memo3[(i, j)]
            
            current = 0 if (i, j) in blocked else fruits[i][j]
            
          
            max_next = max(
                dfs3(i-1, j+1),
                dfs3(i, j+1), 
                dfs3(i+1, j+1)
            )
            
            memo3[(i, j)] = current + max_next
            return memo3[(i, j)]
        
        child3_total = dfs3(n-1, 0)
        
        return child1_total + child2_total + child3_total