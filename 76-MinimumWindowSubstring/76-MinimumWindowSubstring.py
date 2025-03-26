# Last updated: 3/27/2025, 12:25:15 AM
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        s_c = Counter(s)
        t_c = Counter(t)

        # Ensure all chars in t exist in s
        if not all(s_c[char] >= t_c[char] for char in t_c):
            return ""

        check = Counter()  # Track characters in current window
        res = ""
        min_length = float("inf")  # Track minimum substring length
        l = 0
        required = len(t_c)  # Number of unique chars in t
        formed = 0  # Count of unique chars that meet frequency requirement

        for r in range(len(s)):
            char = s[r]
            if char in t_c:
                check[char] += 1
                if check[char] == t_c[char]:  # Required count met
                    formed += 1

            # Shrink window while valid
            while formed == required:
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                    res = s[l:r+1]  # Store smallest valid window

                # Remove leftmost char from window
                if s[l] in t_c:
                    check[s[l]] -= 1
                    if check[s[l]] < t_c[s[l]]:
                        formed -= 1  # Lost a required character

                l += 1  # Move left pointer

        return res if min_length != float("inf") else ""
