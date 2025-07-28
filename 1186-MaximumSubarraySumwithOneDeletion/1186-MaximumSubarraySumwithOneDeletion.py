# Last updated: 7/28/2025, 1:54:35 PM
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        # left[i] = max subarray sum ending at i
        left = [0] * n
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(arr[i], left[i - 1] + arr[i])
            print("left",left[i])

        # right[i] = max subarray sum starting at i
        right = [0] * n
        right[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            right[i] = max(arr[i], right[i + 1] + arr[i])
            print("right",right[i])

        # Now try deleting each element arr[i] and check left[i-1] + right[i+1]
        max_sum = max(left)  # case: no deletion

        for i in range(1, n - 1):
            max_sum = max(max_sum, left[i - 1] + right[i + 1])

        return max_sum
