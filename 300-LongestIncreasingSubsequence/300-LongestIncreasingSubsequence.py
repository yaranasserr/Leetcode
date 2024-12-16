class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        index_map = {num: i for i, num in enumerate(nums)} # key -> number , value-> index
        dp = []
        for num in nums :
            index=bisect_left(dp,num) 
            # bisect_left(sortedlist, element) returns the index in which element to be inserted , keeping the array sorted
             
            if index < len(dp):
                dp[index]=num
            else:
                dp.append(num)
                
        return  len(dp)