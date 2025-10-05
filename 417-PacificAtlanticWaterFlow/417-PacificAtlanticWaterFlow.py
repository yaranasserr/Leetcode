# Last updated: 10/5/2025, 5:21:31 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev):
            if (r, c) in visit or not (0 <= r < m and 0 <= c < n) or heights[r][c] < prev:
                return
            visit.add((r, c))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(r+dr, c+dc, visit, heights[r][c])

        for i in range(m):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, n-1, atl, heights[i][n-1])
        for j in range(n):
            dfs(0, j, pac, heights[0][j])
            dfs(m-1, j, atl, heights[m-1][j])

        return [[r, c] for r in range(m) for c in range(n) if (r, c) in pac & atl]
