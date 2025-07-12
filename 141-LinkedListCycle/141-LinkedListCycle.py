# Last updated: 7/12/2025, 10:39:05 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/") #['', 'home', 'user', 'Documents', '..', 'Pictures']
        print(path)

        for w in path :
            if w == "" or w ==".":
                continue
            if w == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(w)

        return "/" +"/".join(stack)

            
            


        