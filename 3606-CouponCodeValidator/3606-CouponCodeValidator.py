# Last updated: 12/13/2025, 1:37:06 PM
1from typing import List
2import re
3
4class Solution:
5    def validateCoupons(
6        self,
7        code: List[str],
8        businessLine: List[str],
9        isActive: List[bool]
10    ) -> List[str]:
11
12        mid = []
13
14        # Step 1: filter valid coupons
15        for c, b, a in zip(code, businessLine, isActive):
16            if (
17                a
18                and b in {"electronics", "grocery", "pharmacy", "restaurant"}
19                and re.fullmatch(r"[A-Za-z0-9_]+", c)
20            ):
21                mid.append((b, c))
22
23        # Step 2: priority order
24        priority = {
25            "electronics": 0,
26            "grocery": 1,
27            "pharmacy": 2,
28            "restaurant": 3
29        }
30
31        # Step 3: sort by businessLine priority, then by code
32        mid.sort(key=lambda x: (priority[x[0]], x[1]))
33
34        # Step 4: extract codes only
35        return [c for _, c in mid]
36