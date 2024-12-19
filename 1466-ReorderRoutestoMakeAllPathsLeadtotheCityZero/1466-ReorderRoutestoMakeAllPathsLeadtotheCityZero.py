class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Initialize the set of edges and adjacency list
        edges = {(a, b) for a, b in connections}
        neighbours = {city: [] for city in range(n)}
        visit = set()
        changes = 0

        # Build the adjacency list
        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        # Depth-first search (DFS) function
        def dfs(city):
            nonlocal edges, neighbours, visit, changes

            # Visit all the neighboring cities
            for neighbour in neighbours[city]:
                if neighbour in visit:
                    continue
                # If the edge (city, neighbour) is directed, we need to increment changes
                if (city, neighbour) in edges:
                    changes += 1
                visit.add(neighbour)
                dfs(neighbour)

        # Start DFS from city 0
        visit.add(0)
        dfs(0)
        
        return changes
