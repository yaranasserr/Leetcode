# Last updated: 4/11/2025, 3:52:28 PM
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        sym = 0 
        for i in range(low, high + 1):
            digits = list(str(i))
            length = len(digits)

            # Only consider even-digit numbers
            if length % 2 == 0:
                half = length // 2
                first_half = sum(int(x) for x in digits[:half])
                second_half = sum(int(x) for x in digits[half:])
                
                if first_half == second_half:
                    sym += 1

        return sym
