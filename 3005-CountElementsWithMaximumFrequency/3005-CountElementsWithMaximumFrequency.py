# Last updated: 9/22/2025, 12:31:39 PM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # get frequency 
        # get the numbers of maximum frequency 

        return max(Counter(nums).values()) * list(Counter(nums).values()).count(max(Counter(nums).values()))
