from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n=len(grid[0])
        fresh = 0 
        time = 0 
        visit=set()
        q=deque()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        # count the fresh
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh +=1
        # put the rotten in the queue 
                if grid[r][c]==2:
                    q.append([r,c])

        while q and fresh > 0 :
            for i in range(len(q)):
                r,c = q.popleft()
                for dr , dc in directions :
                    row = r +dr
                    col = c +dc
                    if row <0 or col<0 or row>= m or col>=n or grid[row][col]!=1:
                        continue
                    grid[row][col] =2 
                    q.append([row,col])
                    fresh -=1 
            time+=1



        return time if fresh == 0 else -1
        





























        # # multisource bfs 
        # rows = len(grid)
        # cols = len(grid[0])
        # visit = set()
        # q= deque()
        # time = 0 
        # fresh = 0 
        # directions = [[0, 1],  # Right
        #               [0, -1], # Left
        #               [1, 0],  # Down
        #               [-1, 0]] # Up 
        # #count the fresh and add rotten in queue
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             fresh +=1
        #         if grid[r][c] == 2:
        #             q.append([r,c])

        # # bfs from the rotten 
        # while q  and fresh >0:
        #     for i in range(len(q)):
        #         r ,c = q.popleft()
        #         for dr , dc in directions :
        #             row = r +dr 
        #             col = c +dc 

        #             # bound 
        #             if (row < 0 or row >= rows or col <0 or col >= cols or grid[row][col] != 1):
        #                 continue
        #             grid[row][col] = 2
        #             q.append([row, col])


        #             fresh -=1 
        #     time+=1


        # return time if fresh == 0 else -1 


