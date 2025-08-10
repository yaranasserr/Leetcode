# Last updated: 8/10/2025, 2:03:35 PM
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return sorted(str(n)) in (sorted(str(1<<i)) for i in range(30))