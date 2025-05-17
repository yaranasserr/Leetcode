class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Count occurrences of 0, 1, and 2
        freq = [0] * 3
        for n in nums:
            freq[n] += 1

        # Overwrite nums in-place
        index = 0
        for color in range(3):
            for _ in range(freq[color]):
                nums[index] = color
                index += 1
