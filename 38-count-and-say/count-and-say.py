class Solution:
    def countAndSay(self, n: int) -> str:
        
        def intfreq(s):
            res = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                res.append([count, int(s[i])])
                i += 1
            return res

        def build_from_pairs(pairs):
            result = ""
            for count, digit in pairs:
                result += str(count) + str(digit)
            return result

        current = "1"
        for _ in range(n - 1):
            pairs = intfreq(current)
            current = build_from_pairs(pairs)

        return current
