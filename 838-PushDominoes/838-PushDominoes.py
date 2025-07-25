# Last updated: 5/2/2025, 5:55:40 PM
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()

        for i , d in enumerate(dom):
            if d !="." : q.append((i,d))

        while q :
            i,d =q.popleft()

            if d == "L":
                if i > 0 and dom[i-1] ==".":
                    q.append((i-1,"L"))
                    dom[i-1] = "L"
            elif d =="R":
                if i+1 < len(dom)  and dom[i+1] ==".":
                    if i+2 < len(dom) and dom[i+2]=="L" :
                        # it is stuck 
                        q.popleft()
                    else:
                        q.append((i+1,"R"))
                        dom[i+1] = "R"

        return "".join(dom)


                
        