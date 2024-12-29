import collections
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)  # Convert bank to a set for faster lookups
        if endGene not in bank:
            return -1
        # BFS
        queue = collections.deque()
        queue.append((startGene, 0))
        visited = {startGene}
        
        while queue:
            gene, level = queue.popleft()
            if gene == endGene:
                return level
            for i in range(len(gene)):
                for letter in 'ACGT':
                    new_gene = gene[:i] + letter + gene[i+1:]
                    if new_gene not in visited and new_gene in bank:
                        queue.append((new_gene, level + 1))
                        visited.add(new_gene)
        return -1
