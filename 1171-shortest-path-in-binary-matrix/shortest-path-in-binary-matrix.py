class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N= len(grid)
        q= deque([(0,0,1)]) # r ,c ,length
        visit = set((0,0))
        direct = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]

        while q:
            r,c,length = q.popleft()
            if r < 0 or c < 0 or  r >= N or c >=N  or grid[r][c] == 1 :
                continue

            if r == N-1 and c == N-1 :
                return length 

            # neighbours 8 directions
            for dr , dc in direct :
                if (r+dr , c+dc) not in visit :

                    q.append((r+dr, c+dc ,length +1))
                    visit.add((r+dr,c+dc))

        return -1
                




        