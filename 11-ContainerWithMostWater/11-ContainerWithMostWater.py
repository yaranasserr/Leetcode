# Last updated: 10/4/2025, 1:25:48 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l = 0 
        r = len(height)-1
        while l<=r :
            current_area = min(height[l],height[r])* (r-l)
            maxarea = max(maxarea,current_area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1 

        return maxarea 



        