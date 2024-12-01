class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        s.replace(" ", "")
        n = len(s)
        j = n-1
        for i in range(n):
            if s[i] != s[j]:
                return False
            j = j-1
        return True
        