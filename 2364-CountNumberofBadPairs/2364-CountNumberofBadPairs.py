class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
            count_good_pairs = 0
            freq_map = defaultdict(int)

            for i, num in enumerate(nums):
                key = num - i  
                count_good_pairs += freq_map[key]  
                freq_map[key] += 1  
            n = len(nums)
            total_pairs = n * (n - 1) // 2  # Total possible pairs
            return total_pairs - count_good_pairs  # Bad pairs = total - good

                