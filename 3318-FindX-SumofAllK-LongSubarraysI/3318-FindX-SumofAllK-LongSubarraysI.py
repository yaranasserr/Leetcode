# Last updated: 11/4/2025, 1:37:07 PM
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = list()
        for i in range(n - k + 1):
            cnt = Counter(nums[i : i + k])
            freq = sorted(cnt.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            ans.append(xsum)
        return ans