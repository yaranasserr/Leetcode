# Last updated: 5/11/2025, 2:27:45 PM
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c=0
        for i in range(len(arr)):
            if arr[i]%2!=0:
                c+=1
                if c==3:
                    break
            else:
                c=0
        return c==3