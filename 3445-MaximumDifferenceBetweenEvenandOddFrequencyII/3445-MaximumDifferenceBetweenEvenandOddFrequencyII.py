# Last updated: 6/11/2025, 12:04:28 PM
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def getStatus(cnt_a: int, cnt_b: int) -> int:
            # Bit 1: parity of cnt_a, Bit 0: parity of cnt_b
            return ((cnt_a & 1) << 1) | (cnt_b & 1)

        n = len(s)
        ans = float('-inf')

        for a in map(str, range(5)):
            for b in map(str, range(5)):
                if a == b:
                    continue

                best = [float('inf')] * 4
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1

                for right in range(n):
                    if s[right] == a:
                        cnt_a += 1
                    if s[right] == b:
                        cnt_b += 1

                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)

                        left += 1
                        if s[left] == a:
                            prev_a += 1
                        if s[left] == b:
                            prev_b += 1

                    right_status = getStatus(cnt_a, cnt_b)
                    required_status = right_status ^ 0b10

                    if best[required_status] != float('inf'):
                        ans = max(ans, cnt_a - cnt_b - best[required_status])

        return ans
