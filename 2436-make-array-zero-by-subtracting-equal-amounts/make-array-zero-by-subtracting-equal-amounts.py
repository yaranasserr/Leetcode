class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set()
        for i in nums:
            if i !=0 :
                unique.add(i)

        return len(unique)
        