# Last updated: 12/20/2025, 11:34:10 AM
1class Solution:
2    def findAllPeople(self, n, meetings, firstPerson):
3        parent = list(range(n))
4
5        def find(x):
6            if parent[x] != x:
7                parent[x] = find(parent[x])
8            return parent[x]
9
10        def union(a, b):
11            parent[find(b)] = find(a)
12
13        meetings.sort(key=lambda x: x[2])
14
15        union(0, firstPerson)
16
17        i = 0
18        while i < len(meetings):
19            time = meetings[i][2]
20            involved = []
21
22            while i < len(meetings) and meetings[i][2] == time:
23                x, y, _ = meetings[i]
24                union(x, y)
25                involved.append(x)
26                involved.append(y)
27                i += 1
28
29            root0 = find(0)
30            for p in involved:
31                if find(p) != root0:
32                    parent[p] = p
33
34        return [i for i in range(n) if find(i) == find(0)]