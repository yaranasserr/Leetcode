# Last updated: 9/10/2025, 3:16:05 PM
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        known = [set(ls) for ls in languages]
        need = set()

        for u, v in friendships:
            u -= 1; v -= 1
            if known[u] & known[v]:
                continue
            need.add(u); need.add(v)

        if not need:
            return 0

        ans = float('inf')
        for lang in range(1, n + 1):
            cnt = sum(1 for person in need if lang not in known[person])
            ans = min(ans, cnt)
        return ans