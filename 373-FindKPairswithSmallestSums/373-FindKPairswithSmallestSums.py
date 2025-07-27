# Last updated: 7/27/2025, 4:43:27 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n & 1            # Extract the least significant bit
            result = (result << 1) | bit # Append the bit to the result
            n >>= 1                # Right-shift n to process the next bit
        return result