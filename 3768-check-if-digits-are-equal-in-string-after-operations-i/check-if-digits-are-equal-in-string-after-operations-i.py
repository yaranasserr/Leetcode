class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            t = ""
            for i in range(1, len(s)):
                t += str((int(s[i - 1]) + int(s[i])) % 10)
            s = t
        return len(s) == 2 and s[0] == s[1]
