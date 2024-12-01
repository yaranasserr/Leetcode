class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        char_mapping = {}
        
        
        result = ""
        
        for i in range(len(s)):
            if s[i] in char_mapping.keys():
                result = result + char_mapping[s[i]]
                
                if result[i] != t[i]:
                    return False
                
            else:
                if t[i] in char_mapping.values():
                    return False
                char_mapping[s[i]] = t[i] 
                result = result + t[i]
            
        return True
            
        