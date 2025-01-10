class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1 , earn2 = 0,0

        for i in range(len(nums)):
            curEarn = nums[i]* count[nums[i]]
            # cant use both curEarn
            if i> 0 and nums[i] == nums[i-1] +1 :
                # 4 == 3+1
                temp = earn2
                earn2 = max(curEarn+ earn1,earn2) 
                earn1 = temp
                # [ e1 1 , e2 ,2, 3] then slice it [1.e1 2 , e2 3] 
            else:
                # use both 
                temp = earn2 
                earn2 = curEarn + earn2
                earn1 = temp

        return earn2

        