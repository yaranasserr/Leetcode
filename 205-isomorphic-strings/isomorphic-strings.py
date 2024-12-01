class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapST , mapTS  ={} , {}

          # iteration in two arrays

        for c1 ,c2 in zip(s,t):
            if ((c1 in mapST and mapST[c1] != c2 ) or (c2 in mapTS and mapTS[c2] != c1 )):
                return False 
            mapST[c1] = c2 
    
            mapTS[c2] = c1 
          

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
            
        