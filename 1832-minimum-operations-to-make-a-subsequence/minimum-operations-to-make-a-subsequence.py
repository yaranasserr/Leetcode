class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {num: i for i, num in enumerate(target)} # key -> number , value-> index

        a2=[index_map[i] for i in arr if i in index_map] # the index of the common number
        
        dp = []
        for num in a2 :
            index=bisect_left(dp,num)
             
            if index < len(dp):
                dp[index]=num
            else:
                dp.append(num)
                
        return len(target) - len(dp)
        
        