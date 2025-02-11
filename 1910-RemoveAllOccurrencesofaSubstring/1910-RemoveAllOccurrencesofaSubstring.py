class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # stack 
        stack = []
        for i in s :
            stack.append(i)
            if stack and "".join(stack[-len(part):]) == part :
    
                del stack[-len(part):]
           

        return "".join(stack)
        