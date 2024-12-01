class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        
        for i in range(len(nums)):
            temp_sum = 0
            # for j in range(i+1):
            #     temp_sum += nums[j]
            temp_sum += sum(nums[0:i+1])
            result[i] +=  temp_sum
        return result