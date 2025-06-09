class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(prefix):
            total = 0
            curr = prefix
            next_ = prefix + 1
            while curr <= n:
                total += min(n + 1, next_) - curr
                curr *= 10
                next_ *= 10
            return total

        curr = 1
        k -= 1  # عشان أول رقم هو 1 أصلاً

        while k > 0:
            steps = count(curr)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr
