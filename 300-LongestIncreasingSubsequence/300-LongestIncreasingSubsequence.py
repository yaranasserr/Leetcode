class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp and binary search : o(n log n) 
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

        # manual binary serach
""" 
indices = [None for x in range(len(nums)+1)]
length = 0 
for i, num in enumerate(nums):
    updatelength =self.binarysearch(self,length,indices,nums,num)
    indices[updatelength] = i
    length = max(length,updatedlength)

def binarysearch(startindex,endindex,indices,nums,num):
    # base case 
    if startindex > endindex:
        return startindex 

    middleindex = (startindex+endindex) //2
    if nums[indices[middleindex]] < num:
        startindex = middleindex+1
    else:
        end index = middleindex-1

    return self.binarysearch(startindex,endindex,indices,nums,num)





"""