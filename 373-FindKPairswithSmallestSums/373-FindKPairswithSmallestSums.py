# Last updated: 7/27/2025, 4:46:36 PM
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += (num >> i) & 1
            if bit_sum % 3:
                result |= (1 << i)
        if result >= 2**31:
            result -= 2**32
        return result