# Last updated: 7/23/2025, 2:09:05 PM
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove(s, pair, score):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == pair[0] and ch == pair[1]:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return "".join(stack), total

  
        if x > y:
            s, points1 = remove(s, "ab", x)
            _, points2 = remove(s, "ba", y)
        else:
            s, points1 = remove(s, "ba", y)
            _, points2 = remove(s, "ab", x)

        return points1 + points2
