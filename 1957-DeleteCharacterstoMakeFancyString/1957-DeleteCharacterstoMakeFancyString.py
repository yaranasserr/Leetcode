# Last updated: 7/21/2025, 2:23:29 PM
class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) >= 2 and stack[-2] == stack[-1] == c:
                continue
            stack.append(c)
        return ''.join(stack)