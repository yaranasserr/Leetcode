# Last updated: 9/16/2025, 2:58:33 PM
from math import gcd

class Solution(object):
    def replaceNonCoprimes(self, nums):
        stack = []

        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = (stack.pop() * num) // g
            stack.append(num)

        return stack