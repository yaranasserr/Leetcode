class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        # {(0, 1), (4, 0), (2, 3), (4, 5), (1, 3)}
        # Time O(n) Space O(n)
        neis = {city :[] for city in range(n)}
        visit= set()
        changes = 0 
        # adjacency list 
        for a , b in connections:
            neis[a].append(b)
            neis[b].append(a)

        def dfs(city):
            nonlocal edges , neis , visit,changes
            for ne in neis[city]:
                if ne in visit :
                    continue
                if (ne,city) not in edges :
                    changes +=1
                visit.add(ne)
                dfs(ne)

        visit.add(0)
        dfs(0)
        
        return changes


