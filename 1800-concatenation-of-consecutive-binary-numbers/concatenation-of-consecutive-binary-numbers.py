class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return reduce(lambda q,k:(q<<k.bit_length()|k)%(10**9+7),range(n+1))