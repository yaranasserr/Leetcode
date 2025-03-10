class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        
        MOD = 10**9 + 7
        n = len(strength)

        # Prefix sum and prefix of prefix sum
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MOD

        prefix_of_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_of_prefix[i + 1] = (prefix_of_prefix[i] + prefix_sum[i]) % MOD

        # Next smaller element to the left and right
        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate the total strength
        res = 0
        for i in range(n):
            l, r = left[i], right[i]
            total_left = (prefix_of_prefix[i + 1] - prefix_of_prefix[l + 1]) % MOD
            total_right = (prefix_of_prefix[r + 1] - prefix_of_prefix[i + 1]) % MOD
            count_left = i - l
            count_right = r - i

            contribution = (strength[i] * (total_right * count_left - total_left * count_right)) % MOD
            res = (res + contribution) % MOD

        return res

        