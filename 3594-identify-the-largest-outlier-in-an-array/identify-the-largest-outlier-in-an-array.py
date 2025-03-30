from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        num_counts = Counter(nums)  # Simpler than defaultdict(int)

        largest_outlier = float('-inf')

        for num in num_counts:
            potential_outlier = total_sum - 2 * num  

            if potential_outlier in num_counts:
                if potential_outlier != num or num_counts[num] > 1: 
                    largest_outlier = max(largest_outlier, potential_outlier)

        return largest_outlier 