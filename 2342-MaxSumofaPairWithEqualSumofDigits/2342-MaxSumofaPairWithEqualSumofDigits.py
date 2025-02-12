from typing import List
import heapq

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_of_digits = {}  # Dictionary to store (sum of digits : list of numbers)

        # Group numbers by their sum of digits
        for num in nums:
            total = sum(int(digit) for digit in str(num))  # Sum of digits
            if total not in sum_of_digits:
                sum_of_digits[total] = []
            sum_of_digits[total].append(num)

        max_sum = -1  # Default return value

        # Find the maximum sum of two largest values in each group
        for values in sum_of_digits.values():
            if len(values) > 1:  # Only consider lists with at least 2 numbers
                top_two = heapq.nlargest(2, values)  # Get the two largest values
                max_sum = max(max_sum, sum(top_two))  # Update max_sum

        return max_sum
