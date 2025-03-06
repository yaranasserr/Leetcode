class Solution:
    def minSwaps(self, s: str) -> int:
        length = len(s)
        count_0 = s.count('0')
        count_1 = s.count('1')

        # Check if it's impossible to make an alternating string
        if abs(count_0 - count_1) > 1:
            return -1

        # Valid alternating patterns
        valid = [
            '01' * (length // 2) + '0' * (length % 2),
            '10' * (length // 2) + '1' * (length % 2)
        ]

        # Count mismatches for each pattern
        first = sum(v != b for v, b in zip(valid[0], s))
        second = sum(v != b for v, b in zip(valid[1], s))

        # Choose the right pattern based on counts of '0' and '1'
        if count_0 > count_1:
            return first // 2
        if count_1 > count_0:
            return second // 2
        return min(first, second) // 2
