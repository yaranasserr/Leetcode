# Last updated: 9/7/2025, 5:21:20 PM
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1,n//2+1):
            ans.append(i)
            ans.append(-i)

        if n%2 == 1:
            ans.append(0)

        return ans
        