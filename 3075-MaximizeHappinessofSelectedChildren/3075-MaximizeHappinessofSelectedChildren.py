# Last updated: 12/25/2025, 4:45:12 PM
1class Solution:
2    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
3        # Sort in descending order
4        happiness.sort(reverse=True)
5
6        total_happiness_sum = 0
7        turns = 0
8
9        # Calculate the maximum happiness sum
10        for i in range(k):
11            # Adjust happiness and ensure it's not negative
12            total_happiness_sum += max(happiness[i] - turns, 0)
13
14            # Increment turns for the next iteration
15            turns += 1
16
17        return total_happiness_sum
18