# Last updated: 1/4/2026, 1:45:45 PM
1
2class Solution:
3    def sumFourDivisors(self, nums: List[int]) -> int:
4        total = 0
5        
6        for n in nums:
7            divisors = []
8            for i in range(1, int(math.isqrt(n)) + 1):
9                if n % i == 0:
10                    divisors.append(i)
11                    if i != n // i:
12                        divisors.append(n // i)
13            if len(divisors) == 4:
14                total += sum(divisors)
15        
16        return total
17