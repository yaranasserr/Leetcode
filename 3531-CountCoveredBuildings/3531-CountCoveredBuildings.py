# Last updated: 12/11/2025, 12:09:28 PM
1class Solution:
2    def countCoveredBuildings(self, n, buildings):
3        from bisect import bisect_left
4        rowToCol = {}
5        colToRow = {}
6        for x, y in buildings:
7            rowToCol.setdefault(x, []).append(y)
8            colToRow.setdefault(y, []).append(x)
9
10        for v in rowToCol.values():
11            v.sort()
12        for v in colToRow.values():
13            v.sort()
14
15        cnt = 0
16        for x, y in buildings:
17            cols = rowToCol[x]
18            rows = colToRow[y]
19
20            i = bisect_left(cols, y)
21            left = cols[i-1] if i > 0 else None
22            right = cols[i+1] if i+1 < len(cols) else None
23
24            j = bisect_left(rows, x)
25            up = rows[j-1] if j > 0 else None
26            down = rows[j+1] if j+1 < len(rows) else None
27
28            if left is not None and right is not None and up is not None and down is not None:
29                cnt += 1
30
31        return cnt