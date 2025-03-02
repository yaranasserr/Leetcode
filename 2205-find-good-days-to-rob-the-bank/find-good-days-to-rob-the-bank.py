class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        non_increasing = [0] * n
        non_decreasing = [0] * n

        # Fill the non-increasing array
        for i in range(1, n):
            if  security[i] <=  security[i - 1]:
                non_increasing[i] = non_increasing[i - 1] + 1

        # Fill the non-decreasing array
        for i in range(n - 2, -1, -1):
            if  security[i] <=  security[i + 1]:
                non_decreasing[i] = non_decreasing[i + 1] + 1

        good_days = []

        for i in range(time, n - time):
            if non_increasing[i] >= time and non_decreasing[i] >= time:
                good_days.append(i)

        return good_days

        