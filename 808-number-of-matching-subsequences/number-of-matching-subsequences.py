class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # def is_sub(s,t):
        #     i , j =0 , 0
        #     while i < len(s) and j < len(t):
        #         if s[i]==t[j]:
        #             i+=1
        #             j+=1
        #         else:
        #             j+=1

        #     return 1 if  i == len(s) else 0

        # res = 0 
        # for w in words:
        #     res+= is_sub(w,s)
        # return res
        
        
        def is_sub(word):
            index=-1
            for ch in word:
                index=s.find(ch,index+1)
                if index==-1:
                    return False
            return True
        
        c=0
        for word in words:
            if is_sub(word):
                c+=1
        
        return c
        