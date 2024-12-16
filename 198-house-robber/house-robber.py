class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1 , rob2 , n ]
        rob1, rob2 = 0, 0
        for i in nums:
            temp = max(rob2, rob1 + i)  # Decide whether to rob the current house
            rob1 = rob2                # Update rob1 to the value of rob2
            rob2 = temp                # Update rob2 to the new max value
        return rob2
        