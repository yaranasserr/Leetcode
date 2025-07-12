# Last updated: 7/12/2025, 10:37:45 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for w in path :
            if w == "" or w ==".":
                continue
            if w == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(w)

        return "/" +"/".join(stack)

            
            


        