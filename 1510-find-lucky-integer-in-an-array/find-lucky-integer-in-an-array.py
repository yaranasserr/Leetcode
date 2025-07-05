class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        res = []
        for key,val in freq.items():
            if key == val :
                res.append(key)

        return max(res) if res else -1 