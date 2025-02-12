class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapst,mapts = {} ,{}
        for c1 , c2 in zip(s,t):
            if (c1 in mapst and mapst[c1]!= c2) or (c2 in mapts and mapts[c2]!= c1):
                return False 
            mapst[c1]=c2
            mapts[c2]=c1 

        return True 
     
        


           


        







        # if len(s) != len(t):
        #     return False
        
        # char_mapping = {}
        
        
        # result = ""
        
        # for i in range(len(s)):
        #     if s[i] in char_mapping.keys():
        #         result = result + char_mapping[s[i]]
                
        #         if result[i] != t[i]:
        #             return False
                
        #     else:
        #         if t[i] in char_mapping.values():
        #             return False
        #         char_mapping[s[i]] = t[i] 
        #         result = result + t[i]
            
        # return True
            
        