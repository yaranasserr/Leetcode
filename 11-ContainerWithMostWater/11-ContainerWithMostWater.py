# Last updated: 10/4/2025, 1:28:47 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea ,l,r= 0,0,len(height)-1
        while l<r :
            maxarea = max(maxarea,min(height[l],height[r])* (r-l))
            l , r = (l+1,r) if height[l] < height[r] else (l,r-1)
        return maxarea 

               
            # if height[l] < height[r]:
            #     l+=1
            # else:
            #     r-=1 
