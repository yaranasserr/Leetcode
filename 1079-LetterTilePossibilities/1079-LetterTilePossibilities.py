class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # permutation - dfs backtracking 
        unique_perms = set()
        
        # Generate all possible non-empty subsequences and their permutations
        for i in range(1, len(tiles) + 1):
            for perm in permutations(tiles, i):
                unique_perms.add(perm)
        
        return len(unique_perms)

        