# Last updated: 11/3/2025, 4:55:24 PM
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        i = 0
        j = 0

        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0

            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1

            total_time += curr_total - curr_max
            i = j

        return total_time
