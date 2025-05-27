# Last updated: 5/27/2025, 11:35:51 AM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums = range(1,n+1)

        nums1 = sum([x if x%m != 0 else 0 for x in nums])
        nums2 = sum([x if x%m == 0 else 0 for x in nums])
        return nums1-nums2