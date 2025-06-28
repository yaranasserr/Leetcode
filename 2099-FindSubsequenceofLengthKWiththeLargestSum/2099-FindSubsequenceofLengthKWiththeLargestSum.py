# Last updated: 6/28/2025, 2:16:23 PM
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Map each num to its index
        indexed_nums = list(enumerate(nums))  # [(index, num)]
        
        # Sort descendingly by the values
        sorted_by_val = sorted(indexed_nums, key=lambda x: x[1], reverse=True)
        
        # Take top-k items (these are (index, value) pairs)
        top_k = sorted_by_val[:k]
        
        # Sort the top-k items by their original index to maintain order in subsequence
        top_k_sorted_by_index = sorted(top_k, key=lambda x: x[0])
        
        # Extract only the values for the final answer
        return [val for idx, val in top_k_sorted_by_index]
