class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s= s.split()
        if len(pattern) != len(s):  
            return False
        sp ,ps={},{}

        for p ,w in zip(pattern,s):
            if (p in sp and sp[p] != w) or (w in ps and ps[w] != p):
                return False 
            sp[p] = w 
            ps[w]=p

        return True
    
