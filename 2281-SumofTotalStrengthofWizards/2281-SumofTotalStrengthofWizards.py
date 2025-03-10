class Solution:
    # TC: O(n)
    # SC: O(n)
    def totalStrength(self, strength):
        n = len(strength)
        MOD = 10**9 + 7

        preSum = [0] * (n + 1)
        prePrefix = [0] * (n + 2)

        for i in range(n):
            preSum[i + 1] = (preSum[i] + strength[i]) % MOD
        for i in range(n + 1):
            prePrefix[i + 1] = (prePrefix[i] + preSum[i]) % MOD

        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[i] <= strength[stack[-1]]:
                stack.pop()
            left[i] = -1 if not stack else stack[-1]
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[i] < strength[stack[-1]]:
                stack.pop()
            right[i] = n if not stack else stack[-1]
            stack.append(i)

        ans = 0
        for i in range(n):
            left_contrib = (prePrefix[right[i] + 1] - prePrefix[i + 1]) * (i - left[i]) % MOD
            right_contrib = (prePrefix[i + 1] - prePrefix[left[i] + 1]) * (right[i] - i) % MOD
            ans += (left_contrib + MOD - right_contrib) * strength[i] % MOD
            ans %= MOD

        return ans
