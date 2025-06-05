class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # adj list 
        adj = defaultdict(list)

        for u , v in zip(s1 ,s2) :
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        components = []
        def dfs(node,group):
            visit.add(node)
            group.append(node)
            for nei in adj[node]:
                if nei not in visit :
                    dfs(nei,group)

        for char in set(s1+s2):
            if char not in visit:
                group = []
                dfs(char,group)
                components.append(group)

        # components : [['a', 'o'], ['e', 'i'], ['k', 'r', 's'], ['m', 'p']]

        mapping = {char: sorted(component)[0] for component in components for char in component}

        # mapping {'o': 'a', 'a': 'a', 'i': 'e', 'e': 'e', 'k': 'k', 'r': 'k', 's': 'k', 'p': 'm', 'm': 'm'}
        return ''.join(mapping.get(char, char) for char in baseStr)



        
        