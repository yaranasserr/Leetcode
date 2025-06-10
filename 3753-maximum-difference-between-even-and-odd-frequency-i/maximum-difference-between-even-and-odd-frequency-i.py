class Solution:
    def maxDifference(self, s: str) -> int:
        # max odd frequency
        # min even frequency 


        return max(v for v in Counter(s).values() if v%2 != 0 ) -  min(v for v in Counter(s).values() if v%2 == 0)
        