class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2*n -1)
        used = set( ) # no places 
        def backtrack(i):
            if i == len(res):
                return True 
            # try for largest element 
            for num in reversed(range(1,n+1)):
                if num in used :
                    continue
                # out of bounds or position already taken
                if num > 1 and (i+num >= len(res) or res[i+num]):
                    continue
                # try decision 
                used.add(num)
                res[i]=num
                if num > 1:
                    res[i+num]=num
                j = i+1
                while  j < len(res) and res[j]>0:
                    j+=1 
                    
                # recusrion 
                if backtrack(j):
                    return True 
                # undo : backtrack 
                used.remove(num)
                res[i]=0
                if num > 1:
                    res[i+num]=0
            return False 
              

        backtrack(0)    
        return res

        