# Last updated: 1/15/2026, 1:18:16 PM
1class Solution:
2    def maximizeSquareHoleArea(
3        self, n: int, m: int, hBars: List[int], vBars: List[int]
4    ) -> int:
5        hBars.sort()
6        vBars.sort()
7        hmax, vmax = 1, 1
8        hcur, vcur = 1, 1
9        for i in range(1, len(hBars)):
10            if hBars[i] == hBars[i - 1] + 1:
11                hcur += 1
12            else:
13                hcur = 1
14            hmax = max(hmax, hcur)
15        for i in range(1, len(vBars)):
16            if vBars[i] == vBars[i - 1] + 1:
17                vcur += 1
18            else:
19                vcur = 1
20            vmax = max(vmax, vcur)
21        side = min(hmax, vmax) + 1
22        return side * side