class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # get frequency 
        # get the numbers of maximum frequency 
        num_count=Counter(nums)

        maximum = max(num_count.values()) # maximum frequency
        count_maximum = list(num_count.values()).count(maximum) # count of max frequency 

        return maximum*count_maximum