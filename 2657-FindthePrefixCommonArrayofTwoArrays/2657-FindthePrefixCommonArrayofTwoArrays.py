class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        res = []
        count = 0
        for a,b in zip(A, B):
            if a in seen: count += 1
            seen.add(a)
            if b in seen: count += 1
            seen.add(b)
            res.append(count)
        return res