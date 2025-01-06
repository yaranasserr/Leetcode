class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1} # there is one ay to sum up to zero

        for total in range(1,target+1):
            dp[total]= 0
            for n in nums:
                dp[total] += dp.get(total-n,0)

        return dp[target]
    """

Initialization:
dp = {0: 1} (initialize the base case).
Step 1: total = 1
Initialize: dp[1] = 0.
Loop through nums = [1, 2, 3]:

n = 1:
total - n = 1 - 1 = 0 (valid key in dp).
dp[1] = dp[1] + dp[0] → dp[1] = 0 + 1 = 1.
n = 2:
total - n = 1 - 2 = -1 (invalid key in dp).
dp[1] = dp[1] + 0 → dp[1] = 1 + 0 = 1.
n = 3:
total - n = 1 - 3 = -2 (invalid key in dp).
dp[1] = dp[1] + 0 → dp[1] = 1 + 0 = 1.
Result: dp = {0: 1, 1: 1}.

Step 2: total = 2
Initialize: dp[2] = 0.
Loop through nums = [1, 2, 3]:

n = 1:
total - n = 2 - 1 = 1 (valid key in dp).
dp[2] = dp[2] + dp[1] → dp[2] = 0 + 1 = 1.
n = 2:
total - n = 2 - 2 = 0 (valid key in dp).
dp[2] = dp[2] + dp[0] → dp[2] = 1 + 1 = 2.
n = 3:
total - n = 2 - 3 = -1 (invalid key in dp).
dp[2] = dp[2] + 0 → dp[2] = 2 + 0 = 2.
Result: dp = {0: 1, 1: 1, 2: 2}.

Step 3: total = 3
Initialize: dp[3] = 0.
Loop through nums = [1, 2, 3]:

n = 1:
total - n = 3 - 1 = 2 (valid key in dp).
dp[3] = dp[3] + dp[2] → dp[3] = 0 + 2 = 2.
n = 2:
total - n = 3 - 2 = 1 (valid key in dp).
dp[3] = dp[3] + dp[1] → dp[3] = 2 + 1 = 3.
n = 3:
total - n = 3 - 3 = 0 (valid key in dp).
dp[3] = dp[3] + dp[0] → dp[3] = 3 + 1 = 4.
Result: dp = {0: 1, 1: 1, 2: 2, 3: 4}.

Step 4: total = 4
Initialize: dp[4] = 0.
Loop through nums = [1, 2, 3]:

n = 1:
total - n = 4 - 1 = 3 (valid key in dp).
dp[4] = dp[4] + dp[3] → dp[4] = 0 + 4 = 4.
n = 2:
total - n = 4 - 2 = 2 (valid key in dp).
dp[4] = dp[4] + dp[2] → dp[4] = 4 + 2 = 6.
n = 3:
total - n = 4 - 3 = 1 (valid key in dp).
dp[4] = dp[4] + dp[1] → dp[4] = 6 + 1 = 7.
Result: dp = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}.

    """
        