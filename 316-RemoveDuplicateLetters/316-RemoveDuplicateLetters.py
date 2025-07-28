# Last updated: 7/28/2025, 2:13:06 PM
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_ocur = {c:i for i,c in enumerate(s)}
        stack = []
        visit = set()
        # Previous characters are lexicographically greater than current character
        # The previous big characters show up again after position of current character

        for i in range(len(s)):
            if s[i] in visit:
                continue

            while stack and stack[-1] > s[i] and last_ocur.get(stack[-1],-1) > i :
                # remove last char 
                visit.remove(stack.pop())

            visit.add(s[i])
            stack.append(s[i])


        return "".join(stack)
                



        

        