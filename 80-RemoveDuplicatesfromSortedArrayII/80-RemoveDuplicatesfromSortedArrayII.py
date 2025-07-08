# Last updated: 7/8/2025, 11:29:15 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]
