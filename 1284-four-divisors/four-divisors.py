
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        
        for n in nums:
            divisors = []
            for i in range(1, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total
