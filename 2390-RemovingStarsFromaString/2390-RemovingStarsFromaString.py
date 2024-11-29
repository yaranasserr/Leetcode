class Solution:
    def removeStars(self, s: str) -> str:
        lst=[]
        for i in s:
            if i =='*':
                lst.pop()
            else:
                lst.append(i)

        return ''.join(lst)
            
        
        