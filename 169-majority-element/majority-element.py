class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) 
        freq = {}
        for n in nums :
            freq[n] = 1 + freq.get(n,0)

        max_key = max(freq, key=freq.get) # freq.get returns the value for each key.

        return max_key

        